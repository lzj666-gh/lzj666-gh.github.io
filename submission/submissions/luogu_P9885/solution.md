# P9885 题解

# P9885

## 算法

在这篇题解中，用 $P_k$ 代替 $P(k)$。

对 $Q(k)-Q(k-1)=Q(P_k)$ 累和，并注意 $Q(1)=Q(P_1)$，即有
$$\begin{aligned}
&Q(n)\\
=&\sum_{k=1}^nQ(P_k)\\
=&\sum_{x=1}^{P_n-1}\left(\sum_{k=\frac{x^2+x}{2}}^{\frac{x^2+3x}{2}}1\right)Q(x)+\left(\sum_{k=\frac{P_n^2+P_n}{2}}^n1\right)Q(P_n)\\
\end{aligned}$$

第二项中 $Q(P_n)$ 的系数是 $\sum\limits_{k=\frac{P_n^2+P_n}{2}}^n1=n+1-\frac{P_n^2+P_n}{2}$ 可以 $O(1)$ 求出，于是第二项可以递归求出。下面计算第一项。

$$\begin{aligned}
&\sum_{x=1}^{P_n-1}\left(\sum_{k=\frac{x^2+x}{2}}^{\frac{x^2+3x}{2}}1\right)Q(x)\\
=&\sum_{x=1}^{P_n-1}\left((x+1)Q(x)\right)\\
=&\sum_{x=1}^{P_n-1}\left((x+1)\sum_{k=1}^xQ(P_k)\right)\\
=&\sum_{k=1}^{P_n-1}\left(\sum_{x=k}^{P_n-1}(x+1)\right)Q(P_k)\\
=&\sum_{k=1}^{P_n-1}\frac{\left(P_n-k\right)\left(P_n+k+1\right)}{2}Q(P_k)\\
=&\sum_{x=1}^{P_{P_n-1}-1}\left(\sum_{k=\frac{x^2+x}{2}}^{\frac{x^2+3x}{2}}\frac{\left(P_n-k\right)\left(P_n+k+1\right)}{2}\right)Q(x)+\left(\sum_{k=\frac{P_{P_n-1}^2+P_{P_n-1}}{2}}^{P_n-1}\frac{\left(P_n-k\right)\left(P_n+k+1\right)}{2}\right)Q(P_{P_n-1})\\
\end{aligned}$$

第二项中 $Q(P_{P_n-1})$ 的系数是

$$\begin{aligned}
&\sum\limits_{k=\frac{P_{P_n-1}^2+P_{P_n-1}}{2}}^{P_n-1}\frac{\left(P_n-k\right)\left(P_n+k+1\right)}{2}\\
=&\frac{\left(-P_{P_n-1}^2-P_{P_n-1}+2 P_n\right) \left(-P_{P_n-1}^2-P_{P_n-1}+2 P_n+2\right) \left(P_{P_n-1}^2+P_{P_n-1}+4 P_n+2\right)}{48}
\end{aligned}$$

可以 $O(1)$ 求出，于是第二项可以递归求出。下面计算第一项。

$$\begin{aligned}
&\sum_{x=1}^{P_{P_n-1}-1}\left(\sum_{k=\frac{x^2+x}{2}}^{\frac{x^2+3x}{2}}\frac{\left(P_n-k\right)\left(P_n+k+1\right)}{2}\right)Q(x)\\
=&\sum_{x=1}^{P_{P_n-1}-1}\left(\frac{(x+1)\left(12P_n^2+12P_n-3x^4-12x^3-19x^2-14x\right)}{24}\right)Q(x)\\
=&\sum_{x=1}^{P_{P_n-1}-1}\left(\left(\frac{(x+1)\left(12P_n^2+12P_n-3x^4-12x^3-19x^2-14x\right)}{24}\right)\sum_{k=1}^xQ(P_k)\right)\\
=&\sum_{k=1}^{P_{P_n-1}-1}\left(\sum_{x=k}^{P_{P_n-1}-1}\left(\frac{(x+1)\left(12P_n^2+12P_n-3x^4-12x^3-19x^2-14x\right)}{24}\right)\right)Q(P_k)\\
=&\sum_{k=1}^{P_{P_n-1}-1}\frac{\left(k-P_{P_n-1}\right) \left(k+P_{P_n-1}+1\right) \left(k^4+2 k^3+k^2 P_{P_n-1}^2+k^2 P_{P_n-1}+k^2+k P_{P_n-1}^2+k P_{P_n-1}+P_{P_n-1}^4+2 P_{P_n-1}^3-12 P_n^2+P_{P_n-1}^2-12 P_n-4\right)}{48}Q(P_k)\\
=&\sum_{x=1}^{P_{P_{P_n-1}-1}-1}\left(\sum_{k=\frac{x^2+x}{2}}^{\frac{x^2+3x}{2}}\frac{\left(k-P_{P_n-1}\right) \left(k+P_{P_n-1}+1\right) \left(k^4+2 k^3+k^2 P_{P_n-1}^2+k^2 P_{P_n-1}+k^2+k P_{P_n-1}^2+k P_{P_n-1}+P_{P_n-1}^4+2 P_{P_n-1}^3-12 P_n^2+P_{P_n-1}^2-12 P_n-4\right)}{48}\right)Q(x)\\
&+\left(\sum_{k=\frac{P_{P_{P_n-1}-1}^2+P_{P_{P_n-1}-1}}{2}}^{P_{P_n-1}-1}\frac{\left(k-P_{P_n-1}\right) \left(k+P_{P_n-1}+1\right) \left(k^4+2 k^3+k^2 P_{P_n-1}^2+k^2 P_{P_n-1}+k^2+k P_{P_n-1}^2+k P_{P_n-1}+P_{P_n-1}^4+2 P_{P_n-1}^3-12 P_n^2+P_{P_n-1}^2-12 P_n-4\right)}{48}\right)Q(P_{P_{P_n-1}-1})\\
\end{aligned}$$

第一项 $\sum\limits_{x=1}^{P_{P_{P_n-1}-1}-1}$ 里的式子中，$Q(x)$ 的系数等于

$$\begin{aligned}
&\frac{35 x^{13}+455 x^{12}+2905 x^{11}+11935 x^{10}+34475 x^9+72345 x^8+110955 x^7+122325 x^6+90454 x^5+32620 x^4-13160 x^3-24640 x^2-10624 x}{107520}\cdot1\\
+&(x+1)\cdot\frac{P_{P_n-1} \left(P_{P_n-1}+1\right) \left(12 P_n \left(P_n+1\right)+4-P_{P_n-1}^2 \left(P_{P_n-1}+1\right)^2\right)}{48}\\
-&\frac{3 x^5+15 x^4+31 x^3+33 x^2+14 x}{24}\cdot\frac{P_n \left(P_n+1\right)}{2}\\
\end{aligned}$$

这里每一项都是一个关于 $x$ 的多项式和一个关于 $P_n$ 和 $P_{P_n-1}$ 的多项式的乘积。后者是常数可以提出去 $O(1)$ 计算，只需要计算前者乘以 $Q(x)$ 的前缀和。由于 $P_{P_{P_n-1}-1}-1\le183999$，预处理即可。

第二项中 $Q(P_{P_{P_n-1}-1})$ 的系数是：

$$\begin{aligned}
&\sum_{k=\frac{P_{P_{P_n-1}-1}^2+P_{P_{P_n-1}-1}}{2}}^{P_{P_n-1}-1}\frac{\left(k-P_{P_n-1}\right) \left(k+P_{P_n-1}+1\right) \left(k^4+2 k^3+k^2 P_{P_n-1}^2+k^2 P_{P_n-1}+k^2+k P_{P_n-1}^2+k P_{P_n-1}+P_{P_n-1}^4+2 P_{P_n-1}^3-12 P_n^2+P_{P_n-1}^2-12 P_n-4\right)}{48}\\
=&\frac{1}{215040}\left(2 P_{P_n-1}-P_{P_{P_n-1}-1}^2-P_{P_{P_n-1}-1}\right) \left(2 P_{P_n-1}+2-P_{P_{P_n-1}-1}^2-P_{P_{P_n-1}-1}\right)\left(\text{A long polynomial}\right)
\end{aligned}$$

其中 $\text{A long polynomial}$ 因为太长了，所以放到代码块里。它的值是：

```
8960 P_n^2 P_{P_n-1}-960 P_{P_n-1}^5+2240 P_n^2 P_{P_{P_n-1}-1}^2-400 P_{P_n-1}^4 P_{P_{P_n-1}-1}^2-160 P_{P_n-1}^3 P_{P_{P_n-1}-1}^4-60 P_{P_n-1}^2 P_{P_{P_n-1}-1}^6-20 P_{P_n-1} P_{P_{P_n-1}-1}^8-5 P_{P_{P_n-1}-1}^{10}+2240 P_n^2 P_{P_{P_n-1}-1}-400 P_{P_n-1}^4 P_{P_{P_n-1}-1}-320 P_{P_n-1}^3 P_{P_{P_n-1}-1}^3-180 P_{P_n-1}^2 P_{P_{P_n-1}-1}^5-80 P_{P_n-1} P_{P_{P_n-1}-1}^7-25 P_{P_{P_n-1}-1}^9+4480 P_n^2-2400 P_{P_n-1}^4-960 P_{P_n-1}^3 P_{P_{P_n-1}-1}^2-420 P_{P_n-1}^2 P_{P_{P_n-1}-1}^4-180 P_{P_n-1} P_{P_{P_n-1}-1}^6-60 P_{P_{P_n-1}-1}^8-800 P_{P_n-1}^3 P_{P_{P_n-1}-1}-540 P_{P_n-1}^2 P_{P_{P_n-1}-1}^3-260 P_{P_n-1} P_{P_{P_n-1}-1}^5-90 P_{P_{P_n-1}-1}^7+8960 P_n P_{P_n-1}-1408 P_{P_n-1}^3+2240 P_n P_{P_{P_n-1}-1}^2-368 P_{P_n-1}^2 P_{P_{P_n-1}-1}^2-136 P_{P_n-1} P_{P_{P_n-1}-1}^4-49 P_{P_{P_n-1}-1}^6+2240 P_n P_{P_{P_n-1}-1}-128 P_{P_n-1}^2 P_{P_{P_n-1}-1}+68 P_{P_n-1} P_{P_{P_n-1}-1}^3+63 P_{P_{P_n-1}-1}^5+4480 P_n+288 P_{P_n-1}^2+336 P_{P_n-1} P_{P_{P_n-1}-1}^2+170 P_{P_{P_n-1}-1}^4+272 P_{P_n-1} P_{P_{P_n-1}-1}+180 P_{P_{P_n-1}-1}^3+3072 P_{P_n-1}+776 P_{P_{P_n-1}-1}^2+704 P_{P_{P_n-1}-1}+1408
```

虽然很长，但仍然可以 $O(1)$ 求出，又因为 $Q(P_{P_{P_n-1}-1})$ 可以预处理，于是第二项可以 $O(1)$ 求出。

## 复杂度

空间复杂度是 $\Theta(n^{\frac{1}{8}})$，因为需要预处理 $\Theta(n^{\frac{1}{8}})$ 大小的前缀和。

假设大数计算的时间复杂度为 $\Theta(1)$。

预处理的时间复杂度显然是 $\Theta(n^{\frac{1}{8}})$。

设计算 $Q(2^{2^x})$ 的时间复杂度为 $T(x)$。有 $T(x)=O(1)+T(x-1)+T(x-2)$，于是 $T(x)=\Theta(\left(\frac{1+\sqrt{5}}{2}\right)^x)$，故单次询问时间复杂度为 $\Theta(\left(\frac{1+\sqrt{5}}{2}\right)^{\log_2{\log_2{n}}})=\Theta((\log_2{n})^{\log_2{\frac{1+\sqrt{5}}{2}}})$。

## 实现

那些很长的多项式导致常数极大，需要卡常。

* 预处理时适当地通过加法计算 $Q(x)$ 的系数，从而避免使用高精度乘法。
* 用尽量少的计算次数计算那些非常长的多项式。例如可以用 Horner 形式重写多项式。
* 压位高精度。

[代码](https://www.luogu.com.cn/paste/mpu69nv8)