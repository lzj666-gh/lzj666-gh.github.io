# P8710 题解

发现一个性质：最多只会合并 $n-1$ 次（类似树只有 $n-1$ 条边）。

于是在合并的时候暴力统计即可。

时间复杂度 $O(n^2+m)$。

建议使用路径压缩和启发式合并。

```cpp
# include <bits/stdc++.h>
using namespace std;
const int N=10000;
int f[N+10],siz[N+10];
int find(int x){
	if(f[x]==x){
		return x;
	}
	return f[x]=find(f[x]);
}
int val [N + 10], ans [N + 10];
int main () {
	int n,m;
	cin>>n>>m;
	for(int i=1;i<=n;++i){
		f[i]=i;
		siz[i]=1;
	}
	while(m--){
		int op,x,y;
		cin>>op>>x>>y;
		switch(op){
			case 1:{
				x=find(x);
				y=find(y);
				if(x!=y){
					for(int i=1;i<=n;++i){
						ans[i]+=val[find(i)];
					}
					for(int i=1;i<=n;++i){
						val[i]=0;
					}
					if(siz[x]>siz[y]) {
						swap(x,y);
					}
					f[x]=y;
					siz[y]+=siz[x];
				}
				break;
			}
			case 2:{
				x=find(x);
				val[x]+=y;
				break;
			}
		}
	}
	for(int i=1;i<=n;++i) {
		cout<<ans[i]+val[find(i)]<<" ";
	}
	return 0;
}
```