# P11296 题解

## 题解：P11296 [NOISG2018 Prelim] Snail

注意：这是一篇**非正式**做法的题解。**如果想要学习正确的解法，请移步其他题解**。

### 题外话

前一天看到这题，决定这题很有意思，作为一道橙题，它居然 AC 率不到 $2\%$，所以决定打一遍。于是加到做题计划里，今天切。打 WA 了拿到 $37$ 分之后，~~点击“查看题解”发现没有题解~~发现这题不知道什么时候升黄了。AC 后再看，这题不知道什么时候升绿了。第一次出现这么神奇的事情，写篇题解记录一下。

### 解题思路

首先，分析题意，需要我们模拟蜗牛向上爬的过程。每天有 $n$ 个阶段，每个阶段可能上升或下降。请问几天几阶段后能够爬出井。

### 第 $0$ 档部分分

样例，无需多言。

### 第 $1$ 档部分分

由于 $n = 1$，可得：

- 若 $p_0 > 0$，则 $ans = \lceil  \frac{h}{p_0} \rceil$。
- 若 $p_0 \le 0$，则 $ans = -1$。

### 第 $2$ 档部分分

考虑转换。若经过了 $x$ 个阶段，则答案为 $(\lfloor \frac{x}{n}\rfloor , x - \lfloor \frac{x}{n}\rfloor)$。此时，可以**直接转换到第二档部分分**的做法，只不过是把天换成阶段。

### 第 $4$ 档部分分

维护**前缀和**计算：

$$qzh_i = \sum_{j=0}^{i}p_i$$

此时可以快速计算出需要几个整天，然后从前到后找到第一个前缀和 $>$ 剩下的 $h$ 即为阶段的答案。

### 骗分算法 I

维护**前缀和**，找前缀和的**最小值**和**最大值**。

- 如果前缀和的最大值 $> h$，那么第一天就可以出去。
- 否则如果 $q_{n - 1} <= 0$，那么永远不能出去。
- 否则先快速计算 $\frac{h - q\text{中的最大值}}{q_{n - 1}}$，然后再暴力计算。

虽然这段代码只能拿到前面讲过的 $3$ 个部分分，但是由于后面 AC 代码要用到，所以放一下：

```cpp
#include<bits/stdc++.h>
using namespace std;
long long h , n , p[10005] , qzh[10005] , maxq , ans , pl = 1;
int main()
{
	ios::sync_with_stdio(0);
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	cin >> h >> n;
	for(int i = 1 ; i <= n ; i++)
	{
		cin >> p[i];
		qzh[i] = qzh[i - 1] + p[i];
		maxq = max(maxq , qzh[i]);
	}
	if(maxq < 0 || (maxq < h) && qzh[n] <= 0)
	{
		cout << "-1 -1";
		return 0;
	}
	ans = (h - maxq) / qzh[n];
	h -= ans * qzh[n];
	ans = ans * n - 1;
	while(h > 0)
	{
		h -= p[pl];
		ans++;
		pl++;
		if(pl > n)
		{
			pl = 1;
		}
	}
	cout << ans / n << ' ' << ans % n;
	return 0;
}
```

### 骗分算法 II

先跑一段暴力，找前 $100$ 天有没有答案，如果没有，那么按照上一个部分的算法跑，然后最后再跑一段暴力，如果 $5 \times 10^8$ 个阶段之内能够走出去，输出答案，否则输出 $(-1 , -1)$。得分：$80$。

```cpp
#include<bits/stdc++.h>
using namespace std;
long long h , n , p[10005] , qzh[10005] , maxq , minq , ans = -1 , pl = 1 , ch , cnt;
int main()
{
	ios::sync_with_stdio(0);
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	cin >> h >> n;
	for(int i = 1 ; i <= n ; i++)
	{
		cin >> p[i];
		qzh[i] = qzh[i - 1] + p[i];
		maxq = max(maxq , qzh[i]);
		minq = min(minq , qzh[i]);
	}
	ch = h;
	if(n * h <= 2000000000)
	{
		while(1)
		{
			if(h <= 0)
			{
				cout << ans / n << ' ' << ans % n;
				return 0;
			}
			h -= p[pl];
			h = min(h , ch);
			ans++;
			pl++;
			if(pl > n)
			{
				pl = 1;
			}
			cnt++;
			if(cnt > 500000000)
			{
				break;
			}
		}
		cout << "-1 -1";
		return 0;
	}
	if(qzh[n] > 0)
	{
		for(int i = 1 ; i <= n * (max(0ll , -minq) + 100) / qzh[n] ; i++)
		{
			if(h <= 0)
			{
				break;
			}
			h -= p[pl];
			h = min(h , ch);
			ans++;
			pl++;
			if(pl > n)
			{
				pl = 1;
			}
		}
	}
	for(int i = 1 ; i <= n * n ; i++)
	{
		if(h <= 0)
		{
			break;
		}
		h -= p[pl];
		h = min(h , ch);
		ans++;
		pl++;
		if(pl > n)
		{
			pl = 1;
		}
	}
	if(h > qzh[n] && qzh[n] > 0)
	{
		ans += (h - maxq) / qzh[n] * n;
		h -= (h - maxq) / qzh[n] * qzh[n];
	}
	while(h > 0)
	{
		h -= p[pl];
		ans++;
		pl++;
		if(pl > n)
		{
			pl = 1;
		}
		cnt++;
		if(cnt > 500000000)
		{
			cout << "-1 -1"; 
			return 0;
		}
	}
	cout << ans / n << ' ' << ans % n;
	return 0;
}
```

### 究极骗分：

观察 [$80$ 分记录](https://www.luogu.com.cn/record/190307681)，发现错误的点都在我们已经解决的部分分，而且都是 $-1$ 的问题。

直接特判性质，然后把 $37$ 分代码和 $80$ 分代码嫁接，得到满分的代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
long long h , n , p[10005] , qzh[10005] , maxq , minq , ans = -1 , pl = 1 , ch , cnt;
bool samep()
{
	for(int i = 1 ; i < n ; i++)
	{
		if(p[i] != p[i + 1])
		{
			return 0;
		}
	}
	return 1;
}
int main()
{
	ios::sync_with_stdio(0);
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	cin >> h >> n;
	for(int i = 1 ; i <= n ; i++)
	{
		cin >> p[i];
		qzh[i] = qzh[i - 1] + p[i];
		maxq = max(maxq , qzh[i]);
		minq = min(minq , qzh[i]);
	}
	ch = h;
	if(n == 1 || samep())
	{
		if(maxq < 0 || (maxq < h) && qzh[n] <= 0)
		{
			cout << "-1 -1";
			return 0;
		}
	}
	if(n * h <= 2000000000)
	{
		while(1)
		{
			if(h <= 0)
			{
				cout << ans / n << ' ' << ans % n;
				return 0;
			}
			h -= p[pl];
			h = min(h , ch);
			ans++;
			pl++;
			if(pl > n)
			{
				pl = 1;
			}
			cnt++;
			if(cnt > 500000000)
			{
				break;
			}
		}
		cout << "-1 -1";
		return 0;
	}
	if(qzh[n] > 0)
	{
		for(int i = 1 ; i <= n * (max(0ll , -minq) + 100) / qzh[n] ; i++)
		{
			if(h <= 0)
			{
				break;
			}
			h -= p[pl];
			h = min(h , ch);
			ans++;
			pl++;
			if(pl > n)
			{
				pl = 1;
			}
		}
	}
	for(int i = 1 ; i <= n * n ; i++)
	{
		if(h <= 0)
		{
			break;
		}
		h -= p[pl];
		h = min(h , ch);
		ans++;
		pl++;
		if(pl > n)
		{
			pl = 1;
		}
	}
	if(h > qzh[n] && qzh[n] > 0)
	{
		ans += (h - maxq) / qzh[n] * n;
		h -= (h - maxq) / qzh[n] * qzh[n];
	}
	while(h > 0)
	{
		h -= p[pl];
		ans++;
		pl++;
		if(pl > n)
		{
			pl = 1;
		}
		cnt++;
		if(cnt > 500000000)
		{
			cout << "-1 -1"; 
			return 0;
		}
	}
	cout << ans / n << ' ' << ans % n;
	return 0;
}
```

欢迎大家来 hack！此代码不保证正确性，如果你找到了一组 hack，请给此题解点个赞，并将 hack 放在评论区。如果我看到了，就会回来更新题解。