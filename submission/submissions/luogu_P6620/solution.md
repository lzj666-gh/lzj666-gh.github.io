# P6620 题解

# 前言

这也许是我写的最后一篇题解了。

虽然想说这是道送我退役的题，但归根结底还是我菜，跟题目没多大关系。

之前模拟赛还考过那道[如何优雅地求和](http://uoj.ac/problem/269)，今天出考场 [Fuyuki](https://www.luogu.com.cn/user/109236) 跟我讲以前考过我还完全没想起来，过了半天才记起当时我也没想到拆成下降幂，这不是完全没有任何进步吗...

---

# 正文

直接来看题目给的式子：

$$\sum_{k=0}^{n}{f(k)\times x^k\times\binom{n}{k}}$$

这个 $f(k)$ 我们肯定是要拆开来算的，但如果你把它拆成单项式，就会像我一样在考场里浪费光阴，因为这个单项式和组合数不是很搭。

但是如果你组合数学学得好或者能把混凝土数学倒着背，亦或做过前言里提到的那道题，就会想到一个叫做下降幂的玩意儿，它有着非常优秀的性质。

具体来说，假如我们有一个这样的下降幂单项式：

$$k^{\underline{m}}=\prod_{i=k-m+1}^{k}{i}$$

你会发现它和组合数相乘有非常漂亮的结果：

$$\binom{n}{k}\times k^{\underline{m}}=\binom{n-m}{k-m}\times n^{\underline{m}}$$

证明的话把组合数拆成阶乘随便消下就能得证。

于是我们考虑把题目中所给的 $f(k)=\sum_{i=0}^{m}{a_ik^i}$ 转化成下降幂多项式 $f(k)=\sum_{i=0}^{m}{b_ik^{\underline{i}}}$

$$\sum_{k=0}^{n}{\sum_{i=0}^{m}{b_ik^{\underline{i}}}\times x^k\times\binom{n}{k}}=\sum_{i=0}^{m}{b_in^{\underline{i}}\sum_{k=0}^{n}{\binom{n-i}{k-i}x^k}}$$

发现当 $i>k$ 时里头值直接为 $0$ 了可以扔掉，于是内层改成枚举 $k-i$，式子就变成了这样：

$$\sum_{i=0}^{m}{b_in^{\underline i}\sum_{k=0}^{n-i}{\binom{n-i}{k}x^{k+i}}}=\sum_{i=0}^{m}{b_in^{\underline i}x^i\sum_{k=0}^{n-i}{\binom{n-i}{k}x^k}}$$

这时我们发现里头直接变成了 $m=0$ 的部分分，随便套一下我们在小学二年级就学习过的二项式定理可以知道：

$$\sum_{k=0}^{n-i}{\binom{n-i}{k}x^k1^{n-i-k}}=(x+1)^{n-i}$$

于是题目的式子最终可以变成这样：

$$\sum_{i=0}^{m}{b_in^{\underline i}x^i(x+1)^{n-i}}$$

如果我们知道所有的 $b_i$ 就可以在 $O(m)$ 的复杂度内计算出结果，于是最后问题落在了普通多项式转下降幂多项式上。

而我们又知道：

$$x^n=\sum_{i=0}^{n}{\begin{Bmatrix}n\\i\end{Bmatrix}}x^{\underline i}$$

因此有：

$$\begin{aligned}\sum_{i=0}^{m}{a_ik^i}&=\sum_{i=0}^{m}{a_i\sum_{j=0}^{i}{\begin{Bmatrix}i\\j\end{Bmatrix}k^{\underline j}}}\\&=\sum_{i=0}^{m}{k^{\underline i}\sum_{j=i}^{m}{\begin{Bmatrix}j\\i\end{Bmatrix}a_j}}\end{aligned}$$

也就是说：

$$b_i=\sum_{j=i}^{m}{\begin{Bmatrix}j\\i\end{Bmatrix}a_j}$$

直接 $O(m^2)$ 暴力递推第二类斯特林数即可，总时间复杂度 $O(m^2)$，可以通过本题。

---

# 最后

今天的分已经是明天 AK 都救不回的样子了，更何况我也没那个水平 AK Day2，想说的话着实有很多，但在题解里说太多也很奇怪就不多讲了，就祝愿这次进队的同学能走得更远吧。

转眼间 OI 也伴我走过了两年，我大概这一生都会记得这段闪烁着光辉的时光吧。所有看着我以及陪伴我走完这一程的人，真的非常非常感谢你们，希望你们也能在自己的道路上更进一步。

$$\textcolor{#20C1DD}{唯有那份眩目——未曾忘却...}$$