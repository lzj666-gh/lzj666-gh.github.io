# P6154 题解

感谢 [Feecle_6418] (https://www.luogu.com.cn/user/42156) 提供本题。

题意:给定一个有向无环图，求其中一条路径长度的期望。

一条路径长度的期望 $=$ $\dfrac{sum}{cnt}$。

其中 $sum$ 代表所有路径长度的总和， $cnt$ 代表路径的个数。

记忆化搜索，令 $f_i$ 表示从 $i$ 开始的路径长度和， $g_i$ 表示从 $i$ 开始的路径条数。

则 $f_i=\sum\limits_{edge(i,j)}f_j+g_j$（每条路径都变长 $1$）

$g_i=1+\sum\limits_{edge(i,j)}g_j$（所有路径加上自己到自己）

答案即为 $\dfrac{\sum f_i}{\sum g_i}$。

$std$ $by$ [Feecle_6418](https://www.luogu.com.cn/user/42156)

```cpp
//100 points
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
#define mod 998244353ll
using namespace std;
struct Edge{
	int to,next;
}e[700005];
int cnt,h[100005],n,m;
long long f[100005],g[100005],s1,s2;
//f:路径长度和
//g:路径数
void Add_Edge(int x,int y){
	e[++cnt].to=y;
	e[cnt].next=h[x];
	h[x]=cnt;
}
void DP(int now){
	if(g[now])return ;
	g[now]=1;
	for(int i=h[now];i;i=e[i].next){
		int y=e[i].to;
		DP(y);
		(g[now]+=g[y])%=mod;
		(f[now]+=f[y]+g[y])%=mod;
	}
}
long long Power(long long x,long long y,long long z){
	long long ret=1;
	while(y){
		if(y&1)ret=ret*x%z;
		y>>=1;
		x=x*x%z;
	}
	return ret;
}
int main(){
	scanf("%d%d",&n,&m);
	for(int i=1,x,y;i<=m;i++){
		scanf("%d%d",&x,&y);
		Add_Edge(x,y);
	}
	for(int i=1;i<=n;i++)if(!g[i])DP(i);
	for(int i=1;i<=n;i++)(s1+=f[i])%=mod,(s2+=g[i])%=mod;
	printf("%lld\n",s1*Power(s2,mod-2,mod)%mod);
	return 0;
}
```
