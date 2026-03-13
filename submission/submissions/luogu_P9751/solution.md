# P9751 题解

### 题意：

给出一个有向图，当前在 $1$ 号点，初始在时间 $0$，必须在 $k$ 的倍数的时间出发，且到终点的时间也必须是 $k$ 的倍数。

每条边有一个边权 $w_i$，只有在当前时间 $\ge w_i$ 时才可以通过，且不能在原地不动，即每一个时间点必须走一条边。

问从 $1$ 号点出发到 $n$ 号时最早的时刻。（没有方案则输出 $-1$）

### 思路：

因为 $k \le 100$ 很小，所以我们可以从 $k$ 入手。

注意到，如果我当前到达了 $u$ 号点，且当前时间为 $p$，这条边边权为 $w$，如果 $p < w$，那么显然当前不能通过。

但是因为如果当前可以走到这个点，那么可以晚一些 $k$ 的倍数的时间出发，依然可以走到这个点，则我们可以在入口处等待一些时间，使得可以通过这条边，等待时间为 $\lceil \frac{w-p}{k} \rceil \times k$，即等待 $\lceil \frac{w-p}{k} \rceil$ 个 $k$ 的倍数，这样就可以通过这条边了，耗费时间为 $\lceil \frac{w-p}{k} \rceil \times k+p$。

现在通过每条边的时间更出发点为 $k$ 的倍数有关系，则我们可以建立以下状态：定义 $dis_{i,j}$ 为到达 $i$ 号点的时间 $\bmod k$ 的值为 $j$ 时的最短消耗时间。

那么答案显然是 $dis_{n,0}$。

然后看一下转移，如果 $p \ge w$ 了，那么可以直接通过，则 $dis_{v,(p+1) \bmod k} \to \min(dis_{v,(p+1) \bmod k},p+1)$。

否则的话，令 $t=\lceil \frac{w-p}{k} \rceil \times k+p$，即我们在入口处等待一些时间，使得可以走到这条边，转移为 $dis_{v,(t+1) \bmod k} \to \min(dis_{v,(t+1) \bmod k},t+1)$。

可以运用 dijkstra 算法的思想来进行转移，每次去堆顶选取耗时最短的那个点，然后逐层松弛。

时间复杂度为：$O(n \times k \log n)$。

### 完整代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll N=10010,M=105;
inline ll read(){
    ll x=0,f=1;
    char c=getchar();
    while(c<'0'||c>'9'){
        if(c=='-')
          f=-1;
        c=getchar();
    }
    while(c>='0'&&c<='9'){
        x=(x<<1)+(x<<3)+(c^48);
        c=getchar();
    }
    return x*f;
}
inline void write(ll x){
	if(x<0){
		putchar('-');
		x=-x;
	}
	if(x>9)
	  write(x/10);
	putchar(x%10+'0');
}
ll n,m,k;
ll dis[N][M];
bool f[N][M];
vector<pair<ll,ll>> E[N];
priority_queue<pair<ll,ll>,vector<pair<ll,ll>>,greater<pair<ll,ll>>> q;
void add(ll u,ll v,ll w){
	E[u].push_back({v,w});
}
void dijkstra(ll s){
	dis[s][0]=0;
	q.push({0,s});
	while(!q.empty()){
		ll u=q.top().second,p=q.top().first;
		q.pop();
		if(f[u][p%k])
		  continue;
		f[u][p%k]=1;
		for(auto d:E[u]){
			ll v=d.first,w=d.second,t=(p+1)%k;
			if(p>=w)
			  t=p;
			else
			  t=((w-p+k-1)/k)*k+p;
			if(dis[v][(t+1)%k]>t+1){
				dis[v][(t+1)%k]=t+1;
				q.push({t+1,v});
			}
		}
	}
}
int main(){
	memset(dis,0x3f,sizeof(dis));
	n=read(),m=read(),k=read();
	for(int u,v,w,i=0;i<m;i++){
		u=read(),v=read(),w=read();
		add(u,v,w);
	}
	dijkstra(1);
	if(!f[n][0])
	  puts("-1");
	else
	  write(dis[n][0]);
	return 0;
}
```
