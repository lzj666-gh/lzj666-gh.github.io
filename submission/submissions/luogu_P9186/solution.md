# P9186 题解

# 超详细的图解题解！！

~~你肯定看得明白的，对吧~~

## 简要题意

给定数组 $a_1,...,a_N$ 在数组中依次选出一个元素构成排列 $b_1,...,b_N$ 。定义 $T = \sum _{i=1} ^N i \times b_i $ 。现在给出 $Q$ 个操作，每个操作有两个数 $x$ 和 $y$ 表示将 $a_x$ 替换成 $y$ ，对于每一个操作求出操作后的 $T$ 的最大值，每次操作后数组还原成原样。

## 思路

不难发现， $T$ 的最大值是将 $a$ 排序后得到的 $\sum _{i=1} ^N i \times b_i$ ，因此，我们可以先将 $a$ 的元素赋给 $b$ ，然后 `sort(b)` ，记 $P_{a_i}$ 表示 $a$ 数组排序 $a_i$ 后所在位置下标，并算出不进行操作时的最大值，用变量 $sum$ 储存。

接下来考虑操作时的 $T$ 变化情况。以样例一的第三次操作举例：
![](https://huatu.98youxi.com/markdown/work/uploads/upload_aa8ca29e0e502d93679a9842c9d1afb2.png)

![](https://huatu.98youxi.com/markdown/work/uploads/upload_857c8350b963af34f66caaa7a03e70ab.png)

先用二分找到新插入的 $y$ 在数组 $b$ 中应该在的位置，记 `pos=upper_bound(b, y)` 。**注意一定要用 `upper_bound` 而不是 `lower_bound` 不然找到的下标不一致！！（也就是无论 $b$ 中之前有没有 $y$ 这个元素，我们都要找到从左往右第一个严格大于 $y$ 的元素下标）**

![](https://huatu.98youxi.com/markdown/work/uploads/upload_d75f0df191e3cb508d4485d68351aade.png)

操作后：

![](https://huatu.98youxi.com/markdown/work/uploads/upload_85e338e9d6f4e5b2ace13e5219352578.png)

可以发现，此时的 $T$ 比原来减少了 $a_x \times  P_{a_x}$ 也正是被替换掉的元素 $a_x$ 乘 $a_x$ 在 $b$ 中的下标。

此时再把 $P_{a_x}$ 以后的元素向左移动一个下标（不包括 $P_{a_x}$ ），也就是将 $T$ 减去 $P_{a_x}$ 以后的数的和，这里用前缀和数组 $s$ 优化后 $T$ 就比原来小了 $s_n - s_{P_{a_x}}$ ：

![](https://huatu.98youxi.com/markdown/work/uploads/upload_cbc5b868802673eb01701026d7e3033d.png)



那么如何计算把新加入的元素 $y$ 插入 $pos$ 后 $T$ 的变化呢？很简单，首先把 $y$ 插入后的 $T$ 的值求出来， $T$ 比原来大了 $y \times pos$ █ **但是一定要注意，如果 $pos$ 在 $P_{a_x}$ 右边（不包含 $P_{a_x}$ ） $T$ 就要变大 $y \times (pos-1)$ ，因为 $P_{a_x}$ 被删掉后， $pos$ 一定也会向左平移一个下标！！！**

然后将 $pos$ 以后（包括 $pos$ ）的所有数向右平移一个下标， $T$ 就比原来大了 $s_n - s_{pos-1}$ **这里也要注意，如果 $pos$ 在 $P_{a_x}$ 左边，（包括 $P_{a_x}$ ） $T$ 就要减小 $b_{P_{a_x}}$ 因为当 `pos <= p[a[x]]` 时将 $T$ 增加 $s_n - s_{pos-1}$ 会把曾经已经删除的 $b_{P_{a_x}}$ 加回来，然而它已经被删除了，就要减回去。**


![](https://huatu.98youxi.com/markdown/work/uploads/upload_639e7b86347969931c603c24992de9ef.png)


~~如果你没看懂上面的就来看这个吧~~

形式化的，对于该样例：

$$ T = 1 \times b_1 + 2 \times b_2 + 3 \times b_3 + 4 \times b_4 + 5 \times b_5 $$

先删除 $a_4$ ，也就是删除 $b_{P_{a_4}} = b_2$：

$$ T = 1 \times b_1 + 3 \times b_3 + 4 \times b_4 + 5 \times b_5 $$

可以发现 $T$ 减少了 $2 \times b_2$ 也就是 $2 \times b_{P_{a_x}}$ 及 `T-=2*b[P[a[x]]];`

然后将 $P_{a_{x}}$ 后的所有数的系数减一（相当于向左平移一个下标），得到：

$$ T = 1 \times b_1 + 2 \times b_3 + 3 \times b_4 + 4 \times b_5 $$

利用前缀和优化，发现 $T$ 减少了 $s_n - s_{P_{a_x}}$

用 `upper_bound` 找到 $pos = 4$ 然后计算出插入 $y$ 之后 $T$ 的变化：

$$ T =  1 \times b_1 + 2 \times b_3 + 3 \times b_4 + pos \times y + 4 \times b_5$$

$$ =1 \times b_1 + 2 \times b_3 + 3 \times b_4 + 4 \times y + 4 \times b_5 $$

$T$ 比原来大了 $pos \times y$ ，**注意这里要进行判断，具体判断方法参照黑色方框处（█）。**

最后将 $pos$ 右面的所有系数加一（相当于向右平移一个下标），得到：

$$ T = 1 \times b_1 + 2 \times b_3 + 3 \times b_4 + 4 \times y + 5 \times b_5 $$

$T$ 比原来大了 $s_n - s_{pos-1}$ ，**这里同样要注意特判，参照上方黑色方框处。**

最后得到的结果就是：

```cpp
T-=a[x]*P[a[x]];
T-=s[n]-s[P[a[x]]];
T+=y*(pos-(pos > P[a[x]]));
T+=s[n]-s[pos-1];
if(pos <= P[a[x]])	ans-=b[P[a[x]]];
```

## 代码（代码中的 $ans$ 就是 $T$ ）
忽略掉前面的快排，最终时间复杂度 $\Theta(Q \log n)$


```cpp
#include <bits/stdc++.h>
#define ll long long
#define setp setprecision
#define mem(a, m) memset(a, m, sizeof(a));
using namespace std;

ll n; 
ll Q;
ll a[150005];
ll b[150005];
ll s[150005];
ll sum=0;
map<ll, ll> P;//排序后a[i]的位置，记得要开map，因为a[x]最大可以达到1e8
int main()
{
	ios::sync_with_stdio(false);
	cin >> n;
	for(ll i=1;i<=n;i++)	cin >> a[i], b[i]=a[i];
	sort(b+1, b+n+1);
	for(ll i=1;i<=n;i++)	sum+=b[i]*i, s[i]=b[i]+s[i-1], P[b[i]]=i;
	cin >> Q;
	while(Q--)
	{
		ll x, y;
		cin >> x >> y;
		ll pos=upper_bound(b+1, b+n+1, y)-b;//用upper_bound找pos
		ll ans=sum;
		ans-=a[x]*P[a[x]];//减去被删掉的元素
		ans-=s[n]-s[P[a[x]]];//P[a[x]]右边的所有元素向左移一个下标
		ans+=y*(pos-(pos > P[a[x]]));//加上插入的元素y，记得要判断pos减不减一
		ans+=s[n]-s[pos-1];//pos右边的所有元素向右移一个下标
		if(pos <= P[a[x]])	ans-=b[P[a[x]]];//判断向右移动时有没有算上P[a[x]]，算上了就减去
		cout << ans << endl;
	}
	return 0;
}
```

# 十年 OI 一场空，不开 long long 见祖宗！！

别问我为什么知道的

[代码极速版](https://www.luogu.com.cn/paste/az3cvkxe)