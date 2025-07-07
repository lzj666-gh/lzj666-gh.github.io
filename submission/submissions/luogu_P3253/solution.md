# P3253 题解

### 题意：

有两堆物品，我们可以把两堆最上面的物品移到另一堆。当当前优先级最大的物品在堆顶的时候，我们可以将它拿走删掉。要求我们将两堆全部删掉，求所需的最少步数（删除物品操作不计入）。

### 题解：

我们首先考虑按照题意模拟。因为只有优先级最大的物品才可以移除，因此我们每一步的操作是可以确定下来的：我们找到优先级最大的物品，把它上面的物品都移到另一堆上，使其成为堆顶，然后删掉它。我们可以发现这种做法的正确性显然，于是我们 ~~A掉了这道题~~ 发现 $n^2$ 的复杂度显然不正确。

我们发现，我们将一串数从一个堆移向另一个堆之后，这串数字的顺序正好变成了原先的倒序。例如：$1,3,5,7$ 移动后就变成了 $7,5,3,1$ 。(按堆底到堆顶顺序)，~~此规律手玩可知，正确性显然~~。

我们考虑将两个堆的堆顶相接，无论我们是将堆内的数字移动还是删除，任意两个尚没被删掉的物品的相对位置是不变的。

我们可以使用一个变量来记录堆顶的位置，改变此变量相当于移动了堆顶物品。

可以看出：这个变量所指的地方会从初始处移向最大值，再移向次大值，次次大值……我们将其所指向的地方的物品删除，然后统计它再次移动时越过的物品数量即可。

#### 实现：

我们使用树状数组，将物品赋值为 $1$ ，删掉物品就减一变成$0$。我们可以很轻松的 O($logn$)的求出区间1的数量也就是区间和。因此整体复杂度为O($nlogn$)。

code：
```cpp
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
const int N=2e5;
int n,m;
struct node{
	int p,a;
	friend bool operator < (node a,node b) {return a.a > b.a;}
}arr[N];

int z[N];
void add(int x,int a) {for(int i = x;i <= n+m+1;i += i&-i) z[i] += a;}
int query(int x) {int ret = 0;for(int i = x;i >= 1;i -= i&-i) ret += z[i];return ret;}


int main()
{
	scanf("%d %d",&n,&m);
	for(int i = n;i >= 1;i --){
		int a;scanf("%d",&a);
		arr[i] = (node){i,a};
		add(i,1);
	}
	for(int i = n+2;i <= n+1+m;i ++){
		int a;scanf("%d",&a);
		arr[i] = (node){i,a};
		add(i,1);
	}
	sort(arr+1,arr+2+m+n);
	int s = n+1;
	long long ans = 0;
	for(int i = 1;i <= m+n;i ++){
		node tmp = arr[i];
		ans += abs(query(s)-query(tmp.p)) - (tmp.p>s);
		add(tmp.p,-1);s = tmp.p;
	}
	printf("%lld",ans);
	return 0;
}
```
#### 个人实现细节（大佬可略过此处）：

因为我不好判断初始指针位置，所以我在两个堆之间留了一个空位来放初始指针。

用树状数组求 l 与 r 之间的和一般应该是
```cpp 
query(r-1)-query(l)
```
而我的写法是：
```cpp
ans += abs(query(s)-query(tmp.p)) - (tmp.p>s);
```

由于指针变量处的物品已被删掉，所以我就判断一下 $r$ 是不是指针变量所指位置，不是的话就减一，因为最大值处一定有物品存在，我这样写可以少写几个 if 。~~(才不是因为一开始写错了呢！)~~