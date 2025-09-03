# P2880 题解

## 线段树都有了，怎能少了树状数组？？

那我来补一发。

其实这道题有很多种解法，也有写$ST$表的，而且貌似时间复杂度还比较优秀。

但是多一种解法毕竟是好事，可以从不同角度去做一道题。

有一位巨佬也用的树状数组，~~但是貌似只贴了个代码~~，我这里还是发一下详细的题解，毕竟有些人可能不知道如何维护最大最小值。

## 进入正题：

既然明说了需要树状数组，那么肯定要知道树状数组是什么

**不知道树状数组是什么的童鞋们[戳这戳这戳这QWQ](https://www.luogu.org/blog/stonejuice/post-xue-xi-bi-ji-shu-zhuang-shuo-zu)**

阅读题面，很容易就可以发现题目要求区间查询最大值与最小值的差。

那么我们就用两个树状数组，分别维护所有数据的最大值和最小值。

- **树状数组必备：求$lowbit$：**

这个就不过多赘述了，应该都懂。

```cpp
int lowbit(int x)
{
    return x & -x;
}
```

- **建树，维护最大最小值**

首先从建树开始。

前面我们提到过，我们使用两个树状数组维护最大值和最小值，**我们姑且把维护最大值的树状数组定义为$treex$，维护最小值的则定义为$treen$**

那么，在向上传递的过程中，我们每传递一层，就比较一次，更新一次点。

这里打个比方：

- 1、
```
| 输入的数据 | 1 | / | / | / | / | / | / | / |
| 下标i     | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| treex[i]  | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| treen[i]  | 1 | 1 |inf| 1 |inf|inf|inf| 1 |
```
- 2、
```
| 输入的数据 | 1 | 5 | / | / | / | / | / | / |
| 下标i     | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| treex[i]  | 1 | 5 | 0 | 5 | 0 | 0 | 0 | 5 |
| treen[i]  | 1 | 1 |inf| 1 |inf|inf|inf| 1 |
```
- 3、
```
| 输入的数据 | 1 | 5 | 3 | / | / | / | / | / |
| 下标i     | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| treex[i]  | 1 | 5 | 3 | 5 | 0 | 0 | 0 | 5 |
| treen[i]  | 1 | 1 | 3 | 1 |inf|inf|inf| 1 |
```
- 4、
```
| 输入的数据 | 1 | 5 | 3 | 9 | / | / | / | / |
| 下标i     | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| treex[i]  | 1 | 5 | 3 | 9 | 0 | 0 | 0 | 9 |
| treen[i]  | 1 | 1 | 3 | 1 | inf | inf | inf | 1 |
```
- 5、
```
| 输入的数据 | 1 | 5 | 3 | 9 | 4 | / | / | / |
| 下标i     | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| treex[i]  | 1 | 5 | 3 | 9 | 4 | 4 | 0 | 9 |
| treen[i]  | 1 | 1 | 3 | 1 | 4 | 4 | inf | 1 |
```
- 6、
```
| 输入的数据 | 1 | 5 | 3 | 9 | 4 | 2 | / | / |
| 下标i     | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| treex[i]  | 1 | 5 | 3 | 9 | 4 | 4 | 0 | 9 |
| treen[i]  | 1 | 1 | 3 | 1 | 4 | 2 | inf | 1 |
```
- 7、
```
| 输入的数据 | 1 | 5 | 3 | 9 | 4 | 2 | 11 | / |
| 下标i     | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| treex[i]  | 1 | 5 | 3 | 9 | 4 | 4 | 11 | 12 |
| treen[i]  | 1 | 1 | 3 | 1 | 4 | 2 | 11 | 1 |
```
- 8、
```
| 输入的数据 | 1 | 5 | 3 | 9 | 4 | 2 | 11 | 14 |
| 下标i     | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| treex[i]  | 1 | 5 | 3 | 9 | 4 | 4 | 11 | 14 |
| treen[i]  | 1 | 1 | 3 | 1 | 4 | 2 | 11 | 1 |
```
- $END$

就像刚刚那样，每次传递最大值与最小值（就是把求区间和树状数组中的累加改为了求最值）

建树代码：

```cpp
void _add(int x, int k)//建树QAQ 
{
    for(;x <= n; x += lowbit(x))
    {
    	treex[x] = max(treex[x], k);
    	treen[x] = min(treen[x], k);
    }
}
```

- **区间查询最大值与最小值**

我们刚刚说过，建树时可以直接套区间和的板子，只需要把累加改成求最值就可以了。

但是求最大值与最小值不行。因为他没有像求区间和那样的性质。

**因为区间合中，要查询$[x,y]$的区间合，是求出$[1,x-1]$的合与$[1,y]$的合，然后相减就得出了$[x,y]$区间的合。**

但是很明显，求最值是不能相减求得的，这个时候我们就要想另外一种办法。

我们这里分两中情况讨论

- 1、 $y-lowbit(y) > x$ ，这种情况下，**我们可以把求$[x,y]$区间的最值拆分成两部分，先求$[x,y-lowbit(y)]$中最值与$[y-lowbit(y)+1,y]$中的最值，再求这两者的最值。**

	稍微细心一点，就可以发现 $[y-lowbit(y)+1,y]$ 就是$tree[y]$（可以口模一下）。
    
   于是，问题就转化为：求 $[x,y-lowbit(y)]$中最值 与 $tree[y]$的最值。
   
- 2、$y-lowbit(y) < x$，在这种情况下，**我们直接把 a[y]（第$y$个输入的数据）给剥离出来，于是原问就变成了：求 $[x,y-1]$中最值 与 $a[y]$ 的最值。**

这两种情况想明白之后，就可以用**递归**解决问题了。

**递归到某一层时，$x == y$，这个时候返回 $a[x]$ 或 $a[y]$ 就行了。（毕竟 $x == y$时，区间$[x,y]$就只有$a[x]$这一个数据了）**

贴这部分的代码：

```cpp
//下面两个子函数本质上是一样的

int _findmax(int x, int y)//区间查询最大值 
{ 
	if(y > x)
	{
		if(y - lowbit(y) > x) return max(treex[y], _findmax(x, y - lowbit(y)));
		else return max(a[y], _findmax(x, y - 1));//如上所述
	}
	return a[x];
}

int _findmin(int x, int y)//区间查询最小值 
{ 
	if(y > x)
	{
		if(y - lowbit(y) > x) return min(treen[y], _findmin(x, y - lowbit(y)));
		else return min(a[y], _findmin(x, y - 1));
	}
	return a[x];
}
```

- **合并代码**

上面这两个处理完之后，就可以合并代码了。

毕竟这里没有什么单点修改之类的操作。

这里有一个要注意的点：**$treen$（维护最小值的树状数组）最开始要全部赋值为$inf$。毕竟是存最小值。而$treex$（维护最大值的树状数组）就不管了，因为没有数据小于$0$。**（实际上建树的表格里就体现出这一点了）

**最后按照题目要求来，用区间最大值减去最小值就可以了。**

## 上代码！

```cpp
#include<bits/stdc++.h>
#define mian main
#define QWQ puts("QWQ");
using namespace std;

int n, m;
int a[50005] ,treex[50005], treen[50005];

int lowbit(int x)//求lowbit:2进制下末尾0的个数。可表示tree中包含数据数量 
{
    return x & -x;
}

void _add(int x, int k)//建树QAQ 
{
    for(;x <= n; x += lowbit(x))
    {
    	treex[x] = max(treex[x], k);
    	treen[x] = min(treen[x], k);
    }
}

int _findmax(int x, int y)//区间查询最大值 
{ 
	if(y > x)
	{
		if(y - lowbit(y) > x) return max(treex[y], _findmax(x, y - lowbit(y)));
		else return max(a[y], _findmax(x, y - 1));
	}
	return a[x];
}

int _findmin(int x, int y)//区间查询最小值 
{ 
	if(y > x)
	{
		if(y - lowbit(y) > x) return min(treen[y], _findmin(x, y - lowbit(y)));
		else return min(a[y], _findmin(x, y - 1));
	}
	return a[x];
}

int main()
{
    memset(treen, 0x3f3f3f3f, sizeof(treen));
	scanf("%d%d", &n, &m);
    for(int i = 1; i <= n; i ++) 
    {
        scanf("%d", &a[i]);
        _add(i, a[i]);
    }
    for(int i = 1; i <= m; i ++)
    {
        int l, r;
        scanf("%d%d", &l, &r);
        cout << _findmax(l, r) - _findmin(l, r) << endl;
    }
    return 0;
}
```

~~（悄悄求赞，应该没人发现我QAQ）~~