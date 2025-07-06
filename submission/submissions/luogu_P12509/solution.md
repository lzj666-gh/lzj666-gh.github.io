# P12509 题解

*感谢 [xyz123](https://www.luogu.com.cn/user/379926) 对本题的加强建议，原版题目中只要求 $P <2^{31}$。*

*说句闲话：我设计这题的初衷是【模板】哈希 2，而不是【模板】通信题。*

如果 A 程序可以向 B 程序传递一个不大于 $2^{31}-1$ 的非负整数，那么这就是一个 Hash 模板题。弱化后的题目随便用什么 Hash 函数都能过，比如「所有 $\texttt{1}$ 的位置编号之和 $\text{mod } 12345678$」。

然而，这道题目只允许 A 程序向 B 程序传递一个不大于 $2^{20}-1$ 的非负整数，因此我们要优化 Hash 函数——把 Hash 函数改为「所有 $\texttt{1}$ 的位置编号之异或和」就可以通过此题了。

（可以发现，对于不变动的 $N-1$ 位，设所有 $\texttt{1}$ 的位置编号之异或和为 $Q$，则第 $P$ 位为 $\texttt{0}$ 的字符串的最终 Hash 值为 $Q$，而另一个为 $Q \text{ xor } P$，二者的异或和恰好为 $P$。当 $P=0$ 时，两个 Hash 值都是 $Q$，异或和恰好也为 $P=0$。）

```cpp
#include <bits/stdc++.h>
using namespace std;
int Alice(string S)
{
    int X = 0;
    int n = S.size();
    S = ' ' + S;
    for (int i = 1; i <= n; i++)
        if (S[i] == '1') X ^= i;
    return X;
}
int Bob(string T, int X)
{
    int D = 0;
    int n = T.size();
    T = ' ' + T;
    for (int i = 1; i <= n; i++)
        if (T[i] == '1') X ^= i;
    return X;
}

```