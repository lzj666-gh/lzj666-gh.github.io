# P1197 题解

这道题看似很长其实也不是十分的难

如果我们去正这摧毁 想想都有点困难

要不 我们使用逆向思维？

没错 这道题就把摧毁转换成修建~~（和平就是好）~~

利用并查集判断联通就好了

```cpp
#include<iostream>
#include<cstdio>
#define f(i,a,b) for(register int i=a;i<=b;i++)
#define fd(i,a,b) for(register int i=a;i>=b;i--)
using namespace std;
int k,n,m,head[400002],tot,broken[400002],ans[400003];
int father[400003];
struct Node
{
    int next,node,from;
}h[400002];
inline void Add_Node(int u,int v)
{
    h[++tot].from=u;
    h[tot].next=head[u];
    head[u]=tot;
    h[tot].node=v;
}
bool Broken[400001];
inline int Get_father(int x)
{
    if(father[x]==x)    return x;
    return father[x]=Get_father(father[x]);
    //你爸爸的爸爸就是你的爸爸——反查理马特——并查集 
}
inline void hb(int u,int v)
{
    u=Get_father(u),v=Get_father(v);
    if(u!=v)    father[v]=u;
}
int main()
{
    ios::sync_with_stdio(false);
    cin>>n>>m;
    f(i,0,n)
        father[i]=i,head[i]=-1;//并查集初始化 
    f(i,1,m)
    {
        int x,y;
        cin>>x>>y;
        Add_Node(x,y);//储存图 
        Add_Node(y,x);//由于无向图存两遍 
    }
    cin>>k;
    f(i,1,k)
    {
        cin>>broken[i];
        Broken[broken[i]]=1;//标记砸坏了 
    }
    int total=n-k;//初始化为所有点都是单独存在的 
    f(i,1,2*m)//有2*m个边 
        if(!Broken[h[i].from] && !Broken[h[i].node] && Get_father(h[i].from)!=Get_father(h[i].node))
		{//要是起点和终点都没砸坏 而且他们并没有联通
            total--;//连一条边 减一个联通体 
            hb(h[i].from,h[i].node);
        }
    ans[k+1]=total;//当前就是最后一次破坏后的个数 
    fd(i,k,1)
    {
        //total=0 //这里不需要初始化 需要从上一次的废墟上修建 
        total++;//修复一个点 联通体+1 
        Broken[broken[i]]=0;//修复 
        for(int j=head[broken[i]];j!=-1;j=h[j].next)//枚举每一个子点 
        {
            if(!Broken[h[j].node] && Get_father(broken[i])!=Get_father(h[j].node))
            {
                total--;//连一边减一个联通块 
                hb(broken[i],h[j].node);//合并这两个点 
            }
        }
        ans[i]=total;
    }
    f(i,1,k+1)    cout<<ans[i]<<endl;
    return 0;
}
```