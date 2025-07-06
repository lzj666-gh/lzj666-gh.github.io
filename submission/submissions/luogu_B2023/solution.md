# B2023 题解

### 题目分析

首先，需要读入这四种变量。对于不同的变量类型，我们使用 `scanf` 读入时要用到不同的占位符。

+ 对于字符变量，占位符应为 `%c`；
+ 对于整形变量，占位符应为 `%d`；
+ 对于单精度浮点数，占位符应为 `%f`；
+ 对于双精度浮点数，占位符应为 `%lf`。

对于保留小数，我们需要用到 `printf` 的保留小数功能。

+ 单精度浮点数保留 $k$ 位小数的方式为：`"%.kf"`；
+ 双精度浮点数保留 $k$ 位小数的方式为：`"%.klf"`。

输出时，每个变量之间用空格分隔即可。

### 参考代码

```cpp
#include <iostream>
#include <cstdio>
using namespace std;

char a;
int b;
float c;
double d;

int main()
{
    scanf("%c%d%f%lf", &a, &b, &c, &d);
    printf("%c %d %.6f %.6lf", a, b, c, d);
    return 0;
}
```