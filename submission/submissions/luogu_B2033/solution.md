# B2033 题解

## 题目大意

> 计算 $A\times B$ ，满足 $1\le A,B\le 5\times 10^4$ 。

## 题解

提供一下相关类型的大小范围。

$$
\def{\arraystretch}{1.8}
\begin{array}{c|c|c||c|c|c}\hdashline
\textbf{\textsf{类型}} & \textbf{\textsf{下界}} & \textbf{\textsf{上界}} & \textbf{\textsf{类型}} & \textbf{\textsf{下界}} & \textbf{\textsf{上界}} \cr\hline
\verb!char! & -2^7 & 2^7-1 & \verb!unsigned char! & 0 & 2^8-1\cr\hline
\verb!short! & -2^{15} & 2^{15}-1 & \verb!unsigned short! & 0 & 2^{16}-1 \cr\hline
\verb!int! & -2^{31} & 2^{31}-1 & \verb!unsigned int! & 0 & 2^{32}-1 \cr\hline
\verb!long long! & -2^{63} & 2^{63}-1 & \verb!unsigned long long! & 0 & 2^{64}-1 \cr\hdashline
\end{array}$$

那么如果选的类型小了会发生什么？

我们知道，在电脑中使用补码的形式存储所有数字。假如我们用的是 $\verb!unsigned short!$ 类型，那么当我们计算 $1234\times 4321$ 时，本质上是 $100,1101,0010_{(2)}\times 1,0000,1110,0001_{(2)}$ ，得出来的结果应该是：

$$1010001,\underbrace{0101,1100,1001,0010}_{16 \text{位}}$$

事实上， $\verb!unsigned short!$ 只会保留最后 $16$ 位，前面溢出的部分就去除了。把 $0101,1100,1001,0010$ 转换成 $10$ 进制，就是 $23698$ 。你可以拿 C++ 试一试，可以发现强制转换成 $\verb!unsigned short!$ 后的确是这个值。

要注意的是，对于有符号整数，乘法溢出属于**未定义行为**，具体数值与编译器有关。

至于这题，由于 $A,B\le 5\times 10^4$ ，而 $A\times B\le 2.5\times 10^9$ ，可能会突破 $\text{int}$ 的上限（$2,147,483,647$）因此选择 $\verb!long long!$ 类型才行。

## 参考代码

```cpp
#include<bits/stdc++.h>
#define up(l,r,i) for(int i=l,END##i=r;i<=END##i;++i)
#define dn(r,l,i) for(int i=r,END##i=l;i>=END##i;--i)
using namespace std;
typedef long long i64;
const int INF =2147483647;
char s[256]; i64 a,b;
int main(){
    cin>>a>>b; cout<<a*b;
    return 0;
}
```