# P2068 题解

这是一道单点修改，区间查询的线段树。

需要实现的操作有三个：建树，更新与查询。

首先，线段树用结构体维护，如下：

```cpp
struct node {
	int l, r;
	int val;
} tree[maxn * 4];
```

其中l, r表示节点所表示区间左右端点，而val则是区间和。

Build函数如下：

```cpp
void Build(int l, int r, int pos) {
	tree[pos].l = l;
	tree[pos].r = r;
	tree[pos].val = 0;
	if(l == r) return ;
	int mid = (l + r) / 2;
	Build(l, mid, pos * 2);
	Build(mid + 1, r, pos * 2 + 1);
}
```

这个函数就是初始化整棵线段树，没有什么特别需要解释的。

Update函数如下：

```cpp
void Update(int x, int val, int pos) {
	if(tree[pos].r == tree[pos].l) {
        tree[pos].val += val;
        return ;
    }
    
    int mid = (tree[pos].l + tree[pos].r) / 2;
    if(x <= mid) Update(x, val, pos * 2);
    else Update(x, val, pos * 2 + 1);
    tree[pos].val = tree[pos * 2].val + tree[pos * 2 + 1].val;
}
```

x表示需要修改的节点，val表示需要增加的值，pos表示当前节点。

如果走到了叶节点上，直接修改，然后结束。

否则，判断x在当前节点的哪一个儿子上，向下。

最后更新当前节点的值。

Query函数如下：

```cpp
int Query(int l, int r, int pos) {
	if(tree[pos].l >= l && tree[pos].r <= r) {
        return tree[pos].val;
    }
    int mid = (tree[pos].l + tree[pos].r) / 2;
    int ans = 0;
    if(l <= mid) ans += Query(l, r, pos * 2);
    if(mid < r) ans += Query(l, r, pos * 2 + 1);
    return ans;
}
```

如果当前节点的整个区间都已经被包含在所求的区间内了，那么不用再进行划分，返回区间值即可。

否则分三种情况讨论：

    1. 若所求区间只与左儿子有交集，移到左儿子。
    
    2. 若只与右儿子有交集，移到右儿子。
    
    3. 若被当前节点覆盖，左儿子右儿子都算。
    
    
以上就是思路及关键代码。

顺便推荐两道经典的单点修改题目（反正我是做了的）：

    1. HDU1166 敌兵布阵
    
    2. HDU1754 I hate it
    
    （注：第二道题是求区间最值，和模板稍有不同。）