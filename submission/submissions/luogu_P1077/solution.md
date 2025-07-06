# P1077 题解

# 摆花解题报告

> 这是一篇长达三年的解题报告。

### update on 2020.10.21：

增加了前缀和优化

### update on 2021.03.18：

增加了生成函数做法，修改了部分内容，更正了部分谬误。

### update on 2021.07.30：

增加了生成函数（封闭形式）的做法，更正了部分谬误。

## （〇）数学符号注释

> 本文中的某些符号体系并不标准，一些读者会在其他书中学习类似的内容。这里列出了他们可能不熟悉的符号。

| 符号                      | 名称                       | 等价形式                                            |
| :------------------------ | :------------------------- | :-------------------------------------------------- |
| $\sum\limits_{i=1}^na_i$  | 求和（和式）               | $a_1+a_2+\cdots+a_{n-1}+a_n$                        |
| $\prod\limits_{i=1}^na_i$ | 求积                       | $a_1\times a_2\times\cdots\times a_{n-1}\times a_n$ |
| $[m=n]$                   | 如果$m=n$值为$1$;否则为$0$ | $\begin{cases}1&m=n\\ 0& m\not=n\end{cases}$        |


## （一）题目大意

[题目传送门](https://www.luogu.org/problemnew/show/P1077)

简化一下题意：

有 $n$ 个数（$c_1,c_2,...,c_n$）， $0\leqslant c_i\leqslant a_i$,求有多少种方案数使$\sum\limits_{i=1}^nc_i = m$。

## （二）解题思路

乍一看，似乎题目有些复杂，一时找不到思路，肿么办!!!

### 方法一：搜索

没有思路当然就搜索啦 ~~废话~~。如何搜索呢？

从 1 到 $n$​ 考虑每个 $c_i$​ 的值，和当前前 $i$​ 个数的总和 $k$​，然后枚举当前 $x_i$​ 所有可能的值，再递归求解。

时间复杂度 $O(\prod\limits_{i=1}^na_i)$，明显超时，~~但可以拿部分分（30）嘛...~~

代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
const int maxn=105, mod = 1000007;
int n, m, a[maxn];
int dfs(int x,int k)
{
    if(k > m) return 0;
    if(k == m) return 1;
    if(x == n+1) return 0;
    int ans = 0;
    for(int i=0; i<=a[x]; i++) ans = (ans + dfs(x+1, k+i))%mod;
    return ans;
}
int main()
{
    cin>>n>>m;
    for(int i=1; i<=n; i++) cin>>a[i];
    cout<<dfs(1,0)<<endl;
    return 0;
}
```

搜索超时怎么办!!! 别着急...

### 方法二（搜索优化法宝）：记忆化

所谓记忆化，其实就是用一个数组将搜索过的值存起来，避免重复搜索，从而提高效率。~~（有必要可以上网搜一下，会搜索的应该很容易理解记忆化吧）~~

时间复杂度大概是：$O(nma_i)$ 吧，100%的数据稳过。

代码（其实只是改动了一点点）：

```
#include<bits/stdc++.h>
using namespace std;
const int maxn=105, mod = 1000007;
int n, m, a[maxn], rmb[maxn][maxn];
int dfs(int x,int k)
{
    if(k > m) return 0;
    if(k == m) return 1;
    if(x == n+1) return 0;
    if(rmb[x][k]) return rmb[x][k]; //搜过了就返回
    int ans = 0;
    for(int i=0; i<=a[x]; i++) ans = (ans + dfs(x+1, k+i))%mod;
    rmb[x][k] = ans; //记录当前状态的结果
    return ans;
}
int main()
{
    cin>>n>>m;
    for(int i=1; i<=n; i++) cin>>a[i];
    cout<<dfs(1,0)<<endl;
    return 0;
}
```

但是搜索的时间有些不稳定，想要更稳定的算法有木有...

### 方法三：动态规划

记忆化搜索都可以转成动态规划，但是动态规划却不一定能转成记忆化搜索 ——$by$  $clg$

定义状态：$f(i, j)$ 表示前 $i$ 个数总和为 $j$ 的方案数。

那么，易得状态转移方程：$f(i, j) = \sum\limits_{k=0}^{a_{i}}f(i-1,j-k)$

其中, $k$是枚举当前第 $i$ 个数的取值。

时间复杂度：$O(nma_i)$，稳得一批。

空间复杂度：$O(nm)$

代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
const int maxn=105, mod = 1000007;
int n, m, a[maxn], f[maxn][maxn];
int main()
{
    cin>>n>>m;
    for(int i=1; i<=n; i++) cin>>a[i];
    f[0][0] = 1;
    for(int i=1; i<=n; i++)
       for(int j=0; j<=m; j++)
           for(int k=0; k<=min(j, a[i]); k++)
              f[i][j] = (f[i][j] + f[i-1][j-k])%mod;
    cout<<f[n][m]<<endl;
    return 0;
}
```

仔细观察上述代码，有木有发现什么...

### 方法四(dp优化法宝)：滚动数组

因为我们发现，状态转移方程中，当前状态 $f(i, j)$只跟 $f(i-1, j)$ 有关系，与 $i-2,i-3...$无关。于是，我们可以利用滚动数组优化dp。

所谓滚动数组，其实就是**只保留两个状态**（当前状态和前一个状态），算完当前状态后，将当前状态变为前一个状态，再去算下一个状态，看上去就像二维数组的两层不断地**迭代**。

时间复杂度：$O(nma_i)$

空间复杂度：$O(m)$

代码：

```
#include<bits/stdc++.h>
using namespace std;
const int maxn=105, mod = 1000007;
int n, m, a[maxn], f[2][maxn], t;
int main()
{
    cin>>n>>m;
    for(int i=1; i<=n; i++) cin>>a[i];
    f[0][0] = 1;
    for(int i=1; i<=n; i++)
    {
        t = 1-t; //滚动
        for(int j=0; j<=m; j++)
        {
            f[t][j] = 0; //注意初始化
            for(int k=0; k<=min(j, a[i]); k++)
              f[t][j] = (f[t][j] + f[1-t][j-k])%mod;
        }
    }
    cout<<f[t][m]<<endl;
    return 0;
}
```

看到上述dp代码，有木有感觉很熟悉...

这熟悉的优化方法... 这~~TM~~不就是个**背包**吗!!!

### 方法五(背包大法好)：一维动态规划

通过观察上面的代码，二维数组，数组滚动优化空间......还有那熟悉的格式...

猛然发现这怎么可能不是**背包**呢（01背包）？

既然是背包，那么就可以为所欲为啦... [邪恶.jpg]

直接压成一维的**01背包**，跑一波，搞掂!!!

时间复杂度：$O(nma_i)$

空间复杂度：$O(m)$

代码：

```
#include<bits/stdc++.h>
using namespace std;
const int maxn=105, mod = 1000007;
int n, m, a[maxn], f[maxn];
int main()
{
    cin>>n>>m;
    for(int i=1; i<=n; i++) cin>>a[i];
    f[0] = 1;
    for(int i=1; i<=n; i++)
        for(int j=m; j>=0; j--) //注意，是01背包
            for(int k=1; k<=min(a[i], j); k++)
              f[j] = (f[j] + f[j-k])%mod;
    cout<<f[m]<<endl;
    return 0;
}
```

### 方法六：前缀和优化

继续观察方法五的代码，时间复杂度是$\Theta(n^3)$级别的。与背包有一些差别的是这一句：

```cpp
for(int k=1; k<=min(a[i], j); k++)
    f[j] = (f[j] + f[j-k])%mod;
```

然而，这一句的作用只不过是将连续的一段$f[j-a[i]]$到$f[j-1]$累加起来而已。因此，可以用前缀和将这个操作优化（众所周知，前缀和的作用就是$\Theta(1)$求一段区间的和）。

时间复杂度：$\Theta(nm)$

顺便卡到了次优解。

```cpp
#include<bits/stdc++.h>
using namespace std;
const int maxn = 105, mod = 1000007;
int n, m, f[maxn], sum[maxn], a[maxn];
int main(){
    cin>>n>>m;
    for(int i=1; i<=n; i++) cin>>a[i];
	f[0] = 1;
    for(int i=0; i<=m; i++) sum[i] = 1;
    for(int i=1; i<=n; i++){
    	for(int j=m; j>=1; j--) f[j] = (f[j] + sum[j-1] - sum[j - min(a[i], j) - 1] + mod)%mod;
		for(int j=1; j<=m; j++) sum[j] = (sum[j-1] + f[j])%mod;
	}
    cout<<f[m]<<endl;
    return 0;
}
```

提示：上面的程序在计算$f[j]$的时候有可能会出现数组越界的情况，但为了代码美观容易理解，没有特判。这一点需要注意，考场上不慎就会抱灵。

下面是加上了特判的代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
const int maxn = 105, mod = 1000007;
int n, m, f[maxn], sum[maxn], a[maxn];
int main(){
    cin>>n>>m;
    for(int i=1; i<=n; i++) cin>>a[i];
	f[0] = 1;
    for(int i=0; i<=m; i++) sum[i] = 1;
    for(int i=1; i<=n; i++){
    	for(int j=m; j>=1; j--){
    		int t = j - min(a[i], j) - 1;
    		if(t < 0) f[j] = (f[j] + sum[j-1])%mod;
    		else f[j] = (f[j] + sum[j-1] - sum[t] + mod)%mod;
		}
		for(int j=1; j<=m; j++) sum[j] = (sum[j-1] + f[j])%mod;
	}
    cout<<f[m]<<endl;
    return 0;
}
```

### 方法七：生成函数

建议初学者跳过此方法，权当提供一种思路。

回到开头，我们需要求的是这样一个式子：

$$\sum\limits_{c_k=0}^{a_k}\left[\sum\limits_{i=1}^nc_i=m\right ] ,k=\{1,2,...,n-1,n\}$$

于是我们可以构造这样一个生成函数：
$$
g(x)=(1+x^1+x^2+\cdots+x^{a_1})(1+x^1+x^2+\cdots+x^{a_2})\cdots(1+x^1+x^2+\cdots+x^{a_n})
$$
即，
$$
g(x)=\prod\limits_{i=1}^n\sum_{j=0}^{a_i}x^j
$$

#### 7.1多项式

最后所得的多项式中，$x^m$ 项的系数即为答案。可以做$n$​次NTT得到答案。假设$a_i$ 的值域是$k$ ，那么，

时间复杂度：$\Theta(n^2k\log nk)$

实际上，$m$最大可以取到$nk$。因此如果用$k$来表示，前缀和优化后的复杂度应当是：$\Theta(n^2k)$

NTT的局限在于要做$n$次。其实只需要取$\ln$就能将多项乘法转化为多项式加法，具体参考[付公主的背包](https://www.luogu.com.cn/problem/P4389)。

时间复杂度降到了$\Theta(nk\log nk)$​，即 $\Theta(m\log m)$​

#### 7.2封闭形式

也可以将其写成封闭形式，参考[[CEOI2004] Sweets](https://www.luogu.com.cn/problem/P6078)。

等比数列求和，得到：
$$
g(x)=\dfrac{\prod_{i=1}^n(1-x^{a_i})}{(1-x)^n}
$$
在 $n$ 较小，$m$ 很大的时候，可以考虑将 $\prod_{i=1}^n(1-x^{a_i})$​ 暴力展开，对于 $(1-x)^{-n}$ 使用牛顿二项式定理。即，
$$
(1-x)^{-n}=\sum_{i\ge0}\binom {n+i-1}{i}x^i
$$
枚举前一个式子 $x$ 的幂次，假设为 $k$，设 $x^k$ 项的系数为 $c_k$，那么，
$$
{\rm {ANS}}=\sum _{k=0}^m c_k\cdot\binom {n+m-k-1}{m-k}
$$
时间复杂度：$\Theta(2^n+m)$

## (三)总结

总的来说，这道题适合 搜索/动态规划 的初学者练习。

有一点点的思维难度。

这道题的价值在于，它既可以从简单的动态规划开始，一路优化，也可以从生成函数的视角观察，继续优化。这两条道路，竟是殊途同归。或许，这也是数学的魅力吧。