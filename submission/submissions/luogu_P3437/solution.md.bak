# P3437 题解

来[露迭月](https://www.cnblogs.com/ppprseter/p/9582277.html)的博客阅读获取船新体验


注意到这个矩形修改矩形查询最大值的所有位置上的值是非减的，否则我们没法使用二维线段树配合标记永久化完成。

------------
先考虑一维的情况，区间求最大值，区间赋值最大值加上某个正数

在线段树中维护一个$mx$和一个$tag$，分别表示区间最大值和修改后的值

对于修改操作，对路径上的每一个节点都用待修改的值尝试更新$mx$数组，因为这个节点一定包含这个小区间，所以可以更新

但$tag$操作只有区间完全被覆盖时才更新，不下传一直呆在这个区间

对于查询操作，对路径上的每一个节点都尝试使用$tag$数组更新答案，因为tag是对整个区间打的，所以子区间可以直接使用

在区间完全被覆盖的情况下，我们才可以用$mx$数组更新答案

这就是所谓的标记永久化

为什么要这样，因为第二维的树是没法使用子节点快速更新答案的，也不好下传

------------
再考虑第二维的情况，第二维的线段树每一个节点都放着两颗颗第一维线段树

一颗代表$mx$树，一颗代表$tag$树

然后剩下的就和第一维的情况非常相似了

------------
**Code:**
```cpp
#include <cstdio>
const int N=2050;
int n,m;
int max(int x,int y){return x>y?x:y;}
#define ls id<<1
#define rs id<<1|1
struct segy
{
    int mx[N],tag[N];
    void change(int id,int l,int r,int L,int R,int val)
    {
        mx[id]=max(mx[id],val);
        if(l==L&&r==R)
        {
            tag[id]=max(tag[id],val);
            return;
        }
        int Mid=L+R>>1;
        if(r<=Mid) change(ls,l,r,L,Mid,val);
        else if(l>Mid) change(rs,l,r,Mid+1,R,val);
        else change(ls,l,Mid,L,Mid,val),change(rs,Mid+1,r,Mid+1,R,val);
    }
    int query(int id,int l,int r,int L,int R)
    {
        if(l==L&&r==R)
            return mx[id];
        int ans=tag[id],Mid=L+R>>1;
        if(r<=Mid) ans=max(ans,query(ls,l,r,L,Mid));
        else if(l>Mid) ans=max(ans,query(rs,l,r,Mid+1,R));
        else ans=max(ans,max(query(ls,l,Mid,L,Mid),query(rs,Mid+1,r,Mid+1,R)));
        return ans;
    }
};
struct segx
{
    segy mx[N],tag[N];
    void change(int id,int l,int r,int L,int R,int ll,int rr,int val)
    {
        mx[id].change(1,ll,rr,1,m,val);
        if(l==L&&r==R)
        {
            tag[id].change(1,ll,rr,1,m,val);
            return;
        }
        int Mid=L+R>>1;
        if(r<=Mid) change(ls,l,r,L,Mid,ll,rr,val);
        else if(l>Mid) change(rs,l,r,Mid+1,R,ll,rr,val);
        else change(ls,l,Mid,L,Mid,ll,rr,val),change(rs,Mid+1,r,Mid+1,R,ll,rr,val);
    }
    int query(int id,int l,int r,int L,int R,int ll,int rr)
    {
        if(l==L&&r==R)
            return mx[id].query(1,ll,rr,1,m);
        int ans=tag[id].query(1,ll,rr,1,m),Mid=L+R>>1;
        if(r<=Mid) ans=max(ans,query(ls,l,r,L,Mid,ll,rr));
        else if(l>Mid) ans=max(ans,query(rs,l,r,Mid+1,R,ll,rr));
        else ans=max(ans,max(query(ls,l,Mid,L,Mid,ll,rr),query(rs,Mid+1,r,Mid+1,R,ll,rr)));
        return ans;
    }
}t;
int main()
{
    int d,s,h,x,y,k;
    scanf("%d%d%d",&n,&m,&k);
    while(k--)
    {
        scanf("%d%d%d%d%d",&d,&s,&h,&x,&y),++x,++y;
        t.change(1,x,x+d-1,1,n,y,y+s-1,t.query(1,x,x+d-1,1,n,y,y+s-1)+h);
    }
    printf("%d\n",t.query(1,1,n,1,n,1,m));
    return 0;
}

```
