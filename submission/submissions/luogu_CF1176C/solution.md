# CF1176C 题解

本题是一道很不错的题目。

首先，我们不难想到将题目中给的奇奇怪怪的数字进行**离散化**，因为只有$6$个取值，```if```一下也可以。

Code：
```cpp
		if (x == 4)x = 1;
		if (x == 8)x = 2;
		if (x == 15)x = 3;
		if (x == 16)x = 4;
		if (x == 23)x = 5;
		if (x == 42)x = 6;
	
```

这时，我们需要在$O(n)$的时间内确定匹配的方案，需要注意到，**我们并不关心某个数与哪个数配对**，因此只需要记录长度为$i(1 \leq i \leq 6)$的序列已经有多少个完成$(cnt_i$)就可以。

对于扫描时遇到的某个数，我们将它和对应的那个数配对。这时$cnt_{i-1}=cnt_{i-1}-1,cnt_i=cnt_i+1$。特判$i=1$即可。答案为$n-6 \times cnt_6$。代码如下：

```
#include <bits/stdc++.h>
using namespace std;
const int MAXN = 500500;
int a[MAXN];
int n;
int ans;
int cnt[7];
int main()
{
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		int x;
		cin >> x;
		if (x == 4)x = 1;
		if (x == 8)x = 2;
		if (x == 15)x = 3;
		if (x == 16)x = 4;
		if (x == 23)x = 5;
		if (x == 42)x = 6;
		a[i] = x;
	}
	for (int i = 1; i <= n; i++)
	{
		if (a[i] == 1)
			cnt[1]++;
		else
		{
			if (cnt[a[i] - 1])
			{
				cnt[a[i]]++;
				cnt[a[i] - 1]--;
			}
		}
	}
	cout << n - 6 * cnt[6] << endl;
	return 0;
}

```


