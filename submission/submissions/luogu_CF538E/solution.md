# CF538E 题解

[更好的阅读体验](https://www.cnblogs.com/LaoMang-no-blog/p/16278300.html)

---

[**你谷 link**](https://www.luogu.com.cn/problem/CF538E)

[**CF link**](https://codeforces.com/problemset/problem/538/E)

首先将题目转化分别由自己和对面两个人布置叶子权值，求最大的叶子的权值，方便之后的解决。

考虑本题的计算是从叶子向上的，所以应该是自下而上的树形 dp，考虑设 $dp_{x,0/1}$ 表示以 $x$ 为根的子树，先手是不是想大的人，最大能走到的子树内的叶子是子树内第几大的。

如果是先手，则下一步自己就是后手，则应该取下一步后手能走到的子树内最小的，布置的时候就应该把最大的权值全都布置在这个子树里，若这一步是后手，则因为对面还会走到最小的，所以要给每一个儿子均匀分配，所以状态转移方程就是：

$$
\begin{aligned}
f_{x,1}=\min_{y\in\operatorname{son}(x)}\{f_{y,0}\}\\
f_{x,0}=\sum_{y\in\operatorname{son}(x)}f_{y,1}
\end{aligned}
$$

[代码](https://codeforces.com/contest/538/submission/157132426)非常简洁。