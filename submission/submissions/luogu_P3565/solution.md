# P3565 题解

这道题两维的做法应该挺好想的，但是要开2个$5000\times 5000$的数组，好像有点大？开$short$，算出来差不多96M，好像能卡过去？一看空间：67.5M（大艹

那我们考虑一维的做法

我们发现，三个点距离相等的话就是他们深度较深的两个点的$lca$到三个点的距离相等

我开始想的做法是枚举两个点（复杂度显然是$O(n^2)$），然后预处理出来什么东西然后搞，但是不太好弄

等等，如果把那个$lca$拎上来变成根，那么这三个点就在同一深度了，不是很好做了吗？

所以，我们枚举那个点，然后树形$dp\ O(n)$统计一下答案就可以了

但是统计答案还是有点麻烦，我们不能单纯的统计每个深度的点有多少个（样例都过不去），因为我们要保证任意两个的$lca$还是这个根节点，也就是说，我们当前枚举的根节点的每条出边指向的点所在的子树上最多只能选一个点

所以我们要枚举每一个子树，然后统计答案，因为要三个点，所以是当前子树中的个数乘上之前选过的里面选了2个点的情况数了

我们让$box[d]$表示当前子树中深度为$d$的点的个数，$f[d]$表示在整棵树之前遍历的部分中，深度为$d$的所有点中，选出两个点的合法方案数

为了方便转移，我们再引入一个$g[d]$表示在整棵树之前遍历的部分中，深度为$d$的所有点中，选出一个点的方案数

那么对于一次枚举子树，

$$ans=ans+f[d]\times box[d]$$
$$f[d]=f[d]+g[d]\times box[d]$$
$$g[d]=g[d]+box[d]$$

然后输出答案就可以了，记得开$long\  long$

```cpp
#include <bits/stdc++.h>
using namespace std;

# define Rep(i,a,b) for(int i=a;i<=b;i++)
# define _Rep(i,a,b) for(int i=a;i>=b;i--)
# define RepG(i,u) for(int i=head[u];~i;i=e[i].next)

typedef long long ll;

const int N=5005;

template<typename T> void read(T &x){
   x=0;int f=1;
   char c=getchar();
   for(;!isdigit(c);c=getchar())if(c=='-')f=-1;
   for(;isdigit(c);c=getchar())x=(x<<1)+(x<<3)+c-'0';
    x*=f;
}

int n;
int head[N],cnt;
ll box[N],f[N],g[N],deepest;
ll ans;

struct Edge{
    int to,next;
}e[N<<1];

void add(int x,int y){
    e[++cnt]=(Edge){y,head[x]},head[x]=cnt;
}

void dfs(int u,int fa,int dep){
    deepest=max(deepest,1ll*dep);
    box[dep]++;
    RepG(i,u){
        int v=e[i].to;
        if(v==fa)continue;
        dfs(v,u,dep+1);
    }
}

int main()
{
    memset(head,-1,sizeof(head));
    read(n);
    Rep(i,1,n-1){
        int x,y;
        read(x),read(y);
        add(x,y),add(y,x);
    }
    Rep(i,1,n){
        memset(f,0,sizeof(box));
        memset(g,0,sizeof(g));
        RepG(j,i){
            int v=e[j].to;
            deepest=0;
            memset(box,0,sizeof(box));
            dfs(v,i,1);
            Rep(k,1,deepest){
                ans+=f[k]*box[k];
                f[k]+=g[k]*box[k];
                g[k]+=box[k];
            }
        }
    }
    printf("%lld\n",ans);
    return 0;
}
```
