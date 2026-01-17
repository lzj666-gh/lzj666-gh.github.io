# P2827 题解

[您可在我的博客中查看本文，谢谢！](https://www.cnblogs.com/crab-in-the-northeast/p/luogu-p2827.html)

**事实上，本题疑似所有题解和 lyd 蓝书上的证明均有误，本篇题解将给出一个严谨的单调性正确性证明。**

一眼看上去容易想到 $q = 0$ 的 $\mathcal{O}(m \log m)$ 堆做法。

$q >0$ 时，暴力给集合中的元素 $+q$ 显然是不可取的。观察到除了被切开的两个元素不 $+q$ 其余均 $+q$，可以等效地看做：把 $x$ 切为 $\lfloor px\rfloor - q$ 和 $x - \lfloor px\rfloor - q$，然后给所有集合中的元素 $+q$。

那么我们每秒可以不实际给每个元素 $+q$，而是记录整个集合通过全局 $+q$ 产生的偏移量，每次通过给每个数加上这个偏移量得到它的真实数值。发现偏移量 $t$ 秒后就是 $qt$。可以用 $\mathcal{O}(m \log m)$ 较为低效率地解决本题了，总结一下：

循环 $t$ 从 $0$ 到 $m - 1$，表示 $[t, t +1]$ 这一秒（即第 $t +1$ 秒）的操作：

- 取出集合最大值 $x'$，得到其真实值 $x = x' +qt$；
- 切 $x$ 为 $\lfloor px\rfloor$ 和 $x - \lfloor px \rfloor$ 两部分；
- 将 $\lfloor px\rfloor - q -  qt$，$x - \lfloor px\rfloor -  q- qt$ 放回集合（$-q$ 是上面等效的结果，$-qt$ 是要把真实值改为偏移值放回集合）。

---

$\mathcal{O}(m \log m)$ 不够优秀，考虑 $\mathcal{O}(m)$ 的做法，我们还是先考虑 $q = 0$，整个集合是静态的比较好想。

发现我们从大到小取 $x$，切开形成的 $\lfloor px\rfloor$ 显然也是从大到小的（正比例函数和 $\lfloor x \rfloor$ 均单调不降）。那么 $x - \lfloor px\rfloor$ 呢？

严格证明一下。命题：对于 $x_1, x_2 \in \mathbb Z, x_1 \ge x_2, 0< p < 1$，有 $x_1 - \lfloor px_1 \rfloor \ge x_2 - \lfloor px_2 \rfloor$。

证明：$x_1 \ge x_2 \land x_1, x_2 \in \mathbb Z$，因此 $x_1 - x_2 \in \N$。又因为 $0 <p < 1$，所以：
$$
\begin{aligned}x_1 - x_2  &\ge p(x_1 - x_2) \\ x_1 - x_2 + p x_2 & \ge px_1 \\  \lfloor px_2 + (x_1 - x_2) \rfloor & \ge\lfloor px_1 \rfloor \\ \lfloor px_2 \rfloor + (x_1 - x_2) & \ge \lfloor px_1 \rfloor \\ x_1 - \lfloor px_1 \rfloor & \ge x_2 - \lfloor px_2 \rfloor  \end{aligned}
$$
注意这里的证明很容易出现伪证，具体请见 <https://www.luogu.com.cn/paste/c4jthmhz>，这也是几乎所有题解错误的地方，这里不展开了。

因此我们考虑维护 A，B，C 三个队列，初始时队列 A 从大（队头）到小（队尾）保存原始 $n$ 个数字，B 和 C 为空。其中 B 保存每一秒切开形成的 $\lfloor px\rfloor$，C 保存每一秒切开形成的 $x - \lfloor px\rfloor$，具体保存方法就是直接推入 B 或 C 的队尾，根据刚刚的结论，B 和 C 将始终满足单调性，队头大队尾小。所以每次的最大值只有可能是 A，B，C 三个队列中某个队头，取三个队头中的最大值，切开之后分别放入 B 和 C 即可。

考虑 $q \ge 0$，上述结论是否仍成立？

我们假设某一秒，我们切开了一个数 $x_1$，下一秒，我们切开了一个数 $x_2 + q$。$x_2 + q$ 在上一秒时为 $x_2$，因此 $x_1 \ge x_2$。我们的证明目标是 $\lfloor px_1\rfloor+ q \ge \lfloor p(x_2 + q)\rfloor$ 和 $x_1 - \lfloor px_1\rfloor+ q \ge x_2 + q - \lfloor p(x_2 + q)\rfloor$。

对于第一条：$\lfloor px_1\rfloor+ q = \lfloor px_1 + q\rfloor \ge \lfloor px_2 + pq\rfloor = \lfloor p(x_2 + q)\rfloor$。

对于第二条：$x_1 - \lfloor px_1\rfloor+ q \ge x_2 +q - \lfloor px_2\rfloor \ge  x_2 + q - \lfloor p(x_2 +q) \rfloor$。

因此在上述做法的基础上，配合一下 $qt$ 的偏移量即可。

时间复杂度 $\mathcal{O}(m)$。

```cpp
#include <bits/stdc++.h>
inline int read() {
    int x = 0;
    bool f = true;
    char ch = getchar();
    for (; !isdigit(ch); ch = getchar())
        if (ch == '-')
            f = false;
    for (; isdigit(ch); ch = getchar())
        x = (x << 1) + (x << 3) + ch - '0';
    return f ? x : (~(x - 1));
}

const int maxn = (int)1e5 + 5;
const int mininf = 0xc0c0c0c0;
int a[maxn];

std :: queue <int> qw[4];
typedef std :: pair <int, int> pii;

int main() {
    int n = read(), m = read(), q = read(), u = read(), v = read(), t = read();
    for (int i = 1; i <= n; ++i)
        a[i] = read();
    std :: sort(a + 1, a + n + 1, std :: greater <int> ());
    for (int i = 1; i <= n; ++i)
        qw[1].push(a[i]);

    for (int i = 0; i < m; ++i) {
        pii p = std :: max({std :: make_pair(qw[1].empty() ? mininf : qw[1].front(), 1),
                            std :: make_pair(qw[2].empty() ? mininf : qw[2].front(), 2),
                            std :: make_pair(qw[3].empty() ? mininf : qw[3].front(), 3)});
        int x = p.first + q * i, j = p.second;
        qw[j].pop();
        
        int b = 1ll * x * u / v, c = x - b;
        qw[2].push(b - q - q * i);
        qw[3].push(c - q - q * i);

        if (i % t == t - 1)
            printf("%d ", x);
    }

    puts("");

    for (int i = 1; i <= n + m; ++i) {
        pii p = std :: max({std :: make_pair(qw[1].empty() ? mininf : qw[1].front(), 1),
                            std :: make_pair(qw[2].empty() ? mininf : qw[2].front(), 2),
                            std :: make_pair(qw[3].empty() ? mininf : qw[3].front(), 3)});
        int x = p.first, j = p.second;
        qw[j].pop();

        if (i % t == 0)
            printf("%d ", x + q * m);
    }

    puts("");
    return 0;
}
```

如果觉得本篇题解写得好，请不要忘记点赞，让这篇具有严谨的正确性证明的题解更多减少对后人的误导，谢谢！