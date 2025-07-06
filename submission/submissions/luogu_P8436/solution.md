# P8436 题解

## 前言

> 作为一个连链式前向星都不会写的蒟蒻，我决定写一篇 vector 存图的题解，以造福后人。

**前置学习内容：[强连通分量](https://oi-wiki.org/graph/scc/)。**

### 定义

- 连通图：任意两个结点都可以相互到达的**无向图**。
- 桥：一张连通图中，如果删去任意一条边会导致图不连通，则这条边就称为桥。
- 边双连通图：一个没有桥的连通图。
- 边双连通分量：极大的边双连通子图。

## 算法过程

这个边双连通分量和强连通分量十分类似，强连通分量其实就是把环缩起来，而边双连通分量也是一个环。（因为在环上，就算删去一条边，也一定还有另一条边可以连接）

求强连通分量的代码如下：

```cpp
int cnt, ssum;
int dfn[MAXN], low[MAXN], scc[MAXN];
vector<int> e[MAXN];
bitset<MAXN> ins;
stack<int> st;

void tarjan(int x){
    low[x] = dfn[x] = ++cnt;
    st.push(x);
    ins.set(x);
    for (auto i: e[x]){
        if (!dfn[i]){
            tarjan(i);
            low[x] = min(low[x], low[i]);
        }else if (ins.test(i)){
            low[x] = min(low[x], dfn[i]);
        }
    }
    if (dfn[x] == low[x]){
        scc[x] = ++ssum;
        while (st.top() != x){
            scc[st.top()] = ssum;
            ins.reset(st.top());
            st.pop();
        }
        st.pop();
        ins.reset(x);
    }
}
```

而边双连通分量其实更加简单，因为是无向图，所以不需要考虑横叉边，因此不需要 `ins` 来判断是否在栈中，而是直接 `else`。

然后，无向图的边我们一般看成是两条有向图的边，但是这样就会导致一个问题，就是这样会被看成是一个环。所以我们需要加一个判断：不能访问上一个被访问过的结点。

然后答案可以用一个二维 vector 存起来。

给个代码：

```cpp
int cnt;
int dfn[MAXN], low[MAXN];
set<int> e[MAXN];
vector<vector<int>> ans;
stack<int> st;

void tarjan(int x, int las){
	low[x] = dfn[x] = ++cnt;
	st.push(x);
	for (auto i: e[x]){
		if (i == las) continue;
		if (!dfn[i]){
			tarjan(i, x);
			low[x] = min(low[x], low[i]);
		}else low[x] = min(low[x], dfn[i]);
	}
	if (dfn[x] == low[x]){
		vector<int> vec;
		vec.push_back(x);
		while (st.top() != x){
			vec.push_back(st.top());
			st.pop();
		}
		st.pop();
		ans.push_back(vec);
	}
}
```

可是这个代码只能拿到 $50$ 分：[评测记录](https://www.luogu.com.cn/record/112742048)。为什么呢？

通过下载数据可以发现，数据是有**重边**的，而重边就可以往回走了。但是我们这个判断就直接把这个机会给“杀死”了。

因此，我们不能根据顶点来判断，而是要根据边来判断，条件是**不能走上一次走过的边**。我们为了判边，就需要给 vector 多绑上一个 `int` 保存边的编号以判断。

这样就可以 AC 本题了！代码如下：

```cpp
#include <bits/stdc++.h>
using namespace std;
#define MAXN 500001

int n, m, u, v, cnt;
int dfn[MAXN], low[MAXN];
vector<pair<int, int>> e[MAXN];
vector<vector<int>> ans;
stack<int> st;

void tarjan(int x, int las){
	low[x] = dfn[x] = ++cnt;
	st.push(x);
	for (auto i: e[x]){
		if (i.second == (las ^ 1)) continue;
		if (!dfn[i.first]){
			tarjan(i.first, i.second);
			low[x] = min(low[x], low[i.first]);
		}else low[x] = min(low[x], dfn[i.first]);
	}
	if (dfn[x] == low[x]){
		vector<int> vec;
		vec.push_back(x);
		while (st.top() != x){
			vec.push_back(st.top());
			st.pop();
		}
		st.pop();
		ans.push_back(vec);
	}
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	
	cin >> n >> m;
	for (int i(1); i<=m; ++i){
		cin >> u >> v;
		e[u].push_back(make_pair(v, i<<1));
		e[v].push_back(make_pair(u, i<<1|1));
	}
	for (int i(1); i<=n; ++i){
		if (!dfn[i]) tarjan(i, 0);
	}
	
	cout << ans.size() << '\n';
	for (auto i: ans){
		cout << i.size() << ' ';
		for (auto j: i) cout << j << ' ';
		cout << '\n';
	}
	
	return 0;
}
```

我本以为这个会跑得很慢，没想到居然比随机抽的一篇幸运题解还要快：[我的记录](https://www.luogu.com.cn/record/112755622)|[TA 的记录](https://www.luogu.com.cn/record/112757205)。