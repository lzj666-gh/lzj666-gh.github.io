# P2016 题解

# Solution
树形结构!!!

因为是一棵树,所以对于每个节点,我们都把它当成根节点处理$\to$树形dp!!!

>注意，某个士兵在一个结点上时，与该结点相连的所有边将都可以被了望到。

定义状态dp[u][0/1]表示u这个节点不放/放士兵

根据题意,如果当前节点不放置士兵,那么它的子节点必须**全部**放置士兵,因为要满足士兵可以看到所有的边,所以
$$dp[u][0]+=dp[to][1]$$
其中to是u的子节点

如果当前节点放置士兵,它的子节点选不选已经不重要了(**因为树形dp自下而上,上面的节点不需要考虑**),所以
$$dp[u][1]+=min(dp[to][0],dp[to][1])$$

欢迎踩博客[real_l](https://www.cnblogs.com/real-l/p/9620350.html)

# Code
```cpp
#include<bits/stdc++.h>
#define rg register
#define il inline
#define Min(a,b) (a)<(b)?(a):(b)
#define Max(a,b) (a)>(b)?(a):(b)
using namespace std;

const int N=1510;

void in(int &ans) {
    ans=0; char i=getchar();
    while(i<'0' || i>'9') i=getchar();
    while(i>='0' && i<='9') ans=(ans<<1)+(ans<<3)+i-'0',i=getchar();
}

int n,cur;

int to[N<<1],nex[N<<1],head[N];
int dp[N][2];

il void add(int a,int b) {
    to[++cur]=b;
    nex[cur]=head[a];
    head[a]=cur;
}

il void read() {
    for(rg int i=1;i<=n;i++) {
        int x,k,y; in(x),in(k);
        for(rg int j=1;j<=k;j++) {
            in(y); add(x,y),add(y,x);
        }
    }
}

void dfs(int u,int fa) {
    dp[u][1]=1,dp[u][0]=0;
    for(rg int i=head[u];i;i=nex[i]) {
        if(to[i]==fa) continue;
        dfs(to[i],u);
        dp[u][0]+=dp[to[i]][1];
        dp[u][1]+=Min(dp[to[i]][1],dp[to[i]][0]);
    }
}

int main()
{
    in(n); read(); dfs(0,-1);
    printf("%d\n",Min(dp[0][0],dp[0][1]));
    return 0;
}
```