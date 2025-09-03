# P1471 题解


我们把方差公式展开

 ![](https://cdn.luogu.com.cn/upload/pic/3825.png) 

所以只需要维护一个区间平方和和区间和

当我们更新一个区间加时

 ![](https://cdn.luogu.com.cn/upload/pic/3826.png) 

所以pushdown就很好写了

具体见代码

想要进一步学习的可以看[这里](http://www.yhzq-blog.cc/线段树高阶总结/)


        
    
    
```cpp
#include <cstdio>
#include <iostream>
#define lson rt<<1,l,mid
#define rson rt<<1|1,mid+1,r
#define Maxn 300010
using namespace std;
double sega[Maxn],segb[Maxn];
double mark[Maxn];
void pushup(int x)
{
    sega[x]=sega[x<<1]+sega[x<<1|1];
    segb[x]=segb[x<<1]+segb[x<<1|1];
}
void pushdown(int rt,int x)
{
    if (mark[rt])
    {
        segb[rt<<1]+=2*mark[rt]*sega[rt<<1]+(x-x/2)*mark[rt]*mark[rt];
        segb[rt<<1|1]+=2*mark[rt]*sega[rt<<1|1]+(x/2)*mark[rt]*mark[rt];
        sega[rt<<1]+=(x-x/2)*mark[rt];
        sega[rt<<1|1]+=(x/2)*mark[rt];
        mark[rt<<1]+=mark[rt];
        mark[rt<<1|1]+=mark[rt];
        mark[rt]=0;
    }
}
void build(int rt,int l,int r)
{
    if (l==r)
        cin>>sega[rt],segb[rt]=sega[rt]*sega[rt];
    else
    {
        int mid=(l+r)/2;
        build(lson);
        build(rson);
        pushup(rt);
    }
}
double query_a(int rt,int l,int r,int L,int R)
{
    //--L--l--r--R--
    if (l>=L && r<=R)
        return sega[rt];
    else
    {
        pushdown(rt,r-l+1);
        int mid=(r+l)/2;
        double ret=0;
        if (mid>=L)
            ret+=query_a(lson,L,R);
        if (mid<R)
            ret+=query_a(rson,L,R);
        return ret;
    }
}
double query_b(int rt,int l,int r,int L,int R)
{
    //--L--l--r--R--
    if (l>=L && r<=R)
        return segb[rt];
    else
    {
        pushdown(rt,r-l+1);
        int mid=(r+l)/2;
        double ret=0;
        if (mid>=L)
            ret+=query_b(lson,L,R);
        if (mid<R)
            ret+=query_b(rson,L,R);
        return ret;
    }
}
void update(int rt,int l,int r,int L,int R,double x)
{
    if (l>=L && r<=R)
        mark[rt]+=x,segb[rt]+=2*x*sega[rt]+x*x*(r-l+1),sega[rt]+=(r-l+1)*x;
    else
    {
        pushdown(rt,r-l+1);
        int mid=(r+l)/2;
        if (mid>=L)
            update(lson,L,R,x);
        if (mid<R)
            update(rson,L,R,x);
        pushup(rt);
    }
}
double sqr(double x)
{
    return x*x;
}
main()
{
    int n,m,x,y,c;
    double z;
    scanf("%d %d",&n,&m);
    build(1,1,n);
    for (int i=1;i<=m;i++)
    {
        scanf("%d",&c);
        if (c==2)
            scanf("%d%d",&x,&y),printf("%.4lf\n",query_a(1,1,n,x,y)/(y-x+1));
        if (c==1)
            scanf("%d%d",&x,&y),cin>>z,update(1,1,n,x,y,z);
        if (c==3)
        {
            scanf("%d%d",&x,&y);
            double sum1=query_b(1,1,n,x,y)/(y-x+1),sum2=query_a(1,1,n,x,y)/(y-x+1);
            double ans=sum1-sum2*sum2;
            printf("%.4lf\n",ans);
        }
    }
}
```