# P2061 题解

线段树区间修改，维护从l到r的高度

相比坐标的le9，n比较小，所以用数组p离散化，修改的时候二分修改的区间即可

将修改的矩形按高度排序，保证后修改的高度一定覆盖之前的

- 注意右区间和左区间都包括mid

- 以及树的空间要开满2\*4\*40000，部分变量记得用long long【因为这一点贡献了4个提交次数\_(┐「ε:)\_

下面贴代码


    
```cpp
#include<cstdio>
#include<algorithm>
using namespace std;
int n;
long long ans;
int t;
struct node{
    int left,right;
    int c;
}tree[4*40005*2];
struct edge{
    int left,right,h;
}a[40005];
int p[2*40005];
bool cmp(edge e1,edge e2)
{
    return e1.h<e2.h;
}
int erfen(int l,int r,int x)//二分查找当前所要修改的离散化区间，即对应的矩形顶点的区间，【比如样例里，当,处理第一个矩形时，修改的区间为（1，2），即第一个矩形的两个顶点在p数组中对应的下标为1、2；
{
    while(l<=r)
    {
        int mid=(l+r)/2;
        if(p[mid]==x) return mid;
        else if(p[mid]>x) r=mid-1;
        else l=mid+1;
    }
    return 0;
}
void change(int now,int l,int r,int x)//裸的区间修改
{
    if(tree[now].right<l||tree[now].left>r) return;
    if(tree[now].left>=l&&tree[now].right<=r)
    {
        tree[now].c=x;
        return;
    }    
    int mid=(tree[now].left+tree[now].right)/2;
    if(tree[now].c) {
        tree[now*2].c=tree[now].c;
        tree[now*2+1].c=tree[now].c;
        tree[now].c=0;
    }
    if(mid>=r)     change(now*2,l,r,x);
    else if(mid<=l) change(now*2+1,l,r,x);
    else {
        change(now*2,l,r,x); change(now*2+1,l,r,x);
    }
}
void built(int now,int l,int r)
{
    tree[now].left=l;
    tree[now].right=r;
    tree[now].c=0;
    if(l==r-1) return;
    built(now*2,l,(l+r)/2);
    built(now*2+1,(l+r)/2,r);//*右界要包括mid，因为一个矩形所占的位置肯定大于一个点，如果不包括mid，会漏掉一些矩形； 
}
void quest(int now)
{
    if(tree[now].c) 
    {
        ans+=(p[tree[now].right]-p[tree[now].left])*(long long)tree[now].c;
        return;
    }
    if(tree[now].right==tree[now].left+1) return;
    quest(now*2);
    quest(now*2+1);
}
int main()
{ 
    scanf("%d",&n);
    for(int i=1;i<=n;i++) 
    {
    scanf("%d%d%d",&a[i].left,&a[i].right,&a[i].h);
    p[++t]=a[i].left;
    p[++t]=a[i].right;    
```
}//离散化顶点

```cpp
    sort(p+1,p+1+2*n);
    sort(a+1,a+n+1,cmp);
    built(1,1,n*2);
    for(int i=1;i<=n;i++)
    {
        int l=erfen(1,2*n,a[i].left);
        int r=erfen(1,2*n,a[i].right);
        change(1,l,r,a[i].h);
    }
    quest(1);
    printf("%lld",ans);
}
第一次写题解有点丑丑的(｡・`ω´･)，可能表达有点不好，看不太明白的同学可以问我
```