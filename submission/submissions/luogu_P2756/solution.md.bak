# P2756 题解

匈牙利算法自带匹配方案

~~献给所有匈牙利算法党~~

```c
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<cstdlib>
#include<string>
#include<queue>
#include<map>
#include<stack>
#include<list>
#include<set>
#include<deque>
#include<vector>
#include<ctime>
#define ll long long
#define inf 0x7fffffff
#define N 500008
#define IL inline
#define D double
#define U unsigned
#define R register
using namespace std;
template<typename T>void read(T &a)
{
    T x=0,f=1;char ch=getchar();
    while(!isdigit(ch))
    {
        if(ch=='-')f=0;ch=getchar();
    }
    while(isdigit(ch))
    {
        x=(x<<1)+(x<<3)+ch-'0';ch=getchar();
    }
    a=f?x:-x;
}
/*-------------OI使我快乐---------------------*/
ll n,m,ans;
ll to[N];
struct node{
    ll to,nex;
}e[N];
ll x,y,tot;
ll head[N];
bool vis[N];
void add(ll a,ll b)
{
    e[++tot].to=b;
    e[tot].nex=head[a];
    head[a]=tot;
}
bool find(ll x)
{
    ll xx;
    for(ll i=head[x];i;i=e[i].nex)
    {
        xx=e[i].to;
        if(!vis[xx])
        {
            vis[xx]=1;
            if(!to[xx]||find(to[xx]))
            {
                to[xx]=x;
                return 1;
            }
        }
    }
    return 0;
}
int main()
{
    read(n);read(m);
    read(x);read(y);
    while(x!=-1&&y!=-1)
    {
        if(x<=n&&y<=m) add(x,y);
        read(x);read(y);
    }
    for(ll i=1;i<=n;i++)
    {
        memset(vis,0,sizeof(vis));
        if(find(i)) ans++;
    }
    cout<<ans<<endl;
    for(ll i=n+1;i<=m;i++)
    {
        if(to[i]) cout<<to[i]<<" "<<i<<endl;
    }
    return 0;
}
```

最后对应输出即可