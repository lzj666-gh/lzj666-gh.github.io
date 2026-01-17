# P3807 题解

卢卡斯定理

---
首先我们需要证明$C_p^i\equiv\frac{p}{i}C_{p-1}^{i-1}\equiv 0~~~(mod~p),(1<=i<=p-1)$

$C_p^i=\frac{p!}{i!(p-i)!}=\frac{p}{i} \frac{(p-1)!}{(i-1)!(p-1-i+1)!} \frac{p}{i} \frac{(p-1)!}{(i-1)!(p-i)!}=\frac{p}{i}C_{p-1}^{i-1}$

得证。

然后根据这种性质和二项式定理。，我们马上得出

$(1+x)^p\equiv C_p^0+C_p^1x^{1}+....+C_p^px^p\equiv C_p^0x^0+C_p^px^p\equiv 1+x^p(mod ~p)$

然后我们接下来要求证，这个式子是我们递归时用到的。

$C_a^b\equiv C_{a_0}^{b_0}\cdot C_{a_1p}^{b_1p} \cdot C_{a_2p^2}^{b_2p^2}.....(mod~p)$

但其实我们令$a=lp+r,b=sp+j$~~随便起的~~  

求证$C_a^b\equiv C_{l}^{s}\cdot C_{r}^{j}(mod~p)$然后利用性质递归求解就可以了。

继续从二次项定理出发

$(1+x)^a=(1+x)^{lp} \cdot (1+x)^r$

然后展开$(1+x)^{lp}$

$(1+x)^{lp} \equiv ((1+x)^p)^l \equiv (1+x^p)^l(mod~p)$

$\therefore (1+x)^a \equiv (1+x^p)^l \cdot (1+x)^r(mod~p)$

观察项$x^b$的系数

$\because C_a^bx^b \equiv C_l^sx^{sp} \cdot C_r^jx^j(mod~p)$

$\therefore C_a^bx^b \equiv C_l^s \cdot C_r^jx^b(mod~p)$

$\therefore C_a^b\equiv C_l^s\cdot C_r^j \equiv C_{\lfloor \frac{a}{p} \rfloor}^{\lfloor \frac{b}{p} \rfloor}\cdot C_{a~mod~p}^{b~mod~p}(mod~p)$

Ps:左边的是原来不经过化简的二项式展开，同时因为保证了$a=lp+r,b=sp+j$,所以右边不会出现其他的项。

---
后：本人已退役qwq。而且并没有用上自己学的（自我感觉省选无望qwq）

而且也系统的学过了二项式（好像暴漏年龄了）

对之前的错误表示抱歉，也欢迎大家继续挑刺/cy

转载什么的就不用问。转~，都可以转~