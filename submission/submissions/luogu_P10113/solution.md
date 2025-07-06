# P10113 题解

难度约为绿。

前置知识：倍增求最近公共祖先。

---
### 思路
将领导关系抽象为一棵树，要求的就是 $x_1,x_2,\dots,x_m$ 的所有公共祖先中编号最大的。

定义 $\operatorname{lca}(x_1,x_2,\dots,x_m)$ 表示 $x_1,x_2,\dots,x_m$ 的最近公共祖先。  

显然对于每次合作，如果不考虑编号，则 $\operatorname{lca}(x_1,x_2,\dots,x_m)$ 可以成为主持者。  
因此我们可以先求出 $\operatorname{lca}(x_1,x_2,\dots,x_m)$。

可以通过最近公共祖先的性质，求得 $\operatorname{lca}(x_1,x_2,\dots,x_m)=\operatorname{lca}(\operatorname{lca}(\operatorname{lca}(x_1,x_2),x_3)\dots,x_m)$。  

已知最近公共祖先后，所有能成为主持者的人必定都在 $0\sim\operatorname{lca}(x_1,x_2,\dots,x_m)$ 的这条链上，我们只需要求出这条链上编号最大的即可。  
在 dfs 时预处理前缀最大值，就能在后面的询问中 $O(1)$ 求出链上最大值。  

总时间复杂度为 $O(N+Qm\log N)$。

具体细节请看代码。

---
### 代码
```cpp
#include<bits/stdc++.h>
using namespace std;

int n,q,m;
int fa[100003][30];
int mx[100003],dep[100003];
int l2[100003];
vector<int>edg[100003];

void dfs(int x,int f,int mxn){
	if(x>mxn)mxn=x;
	mx[x]=mxn;  dep[x]=dep[f]+1;//预处理前缀最大值和深度
	if(x!=0){
		fa[x][0]=f;
		for(int i=1;i<=l2[dep[x]];i++)
			fa[x][i]=fa[fa[x][i-1]][i-1];//预处理2^i级祖先
	}
	for(int i=0;i<edg[x].size();i++)
		dfs(edg[x][i],x,mxn);//向下递归
}

int lca(int a,int b){
	if(dep[a]<dep[b])swap(a,b);
	while(dep[a]>dep[b]){//调平深度
		a=fa[a][l2[dep[a]-dep[b]]];
	}
	if(a==b)return a;//特判
	for(int i=l2[dep[a]];i>=0;i--){//求祖先
		if(fa[a][i]!=fa[b][i]){
			a=fa[a][i];
			b=fa[b][i];
		}
	}
	return fa[a][0];
}

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);cout.tie(0);
	cin>>n;
	l2[0]=-1;
	for(int i=1;i<n;i++){
		l2[i]=l2[i>>1]+1;//预处理对数
		int f;  cin>>f;
		edg[f].push_back(i);//连边
	}
	dfs(0,0,0);
	cin>>q;
	while(q--){
		int F,x;
		cin>>m>>F;
		while(--m){
			cin>>x;
			F=lca(F,x);
		}
		cout<<mx[F]<<'\n';
	}
	return 0;
}
```