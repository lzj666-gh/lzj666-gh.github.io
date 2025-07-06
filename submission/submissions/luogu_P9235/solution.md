# P9235 题解

提供一种与 kruskal 相关做法相比代码难度显著减少的做法，灵感来源于 ICPC 2023 第一场网络赛。

化简题意后发现，这题本质是将边按边权从大到小排序后依次插入原图，询问两个点在什么时候会连通，允许离线。

每插入一条边本质就是在合并两个连通块，很自然地想到启发式合并。

利用启发式合并的思想，我们将每个询问挂在它的两个端点上，在合并两个联通块时，处理较小的连通块中的询问。

判断询问是否已成立的方法也很简单，只需查询该询问中的另一个端点是否在我们将要合并的连通块内即可，时间复杂度 $O(\alpha(n))$。

对于未成立的询问，只需将其合并到另一个连通块内便于之后查询即可。

有些读者可能发现一个询问在两个点上，会不会造成重复查询呢？会不会影响该做法的正确性呢？请自行思考，理解它才真正理解了本做法。

时间复杂度 $O(n \log n\alpha(n))$。

代码：
```cpp
#include<bits/stdc++.h>
using namespace std;
//#pragma GCC optimize("Ofast,no-stack-protector,unroll-loops")
#define ALL(v) v.begin(),v.end()
#define For(i,_) for(int i=0,i##end=_;i<i##end;++i) // [0,_)
#define FOR(i,_,__) for(int i=_,i##end=__;i<i##end;++i) // [_,__)
#define Rep(i,_) for(int i=(_)-1;i>=0;--i) // [0,_)
#define REP(i,_,__) for(int i=(__)-1,i##end=_;i>=i##end;--i) // [_,__)
typedef long long ll;
typedef unsigned long long ull;
#define V vector
#define pb push_back
#define pf push_front
#define qb pop_back
#define qf pop_front
#define eb emplace_back
typedef pair<int,int> pii;
typedef pair<ll,int> pli;
#define fi first
#define se second
const int dir[4][2]={{-1,0},{0,1},{1,0},{0,-1}},inf=0x3f3f3f3f,mod=1e9+7;
const ll infl=0x3f3f3f3f3f3f3f3fll;
template<class T>inline bool ckmin(T &x,const T &y){return x>y?x=y,1:0;}
template<class T>inline bool ckmax(T &x,const T &y){return x<y?x=y,1:0;}
int init=[](){return cin.tie(nullptr)->sync_with_stdio(false),0;}();
int main(){
	int m,n,q;
	scanf("%d%d",&n,&m);
	V<int>x(m),y(m),z(m);
	For(i,m)scanf("%d%d%d",&x[i],&y[i],&z[i]),--x[i],--y[i];
	V<V<pii>>to(n);
	scanf("%d",&q);
	For(i,q){
		int u,v;
		scanf("%d%d",&u,&v);
		--u,--v;
		to[u].eb(v,i),to[v].eb(u,i);
	}
	V<int>fa(n,-1);
	function<int(int)>find=[&](int k){return fa[k]<0?k:fa[k]=find(fa[k]);};
	V<int>id(m);
	iota(ALL(id),0);
	sort(ALL(id),[&](int x,int y){return z[x]>z[y];});
	V<int>ans(q,-1);
	for(int i:id){
		int fx=find(x[i]),fy=find(y[i]);
		if(fx==fy)continue;
		if(-fa[fx]<-fa[fy])swap(fx,fy);
		for(pii &j:to[fy])if(find(j.fi)==fx)ans[j.se]=z[i];else to[fx].pb(j);
		fa[fx]+=fa[fy],fa[fy]=fx;
	}
	For(i,q)printf("%d\n",ans[i]);
	return 0;
} 
```
