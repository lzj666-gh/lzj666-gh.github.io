# P4213 题解

杜教筛模板

杜教筛是用来干蛤的呢？

它可以在非线性时间内求积性函数前缀和。

## 前置知识

#### 积性函数

积性函数：对于任意互质的整数 $a,b$ 有 $f(ab)=f(a)f(b)$ 则称 $f(x)$ 的数论函数。

完全积性函数：对于任意整数 $a,b$ 有 $f(ab)=f(a)f(b)$ 的数论函数。
- 常见的积性函数：$\varphi,\mu,\sigma,d$
- 常见的完全积性函数：$\epsilon,I,id$

这里特殊解释一下 $\epsilon,I,id$ 分别是什么意思：
$\epsilon(n) = [n=1], I(n) = 1, id(n) = n$



#### 狄利克雷卷积

设 $f, g$ 是两个数论函数，它们的狄利克雷卷积卷积是：$(f*g)(n) = \sum \limits _{d | n} f(d) g(\frac{n}{d})$

性质：满足交换律，结合律

单位元：$\epsilon$ （即 $f*\epsilon=f$）

结合狄利克雷卷积得到的几个性质：
1. $\mu * I = \epsilon$
2. $\varphi * I = id$
3. $\mu * id = \varphi$

#### 莫比乌斯反演


若 
$$g(n) = \sum\limits_{d|n}f(d)$$

则
$$f(n)=\sum\limits_{d|n}\mu(d)g(\frac{n}{d})$$

证明：这里需要用到前面提到的性质：$\mu * I = \epsilon$

给出的条件等价于 $g=f * I$

所以 $g*\mu=f*I*\mu=f*\epsilon=f$ 即 $g * \mu = f$ 即 结论。

--- 

## 杜教筛

设现在要求积性函数 $f$ 的前缀和， 设  $\sum \limits_{i=1}^{n} f(i) = S(n)$。

再找一个积性函数 $g$ ，则考虑它们的狄利克雷卷积的前缀和

$$\sum\limits_{i=1}^{n}(f*g)(i)$$


$$\begin{aligned} &= \sum\limits_{i=1}^{n} \sum \limits _{d|i} f(d)g(\frac{i}{d}) \\ &= \sum \limits _{d=1}^{n} g(d)\sum\limits _{i=1}^{\lfloor \frac{n}{d}\rfloor } f(i) \\ &= \sum \limits _{d=1}^{n} g(d) S(\lfloor \frac{n}{d} \rfloor)     \end{aligned}$$

其中得到第一行是根据狄利克雷卷积的定义。

得到第二行则是先枚举 $d$ 提出 $g$ 。

得到第三行则是把 $\sum\limits _{i=1}^{\lfloor \frac{n}{d}\rfloor } f(i) $ 替换为 $S(\lfloor \frac{n}{d} \rfloor) $

接着考虑 $g(1)S(n)$ 等于什么。

可以发现，他就等于 
$$ \sum \limits _{i=1}^{n} g(i) S(\lfloor \frac{n}{i} \rfloor) - \sum \limits _{i=2}^{n} g(i) S(\lfloor \frac{n}{i} \rfloor)$$ 

（可以理解成从1开始的前缀和减去从2开始的前缀和就是第一项）

前面这个式子$\sum \limits _{i=1}^{n} g(i) S(\lfloor \frac{n}{i} \rfloor)$ ，根据刚才的推导，他就等于 $\sum\limits_{i=1}^{n}(f*g)(i)$

所以得到杜教筛的核心式子：

$$g(1)S(n)=\sum\limits_{i=1}^{n}(f*g)(i) - \sum \limits _{i=2}^{n} g(i) S(\lfloor \frac{n}{i} \rfloor)$$

得到这个式子之后有什么用呢？

现在如果可以找到一个合适的积性函数 $g$ ，使得可以快速算出 $\sum\limits_{i=1}^{n}(f*g)(i)$ 和 $g$ 的前缀和，便可以用数论分块递归地求解。

代码按照理解大概可以写成这样（默认 `ll` 为 `long long`）
（可以理解成一个伪代码。。就是一个思路的框架）
```cpp
ll GetSum(int n) { // 算 f 前缀和的函数
  ll ans = f_g_sum(n); // 算 f * g 的前缀和
  // 以下这个 for 循环是数论分块
  for(ll l = 2, r; l <= n; l = r + 1) { // 注意从 2 开始
    r = (n / (n / l)); 
    ans -= (g_sum(r) - g_sum(l - 1)) * GetSum(n / l);
    // g_sum 是 g 的前缀和
    // 递归 GetSum 求解
  } return ans; 
}
```
这个代码的复杂度是 $O(n^{\frac{3}{4}})$，证明如下：

设求出 $S(n)$ 的复杂度是 $T(n)$ ，要求出 $S(n)$ 需要求出 $\sqrt n$ 个 $S (\lfloor \frac{n}{i} \rfloor)$ 的值，结合数论分块的复杂度 $O(\sqrt n)$ 可得：
$$T(n) = \sum\limits_{i=1}^{\sqrt n} O(\sqrt i) + O(\sqrt {\frac{n}{i}})=O(n^{\frac{3}{4}})$$

还可以进一步优化杜教筛，即先线性筛出前 $m$ 个答案，之后再用杜教筛。这个优化之后的复杂度是：

$$T(n) = \sum\limits_{i=1}^{\lfloor \frac{n}{m} \rfloor} \sqrt \frac{n}{i} = O({\frac{n}{\sqrt m}})$$

当 $m = n ^ {\frac{2}{3}}$ 时，$T(n) = O(n^{\frac{2}{3}})$

可以使用哈希表来存下已经求过的答案，也可以不用。

考虑到上面的求和过程中出现的都是 $\lfloor \frac{n}{i} \rfloor $ 。开一个大小为两倍 $\sqrt n$ 的数组 $dp$ 记录答案。如果现在需要求出 `GetSum(x)` ，若 $x \leq \sqrt n$ ，返回 `dp[x]` ，否则返回 `dp[sqrt n + n / i]` 即可。这样可以省去哈希表的复杂度。  

------------


------------

### 实战演练
再挂一次核（tao）心（lu）式，全都要靠它：
$$g(1)S(n)=\sum\limits_{i=1}^{n}(f*g)(i) - \sum \limits _{i=2}^{n} g(i) S(\lfloor \frac{n}{i} \rfloor)$$

它的关键就是要找到合适的 $g$ 使得这个东西可以快速地算。

理论知识大概就这么多，接下来看几个例子：

#### (1) $\mu$ 的前缀和 

考虑到莫比乌斯函数的性质 $\mu * I = \epsilon$ ，自然想到取  $f=\mu,g=I,f*g=\epsilon$ 。

其中 $I$ 的前缀和和 $\epsilon$ 的前缀和都弱到爆了。。

所以就轻松的解决了。

杜教筛代码：

```cpp
inline ll GetSumu(int n) {
  if(n <= N) return sumu[n]; // sumu是提前筛好的前缀和
  if(Smu[n]) return Smu[n]; // 记忆化
  ll ret = 1ll; // 单位元的前缀和就是 1
  for(int l = 2, r; l <= n; l = r + 1) {
    r = n / (n / l); ret -= (r - l + 1) * GetSumu(n / l);
    // (r - l + 1) 就是 I 在 [l, r] 的和
  } return Smu[n] = ret; // 记忆化
}
```

#### (2) $\varphi$ 的前缀和

考虑到 $\varphi$ 的性质 $\varphi * I = id$，取 $f = \varphi, g = I, f * g = id$

$f * g$ 即 $id$ 的前缀和为 $\frac{n * (n+1)}{2}$

杜教筛代码：

```cpp
inline ll GetSphi(int n) {
  if(n <= N) return sump[n]; // 提前筛好的
  if(Sphi[n]) return Sphi[n]; // 记忆化
  ll ret = 1ll * n * (n + 1) / 2; // f * g = id 的前缀和
  for(int l = 2, r; l <= n; l = r + 1) {
    r = n / (n / l); ret -= (r - l + 1) * GetSphi(n / l);
    // 同上，因为两个的 g 都是 I 
  } return Sphi[n] = ret; // 记忆化
}
```



(1) & (2) 就是杜教筛模板 [luogu p4213](https://www.luogu.org/problemnew/show/P4213)

#### (3) （综合）$\sum\limits_{i=1}^{n}\varphi(i) \cdot i$ 

令 $f = \varphi \cdot id, g = id$, 考虑迪利克雷卷积的形式得到 $(f*g)(n)=\sum \limits _{d|n} (\varphi(d) \cdot d) \cdot (\frac{n}{d}) = n \sum\limits_{d|n}\varphi(d)=n^2$ 

即 $(f * g)(i) = i^2$

这样就可以快速求得 $(f*g)(i)$ 的前缀和 $\frac{n(n+1)(2n+1)}{6}$

就可以了。

---
---

## 题目

先推荐洛谷模板题

还有一题 luoguP3768 简单的数学题，这道题推完式子可以用杜教筛来求 $\varphi(i)i^2$ 的前缀和，和 $\varphi(i)i$ 所差无几。

51nod 上也有很多杜教筛的题目，放几个：
- 51nod 1244
- 51nod 1237 
- 51nod 1238
- 51nod 1239 
- 51nod 1220 
- ...



