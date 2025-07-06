# P5713 题解

### Update Log

- $\textit{2021.12.13}$ 修改了文章排版与错误，希望管理能够再次通过！

**本文适用于 C 和 C++ 语言 OIer。**

因为题解中 $\texttt{if}$ 肯定被大规模使用，所以本文主要讲解**三目运算符** $\texttt{? :}$。

### Introduction

```cpp
p ? a : b
// 当 p 成立时返回 a，否则返回 b
```
$\texttt{e.g.}$

`printf("%d", (400 % 4 != 0) ? 1 : 2);`

上面的这行代码中，由于 $400\equiv0\pmod4$，所以表达式 `400 % 4 != 0` 不成立，输出的值是 $2$。

### Description

当在本地时间**短**时输出 $\texttt{Local}$ ，**否则**输出 $\texttt{Luogu}$ 。

这样就可以使用三目运算符控制输出。

### Solution

使用 $\texttt{printf}$ 中 `%s` 字符串格式符（或直接用 $\texttt{puts}$），参数值使用三目运算符。

### Code

**再次强调**，当 $n\times 5>n\times 3+11$ 时，本地比团队长，输出 $\texttt{Luogu}$ ，否则输出 $\texttt{Local}$。

同时我们也可以化简上面的式子，得到输出 $\texttt{Luogu}$ 的条件为 $n>5.5$，由于 $n$ 取整数，所以可以写作 $n\ge6$。

```cpp
#include <cstdio>

using namespace std;
int n;
int main(){
    scanf("%d", &n);
    puts(n >= 6 ? "Luogu" : "Local");
    return 0;
}
```