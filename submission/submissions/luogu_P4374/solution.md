# P4374 题解

其实这题也可以不用树剖，先把新加的道路按照代价从小到大排个序，这样每次往上走的时候原来访问过的就可以直接跳过了（因为答案不会变得更优），这样直接就可以用类似并查集的方法就行了。
```cpp
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;
int ans[50010];
int n,m;
int par[50010][17];
int dep[50010];
int po[50010];
int to[50010];
vector<pair<int,int> >G[50010];
pair<int,pair<int,int> >roads[50010];
int getto(int x)
{
	if(to[x]==x)return x;
	return to[x]=getto(to[x]);
}
void dfs(int x,int p)
{
	for(int i=0;i<G[x].size();i++)
	{
		int y=G[x][i].first,id=G[x][i].second;
		if(y==p)continue;
		po[id]=y;
		par[y][0]=x;
		dep[y]=dep[x]+1;
		dfs(y,x);
	}
}
int lca(int x,int y)
{
	if(dep[x]<dep[y])swap(x,y);
	for(int i=16;i>=0;i--)if(dep[par[x][i]]>=dep[y])x=par[x][i];
	if(x==y)return x;
	for(int i=16;i>=0;i--)if(par[x][i]!=par[y][i])x=par[x][i],y=par[y][i];
	return par[x][0];
}
int main()
{
	scanf("%d%d",&n,&m);
	for(int i=1;i<n;i++)
	{
		int x,y;
		scanf("%d%d",&x,&y);
		G[x].push_back(make_pair(y,i));
		G[y].push_back(make_pair(x,i)); 
	}
	for(int i=1;i<=m;i++)
	{
		int x,y,z;
		scanf("%d%d%d",&x,&y,&z);
		roads[i]=make_pair(z,make_pair(x,y));
	}
	dep[0]=-1;
	dfs(1,0);
	for(int i=1;i<=16;i++)
	{
		for(int j=1;j<=n;j++)par[j][i]=par[par[j][i-1]][i-1];
	}
	for(int i=1;i<=n;i++)to[i]=i;
	for(int i=1;i<=n;i++)ans[i]=-1;
	sort(roads+1,roads+m+1);
	for(int i=1;i<=m;i++)
	{
		int v=roads[i].first;
		int x=roads[i].second.first,y=roads[i].second.second;
		int xy=lca(x,y);
		for(x=getto(x);dep[x]>dep[xy];x=getto(par[x][0]))
		{
			ans[x]=v;
			to[x]=par[x][0];
		}
		for(y=getto(y);dep[y]>dep[xy];y=getto(par[y][0]))
		{
			ans[y]=v;
			to[y]=par[y][0];
		}
	}
	for(int i=1;i<n;i++)printf("%d\n",ans[po[i]]);
	return 0;
}
```