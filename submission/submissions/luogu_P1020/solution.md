# P1020 题解

> $\text{upd 2022.6.21}$：改了点笔误。

## 第一问

将拦截的导弹的高度提出来成为原高度序列的一个子序列，根据题意这个子序列中的元素是单调不增的（即后一项总是不大于前一项），我们称为**单调不升子序列**。本问所求能拦截到的最多的导弹，即求**最长的单调不升子序列**。

考虑记 $dp_{i}$ 表示「对于前 $i$ 个数，在选择第 $i$ 个数的情况下，得到的单调不升子序列的长度最长是多少」。于是可以分两种情况：

- 第 $i$ 个数是子序列的第一项。则 $\mathit{dp}_i\gets 1$。
- 第 $i$ 个数不是子序列的第一项。选择的第 $i$ 个数之前选择了第 $j$ 个数。根据题意，第 $j$ 个数的值 $h(j)$ 应当小于第 $i$ 个数的值 $h(i)$。枚举这样的 $j$，可以得到状态转移方程：

$$\mathit{dp}_i=\max_{j<i,h(j)\ge h(i)} \{\mathit{dp_j}+1\}$$

综合这两种情况，得到最终的状态转移方程：

$$\mathit{dp}_i=\max\{1,\max_{j<i,h(j)\ge h(i)}\{\mathit{dp}_j+1\}\}$$

![](https://cdn.luogu.com.cn/upload/image_hosting/25xnydfw.png)

值得注意的是，第 $n$ 个数不一定是最长单调不升子序列的最后一项。为了求出答案，我们需要枚举最后一项是哪个：

$$\mathit{ans}=\max_{1\le i\le n}\{\mathit{dp}_i\}$$

直接枚举进行状态转移，时间复杂度显然是 $\mathcal O(n^2)$。
下面考虑优化。

记 $f_i$ 表示「对于**所有**长度为 $i$ 的单调不升子序列，它的最后一项的大小」的最大值。特别地，若不存在则 $f_i=0$。下面证明：

- 随 $i$ 增大，$f_i$ 单调不增。即 $f_i\ge f_{i+1}$。

考虑使用反证法。假设存在 $u<v$，满足 $f_u<f_v$。考虑长度为 $v$ 的单调不升子序列，根据定义它以 $f_v$ 结尾。显然我们可以从该序列中挑选出一个长度为 $u$ 的单调不升子序列，它的结尾同样是 $f_v$。那么由于 $f_v>f_u$，与 $f_u$ 最大相矛盾，得出矛盾。

因此 $f_i$ 应该是单调不增的。

现在考虑以 $i$ 结尾的单调不升子序列的长度的最大值 $\mathit{dp}_i$。由于我们需要计算所有满足 $h(j)>h(i)$ 的 $j$ 中，$\mathit{dp}_j$ 的最大值，不妨考虑这个 $\mathit{dp}_j$ 的值是啥。设 $\mathit{dp}_j=x$，那么如果 $h(i)> f_x$，由于 $f_x\ge h(j)$，就有 $h(i)>h(j)$，矛盾，因此总有 $h(i)\le f_x$。

根据刚刚得出的结论，$f_i$ 单调不增，因此我们要找到尽可能大的 $x$ 满足 $h(i)\le f_x$。考虑二分。

![](https://cdn.luogu.com.cn/upload/image_hosting/0hratrdy.png)

绿色区域表示合法的 $f_x$（即 $f_x\ge h(i)$），红色区域表示不合法的 $f_x$（即 $f_x< h(i)$），我们需要找到红绿之间的交界点。

假设二分区域为 $[l,r)$（注意开闭区间。图上黄色区域标出来了二分区域内实际有效的元素）。每次取 $m=\frac{l+r}{2}$，如果 $f_m$ 在绿色区域内，我们就把 $l$ 移动到此处（$l\gets m$）；否则把 $r$ 移动到此处（$r\gets m$）。

当 $r-l=1$ 时，$l$ 处位置即为我们需要找的位置。转移 $\mathit{dp}_i\gets l+1$ 即可。记得更新 $f$。但是我们只用更新 $f_{\mathit{dp}_i}$，这是因为 $f_1,f_2,\cdots f_{\mathit{dp_i}-1}$ 的大小肯定都是不小于 $h(i)$ 的。$f_{\mathit{dp}_i}$ 是最后一个不小于 $h(i)$ 的位置，$f_{\mathit{dp}_i+1}$ 则小于 $h(i)$。

时间复杂度 $\mathcal O(n\log n)$，可以通过该问。

## 第二问

考虑贪心。

从左到右依次枚举每个导弹。假设现在有若干个导弹拦截系统可以拦截它，那么我们肯定选择这些系统当中位置最低的那一个。如果不存在任何一个导弹拦截系统可以拦截它，那我们只能新加一个系统了。

假设枚举到第 $i$ 个导弹时，有 $m$ 个系统。我们把这些系统的高度按照从小到大排列，依次记为 $g_1,g_2,\cdots g_m$。容易发现我们就是要找到最小的 $g_x$ 满足 $g_x\ge h_i$（与第一问相同，这是可以二分得到的），然后更新 $g_x$ 的值。更新之后，$g_1,g_2\cdots g_x$ 显然还是单调不增的，因此不用重新排序；如果找不到符合要求的导弹拦截系统，那就说明 $g_m<h_i$，直接在后头增加一个就行。

时间复杂度 $\mathcal O(n\log n)$，可以通过该问。

## 参考代码

```cpp
#include<bits/stdc++.h>
#define up(l,r,i) for(int i=l,END##i=r;i<=END##i;++i)
#define dn(r,l,i) for(int i=r,END##i=l;i>=END##i;--i)
using namespace std;
typedef long long i64;
const int INF =2147483647;
const int MAXN=1e5+3;
int n,t,H[MAXN],F[MAXN];
int main(){
    while(~scanf("%d",&H[++n])); --n;
    t=0,memset(F,0,sizeof(F)),F[0]=INF;
    up(1,n,i){
        int l=0,r=t+1; while(r-l>1){
            int m=l+(r-l)/2;
            if(F[m]>=H[i]) l=m; else r=m;
        }
        int x=l+1;  // dp[i]
        if(x>t) t=x; F[x]=H[i];
    }
    printf("%d\n",t);
    t=0,memset(F,0,sizeof(F)),F[0]=0;
    up(1,n,i){
        int l=0,r=t+1; while(r-l>1){
            int m=l+(r-l)/2;
            if(F[m]<H[i]) l=m; else r=m;
        }
        int x=l+1;
        if(x>t) t=x; F[x]=H[i];
    }
    printf("%d\n",t);
    return 0;
}
```

观察第二问的代码，与第一问进行比较，可以发现这段代码**等价于**计算最长上升子序列（严格上升，即后一项大于前一项）。这其实是 $\text{Dilworth}$ 定理（将一个序列剖成若干个单调不升子序列的最小个数等于该序列最长上升子序列的个数），本处从代码角度证明了该结论。