# P5686 题解

感觉现在这里的题解都比较啰嗦，写一个简单一点的数学推导……

考虑$O(n)$枚举每个右端点$r$。我们要求的式子即

$ans_r=\sum_{l=1}^rS(l,r)=\sum_{l=1}^rS(l,r)=\sum_{l=1}^r(\sum_{i=l}^ra_i\times \sum_{i=l}^rb_i)$

记$suma_i=\sum_{j=1}^ia_i,sumb_i=\sum_{j=1}^ib_i$，即$a_i,b_i$的前缀和，特别地，记$suma_0=sumb_0=0$，则

$ans_r=\sum_{l=1}^r(suma_r-suma_{l-1})(sumb_r-sumb_{l-1})$

$\text{ }\text{ }\text{ }\text{ }\text{ }\text{ }\text{ }\text{ }=\sum_{l=1}^r(suma_rsumb_r-suma_{l-1}sumb_r-suma_{r}sumb_{l-1}+suma_{l-1}sumb_{l-1})$

$\text{ }\text{ }\text{ }\text{ }\text{ }\text{ }\text{ }\text{ }=r\times suma_rsumb_r-sumb_r\sum_{l=0}^{r-1}suma_l-suma_r\sum_{l=0}^{r-1}sumb_l+\sum_{l=0}^{r-1}suma_lsumb_l$

扫描的时候可以用三个变量分别记录$suma_l,sumb_l,suma_l\times sumb_l$的和，套入上式直接计算即可，再更新变量的值。

最后输出$\sum_{r=1}^nans_r$即可。

总时间复杂度$O(n)$。