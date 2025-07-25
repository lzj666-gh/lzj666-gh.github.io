# P10780 题解

## P10780 BZOJ3028 食物

考虑若**承德汉堡**和**可乐**共选了 $x$ 个，那么我们其实可以确定二者分别选了几个，即 $x-x\bmod 2$ 个和 $x\bmod 2$ 个，所以我们可以将二者合并，表示成这一类可以选任意多个。

同理，**鸡腿**和**面包**，**鸡块**和**包子**均能分别合并成选任意多个的两类。

发现**蜜桃多**至少选一个，把这一个提出来单独考虑，剩下的**蜜桃多**和**土豆片炒肉**也能合并成选任意多个的一类。

现在问题变为了：选一个**蜜桃多**，剩下四类食品每一类任选若干个，总共选 $n$ 个食品的方案数，即求解 $a+b+c+d=n-1$ 的非负整数解组数，由插板法易得答案为 $\dbinom{n+2}3=\dfrac{n(n+1)(n+2)}6$。