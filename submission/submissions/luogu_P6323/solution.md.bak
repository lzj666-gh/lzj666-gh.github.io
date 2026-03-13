# P6323 题解

本题存在低于 $O(nc)$ 的做法。

逆序对是大小关系，我们在小的那个数处统计每对逆序对，考虑从大到小插入每一个数，这样所有数都比他大，这样它插入在第 $i$ 个就会产生 $i$ 个逆序对，假设现在有 $x$ 个数则它可以产生 $[0,x]$ 中个逆序对，且每种都恰好有一种插法。


那么我们现在可以进行一个 $O(nc^2)$ 的 dp 了，$f_{i,j}$ 表示前 $i$ 个数有 $j$ 个逆序对的方案数，使用前缀和优化可以做到 $O(nc)$。

---

重新回顾我们现在的问题：第 $i$ 个数在 $[0,i)$ 中任选，求所有数和为 $c$ 的方案数，

考虑没有 $[0,i)$ 这个限制的方案数，$n$ 个任意正整数和为 $c$，这是经典的插板法，答案即 $\dbinom {c+n-1}{n-1}$。

我们考虑容斥去掉限制，$[0,i)$ 是困难的，而将其容斥为 $[i,+\infty)$ 后是简单的，我们直接从 $c$ 中扣掉 $i$ 即可。

钦定一些 $i$ 超限了，我们只关心我们钦定的 $i$ 的和为 $s$ 的容斥系数之和。

---

问题变为对所有 $s$ 求出 $1\dots n$ 中选一些数 $s$ 和为 $s$ 的容斥系数之和，每选一个数带来 $-1$ 的容斥系数。

这个问题直接做似乎还是只能 $O(nc)$。

考虑经典的性质：最多选择了 $O(\sqrt c)$ 个数，否则和一定 $>c$。

证明：选择前 $t$ 小的数的和是 $\frac {t(t+1)}{2}=O(t^2)$ 的，所以无论如何选的个数都是 $O(\sqrt c)$ 级别的。

---

于是我们考虑从竖着一个数一个数 dp，换成横着一层一层 dp，从大到小加入每个数 $a_1\dots a_n$，则 $a_{i}-a_{i+1}$ 会在 $i$ 个数中产生贡献，即 $\sum a_i=\sum i\times (a_i-a_{i-1})$。（相当于给所有已经加入的数”垫高“若干并加入新的数）

让 $f_{i,j}$ 表示目前有 $i$ 个数，$\sum_{x=1}^{i} i\times (a_i-a_{i-1})$为 $j$ 的方案数，那么我们有

$$

f_{i,j}=f_{i-1,j-i}+f_{i,j-i} - f_{i-1,j-n-1}
$$

分别表示：新加入一个数并往上垫高一层，往上垫高一层。

然后因为要求了每个数都不超过 $n$，我们减去第一个数在垫高这一层后达到 $n+1$ 的情况，这是一个子问题，减去 $n+1$ 后变为一个 $i-1$ 个数和为 $j-n-1$ 的方案数。
 
 
于是我们在 $O(c\sqrt {c})$ 的时间复杂度内解决了本题。

---

代码：2024/6/20 提交时为最优解。

```cpp
#include<bits/stdc++.h>
#define ll long long
#define ull unsigned long long
#define all(x) x.begin(),x.end()
#define FIN(x) freopen(#x,"r",stdin)
#define FOUT(x) freopen(#x,"w",stdout)
#define cerr(x) cerr << #x"= " << x << "\n" 
#define rep(i,x,y) for(int i = (x) ; i <= (y) ; ++ i)
#define Rep(i,x,y) for(int i = (x) ; i >= (y) ; -- i)
#define SYNC(x) std :: ios :: sync_with_stdio (x); if (!x) {cin.tie(0);cout.tie(0);}
using std :: cin , std :: cout , std :: cerr ;
template<ll Mod> 
struct math {
    std :: vector <ll> fac , fiv , inv ;
    ll pow (ll x , ll y = Mod - 2) {
        ll res = 1 ; 
        for (x %= Mod ; y ; (x *= x) %= Mod , y >>= 1)
            if (y & 1)
                (res *= x) %= Mod ;
        return res; 
    }

    inline math () {}
    inline math (int n) : fac(n + 1) , fiv(n + 1) , inv(n + 1) {
        fac[0] = 1 ; 
        rep (i,1,n)
            fac[i] = fac[i - 1] * i % Mod ;
        fiv[n] = pow(fac[n]) ;
        Rep (i,n,1)
            fiv[i - 1] = fiv[i] * i % Mod ,
            inv[i] = fac[i - 1] * fiv[i] % Mod ;
    }
    inline void init (int n) {
        fac.resize(n + 1) , fiv.resize(n + 1) , inv.resize(n + 1) ;
        fac[0] = 1 ; 
        rep (i,1,n)
            fac[i] = fac[i - 1] * i % Mod ;
        fiv[n] = pow(fac[n]) ;
        Rep (i,n,1)
            fiv[i - 1] = fiv[i] * i % Mod ,
            inv[i] = fac[i - 1] * fiv[i] % Mod ;
    }

    inline ll binom (int n,int m) {
        if (n < m || m < 0)
            return 0;
        return fac[n] * fiv[m] % Mod * fiv[n - m] % Mod ;
    }
    inline ll perm (int n,int m) {
        if (n < m || m < 0)
            return 0;
        return fac[n] * fiv[n - m] % Mod ;
    }
    inline ll bracket (int x) {
        return fac[x * 2] * fiv[x] % Mod * fiv[x + 1] % Mod ;
    }
} ;


const int mod = 1e9 + 7 ;

inline void inc (int &tar,int ths) {
    if ((tar += ths) >= mod) 
        tar -= mod ;
}
inline void dec (int &tar,int ths) {
    if ((tar -= ths) < 0) 
        tar += mod ;
}

signed main( ) {  SYNC (false); 
    int n , c ;
    cin >> n >> c ;
    math<mod> M (n + c) ;
    std :: vector <int> f (c + 1) ;
    f[0] = 1 ; 
    ll res = M.binom (c + n - 1 , n - 1) ;
    for (int i = 1 ; i * (i + 1) / 2 <= c && i <= n ; ++ i) {                
        std :: vector <int> g(c+1) ;
        rep (j,i,c) {   
            g[j] = f[j - i] ;
            inc (g[j] , g[j - i]) ;
            if (j >= n + 1)
                dec (g[j] , f[j - n - 1]) ;
        }

        f.swap(g) ;
        rep (j,0,c) {
            (res += (i&1?mod-f[j]:f[j]) * M.binom (c - j + n - 1 , n - 1)) %= mod ;   
        }   
    }
    cout << res << '\n' ;
}
```



---

更加本质的东西：

直接从生成函数和 Ferrers 图像的角度也可以得到相同复杂度的做法，上面那个容斥的本质是 $(1+x^1+x^2\dots x^p)=\frac {(1-x^{p+1})}{(1-x)}$，后面的部分我们是在快速求 $[x^c]\prod_{i=1}^{n}(1-x^i)$，从分拆数等角度有很多 $O(c\sqrt c)$ 的做法。