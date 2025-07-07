# P3367 题解

>  _并查集是一种用于管理元素所属集合的数据结构，实现为一个森林，其中每棵树表示一个集合，树中的节点表示对应集合中的元素。_
> 
> ——摘自 [OI wiki](https://oi-wiki.org/ds/dsu/)

这是一道并查集的模板题，有四种不同的做法。

## 基础思路
在这道题目中，我们需要实现并查集的查询和合并操作。

在信息竞赛（以及其它大部分领域）中，并查集最常见的实现是**把一个集合抽象为一棵树**，树根即为该集合的“代表元素”。如图：

![](https://oi-wiki.org/ds/images/disjoint-set.svg)

这里有两个集合：$\{1,2,3,4, 5\},\{6,7,8\}$。

查询的实现方法很简单，即是找自身所在树的“代表元素”，或树根。显然，“代表元素”相同的两个元素处在同一个集合中。最朴素的做法是 $O(n)$ 的。

![](https://oi-wiki.org/ds/images/disjoint-set-find.svg)

如图，$4$ 号元素所在集合的代表元素是 $1$。

合并的实现是使得两个集合拥有同一个代表元素，一种简单的实现方法是将一个集合的根节点连接到另一个集合的根节点，这样，在两个集合中找根节点（代表元素）时都会找到同一个元素。

![](https://oi-wiki.org/ds/images/disjoint-set-merge.svg)

上图是合并的一个实例。

### $O(nm)$ 算法
朴素的查询与合并，时间复杂度都是 $O(n)$ 的。对于 $m$ 次查询显然有 $O(nm)$ 的复杂度。

下面是一些小技巧：
- 对于并查集，一种很好的存树方式是只存父亲，这样空间复杂度是 $O(n)$ 的，不可能再好了。
- 对于根节点，应该将其父亲设为一个辨识度高的值，如 `inf`。但最常见的实现方法是设为节点自身。
- 查找操作用递归实现最简单。

贴出一种实现：

```cpp
#include <bits/stdc++.h>
using namespace std;

const int N = 2e5+5;
int fa[N];
int n, m;

int find(int x){
	if(fa[x] == x) return x; // 已经是根节点 
	else return find(fa[x]); // 继续找 
}

int main(){
	cin >> n >> m;
	for(int i = 1; i <= n; ++i) fa[i] = i; // 初始化
	for(int i = 1; i <= m; ++i){
		int op, x, y;
		cin >> op >> x >> y;
		if(op == 1){ // 合并操作 
			x = find(x), y = find(y); // 查询各自的代表元素
			fa[x] = y; // 这里的合并顺序可以任意 
		}
		else{ // 查询操作的一种变形 
			x = find(x), y = find(y); // 查询各自的代表元素
			if(x == y) cout << "Y" << endl; // 是否在同一个集合
			else       cout << "N" << endl; 
		}
	} 
	return 0;
}

```

在这道题目中，这种做法只能获得 50 分。

## 两种常见优化
并查集的优化不止两种，具体可以看参考资料里的论文。这里重点讲**路径压缩优化**和**按秩合并优化**。

### 路径压缩优化
观察朴素的实现，可以发现一点：**并查集只关注集合的代表元素**。因此，我们可以在查询回溯时顺路把路过节点的父亲**直接指向代表元素**，这样下一次查询的时候就会快很多。这么讲可能不够直观，看图：

![](https://oi-wiki.org/ds/images/disjoint-set-compress.svg)

单独用路径压缩优化可以将均摊时间复杂度优化到 $O(\log n)$，可以通过本题。一种实现：


```cpp
#include <bits/stdc++.h>
using namespace std;

const int N = 2e5+5;
int fa[N];
int n, m;

int find(int x){
	if(fa[x] == x) return x;
	else return fa[x] = find(fa[x]); // 比起朴素代码只改了这里 
}

int main(){
	cin >> n >> m;
	for(int i = 1; i <= n; ++i) fa[i] = i; // 初始化
	for(int i = 1; i <= m; ++i){
		int op, x, y;
		cin >> op >> x >> y;
		if(op == 1){ // 合并操作 
			x = find(x), y = find(y); // 查询各自的代表元素
			if(x == y) continue; // 如果已经在同一个集合，跳过
			fa[x] = y; // 这里的合并顺序可以任意 
		}
		else{ // 查询操作的一种变形 
			x = find(x), y = find(y); // 查询各自的代表元素
			if(x == y) cout << "Y" << endl; // 是否在同一个集合
			else       cout << "N" << endl; 
		}
	} 
	return 0;
}

```

### 按秩合并优化
这里的“秩”可以指树的高度或树的节点数，不影响时间复杂度。按秩合并的主要思想是：**将小的结构合并到大的结构里**。这样，合并操作能劣化的节点也要少一些。

单独使用按秩合并优化也能将均摊时间复杂度优化到 $O(\log n)$。理论上按节点数合并慢于按高度合并。

这是按高度合并的实现：

```cpp
#include <bits/stdc++.h>
using namespace std;

const int N = 2e5+5;
int fa[N], siz[N];
int n, m;

int find(int x){
	if(fa[x] == x) return x; // 已经是根节点 
	else return find(fa[x]); // 继续找 
}

int main(){
	cin >> n >> m;
	for(int i = 1; i <= n; ++i) fa[i] = i, siz[i] = 1; // 初始化
	for(int i = 1; i <= m; ++i){
		int op, x, y;
		cin >> op >> x >> y;
		if(op == 1){ // 合并操作 
			x = find(x), y = find(y); // 查询各自的代表元素
			if(x == y) continue; // 如果已经在同一个集合，跳过
			if(siz[y] < siz[x]) swap(x, y); // 改变合并顺序
			if(siz[x] == siz[y]) siz[y] = siz[x]+1; // 计算新的秩：如果两个集合的秩相等，那么秩加一
			// 否则秩不变 
			fa[x] = y; // 合并 
		}
		else{ // 查询操作的一种变形 
			x = find(x), y = find(y); // 查询各自的代表元素
			if(x == y) cout << "Y" << endl; // 是否在同一个集合
			else       cout << "N" << endl; 
		}
	} 
	return 0;
}
```

这是按集合大小合并的实现：  
_写按集合大小合并的时候必须判断是否在同一个集合，否则时间复杂度会退化成 $O(n^2)$。_

```cpp
#include <bits/stdc++.h>
using namespace std;

const int N = 2e5+5;
int fa[N], siz[N];
int n, m;

int find(int x){
	if(fa[x] == x) return x; // 已经是根节点 
	else return find(fa[x]); // 继续找 
}

int main(){
	cin >> n >> m;
	for(int i = 1; i <= n; ++i) fa[i] = i, siz[i] = 1; // 初始化
	for(int i = 1; i <= m; ++i){
		int op, x, y;
		cin >> op >> x >> y;
		if(op == 1){ // 合并操作 
			x = find(x), y = find(y); // 查询各自的代表元素
			if(x == y) continue; // 如果已经在同一个集合，跳过
			if(siz[y] < siz[x]) swap(x, y); // 改变合并顺序
			siz[y] += siz[x]; // 计算新的秩
			fa[x] = y; // 合并 
		}
		else{ // 查询操作的一种变形 
			x = find(x), y = find(y); // 查询各自的代表元素
			if(x == y) cout << "Y" << endl; // 是否在同一个集合
			else       cout << "N" << endl; 
		}
	} 
	return 0;
}
```

## $O(m\alpha(n))$ 算法
 _在这里你只需要知道 $\alpha(n)$ 是一个近似于常数的函数，具体来说，对于 $n\le10^{2^{10^{19279}}}$，有 $\alpha(n)\le5$。_ 

显然两种优化并不矛盾，于是我们可以同时使用，让复杂度达到 $O(m\alpha(n))$。代码实现并不困难，优化叠上即可。

路径压缩+按高度合并实现：

```cpp
#include <bits/stdc++.h>
using namespace std;

const int N = 2e5+5;
int fa[N], siz[N];
int n, m;

int find(int x){
	if(fa[x] == x) return x; // 已经是根节点 
	else return fa[x] = find(fa[x]); // 继续找 
}

int main(){
	cin >> n >> m;
	for(int i = 1; i <= n; ++i) fa[i] = i, siz[i] = 1; // 初始化
	for(int i = 1; i <= m; ++i){
		int op, x, y;
		cin >> op >> x >> y;
		if(op == 1){ // 合并操作 
			x = find(x), y = find(y); // 查询各自的代表元素
			if(x == y) continue; // 如果已经在同一个集合，跳过
			if(siz[y] < siz[x]) swap(x, y); // 改变合并顺序
			if(siz[x] == siz[y]) siz[y] = siz[x]+1; // 计算新的秩：如果两个集合的秩相等，那么秩加一
			// 否则秩不变 
			fa[x] = y; // 合并 
		}
		else{ // 查询操作的一种变形 
			x = find(x), y = find(y); // 查询各自的代表元素
			if(x == y) cout << "Y" << endl; // 是否在同一个集合
			else       cout << "N" << endl; 
		}
	} 
	return 0;
}
```
路径压缩+按集合大小实现：

```cpp
#include <bits/stdc++.h>
using namespace std;

const int N = 2e5+5;
int fa[N], siz[N];
int n, m;

int find(int x){
	if(fa[x] == x) return x; // 已经是根节点 
	else return fa[x] = find(fa[x]); // 继续找 
}

int main(){
	cin >> n >> m;
	for(int i = 1; i <= n; ++i) fa[i] = i, siz[i] = 1; // 初始化
	for(int i = 1; i <= m; ++i){
		int op, x, y;
		cin >> op >> x >> y;
		if(op == 1){ // 合并操作 
			x = find(x), y = find(y); // 查询各自的代表元素
			if(x == y) continue; // 如果已经在同一个集合，跳过
			if(siz[y] < siz[x]) swap(x, y); // 改变合并顺序
			siz[y] += siz[x]; // 计算新的秩
			fa[x] = y; // 合并 
		}
		else{ // 查询操作的一种变形 
			x = find(x), y = find(y); // 查询各自的代表元素
			if(x == y) cout << "Y" << endl; // 是否在同一个集合
			else       cout << "N" << endl; 
		}
	} 
	return 0;
}
```
## 参考文献
1. [Tarjan, R. E., & Van Leeuwen, J. (1984). Worst-case analysis of set union algorithms. Journal of the ACM (JACM), 31(2), 245-281.](https://www.researchgate.net/publication/220430653_Worst-case_Analysis_of_Set_Union_Algorithms)
2. [OI wiki - 并查集](https://oi-wiki.org/ds/dsu/)，本文的所有配图也来自于此。

## 更新日志
- $\text{upd.2025.3.11}$ 初次提交审核。
- $\text{upd.2025.3.21}$ 因为按集合大小合并代码有误，因此修改，再次提交审核。感谢 @[LionBlaze](https://www.luogu.com.cn/user/911054) @[M1saka16I72](https://www.luogu.com.cn/user/422684) @[wanjiabao](https://www.luogu.com.cn/user/939957) @[lijunxi2026](https://www.luogu.com.cn/user/1078578) 指出了错误。