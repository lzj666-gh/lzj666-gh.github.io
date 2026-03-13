# P9748 题解

# [CSP-J 2023] 小苹果

## Description

有 $n$ 个苹果手机排成一排，标号 $1 \sim n$。接下来每天都会抢走一些苹果手机，每次从最左边的第 $1$ 个苹果手机开始，每隔 $2$ 个拿一个苹果手机。取完后将剩下的苹果手机重新排成一排。求：

1. 多少天能拿完所有苹果手机；
2. 第 $n$ 个苹果手机是在第几天拿的。

## Solution

我们可以把「每隔 $2$ 个取一个苹果手机」这件事情这样理解：将苹果手机每 $3$ 个分一组，每次取这一组的第一个。

例如有 $11$ 个苹果手机：

![](https://cdn.luogu.com.cn/upload/image_hosting/thumiejn.png)

标红的是这一轮拿的。如果最后剩下的不足以拼成 $3$ 个一组的，就拼成不完整的一组。

很显然，这一轮取走的苹果手机数量就是分成的组数，即 $\left \lceil \dfrac n3 \right \rceil$。那么我们暴力模拟这件事，每次 $n \gets n - \left \lceil \dfrac n3 \right \rceil$，看多少次操作后 $n$ 变成 $0$ 即可。这是第一问。

对于第二问，我们可以这样考虑。首先最后一个苹果手机一定是在最后一组的，那么如果想取走这个苹果手机，就相当于**这个苹果手机在最后一组的第一个**。例如有 $11$ 个和 $10$ 个苹果手机：

![](https://cdn.luogu.com.cn/upload/image_hosting/akcyfbiw.png)

可以发现，只有在**最后一组仅有 $1$ 个苹果手机时，最后一个苹果手机是这一组的第一个**。也就等价于当 $n \bmod 3 = 1$ 时，可以在这一轮取到最后一个苹果手机。

那么我们在求第一问的暴力模拟时，判断当前的 $n$ 是否模 $3$ 为 $1$。若是，记录下来这是第几轮取苹果手机。这就是第二问的答案。

注意在第一次 $n \bmod 3 = 1$ 时就可以取到最后一个苹果手机了。往后如果还有这样的机会就不算了。

考虑计算时间复杂度。每次将 $n$ 减去 $\left \lceil \dfrac n3 \right \rceil$，也就大约是 $n \gets \dfrac 23n$。不妨将其大约看作 $n \gets \dfrac 12n$，也就是每次将 $n$ 缩小一半。因此这样计算的话时间复杂度为 $\Theta(\log_2 n)$。实际运行时会偏高。

## Code

```cpp
#include <iostream>
#include <cmath> 

using namespace std;

int n, res1, res2;

int main()
{
	freopen("apple.in", "r", stdin);
	freopen("apple.out", "w", stdout);
	
	cin >> n;
	
	for (int i = 1; ; ++ i )
	{
		if (n == 0) break;
		if (!res2 && n % 3 == 1) res2 = i;		// 只有在第一次 n % 3 == 1 时记录答案 
		n -= ceil(n / 3.0);
		++ res1;
	}
	
	cout << res1 << ' ' << res2 << '\n';
	
	return 0;	
}
```

