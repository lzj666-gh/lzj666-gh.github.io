# P4014 题解

挂个博客[Youngsc](https://youngscc.github.io/)


**首先膜拜楼下机房巨佬%%%KM二分图最佳完美匹配**

**蒟蒻只想说我根本不知道咋求顶标，好在本蒟蒻会~~费用流~~**

**关于二分图最佳完美匹配问题，就是让二分图带上边权，然后让选出来的完美匹配权值之和最大**

**费用流的话很简单，先建一个超级源超级汇**

**然后从超级源想每一个人连一条容量为1，费用为0的弧**

**同样的，从每一个任务向超级汇连一条容量为1，费用为0的弧**

**然后对于每一个人和每一个任务，对应的从人向任务连一条容量为1，费用为$C_{i,j}$的弧**

**以上各弧容量为1是为了防止一个点被多次匹配**

**然后跑一个最大费用最大流和最小费用最大流就完美的解决了**


**注意题面里并没有说$C_{i,j}$是正整数，所以可能会有负值**


### 代码如下


```cpp
# include <bits/stdc++.h>
# define R register
# define LL long long
# define inf 2147483647

using namespace std;

int n,s,t,ans,fr[210],h[210],flo[210],e=-1,dis[210],pre[210],x;
bool v[210];

queue <int> q;

struct zx{int v,flow,w,pre;} ed[50010];

template <typename T> inline void in(R T& a){
    R char c=getchar();R T x=0,f=1;
    while(!isdigit(c)) (c=='-'? f=-1:0),c=getchar();
    while(isdigit(c)) x=(x<<1)+(x<<3)+c-'0',c=getchar();
    a=x*f;
}

inline void add(R int x,R int y,R int z,R int w){
    ed[++e] = (zx){y,z,w,h[x]};
    h[x] = e;
}

inline bool bfs_max(){
    for(R int i=s; i<=t; ++i) dis[i] = -inf/3;
    dis[s] = 0,flo[s] = inf;
    q.push(s);
    while(!q.empty()){
        R int x=q.front();
        q.pop();
        for(R int i=h[x]; i!=-1; i=ed[i].pre){
            R int p=ed[i].v;
            if(dis[p] < dis[x] + ed[i].w&&ed[i].flow){
                dis[p] = dis[x] + ed[i].w;
                if(!v[p]) v[p] = 1,q.push(p);
                flo[p] = min(ed[i].flow,flo[x]);
                pre[p] = i;
                fr[p] = x;
            }
        }
        v[x] = 0;
    }
    return dis[t] > -inf/3;;
}

inline bool bfs_min(){
    for(R int i=s; i<=t; ++i) dis[i] = inf/3;
    dis[s] = 0,flo[s] = inf;
    q.push(s);
    while(!q.empty()){
        R int x=q.front();
        q.pop();
        for(R int i=h[x]; i!=-1; i=ed[i].pre){
            R int p=ed[i].v;
            if(dis[p] > dis[x] + ed[i].w&&ed[i].flow){
                dis[p] = dis[x] + ed[i].w;
                if(!v[p]) v[p] = 1,q.push(p);
                flo[p] = min(ed[i].flow,flo[x]);
                pre[p] = i;
                fr[p] = x;
            }
        }
        v[x] = 0;
    }
    return dis[t] < inf/3;
}

int main(){
    // freopen("home.in","r",stdin);
    // freopen("home.out","w",stdout);
    in(n);
    memset(h,-1,sizeof(h));
    for(R int i=1; i<=n; ++i)
        for(R int j=1; j<=n; ++j)
            in(x),add(i,j+n,1,x),add(j+n,i,0,-x);
    s=0,t=n+n+1;
    for(R int i=1; i<=n; ++i) add(s,i,1,0),add(i,s,0,0),add(i+n,t,1,0),add(t,i+n,0,0);
    while(bfs_min()){
        ans += dis[t]*flo[t];
        R int now = t;
        while(now != s){
            ed[pre[now]].flow -= flo[t];
            ed[pre[now]^1].flow += flo[t];
            now = fr[now];
        }
    }
    printf("%d\n",ans);
    for(R int i=0; i<=e; i+=2) ed[i].flow += ed[i^1].flow,ed[i^1].flow = 0;
    ans = 0;
    while(bfs_max()){
        ans += dis[t]*flo[t];
        R int now = t;
        while(now != s){
            ed[pre[now]].flow -= flo[t];
            ed[pre[now]^1].flow += flo[t];
            now = fr[now];
        }
    }
    printf("%d\n",ans);
    return 0;
}
```