# P3954 题解

本题的要求已经说的足够清楚了，直接将输入的三个分数代入总分公式即可计算所求的总成绩。

于是可以得到下面的代码。

```cpp
#include <stdio.h>
int a, b, c, score;
int main() {
  scanf("%d%d%d", &a, &b, &c);
  score = a * 0.2 + b * 0.3 + c * 0.5;
  printf("%d", score);
  return 0;
}
```

然而，这份代码存在一些问题。在部分机器上，上面的程序对于样例 2 的输入会得到 78 的结果，与样例输出不符。

这是因为 [浮点运算存在误差]()。限于篇幅，本题解将不再详细展开浮点误差的内容，感兴趣的读者可以点击前面的链接了解相关知识。

事实上，本题输入数据的特殊性质可以让我们避免浮点运算，从而得到准确的结果。将原式稍微改写一下得到：

$$
\begin{aligned}
\textit{score} &=a \times 0.2 + b \times 0.3 + c \times 0.5\\
 &=(a \times 2 + b \times 3 + c \times 5) \div 10
\end{aligned}
$$

而数据范围里提到了 $a,b,c$ 均为 $10$ 的倍数，这样所有运算都可以在整数下进行，避免了浮点误差造成的结果不准确。

```cpp
#include <stdio.h>
int a, b, c, score;
int main() {
  scanf("%d%d%d", &a, &b, &c);
  score = (a * 2 + b * 3 + c * 5) / 10;
  printf("%d", score);
  return 0;
}
```