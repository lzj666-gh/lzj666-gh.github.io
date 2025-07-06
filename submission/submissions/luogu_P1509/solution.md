# P1509 题解

通过读题，不难发现，这道题是一道 0-1 背包问题，只是有点特殊罢了。既然是 0-1 背包问题，那么基本的套路都是一样的：**开数组，写循环**。

接下来让我们分析一下此题特殊之处，顺便梳理一下思路。
1. 普通的 0-1 背包问题只有一个成本，而这道题有两个成本（泡妹子所需的 rmb 和 rp）。所以，需要**多写一层循环，同时 dp 数组也要多一维**。
2. 普通的 0-1 背包问题，只要求出最大价值就好了。而这道题不仅要泡到尽量多的妹子，而且还要保证花费的时间尽量小。所以需要**两个 dp 数组**，分别保存泡到的妹子数量、所花费的时间。且，每个妹子的价值都为 1。

----------

综上，可以得出代码：

```cpp
//【P1509】找啊找啊找 GF - 洛谷 - 100 
#include <iostream>
#include <algorithm>

int n, m, r;
const int kMaxN = 100, kMaxM = 100, kMaxR = 100; // 常量开头带 k，符合命名规范 
int rmb[kMaxN + 5], rp[kMaxN + 5], time[kMaxN + 5];
int dpNum[kMaxM + 5][kMaxR + 5], dpTime[kMaxM + 5][kMaxR + 5]; // 两个 dp 

int main() {
	std::cin >> n;
	for (int i = 1; i <= n; ++i) std::cin >> rmb[i] >> rp[i] >> time[i];
	std::cin >> m >> r;

	for (int i = 1; i <= n; ++i)
		for (int j = m; j >= rmb[i]; --j) // 小心，不要把 j 和 m 写混，否则死循环 
			for (int k = r; k >= rp[i]; --k) {
				// 如果能泡到更多妹子 
				if (dpNum[j][k] < dpNum[j - rmb[i]][k - rp[i]] + 1) {
					dpNum[j][k] = dpNum[j - rmb[i]][k - rp[i]] + 1; // 数量++ 
					dpTime[j][k] = dpTime[j - rmb[i]][k - rp[i]] + time[i]; // 花费的时间加进去 
				}
				else if (dpNum[j][k] == dpNum[j - rmb[i]][k - rp[i]] + 1)
					// 如果能泡到同样多的妹子，选择时间最少的方案 
					dpTime[j][k] = std::min(dpTime[j][k], dpTime[j - rmb[i]][k - rp[i]] + time[i]);
			}
	
	// 不需要特判能否泡到妹子，因为如果泡不到，这里的值一定为 0 
	std::cout << dpTime[m][r] << std::endl;
}
```

----------

如果对于动态规划的背包问题仍然不是很懂（包括但不限于不知道数组该开多大、循环条件和边界是什么），建议刷一下洛谷试炼场当中的这几道简单题，不仅可以有效帮助**理解**，还可以在忘了的时候辅助**复习**：
+ [P1048 采药](https://www.luogu.org/problemnew/show/P1048)
+ [P1049 装箱问题](https://www.luogu.org/problemnew/show/P1049)
+ [P1060 开心的金明](https://www.luogu.org/problemnew/show/P1060)

注：采药那道题里面有一篇质量非常高的题解（20+ 赞同），详细分析了 0-1 背包问题的基本做法，值得一看。

----------

最后，祝愿广大 OIer 早日找到 GF~~（虽然这不可能~~