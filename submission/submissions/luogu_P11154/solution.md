# P11154 题解

### 题意简述
在某款游戏中，有着 $n$ 个物件，每个物件都有四种判定方式。

- **大 Pure** 判定，该玩家获得 $\frac{10^7}{n} + 1$ 分。
- **小 Pure** 判定，该玩家获得 $\frac{10^7}{n}$ 分。
- **Far** 判定，该玩家获得 $\frac{\frac{10^7}{n}}{2}$ 分。
- **Lost** 判定，该玩家不得分。

玩家获得的分数也有着一种评级方式。

设 $s$ 为该玩家获得的分数。
- $s < 8.6\times 10^6$ 时，该玩家获得 **D** 评级。
- $8.6\times 10^6 \leq s < 8.9\times 10^6$ 时，该玩家获得 **C** 评级；
- $8.9\times 10^6 \leq s < 9.2\times 10^6$ 时，该玩家获得 **B** 评级；
- $9.2\times 10^6 \leq s < 9.5\times 10^6$ 时，该玩家获得 **A** 评级；
- $9.5\times 10^6 \leq s < 9.8\times 10^6$ 时，该玩家获得 **AA** 评级；
- $9.8\times 10^6 \leq s < 9.9\times 10^6$ 时，该玩家获得 **EX** 评级；
- $s \geq 9.9\times 10^6$ 时，该玩家获得 **EX+** 评级；

现告诉你该玩家获得 **大 Pure、小 Pure、Far、Lost** 评定的物件的个数，请你求出玩家所得分数的评级。

### 解题思路
设 $n = p_1 + p_0 + f + l,x = \frac{10^7}{n}$。

- 对于 **大 Pure** 判定，我们把总分加上 $(x + 1) \times p_1$。
- 对于 **小 Pure** 判定，我们把总分加上 $x \times p_0$。
- 对于 **Far** 判定，我们把总分加上 $\frac{x}{2} \times f$。
- 对于 **Lost** 判定，我们什么也不用管。

算出来总分后，我们挨个判定当前分数属于哪个评级即可。

CODE：
```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
	int p1, p0, f, l;
	cin >> p1 >> p0 >> f >> l;
	int n = p1 + p0 + f + l;
	int scores = (1e7 / n + 1) * p1;
	scores += (1e7 / n) * p0;
	scores += (1e7 / n / 2) * f;
	scores += 0;   //Lost 不用加分。
	if (scores < 8.6 * 1e6) {
		cout << "D";
	} else if (scores < 8.9 * 1e6) { //这里已经满足 scores >= 8.6 * 1e6
		cout << "C";
	} else if (scores < 9.2 * 1e6) {
		cout << "B";
	} else if (scores < 9.5 * 1e6) {
		cout << "A";
	} else if (scores < 9.8 * 1e6) {
		cout << "AA";
	} else if (scores < 9.9 * 1e6) {
		cout << "EX";
	} else {
		cout << "EX+";
	}
	return 0;
}
```