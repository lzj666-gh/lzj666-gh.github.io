# P11295 题解

来一个离线做法。

由于我们要求的是一条从 $1$ 到某个点的路径上大于 $0$ 的点的不同种类数，在线比较麻烦，考虑离线。

设 $val_i$ 表示第 $i$ 个点会在前 $val_i$ 只蜻蜓的操作后都大于等于 $0$，那么如果我们有了 $val_i$，就相当于要算一条 $1$ 到 $h_i$ 的路径中有多少个种类，使得至少有一个是这个种类的点的 $val\ge i$。这个明显可以离线二维数点。

接下来考虑怎样才能求出 $val_i$，发现我们可以二分，于是直接整体二分就做完了。

时间复杂度为 $O(n\log n+n\log d+d\log d\log n)$。


```cpp
#include<bits/stdc++.h>
using namespace std;
int plen,ptop,pstk[40];
char rdc[1<<20],out[1<<20],*rS,*rT;
#define gc() (rS==rT?rT=(rS=rdc)+fread(rdc,1,1<<20,stdin),(rS==rT?EOF:*rS++):*rS++)
#define pc(x) out[plen++]=(x)
#define flush() fwrite(out,1,plen,stdout),plen=0
template<class T=int>inline T read(){
    T x=0;char ch;bool f=1;
    while(!isdigit(ch=gc()))if(ch=='-')f^=1;
    do x=(x<<1)+(x<<3)+(ch^48);while(isdigit(ch=gc()));
    return f?x:-x;
}
inline int read(char*const s){
	char *t=s,ch;
    while(!isgraph(ch=gc()));
	do(*(t++))=ch;while(isgraph(ch=gc()));
	return (*t)='\000',t-s;
}
template<class T=int>inline void write(T x){
	if(plen>=1000000)flush();
	if(!x)return pc('0'),void();
	if(x<0)pc('-'),x=-x;
	for(;x;x/=10)pstk[++ptop]=x%10;
	while(ptop)pc(pstk[ptop--]+'0');
}
inline void write(const char*s){
	if(plen>=1000000)flush();
	for(int i=0;(*(s+i))!='\000';pc(*(s+(i++))));
}
inline void write(char*const s){
	if(plen>=1000000)flush();
	for(int i=0;(*(s+i))!='\000';pc(*(s+(i++))));
}
const int Maxn=2e5+5,N=2e6+5;
int n,m;
int b[Maxn],s[Maxn],val[Maxn];
int h[N];
int head[Maxn],to[Maxn<<1],nxt[Maxn<<1],cnt1;
inline void add_e(int u,int v){
	to[++cnt1]=v;nxt[cnt1]=head[u];
	head[u]=cnt1;
}
int dfn[Maxn],cnt2,si[Maxn];
void dfs(int u,int v){
	dfn[u]=++cnt2;si[u]=1;
	for(int i=head[u];i;i=nxt[i]){
		int y=to[i];if(y==v)continue;
		dfs(y,u);si[u]+=si[y];
	}
}
int t[Maxn];
inline void add(int x,int d){
	for(;x<=n;x+=x&-x)t[x]+=d;
}
inline int query(int l,int r){
	int res=0;
	for(int x=r;x;x-=x&-x)res+=t[x];
	for(int x=l-1;x>0;x-=x&-x)res-=t[x];
	return res;
}
int d[Maxn],d1[Maxn];
void solve(int l,int r,int L,int R){
//	printf("%d %d:\n",l,r);
//	for(int i=L;i<=R;i++)printf("%d ",d[i]);
//	puts("");
	if(l==r){
		for(int i=L;i<=R;i++)val[d[i]]=l;
		return;
	}int mid=l+r>>1;
	for(int i=l;i<=mid;i++)add(dfn[h[i]],1);
	int tot1=L-1,tot2=R+1;
	for(int j=L;j<=R;j++){
		int i=d[j];
		if(query(dfn[i],dfn[i]+si[i]-1)>=b[i])d1[++tot1]=i;//,printf("[%d,%d]:%d\n",l,r,i);
		else d1[--tot2]=i;
	}
	for(int j=L;j<=R;j++)d[j]=d1[j];
	solve(mid+1,r,tot2,R);
	for(int i=l;i<=mid;i++)add(dfn[h[i]],-1);
	solve(l,mid,L,tot1);
}
vector<int>Q[Maxn];
int ans[N];
multiset<int>a[Maxn];
int t1[N];
inline void add1(int x,int d){
	x=-x;
	for(;x;x-=x&-x)t1[x]+=d;
}
inline int query1(int x){
	int res=0;
	for(;x<=m;x+=x&-x)res+=t1[x];
	return res;
}
void Dfs(int u,int v){
	if(!a[s[u]].empty())add1(*a[s[u]].begin(),-1);
	a[s[u]].insert(-val[u]);
	add1(*a[s[u]].begin(),1);
	for(int i:Q[u])ans[i]=query1(i);
	for(int i=head[u];i;i=nxt[i]){
		int y=to[i];if(y==v)continue;
		Dfs(y,u);
	}add1(*a[s[u]].begin(),-1);
	a[s[u]].erase(a[s[u]].find(-val[u]));
	if(!a[s[u]].empty())add1(*a[s[u]].begin(),1);
}
int main(){
//	freopen("P11295_4.in","r",stdin);
//	freopen("P11295.out","w",stdout);
	n=read();m=read();
	for(int i=1;i<=n;i++)b[i]=read(),val[i]=m,d[i]=i;
	for(int i=1;i<=n;i++)s[i]=read();
	for(int i=1;i<=m;i++)h[i]=read(),Q[h[i]].emplace_back(i);
	for(int i=1;i<n;i++){
		int u=read(),v=read();
		add_e(u,v);add_e(v,u);
	}
	dfs(1,0);
	solve(1,m,1,n);
	for(int i=1;i<=n;i++)if(!b[i])val[i]=0;
//	for(int i=1;i<=n;i++)printf("val[%d]=%d\n",i,val[i]);
	Dfs(1,0);
	for(int i=1;i<=m;i++)write(ans[i]),pc(' ');
	flush();
	return 0;
}
/*
10 10
3 3 3 5 6 9 3 1 7 3
10 10 5 3 7 6 1 10 6 6
2 6 2 7 3 6 6 5 3 4
1 4
6 7
7 9
8 7
3 6
8 10
3 1
6 2
5 2
*/
```