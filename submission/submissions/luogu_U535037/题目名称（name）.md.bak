# 题目名称（name）

## 题目描述

给定一个长度为 $n$ 的数列 $a_1, a_2, a_3, \dots, a_n$。

令 $k=(\sum_{i=1}^{n}\sum_{j=i+1}^{n}\mathrm{lcm}(a_i,a_j)) \bmod 3499999$，求一个 $S$ 使得  $k+1|S$，$S$ 的数位累加和最小。

## 输入格式

输入包含两行，第一行是一个整数 $n$ 表示输入的数据个数，第二行包含 $n$ 个整数，用空格分开。

## 输出格式

输出最后的答案（$S$ 的数位累加和）。

## 提示

样例解释：

对于第一个样例，它的 $k=1(\operatorname{lcm}(a_1,a_2))+4(\operatorname{lcm}(a_1,a_3))+4(\operatorname{lcm}(a_2,a_3))=9$，可以证明 $10$ 的 $1$ 倍是各个数位之和最小的解。

对于第二个样例，它的 $k=5(\operatorname{lcm}(a_1,a_2))+20(\operatorname{lcm}(a_1,a_3))+4(\operatorname{lcm}(a_2,a_3))=29$，可以证明 $30$ 的 $1$ 倍是各个数位之和最小的解。

- $1 \le N \le 200000$
- $1 \le a_i \le 1000000$

| $n\le$ | $a_i\le$ | 特殊性质 | 分数 |
| :----------: | :----------: | :----------: | :----------: |
| 100 | 100 |  | 20 |
| 20000 |  |  | 10 |
|  |  | A | 10 |
|  |  | B | 10 |
|  |  | C | 10 |

- 特殊性质A：保证 $a_i=i$
- 特殊性质B：保证 $\displaystyle\sum^{n-1}_{i=1}a_i<a_n$
- 特殊性质C：保证 $\displaystyle\prod^{\lfloor\frac{n}{2}\rfloor}_{i=1}a_i<\prod^{n}_{i=\lfloor\frac{n}{2}\rfloor+1}a_i$

温馨提示：如果你无法保证自己会输出正解，但是可以保证自己会做出正确的 $k$，你也可以输出 $k$ 来获取这个测试点 $70\%$ 的分。

~~陈仓佚提示~~：大样例中的第一行为 $k$ 的值，第二行为真正的答案。

checker.cpp:
```cpp
#include "testlib.h"
int main(int argc, char* argv[]) {
    registerTestlibCmd(argc, argv);
	int a=ouf.readInt(),ans1=ans.readInt(),ans2=ans.readInt();
	if(a==ans2) quitf(_ok, "The answer is correct. answer is %d",ans2);
	else if(a==ans1) quitp(0.7,"Partially Correct get %d percent", 70);
	else quitf(_wa, "The answer is wrong: expected k = %d, ans = %d, found = %d", ans1, ans2, a);
	return 0;
}
```

## 时空限制

时间限制: 3000 ms
内存限制: 512 MB
