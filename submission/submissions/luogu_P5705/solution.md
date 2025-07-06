# P5705 题解

**Updated on 2021.08.05** 优化了原题解，增加了关于输入输出的详细说明，希望能再次通过审核！

___

你当然可以使用 string 类的 reverse 操作，或者是字符数组倒序输出，这里介绍一种可能在你整个 OI 生涯与你相伴的做法。

本文将为你介绍 **格式化输入输出函数**：$\tt scanf$ 和 $\tt printf$。

### 0 为什么

$\tt scanf/printf$ 相比 $\tt cin/cout$ 快得多，应对多数题目绰绰有余。

以 [Luogu P7505 「Wdsr-2.5」小小的埴轮兵团](/problem/P7505) 为例。

笔者先后提交了两次，一次是使用自己的验题代码（使用了 scanf/printf），一次是使用 cin/cout。

![](https://cdn.luogu.com.cn/upload/image_hosting/rgi1rk74.png)

可以看出，差异是相当大的了。

（当然用快读更快）

### 1 语法


```cpp
#include <cstdio> //头文件
... ...
scanf("输入控制符", 输入参数);
printf("输出控制符", 输出参数);
```

其中常用的输入控制符有：

- `%d`：读入一个 $32$ 位有符号整数。
- `%u`：读入一个 $32$ 位无符号整数。
- `%lld`：读入一个 $64$ 位有符号整数。
- `%llu`：读入一个 $64$ 位无符号整数。
- `%f`：读入一个 `float` 类型。
- `%lf`：读入一个 `double` 类型。

输出控制符与之类似。

**练习：** [Luogu P1001 A+B Problem](/problem/P1001)

### 2 Solution

而这道题用 `%d` 类型是过不了的，因为输入没有空格，但可以用 `%1d` 输入，代表读入的整数都只有 $1$ 位。

先定义四个字符类型。

当然，如果输入中有多余的已知字符，可以在 scanf 中用该字符占位。

例如输入是 $2021.805$，使用如下代码读入，$a,b$ 的值分别为 $2021,805$。

```cpp
scanf("%d.%d", &a, &b);
```

本题 AC 代码：

```cpp
#include <cstdio>

using namespace std;
char a, b, c, d;
int main(){
	scanf("%c%c%c.%c", &a, &b, &c, &d);
	printf("%c.%c%c%c", d, c, b, a);
	return 0;
}
```

**练习：** [Codeforces 1A Theatre Square](/problem/CF1A)，[[NOIP2011 普及组] 数字反转](/problem/P1307)，[Luogu P1553 数字反转（升级版）](/problem/P1553)

**拓展练习：** [	[NOI2021] 量子通信](https://loj.ac/p/3535)