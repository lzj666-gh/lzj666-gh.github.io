# P10996 题解

# C. Tuple 官方题解

本题考察的主要知识点：

- 【1】枚举法
- （yummy 做法）【4】vector
- （yummy 做法）【4】指针

## 暴力做法

### 20 分

枚举四个点 $a,b,c,d$，检查四个三元组是否都存在。

时间复杂度 $O(n^4)\sim O(n^4 m)$ 不等，取决于你使用 `vector`、`set` 还是 `unordered_set` 存储所有的边。后两者不在 J 组考纲内，所以有一个办法使用 `bool` 数组解决。

如果我们开一个数组 $ex_{b,c,a}$ 表示 $(a,b,c)$ 是否存在，那么空间复杂度为 $O(n^3)$，但是大部分 $ex_{x,y}$ 都是全空的，非常浪费。我们可以开一个 `bool *ex[2005][2005];`，然后某条 $(a,b,c)$ 加入时，如果 `ex[a][b]` 已经存在就把 `ex[b][c][a]` 设成 $1$，如果不存在就先 `new` 一个。

这样一共只有 $m$ 个 `bool[2005]` 真实存在，空间复杂度 $O(nm)$。

### 32 分

枚举两条边 $p,q$，判断 $p,q$ 是否拥有相同的 $u,v$（记为 $a,b$），记 $p,q$ 的第三个数分别为 $c,d$，检查 $(a,c,d)$ 和 $(b,c,d)$ 是否存在。时间复杂度 $O(m^2)$。

## 正解

### yummy 法

和 32 分类似的做法，但是优化枚举 $p,q$ 的过程。

记录 $eg_{a,b}$ 表示所有 $(a,b,c)$ 中的 $c$ 构成的 `vector`。

四重循环，外两层循环枚举 $(a,b)$，内两层循环在 $eg_{a,b}$ 内枚举 $c,d$，然后使用 20 分思路里压缩空间的方法，可以做到空间都 $O(nm)$、单次查询 $O(1)$。

虽然看上去有四重循环，但是事实上每个三元组最多和 $n$ 个三元组产生一次查询，所以时间复杂度 $O(nm)$。

```cpp
#include<bits/stdc++.h>
using namespace std;
int n,m,cnt=0;
vector<int> eg[2005][2005];
bool *ex[2005][2005];
int main(){
	scanf("%d%d",&n,&m);
	for(int i=1;i<=m;i++){
		int u,v,w;
		scanf("%d%d%d",&u,&v,&w);
		eg[u][v].emplace_back(w);
		if(ex[v][w]==nullptr){
			ex[v][w]=new bool[2005];
			memset(ex[v][w],0,2005);
		}
		ex[v][w][u]=1;
	}
	for(int a=1;a<n;a++)
		for(int b=a+1;b<=n;b++){
			sort(eg[a][b].begin(),eg[a][b].end());
			for(int cc=0;cc<eg[a][b].size();cc++)
				for(int dd=cc+1;dd<eg[a][b].size();dd++){
					int c=eg[a][b][cc],d=eg[a][b][dd];
					if(ex[c][d]!=nullptr && ex[c][d][a] && ex[c][d][b])
						cnt++;
				}
		}
	cout<<cnt<<endl;
	return 0;
}
```

### EA 法

然而事实上不需要这么麻烦。

考虑先枚举 $a$。枚举 $a$ 的时候，你可以 $O(m)$ 地维护一个桶 $c_{x,y}$，使得 $c_{x,y}$ 记录 $(a,x,y)$ 是否存在。然后枚举 $(u,v,w)$，如果 $c_{u,v},c_{v,w},c_{u,w}$ 都为 true，则 $(a,u,v,w)$ 是一个合法数对。

时间复杂度 $O(nm)$，空间复杂度 $O(n^2)$。

```cpp
#include<bits/stdc++.h>
using namespace std;
int n,m,u[50005],v[50005],w[50005],cnt=0;
bool c[2005][2005];
int main(){
	scanf("%d%d",&n,&m);
	for(int i=1;i<=m;i++)
		scanf("%d%d%d",&u[i],&v[i],&w[i]);
	for(int a=1;a<=n;a++){
		for(int i=1;i<=m;i++)
			if(u[i]==a)
				c[v[i]][w[i]]=1;
		for(int i=1;i<=m;i++)
            if(c[u[i]][v[i]] && c[v[i]][w[i]] && c[u[i]][w[i]])
                cnt++;
		for(int i=1;i<=m;i++)
			if(u[i]==a)
				c[v[i]][w[i]]=0;
	}
	cout<<cnt;
	return 0;
}
```