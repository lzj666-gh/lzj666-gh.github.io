# SP7734 题解

# TWIST - Twist and whirl - want to cheat （文艺平衡树板子）

此篇运用 FHQ-treap，如果不会普通的 FHQ-treap 请另行学习。

***
## 题目分析

普通的 `split` 函数是按**值**进行分裂的，文艺平衡树应按**元素的数量**分裂，即将前 $k$ 个元素分为一部分，其余的分为一部分。

### 输出答案
先不管怎样修改，怎样在最后输出答案呢？是用前序遍历、后序遍历还是中序遍历？

![](https://cdn.luogu.com.cn/upload/image_hosting/nvau0jkf.png)

观察一下这个图片，我们想从左向右输出，发现用**中序遍历**可以解决。

### 修改

还是上面那个例子，在不反转的时候，输出 $\mathtt{1\ 2\ 3\ 4\ 5}$，反转后就是 $\mathtt{5\ 4\ 3\ 2\ 1}$。

怎么处理？

![](https://cdn.luogu.com.cn/upload/image_hosting/zrilbsqh.png)

上面那个东西就是我们想要的，其实就是**交换这棵树内所有子树的左右儿子**，可以理解为左半区间的所有元素要到右半区间去，右半区间的所有元素要到左半区间，左子树就代表左半区间，右子树代表右半区间，所以交换左右子树就相当于交换左右区间（感性理解下QAQ）。

就有了一个初步的思路，找到代表目标区间的子树（通过对 `split` 函数的小修改，很容易就能做到），再将这棵子树的所有子树交换左右儿子。那一次修改就是 $O(r-l+1)$，复杂度爆炸。**区间修改**让我们想到**懒标记**（可以类比线段树），用到子节点时下传一下就行了。

细节见代码。

## 代码
```cpp
#include <bits/stdc++.h>

using namespace std;

int read() {
	int x;
	scanf("%d", &x);
	return x;
}

mt19937 rd(388651);// %5k

const int maxN = 1e5 + 7;

int root, tot;
struct Tree {
	int ls, rs;
	int siz, key;
	int val, tg = 0;
} t[maxN];
int add(int x) {
	t[++tot].siz = 1;
	t[tot].key = rd();
	t[tot].val = x;
	return tot;
}
void upd(int cur) {
	t[cur].siz = t[t[cur].ls].siz + t[t[cur].rs].siz + 1;
}
void down(int cur) {
	if (!t[cur].tg) return;
	swap(t[cur].ls, t[cur].rs);
	t[t[cur].ls].tg ^= 1;//tag为1为翻转，为0就不翻转。翻转后再翻转一次，就相当于没翻转。
	t[t[cur].rs].tg ^= 1;
	t[cur].tg = 0;
}
int merge(int x, int y) {
	if (!x || !y) return x | y;
	if (t[x].key <= t[y].key) {
		down(x);
		t[x].rs = merge(t[x].rs, y);
		upd(x);
		return x;
	} else {
		down(y);
		t[y].ls = merge(x, t[y].ls);
		upd(y);
		return y;
	}
}
void split(int cur, int k, int &x, int &y) {
	if (!cur) x = y = 0;
	else {
		down(cur);
		if (t[t[cur].ls].siz + 1 <= k)//按size分裂
			x = cur, split(t[cur].rs, k - t[t[cur].ls].siz - 1, t[cur].rs, y);
		else
			y = cur, split(t[cur].ls, k, x, t[cur].ls);
		upd(cur);
	}
}

int n, m;

void put(int cur) {
	if (!cur) return;
	down(cur);//别忘了下传懒标记！
	put(t[cur].ls);
	cout << t[cur].val << ' ';
	put(t[cur].rs);
}

int main() {
	n = read(); m = read();
	for (int i = 1; i <= n; i++)
		root = merge(root, add(i));
	
	while (m--) {
		int l = read(), r = read(), g = 0;//取出目标区间
		split(root, r, g, r);//先取出[1,r]和[r+1,n]
		split(g, l - 1, l, g);//再从[1,r]中取[1,l-1]和[l,r]
		t[g].tg ^= 1;//修改这个区间的tag
		root = merge(merge(l, g), r);
	}
	
	put(root);
}
```