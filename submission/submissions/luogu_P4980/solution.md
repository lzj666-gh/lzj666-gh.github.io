# P4980 题解

长文警告。

本文对于 $\rm Polya$ 定理中使用到的绝大部分引理都进行了~~伪证~~ 较为成分的证明。

在阅读这篇文章的时候，您可以选择性的跳过您所知道的知识，下面将从 "群" 这一个充满魔法的东西开始谈起。

## 群

### 群的定义

定义集合 $\rm G$ 和作用与集合 $\rm G$ 的二元运算 $\times$ 

若其满足以下 $4$ 个性质，则称其为一个群$(\sf Group)$，记为 $(~G,\times~)$：

$1.$  封闭性 $(\sf Closure)$

> 若存在 $a$ 和 $b$ 满足 $a\in G,b\in G$ ，则有 $a\times b\in G$

$2.$  结合律 $(\sf Associativity )$

> 对于任意 $a,b,c$ 有 $(a\times b)\times c = a\times (b\times c)$

$3.$  单位元 $(\sf Identity)$

>存在 $e\in G$，满足对于任意 $a\in G$ 有： $a\times e = e\times a = a$
>
> 这样的 $e$ 被称为单位元。容易证明单位元唯一（你假设有多个可以马上推出矛盾）
>
> $\rm e.g:$ 实数的乘法运算就是一个群，模意义下的乘法运算（不包括$0$）同样是一个群。这些例子中的单位元均为 $1$

$4.$  逆元 $(\sf Inverse)$

>对于任意 $a\in G$ 存在 $a'\in G$ 满足 $a\times a' = a'\times a = e$
>
>值得注意的是这个 $a'$ 是唯一的。读者可以尝试自行证明。


**性质的实际应用：**

$\sf 1- question:$  为什么不能使用传统的树状数组实现区间最值查询。

$\sf 1-answer:$ 树状数组在于运算上存在一个差分的过程，换而言之需要"逆元"的存在，然而最值函数与数集$\rm S$不构成群。~~（好像在扯淡）~~

### 子群：

如果 $H$ 为 $G$ 的一个子集，且有 $(~H,\times ~)$ 构成一个群，那么称 $(H,\times )$ 为 $(G,\times)$ 的一个子群。简记为 $H\le G$。

如果 $G$ 是一个群，$H$ 为其一个子群，且有 $g\in G$，那么：

> $gH={g\times h,h\in H}$，称其为 $H$ 在 $G$ 内的关于 $g$ 的左陪集。

> $Hg={h\times g,h\in H}$，称其为 $H$ 在 $G$ 内的关于 $g$ 的右陪集。

陪集的一些性质：

下面只讨论右陪集：（左陪集同理）


> $1.$ $\forall g\in G$，$|H|=|Hg|$

证明：注意到 "群的性质" ： 逆元唯一，所以有对于任意的 $g\times h_1$ 与 $g\times h_2$ 其必然不同。

> $2.$ $\forall g\in G$，$g\in Hg$

证明：注意到 $H$ 是一个群，所以 $H$ 必然包括了单位元$e$，所以 $e\times g\in Hg\iff g\in Hg$

> $3.$ $Hg = H\iff g\in H$

证明显然，由于封闭性可以得到。

> $4.$ $H a=Hb\iff a\times b^{-1}\in H$

证明：

首先你发现陪集像极了运算，所以有：$Ha=Hb \implies Ha\times b^{-1}=H$ 由于性质$3$ 得到： $a\times b^{-1}\in H$

由于 $a\times b^{-1}\in H$ 所以 $Ha = Hb$ ...这个显然，配合性质 $3$ 食用。

> $5.$ $Ha\cap Hb\ne \varnothing \to Ha=Hb$ 

这个性质非常有用，其意味着一个子群 $H$ 的陪集的交集要么是空要么两个相等。

证明：假设 $c\in Ha,c\in Hb$ ，于是有 $\exists ~h_1,h_2\in H$，$h_1\times a=c,h_2\times b=c$ 所以我们得到：$ab^{-1}=h_2 h_1^{-1}\in H$ 由于 性质$4$ 得到 $Ha=Hb$。

> $6.$ $H$ 的全体右陪集的并为 $G$

证明：因为 $H$ 存在单位元，$g$ 取遍 $G$ 中每一个元素。

#### 较为常见的表述：

若 $H\le G$，则 $G/H$ 代表 $G$ 中所有的 $H$ 的左陪集即$\{gH,g\in G\}$

若 $H\le G$，则 $[G:H]$ 表示 $G$ 中 $H$ 的不同的陪集的数量。


#### **拉格朗日定理：**

对于有限群 $G$ 与有限群 $H$ ，若 $H$ 为 $G$ 的子群，那么有：

$$|H| \text{整除} |G|$$

即 $H$ 的阶整除 $G$ 的阶。

更具体点：

$$|H|\times [G:H]=|G|$$

证明：

由于陪集的性质$1,5,6$，所有本质不同的陪集互不相交且大小均为 $|H|$ 且并的大小为$|G|$，可以得到不同的陪集数量乘以陪集大小$(|H|)$为 $G$ 。你会发现有了陪集的性质之后这些都特别自然了。

## 置换

> 备注：一个充满魔法的科技。

### 一些定义：

-----

#### **$\sf Two-line notation$**

双行表示法，大概就是用两个括号括起来，然后令 "元素/置换" 表示一个从【上列】 到 【下列】 的置换。

比如：

$\sigma=\begin{pmatrix}1&2&3&4&5\\2&5&4&3&1\end{pmatrix}$

其表示的置换为将排列 $1~2~3~4~5$ 变为 $2~5~4~3~1$ 的一个置换，可以理解为用原本第二个元素代替第一个元素，用原本的第 $5$ 个元素代替第 $2$ 个元素...依次类推。


不过我更喜欢强行规定第一列是 $(1,2,...n)$

然后第二列就是：

$\sigma =(a_1,a_2...a_n)$ 表示一个置换。

每个置换都是一个这样的排列，一个长度为 $n$ 的不同的置换的数量为 $n!$ 


#### 运算：

可以写为 $\sigma \times a$ 不过更习惯被表示为 $\sigma(a)$ 

其运算规则为：$\sigma(a)= (a_{\sigma_1},a_{\sigma_2}...a_{\sigma_n})$

没错，这是一个运算，通常可以称呼其为置换的「魔法」/「乘法」，如上例可以用文字描述为：$\sigma$ 和 $a$「魔法」起来。（这里是我个人认为它非常神奇而称呼其为「魔法」诸位笑笑便好）

更正式的，我们称呼其为置换的「合成」

### 置换群：

不妨令集合 $N = \{1,2,3...n\}$ ，令集合 $M$ 为 $N$ 的若干个排列构成的集合，我们令群 $G=(M,\times )$，其中 $\times$ 这个运算为「魔法」/「合成」，若再此基础上，其满足群的性质。则我们称 $G$ 是一个置换群。

我们现在来验证一个例子，$N$ 的所有可能的排列与运算「魔法」构成的 "二元组?"（这里不太清楚如何称呼） 是一个合法的置换群：


$1.$ 封闭性，显然，注意上面定义的是所有可能的排列。

$2.$ 单位元$~:e=(1,2,...n)$

> 容易发现 $\sigma$「魔法」$e= e$「魔法」$\sigma=\sigma$

$3.$ 结合律：容易验证「魔法」满足结合律。

$4.$ 逆元：容易验证「魔法」运算存在逆元。


### 「群作用」

分为 左群作用 和 右群作用。具体不太记得了...下面描述的是左群作用的定义，下文出于方便，将同一称为「群作用」，并使用此处的定义。

定义：

对于一个集合 $M$ 和群 $G$ 。

若给定了一个二元函数 $\varphi(v,k)$ 其中 $v$ 为群中的元素，$k$ 为集合元素，且有：

$$\varphi(e,k)=k\quad (e~\text{是单位元})$$

$$\varphi(g,\varphi(s,k))=\varphi(g\times s,k)$$

则称呼群 $G$ 作用于集合 $M$。


### 轨道-稳定子定理：

----

#### 轨道

考虑一个作用在 $X$ 上的群 $G$ 。 $X$ 中的一个元素 $x$ 的「轨道」则是 $x$ 通过 $G$ 中的元素可以转移到的元素的集合。$x$ 的轨道被记为 $G(x)$，方便起见，我们用 $g(x)$ 表示群 $G$ 元素 $g$ 作用于 $x$ 的群作用的返回值，即 $g(x)=\varphi(g,x)$。

#### 稳定子

稳定子被定义为：$G^x = \{g|g\in G,g(x)=x\}$

使用语言描述，便是群 $G$ 中满足 $g(x)=x$ 的所有元素 $g$ 所构成的集合。

$\rm e.g:$

给定一个 $2\times 2$ 的矩形，每个点可以使用黑白染色，这样得到的所有矩形构成的集合为 $M$

给定一个群 $G$ ，其成员为 $1.$ 顺时针旋转$90$°，$2.$ 顺时针旋转$180$°，$3.$ 顺时针旋转$270$°，$4.$ 顺时针旋转$0$°。其运算为模$360$意义下的加法（大概，想必诸位理解我的意思）

那么对于一个 $M$ 内的一个元素（$0$表示白，$1$表示黑）

$\begin{pmatrix}1&1\\0&0\end{pmatrix}$

而言，其稳定子 $G^x$ 为 $\{$顺时针旋转$0$°$\}$

其轨道为：


$\begin{pmatrix}1&1\\0&0\end{pmatrix},\begin{pmatrix}0&1\\0&1\end{pmatrix},\begin{pmatrix}0&0\\1&1\end{pmatrix},\begin{pmatrix}1&0\\1&0\end{pmatrix}$

似乎有一个巧合，轨道大小与稳定子的大小乘积为 $4$ 刚好是群 $G$ 的大小！

* 诸位可以去举其他例子来类比，总是可以发现这个规律。

这个东西有一个名字，叫做轨道-稳定子定理：


#### 轨道-稳定子定理：

$$|G^x|\times |G(x)|=|G|$$

首先可以证明：$G^x$ 是 $G$ 的一个子群。

首先根据群作用的定义，我们得知：$e\in G^x$

结合律显然满足，我们接下来考虑证明逆元和封闭性。

封闭性：$f\in G^x, g\in G^x$ 则 $f(x)=x,g(x)=x$ 根据群作用的定义，此时有：$(f\times g)(x)=x$，所以 $f\times g\in G^x$

逆元：若 $g\in G^x$ 则 $g(x)=x$ 又因为 $(g\times g^{-1})(x)=e(x)=x$ 所以 $g^{-1}(x)=x$ 所以 $g^{-1}\in G^x$

所以按照拉格朗日定理有： $|G^x|\times [G:G^x] = |G|$

于是只需要证明 $[G:G^x]=|G(x)|$

然后这个东西直观感受挺对的...但是还是丢一个严谨的证明：

我们只需要证明，每一个 $g(x)$ 都能对应 $[G:G^x]$ 中的一个左陪集/右陪集即可。

不妨这样构造一个一一对应的关系：

若 $f(x)=g(x)$ 则可得：$f\times g^{-1}=x=e(x)\in G^x$，由于陪集的性质$f\times G^x=g\times G^x$ ，这意味着我们证明了相同的 $f(x)$ 都可以对应相同的陪集。

反之亦然 $fG^x=gG^x\iff f(x)=g(x)$

于是每一个 $g(x)$ 我们令 $gG^x$ 表示它对应的陪集即可，正确性由上述性质保证不会重复，相同的 $g(x)$ 总是对应着相同的陪集。


## **Burnside** 定理

公式：

定义 $G$ 为一个置换群，定义其作用于 $X$，如果 $x,y\in X$ 在 $G$ 作用下可以相等即存在 $f\in G$ 使得 $f(x)=y$ 则定义$x,y$ 属于一个等价类，则不同的等价类的数量为：

$$|X/G|=\dfrac{1}{|G|}\sum_{g\in G} X^g$$

其中， $X^g$ 为 $X$ 在 $g$ 作用下的不动点的数量。即满足 $g(x)=x$ 这样的 $x$ 的数量。

文字描述：$X$ 在群 $G$ 作用下的等价类总数等于每一个 $g$ 作用于 $X$ 的不动点的算数平均值。

证明：

由于每个元素属于仅属于一个轨道，轨道内部在群 $G$ 作用下互达，(陪集性质) 所以我们可以得到：

$$|X/G|=\sum_{x\in X} \dfrac{1}{[G:G^x]}$$

根据轨道-稳定子定理，得到：

$$[G:G^x]=\dfrac{G}{|G^x|}$$

$$|X/G|=\sum_{x\in X}\dfrac{G^x}{G}$$

$$|X/G|=\dfrac{1}{|G|}\sum_{x\in X} G^x$$

后面那一坨，反过来，就是对于每一个群作用 $g$ ，其作用下不动点的数量。

综上，我们得到 $\sf Burnside$ 定理。

--------

### 回到本题，下面的关于本题的做法在一定程度上算对于 $\rm P\acute{o}lya$ 定理的推导。

首先观察本题与 $\sf Burnside$ 定理的关系。

容易发现，本质不同的 $n$ 个点的环可以看作，在群 $G$ 为$\{$ 旋转$0$ 个，旋转 $1$ 个...旋转$n-1$个 $\}$ 这些置换作用下得到的等价类的数量。

同时我们定义集合 $M$ 为 $\{1\to n\}$ 的所有可能排列表示初始的环。

于是由于 $\sf Burnside$ 定理，得到：

$$Ans=\dfrac{1}{|G|}\sum_{g\in G}M^g$$
  
我们依次考虑每个置换对于答案的贡献，显然旋转 $0$ 个的不动点的数量为：$n^n$ 即所有集合都合法。

对于旋转 $k$ 个而言，我们知道一个元素是不动点等价于其存在一个长度为 $a$ 的循环节满足 $a|k$ ，又因为对于循环节 $a$ 而言，必然存在 $a|n$ ，所以我们可以改写判定条件为存在一个长度为 $\gcd(k,n)$ 的循环节。

于是对于旋转 $k$ 个而言，每个子串的前 $\gcd(k,n)$ 都是任意取的，所以得到其贡献为 $n^{\gcd(k,n)}$

于是答案为：

$$\dfrac{1}{n}\sum_{k=1}^n n^{\gcd(k,n)}$$

剩下的就是莫比乌斯反演那一套的套路工作了，下面简单推导：

枚举 $\rm gcd$ 变为：

$$\dfrac{1}{n}\sum_{d|n} n^d \times \sum_{k=1}^{\frac{n}{d}} [\gcd(k,\dfrac{n}{d})==1]$$

后面那个式子是欧拉函数，直接带入即可：

$$\dfrac{1}{n}\sum_{d|n}n^d \varphi(\frac{n}{d})$$

然后本题暴力计算欧拉函数是可以通过的，复杂度为$O(Tn^{\frac{3}{4}})$

$Code:$

```cpp
#include<bits/stdc++.h>
using namespace std ;
#define rep( i, s, t ) for( register int i = s; i <= t; ++ i )
#define re register
#define int long long
int gi() {
	char cc = getchar() ; int cn = 0, flus = 1 ;
	while( cc < '0' || cc > '9' ) {  if( cc == '-' ) flus = - flus ; cc = getchar() ; }
	while( cc >= '0' && cc <= '9' )  cn = cn * 10 + cc - '0', cc = getchar() ;
	return cn * flus ;
}
const int P = 1e9 + 7 ; 
int T, n ; 
int fpow( int x, int k ) {
	int ans = 1, base = x ; 
	while( k ) {
		if( k & 1 ) ans = 1ll * ans * base % P ; 
		base = base * base % P, k >>= 1 ; 
	} return ans ; 
}
int phi( int x ) {
	int ans = x ; 
	for( re int i = 2; i <= sqrt(x); ++ i ) {
		if( x % i ) continue ;
		ans = ans - ans / i ;
		while( x % i == 0 ) x /= i ;
	}
	if( x != 1 ) ans = ans - ans / x ;
	return ans ; 
}
void inc( int &x, int y ) {
	( ( x += y ) >= P ) && ( x -= P ) ;
}
signed main()
{
	int T = gi() ; 
	while( T-- ) {
		int n = gi(), cnt = sqrt(n), Ans = 0 ; 
		for( re int i = 1; i <= cnt; ++ i ) {
			if( n % i ) continue ;
			int p1 = phi(i), f1 = fpow( n, n / i ) ; 
			f1 = f1 * p1 % P, inc( Ans, f1 ) ;
			if( i * i != n ) {
				int p2 = phi( n / i ), f2 = fpow( n, i ) ;
				f2 = f2 * p2 % P, inc( Ans, f2 ) ;
			}
		}
		cout << Ans * fpow( n, P - 2 ) % P << endl ; 
	}
	return 0 ;
}
```

这样，这道题做完了，但是这篇文章还没完，接下来要介绍 $\rm P\acute{o}lya$ 定理。（其实也差不多）

## $\rm P\acute{o}lya$ 定理

考虑如何快速的使用 $\sf Burnside$ 定理进行计算。

我们可以注意到在一般的染色问题/类似的问题求本质不同的xxx的问题当中（即 $\sf Burnside$ 派上用场的时候）我们一般都是要求不动点的数量。

对于一个置换 $(a_1,a_2...a_n)$ 按照前文，我们规定上列为 $(1,2...n)$ 则其描述的是第一个位置变成 $a_1$...诸如此类的轮换。

在使用 $\sf Burnside$ 解决染色问题的时候，我们需要求的是不动点的数量，而对于上述的置换，假设我们令每个 $i$ 向 $a_i$ 连一条边容易发现会得到若干个环，仔细思考，每个环的颜色应当相同。

我们定义这个环的数量为 $c(g)$ 即置换 $g$ 的轮换(环)数。

那么我们现在可以改写 $\sf Burnside$ 定理为：

$$\dfrac{1}{|G|}\sum_{g\in G}m^{c(g)}$$

$m$ 表示可用的颜色数。

这就是 $\rm P\acute{o}lya$ 定理辣！

* 如果你认真的读完了前文的内容，那么这一步应该是相当显然的（

完结撒花！

-------

## 参考资料：

https://www.cnblogs.com/cyx0406/p/burnside_and_polya.html

https://www.cnblogs.com/yyf0309/p/Burnside.html

https://en.wikipedia.org/wiki/Burnside%27s_lemma

https://en.wikipedia.org/wiki/Group_action

https://en.wikipedia.org/wiki/Coset

https://en.wikipedia.org/wiki/Lagrange%27s_theorem_(group_theory)

感谢 tiger 对于本文的改正意见以及指导。