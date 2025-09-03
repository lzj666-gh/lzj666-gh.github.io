# P3740 题解

这道题我有两种做法：线段树和浮水法（表示不会离散化，好在数据还用不到）。

1. 线段树 维护区间是否被染色：区间修改没被染色的点，标记，++ans；如果区间的点全被染过色，那ans不变。

2. 浮水法，专门解决这类区间染色问题：

记录某一个线段是不是（或者是有一部分）浮到了最上面。

上浮思想：设竖直平面中存在有一些高度不同的线段，当一个线段上方没有被其他线段挡着时，这个线段就可以上浮，如果一个线段（或是它的一部分）可以上浮到无限高，那么显然，这个线段（或这一部分）所在的高度是他所覆盖的这一个数轴范围内（将平面的无限低的地方看做有一个数轴）最高的。

浮水法其实是一个递归的过程，首先，当一条线段满足上浮的条件时，让他上浮（用 while 循环控制），但是当他不满足上浮的条件时，将他被挡住的那一段切掉，然后接着递归的让他剩下的那部分上浮。

（摘自http://www.cnblogs.com/SueMiller/archive/2011/08/05/2128794.html，网上没有很多相关的）


补代码：1.线段树

```cpp
#include<cmath>
#include<cstdio>
#include<algorithm>
using namespace std;
const int N=10000005,M=1005;

int n,m,Ans,A[M],B[M];
bool flag,colored[N<<2];

int read()
{
    int now=0;char c=getchar();
    while(c<'0'||c>'9')c=getchar();
    while(c>='0'&&c<='9')now=(now<<3)+(now<<1)+c-'0',c=getchar();
    return now;
}

void PushUp(int rt)
{
    colored[rt]= colored[rt<<1]&&colored[rt<<1|1];
}

/*void Build(int l,int r,int rt)
{
    if(l==r)
      return;
    int m=(l+r)>>1;
    Build(l,m,rt<<1);
    Build(m+1,r,rt<<1|1);
    PushUp(rt);
}*/

void Modify(int l,int r,int rt,int L,int R)
{
    if(colored[rt]) return;
    if(L<=l && r<=R)
    {
        flag=1;colored[rt]=1;
        return;
    }
    int m=(l+r)>>1;
    if(L<=m) Modify(l,m,rt<<1,L,R);
    if(m<R) Modify(m+1,r,rt<<1|1,L,R);
    PushUp(rt);
}

int main()
{
    freopen("ha14d.in","r",stdin);
    freopen("ha14d.out","w",stdout);
    n=read();m=read();
//    Build(1,n,1);
    for(int i=1;i<=m;i++)
      A[i]=read(),B[i]=read();
    for(int i=m;i>=1;i--)
    {
        flag=0;
        Modify(1,n,1,A[i],B[i]);
        if(flag) ++Ans;
    }
    printf("%d",Ans);
    fclose(stdin);fclose(stdout);
    return 0;
}
```
2.浮水法：

```cpp
#include<cstdio>
using namespace std;
const int N=10000005,M=1005;

int n,m,Ans,cur,A[M],B[M];
bool vis[M];

int read()
{
    int now=0;char c=getchar();
    while(c<'0'||c>'9')c=getchar();
    while(c>='0'&&c<='9')now=(now<<3)+(now<<1)+c-'0',c=getchar();
    return now;
}

void Solve(int a,int b,int now)
{
    if(vis[cur]) return;
    while(now<=m && (a>=B[now]||b<=A[now]))//需要等于 
      ++now;
    if(now>m)
      ++Ans,vis[cur]=1;//printf("%d:%d--%d\n",Ans,a,b);
    if(a<A[now] && A[now]<b) Solve(a,A[now],now+1);//不能等于 
    if(b>B[now] && B[now]>a) Solve(B[now],b,now+1);
}

int main()
{
//    freopen("ha14d.in","r",stdin);
//    freopen("ha14d.out","w",stdout);
    n=read();m=read();
    for(int i=1;i<=m;i++)
      A[i]=read(),B[i]=read(),++B[i];//右端点再加1，因为两端点是都不能放其他海报的(看不见) 
    for(cur=m-1;cur>=1;cur--)
      Solve(A[cur],B[cur],cur+1);
    printf("%d",++Ans);
//    fclose(stdin);fclose(stdout);
    return 0;
}
```
其实还可以暴力 ：这题数据真水，暴力就能ac。cogs上加强了数据暴力只能80（还是挺高的）。
