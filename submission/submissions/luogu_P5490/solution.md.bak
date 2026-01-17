# P5490 题解

# 扫描线
扫描线是一种求矩形面积并/周长并的好方法。~~**听说今年考到的概率还比较大（逃**~~

\[2020.03.23\] **更新：** CSP-S 2019并没有考到扫描线，脸好疼…

---

**扫描线**：假设有一条扫描线从一个图形的下方扫向上方（或者左方扫到右方），那么通过分析扫描线被图形截得的线段就能获得所要的结果。该过程可以用**线段树**进行加速。

# 面积并
**例题** [P5490](https://www.luogu.org/problem/P5490) / [POJ 1151](http://poj.org/problem?id=1151)

这两道题都是求**面积并**。

由于都是矩形，因此运用扫描线以后，面积的求法其实可以简化为 $\sum$截线段长度$\times$扫过的高度。这也是扫描线算法最基础的应用。

考虑以下这个简单的例子。

![image.png](https://img.ffis.me/images/2019/08/10/image.png)

问题在于如何才能模拟扫描线从下向上扫过图形，并且快速计算出当前扫描线被截得的长度。

现在假设，扫描线每次会在碰到横边的时候停下来，如图。

![image1cba39d5beb42edc.png](https://img.ffis.me/images/2019/08/10/image1cba39d5beb42edc.png)

简单来说，可对图形面积产生影响的元素，也就是这些横边左右端点的坐标。

为了快速计算出截线段长度，可以将横边赋上不同的权值，具体为：对于一个矩形，其下边权值为$1$，上边权值为$-1$。

![image805e198e60891448.png](https://img.ffis.me/images/2019/08/10/image805e198e60891448.png)

然后把所有的横边按照$y$坐标升序排序。这样，对于每个矩形，扫描线总是会**先碰到下边，然后再碰到上边**。那么就能保证扫描线所截的长度永远非负了。

这样操作以后，就可以和线段树扯上关系。先把所有端点在$x$轴上离散化（其实就是把所有点的横坐标存到$X[]$里，然后升序排个序，最后去重）。

![imagec6ca891e8480bea8.png](https://img.ffis.me/images/2019/08/10/imagec6ca891e8480bea8.png)

在这个例子中，$4$个端点的纵投影总共把$x$轴切割成了$5$部分。取中间的$3$部分线段，建立一棵线段树，其每个端点维护**一条线段**（也就是一个区间）的信息：
1. 该线段被覆盖了多少次（被多少个矩形所覆盖）。
2. 该线段内被整个图形所截的长度是多少。

![image0a03aa15aca4877e.png](https://img.ffis.me/images/2019/08/10/image0a03aa15aca4877e.png)

显然，只要一条线段被覆盖，那么它肯定被图形所截。所以，整个问题就转化为了一个**区间查询问题**，即：每次将 当前扫描线扫到的边 对应的信息 按照之前赋上的权值更新，然后再查询线段树根节点的信息，最后得到当前扫描线扫过的面积。这就可以用线段树来实现了（毕竟人家叫 **“线段”** 树嘛）。

### 下面是模拟的过程：

![imaged818935608ff1757.png](https://img.ffis.me/images/2019/08/10/imaged818935608ff1757.png)

![image65ecdba6bd78c3ce.png](https://img.ffis.me/images/2019/08/10/image65ecdba6bd78c3ce.png)

注：上图的$5$号节点的$sum=2$，绿色部分表示已计算的面积。

![image8f0d94e5f164aef1.png](https://img.ffis.me/images/2019/08/10/image8f0d94e5f164aef1.png)

![image82b25ef8956c45ad.png](https://img.ffis.me/images/2019/08/15/image.png)

还剩下一个棘手的问题：线段树到底该怎么建？保存什么信息？怎么在节点间传递信息？

这里我使用自己最习惯的线段树写法，个人感觉这样的逻辑最清晰。

先看下面的建树过程：
```cpp
void build_tree(int x, int l, int r) {
//	初始化节点信息
	if(l == r)
		return;
	int mid = (l + r) >> 1;
	build_tree(lson, l, mid);
	build_tree(rson, mid + 1, r);
	return;
}
```
我们已经知道，这棵线段树的每个节点都对应了一条线段。考虑将线段树上节点对应的区间和横边建立**映射关系**。先看对于一个叶子节点$x$，建树时保证了$tree[x].l=tree[x].r$，但其保存的信息很显然不可能只是某条线段的一个端点（如果一条线段的两个端点重合，那么它实质上仅是一个点）。再看一个节点的左右儿子，同样地，建树的时候已经保证了左右儿子的区间不会重合（交集为空），但是看这样两条相邻线段：$[1,2],[2,3],$你会发现$[1,2]\cap[2,3]=\{2\}$，也就是说左儿子的右端点和右儿子的左端点其实是重合的。所以如果想得太简单，就gg了。

考虑把线段树每个节点$x$对应的区间（$tree[x].l,tree[x].r$）不变，改变区间和横边的映射关系，具体为：节点$x$对应$[X[tree[x].l],\,X[tree[x].r+1]]$这条横边。可以看到，这里~~很机智地~~把右端点的对应关系给改了下，于是就兼容了。

自我感觉代码已经足够清晰了，注释还有其它解释。

**注意一下：** 变量名“$y1$”在<cmath>库里头有定义，会冲突，所以不开bits库就好。

### 这道题的代码：
```cpp
//  code for P5490
//  代码没有挖坑
#include <stdio.h>
#include <iostream>
#include <algorithm>
#define lson (x << 1)
#define rson (x << 1 | 1)
using namespace std;
const int MAXN = 1e6 + 10;
typedef long long ll;

int n, cnt = 0;
ll x1, y1, x2, y2, X[MAXN << 1];

struct ScanLine {
	ll l, r, h;
	int mark;
//  mark用于保存权值 (1 / -1)
	bool operator < (const ScanLine &rhs) const {
		return h < rhs.h;
	}
} line[MAXN << 1];

struct SegTree {
	int l, r, sum;
	ll len;
//  sum: 被完全覆盖的次数；
//  len: 区间内被截的长度。
} tree[MAXN << 2];

void build_tree(int x, int l, int r) {
//  我觉得最不容易写错的一种建树方法
	tree[x].l = l, tree[x].r = r;
	tree[x].len = 0;
	tree[x].sum = 0;
	if(l == r)
		return;
	int mid = (l + r) >> 1;
	build_tree(lson, l, mid);
	build_tree(rson, mid + 1, r);
	return;
}

void pushup(int x) {
	int l = tree[x].l, r = tree[x].r;
	if(tree[x].sum /* 也就是说被覆盖过 */ )
		tree[x].len = X[r + 1] - X[l];
//      更新长度        
	else
		tree[x].len = tree[lson].len + tree[rson].len;
//      合并儿子信息
}

void edit_tree(int x, ll L, ll R, int c) {
	int l = tree[x].l, r = tree[x].r;
//  注意，l、r和L、R的意义完全不同
//  l、r表示这个节点管辖的下标范围
//  而L、R则表示需要修改的真实区间
	if(X[r + 1] <= L || R <= X[l])
		return;
//  这里加等号的原因：
//  假设现在考虑 [2,5], [5,8] 两条线段，要修改 [1,5] 区间的sum
//  很明显，虽然5在这个区间内，[5,8] 却并不是我们希望修改的线段
//  所以总结一下，就加上了等号
	if(L <= X[l] && X[r + 1] <= R) {
		tree[x].sum += c;
		pushup(x);
		return;
	}
	edit_tree(lson, L, R, c);
	edit_tree(rson, L, R, c);
	pushup(x);
}

int main() {
	scanf("%d", &n);
	for(int i = 1; i <= n; i++) {
		scanf("%lli %lli %lli %lli", &x1, &y1, &x2, &y2);
		X[2 * i - 1] = x1, X[2 * i] = x2;
		line[2 * i - 1] = (ScanLine) {x1, x2, y1, 1};
		line[2 * i] = (ScanLine) {x1, x2, y2, -1};
//      一条线段含两个端点，一个矩形的上下边都需要扫描线扫过
	}
	n <<= 1;
//  直接把 n <<= 1 方便操作
	sort(line + 1, line + n + 1);
	sort(X + 1, X + n + 1);
	int tot = unique(X + 1, X + n + 1) - X - 1;
//  去重最简单的方法：使用unique！（在<algorithm>库中）
	build_tree(1, 1, tot - 1);
//  为什么是 tot - 1 ：
//  因为右端点的对应关系已经被篡改了嘛…
//  [1, tot - 1]描述的就是[X[1], X[tot]]
	ll ans = 0;
	for(int i = 1; i < n /* 最后一条边是不用管的 */ ; i++) {
		edit_tree(1, line[i].l, line[i].r, line[i].mark);
//      先把扫描线信息导入线段树
		ans += tree[1].len * (line[i + 1].h - line[i].h);
//      然后统计面积
	}
	printf("%lli", ans);
	return 0;
}
```

---

### POJ 1151的话…
把P5490代码改一改就过了，所以就不放了。

---
# 周长并
                        
**例题** [POJ 1177](http://poj.org/problem?id=1177)
                        
周长并比面积并还要麻烦些 ~~（画图也要麻烦些，所以我就偷懒了）~~，我直接拿POJ 1177的样例来举例子：

![imaged3ade113f8ed97a4.png](https://img.ffis.me/images/2019/08/10/imaged3ade113f8ed97a4.png)

观察这三条扫描线扫过的纵边，你会发现它比较变幻莫测，总结一下显然有这样一个有趣的现象：纵边总长度$=\sum2\times$被截得的线段条数$\times$扫过的高度。

再看这个：

![image875b5bc59b29c404.png](https://img.ffis.me/images/2019/08/10/image875b5bc59b29c404.png)

事情就更加 ~~恶心~~ 有趣了，你会发现横边总长度$=\sum|$上次截得的总长$-$现在截得的总长$|$。

所以和面积并比起来，周长并中的线段树还要维护 **线段的条数**。另外，横边和纵边需分别计算。

剩余的代码注释有讲。

```cpp
#include <iostream>
#include <stdio.h>
#include <algorithm>
#define lson (x << 1)
#define rson (x << 1 | 1)
using namespace std;
const int MAXN = 2e4;
int n, X[MAXN << 1];
int x1, y1, x2, y2, pre = 0; /* 先初始化为 0 */

struct ScanLine {
	int l, r, h, mark;
	if(h == rhs.h)
		return mark > rhs.mark;
    return h < rhs.h;
//		注意！这里是后来被 hack 掉以后加上去的
//		在此感谢 @leprechaun_kdl 指出问题
//		如果出现了两条高度相同的扫描线，也就是两矩形相邻
//		那么需要先扫底边再扫顶边，否则就会多算这条边
//		这个对面积并无影响但对周长并有影响
//		hack 数据：2 0 0 4 4 0 4 4 8 输出应为：24
} line[MAXN];

struct SegTree {
	int l, r, sum, len, c;
//  c表示区间线段条数
    bool lc, rc;
//  lc, rc分别表示左、右端点是否被覆盖
//  统计线段条数(tree[x].c)会用到
} tree[MAXN << 2];

void build_tree(int x, int l, int r) {
	tree[x].l = l, tree[x].r = r;
	tree[x].lc = tree[x].rc = false;
	tree[x].sum = tree[x].len = 0;
	tree[x].c = 0;
	if(l == r)
		return;
	int mid = (l + r) >> 1;
	build_tree(lson, l, mid);
	build_tree(rson, mid + 1, r);
}

void pushup(int x) {
	int l = tree[x].l, r = tree[x].r;
	if(tree[x].sum) {
		tree[x].len = X[r + 1] - X[l];
		tree[x].lc = tree[x].rc = true;
		tree[x].c = 1;
//      做好相应的标记
	}
	else {
		tree[x].len = tree[lson].len + tree[rson].len;
		tree[x].lc = tree[lson].lc, tree[x].rc = tree[rson].rc;
		tree[x].c = tree[lson].c + tree[rson].c;
//      如果左儿子左端点被覆盖，那么自己的左端点也肯定被覆盖；右儿子同理
		if(tree[lson].rc && tree[rson].lc)
			tree[x].c -= 1;
//      如果做儿子右端点和右儿子左端点都被覆盖，
//      那么中间就是连续的一段，所以要 -= 1
	}
}

void edit_tree(int x, int L, int R, int c) {
	int l = tree[x].l, r = tree[x].r;
	if(X[l] >= R || X[r + 1] <= L)
		return;
	if(L <= X[l] && X[r + 1] <= R) {
		tree[x].sum += c;
		pushup(x);
		return;
	}
	edit_tree(lson, L, R, c);
	edit_tree(rson, L, R, c);
	pushup(x);
}

ScanLine make_line(int l, int r, int h, int mark) {
	ScanLine res;
	res.l = l, res.r = r,
	res.h = h, res.mark = mark;
	return res;
}
//  POJ 不这样做就会CE，很难受

int main() {
	scanf("%d", &n);
	for(int i = 1; i <= n; i++) {
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		line[i * 2 - 1] = make_line(x1, x2, y1, 1);
		line[i * 2] = make_line(x1, x2, y2, -1);
		X[i * 2 - 1] = x1, X[i * 2] = x2;
	}
	n <<= 1;
	sort(line + 1, line + n + 1);
	sort(X + 1, X + n + 1);
	int tot = unique(X + 1, X + n + 1) - X - 1;
	build_tree(1, 1, tot - 1);
	int res = 0;
	for(int i = 1; i < n; i++) {
		edit_tree(1, line[i].l, line[i].r, line[i].mark);
		res += abs(pre - tree[1].len);
		pre = tree[1].len;
//      统计横边
		res += 2 * tree[1].c * (line[i + 1].h - line[i].h);
//      统计纵边
	}
	res += line[n].r - line[n].l;
//  特判一下枚举不到的最后一条扫描线
	printf("%d", res);
	return 0;
}
```
我觉得自己讲得够清晰了 (=$\small\triangledown$=)