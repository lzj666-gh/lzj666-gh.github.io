# P4139 题解

各位dalao应该都知道扩展欧拉定理吧……

大概长这样：

对于任意$b \geq \varphi(p)$,有：

![](https://www.zhihu.com/equation?tex=a^b%20\equiv%20a^{b\text{%20mod%20}\varphi(p)%20%2B%20\varphi(p)}%20(\text{mod%20}p))

当$b < \varphi(p)$时有$a^b \equiv a^{b \text{ mod } \varphi(p)} (\text{mod } p)$


其中$a,p$可以不互质。

  
有了这个式子，题目中的$2^{2^{2^{2^{\cdots}}}} \text { mod } p$就很好求了，照着上面的式子递归就行。这里要注意应用条件：这里的指数$b=2^{2^{2^{2^{\cdots}}}}$是满足$b \geq \varphi(p)$的，于是可以直接用第一个式子。

  
附上代码。本蒟蒻不会线性筛，只好用Eratosthenes筛代替了= =


```cpp
#include <bits/stdc++.h>
using namespace std;
const int MAXP = 1e7;

int T, p, phi[MAXP+10];

void InitPhi() {
    phi[1] = 1; 
    for(int i=2; i<=MAXP; i++)
        if(!phi[i]) {
            for(int j=i; j<=MAXP; j+=i) {
                if(!phi[j]) phi[j] = j; 
                phi[j] = phi[j] / i * (i-1);
            }
        }
}

inline int fastmul(int a, int x, int mod) {
    int ret = 0;
    while(x) {
        if(x&1) ret = ((ret%mod) + (a%mod))%mod;
        x>>=1; a = ((a%mod) + (a%mod)) %mod;
    }
    return ret;
}

inline int fastpow(int a, int x, int mod) {
    int ret = 1;
    while(x) {
        if(x&1) ret = fastmul(ret, a, mod) % mod;
        x>>=1; a = fastmul(a, a, mod) % mod;
    }
    return ret;
}

int solve(int mod) {
    if(mod == 1) return 0;
    return fastpow(2, solve(phi[mod])+phi[mod], mod);
}

int main() {
    InitPhi();
    scanf("%d", &T);
    while(T--) {
        scanf("%d", &p);
        printf("%d\n", solve(p));
    }
}
```
