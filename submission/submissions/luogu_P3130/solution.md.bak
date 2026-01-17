# P3130 题解

##
线段树(ｷ｀ﾟДﾟ´)!!

维护两个值,sum,min;
然后还有懒标记；
是不是很简单；

不会线段树的可以去做模板题，虽然我觉得这个也是个模板QwQ;
```
#include<iostream>
#include<cstdio>
#include<cmath>
#include<queue>
#include<cstring>
#include<algorithm>
#define int long long
using namespace std;
const int N=400000;
int n,m,a[N];
char c;
struct tree
{
    int l;
    int r;
    int min;
    int sum;
    int add;
}t[N<<2];//四倍！！！
void pushup(int p)
{
    t[p].sum=t[p<<1].sum+t[p<<1|1].sum;
    t[p].min=min(t[p<<1].min,t[p<<1|1].min);
}//个人比较喜欢写函数，方便好调试；（向上传）
void pushdown(int p)
{
	if(!t[p].add)return;
    t[p<<1|1].add+=t[p].add; 
	t[p<<1].add+=t[p].add;	
	t[p<<1].min+=t[p].add;
	t[p<<1|1].min+=t[p].add;
	t[p<<1|1].sum+=(t[p<<1|1].r-t[p<<1|1].l+1)*t[p].add;
	t[p<<1].sum+=(t[p<<1].r-t[p<<1].l+1)*t[p].add;
	t[p].add=0;//不要忘了清零QwQ
}//对于懒标记的处理（向下传）
void build(int p,int l,int r)
{
    t[p].l=l,t[p].r=r;
    if(l==r){t[p].min=t[p].sum=a[l];return;}
    int mid=l+r>>1;
    build(p<<1,l,mid);build(p<<1|1,mid+1,r);
    pushup(p);//别忘了传递，这里用手写函数的话是不是很好看，线段树多可爱呀！
}//建树没什么说的吧QwQ
void change(int p,int l,int r,int z)
{
    if(l<=t[p].l&&r>=t[p].r){t[p].add+=z,t[p].min+=z,t[p].sum+=(t[p].r-t[p].l+1)*z;return;}
    pushdown(p);
    int mid=t[p].l+t[p].r>>1;
    if(l<=mid)change(p<<1,l,r,z);
    if(r>mid)change(p<<1|1,l,r,z);
    pushup(p);//传递
}
int querysum(int p,int l,int r)
{
    if(l<=t[p].l&&r>=t[p].r)return t[p].sum;
    pushdown(p);//懒标记要向下传递信息；
    int mid=t[p].l+t[p].r>>1;
    int ans=0;
    if(l<=mid)ans+=querysum(p<<1,l,r);
    if(r>mid)ans+=querysum(p<<1|1,l,r);
    return ans;
}
int querymin(int p,int l,int r)
{
    if(l<=t[p].l&&r>=t[p].r)return t[p].min;
    pushdown(p);
    int mid=t[p].l+t[p].r>>1;
    int ans=0x7f7f7f7f;
    if(l<=mid)ans=querymin(p<<1,l,r);
    if(r>mid)ans=min(ans,querymin(p<<1|1,l,r));
    return ans;
}//这个和sum没什么区别吧，嘻嘻
signed main()
{
    scanf("%lld%lld",&n,&m);
    for(int i=1;i<=n;i++)
    {
        scanf("%lld",&a[i]);
    }
    build(1,1,n);
    for(int i=1;i<=m;i++)
    {
        cin>>c;
        if(c=='P')
        {
            int l,r,z;
            scanf("%lld%lld%lld",&l,&r,&z);
            change(1,l,r,z);
        }
        if(c=='M')
        {
            int l,r;
            scanf("%lld%lld",&l,&r);
            printf("%lld\n",querymin(1,l,r));
        }
        if(c=='S')
        {
            int l,r;
            scanf("%lld%lld",&l,&r);
            printf("%lld\n",querysum(1,l,r));
        }
    }
    return 0;
}
```
总结：线段树是个妹子，她很可爱