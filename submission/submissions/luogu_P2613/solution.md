# P2613 题解

*2019-02-22 更新*

分数取余？我不知道是什么概念。分子分母还特别大？

一步一步来。

**考虑一下，分数取余也要满足取余运算的性质！**

取余运算的性质有：

* **如果两个数对模 $p$ 同余，那么它们乘上同一个数以后依然对模 $p$ 同余。$(I)$**

所以，虽然我不知道分数取余是什么，但是如果

$x \equiv \frac{a}{b} \pmod p$ （满足此方程的 $x$ 有多个，本题实际上是要求**最小的正整数解**，求出任意一个 $x$ ，模 $p$ 后即本题答案）

那么根据 $(I)$，它可以两边同时乘以 $b$，

$ x × b \equiv \frac{a}{b} × b \pmod p$

那么问题已经转化为：

**已知 $bx \equiv a \pmod p$ ①，求 $x$。**

等等，先别看这个。**如果这时我们能求出一个 $x_1$ 使得 $bx_1 \equiv 1 \pmod p$ ② 呢？**

又根据 $(I)$，② 两边同时乘以 $a$ 后仍然成立：

$b × (ax_1) \equiv a \pmod p$

和 ① 对比一下，可见 $a × x_1$ 就是答案 $x$ 了（别忘了最后模一下 $p$）。

**于是抛出一个问题 II：求一个 $x_1$ 满足 $bx_1 \equiv 1 \pmod p$**。

如果你不能解决，你需要问题 II [P1082 同余方程](https://www.luogu.org/problemnew/show/P1082)，我也发布了它的一份[题解](https://cicos.blog.luogu.org/solution-p1082)（本题解的中间部分）！

问题 II 解决了，那 $a,b$ 太大怎么解决？

**把条件 $bx \equiv a \pmod p$ 也转化一下：**

$(b \mod p) × x \equiv a \mod p \pmod p$

这个转化为什么是对的？其实你可以按照程序中的模运算来理解，任何同余式右边的 $\pmod p$ 相当于对两边结果分别进行一次最终模运算。对于其中的因数，你不管怎么模，同余式都保持成立。

由此可见，只要在快读的时候也不断把 $a,b$ 对模数求余就好了。

题目说还有无解的情况？

* 当 $b$ 是 $p$ 的倍数时，$bx \mod p = 0$。

  * 如果 $a$ 也是 $p$ 的倍数，则 $a \mod p = 0$，所以 $bx \equiv a \pmod p$ 恒成立（有无数解）。

  * 如果 $a$ 不是 $p$ 的倍数，则 $a \mod p ≠ 0$，故上面这个方程不可能成立。

* 若 $b$ 不是 $p$ 的倍数，那么因为模数是一个质数，所以 $b$ 与 $p$ 互质，那么 $bx_1 \equiv 1 \pmod p$ 一定有解（根据问题 II 中的一个结论），故一定有符合条件的 $x = a × x_1$。

所以当且仅当 $b \mod p = 0$ 时无解。

重新理清思路：求解 $\frac{a}{b} \mod p$。

* 读入 $a, b$ 时用快读（分字符读入），以便于在其中直接模 $p$。

* 判断取余后的 $b$ 是不是 $0$，是则无解或者无意义，不是则一定有解。

* 求解关于 $x_1$ 的方程：$bx_1 \equiv 1 \pmod p$。

* 答案 $x$ 等于 $a × x_1 \mod p$。

```cpp
#include <cstdio>
#include <cctype>
const int MOD = 19260817;//MOD是题解中的"p"
inline int getint()
{
    int res = 0, ch = getchar();
    while(!isdigit(ch) and ch != EOF)
        ch = getchar();
    while(isdigit(ch))
    {
        res = (res << 3) + (res << 1) + (ch - '0');
        res %= MOD;//直接对MOD取余
        ch = getchar();
    }
    return res;
}

int x, y;
void exgcd(int a, int b)
{
    if(b == 0)
    {
        x = 1;
        y = 0;
        return;
    }
    exgcd(b, a % b);
    int Last_x = x;
    x = y;
    y = Last_x - a / b * y;
}

int main()
{
	int a, b;
    a = getint();
    b = getint();
    
    if(b == 0)
    {
        puts("Angry!");
        return 0;
    }
    exgcd(b, MOD);
    x = (x % MOD + MOD) % MOD;
    printf("%lld\n", a * (long long)(x) % MOD);//小心相乘后爆int
    return 0;
}
```

___

更新日志：

2019-02-22 打扫了 `mimi` 指出的错误，很感谢；修改语句。