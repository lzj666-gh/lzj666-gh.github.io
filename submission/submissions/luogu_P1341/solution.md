# P1341 题解

这是我这个小蒟蒻第一次敲欧拉回路，于是参照了一波题解。同时也发现好像就没有题解判断了图是否联通。因此在这里呼吁一下，加强一下数据好吧。

思路就不会说了吧，每读入两个字母就给这两个字母连一条无向边，跑一边欧拉回路就行了。

下面是代码：（欧拉回路我主要是参照了第一篇题解，然后判断图是否联通我用了并查集维护了一下。）
```
#include<bits/stdc++.h>
using namespace std;
#define res register int
#define LL long long
#define inf 0x3f3f3f3f
inline int read(){
	int s=0,w=1;
	char ch=getchar();
	while(ch<'0'||ch>'9'){if(ch=='-')w=-1;ch=getchar();}
	while(ch>='0'&&ch<='9')s=s*10+ch-'0',ch=getchar();
	return s*w; 
}
const int N=257;
int G[N][N],depth[N],n,cnt,hen,f[N],sum[N];
char tmp[N],rb[N*N]; 
inline void dfs(int x){
	for(res i=0;i<N;i++)
		if(G[x][i])G[x][i]=G[i][x]=0,dfs(i);
	rb[n--]=x;
}
inline int find(int x){
	if(f[x]!=x)f[x]=find(f[x]);
	return f[x];
}
int main(){
	n=read();
	for(res i=0;i<N;i++)f[i]=i;
	for(res i=1;i<=n;i++){
		scanf("%s",tmp);
		G[tmp[0]][tmp[1]]=G[tmp[1]][tmp[0]]=1;
		int fx=find(tmp[0]),fy=find(tmp[1]);
		f[fx]=fy;
        depth[tmp[0]]++;
        depth[tmp[1]]++;
	}
	int ans=0;
	for(res i=0;i<N;i++)if(f[i]==i&&depth[i])ans++;
	if(ans!=1){puts("No Solution");return 0;}
	for(res i=0;i<N;i++)
		if(depth[i]&1){
		    cnt++;
			if(!hen)hen=i;
		}
	if(!hen)
	    for(res i=0;i<N;i++)
		    if(depth[i]){hen=i;break;}
	if(cnt&&cnt!=2){puts("No Solution");return 0;}
	dfs(hen);
	puts(rb);
	return 0;
}
```