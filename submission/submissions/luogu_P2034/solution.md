# P2034 题解

[Youngsc](http://youngscc.github.io/)

既然是选择一些数让其和最大，也就是等价于我删除一些数且这些数的和最小。并且任意两个被删的数之间的距离一定小于k，即任意连续的k个数之中至少有一个数被删。

~~正难则反~~，我们定义$f[i]$ 为前i个数中被删除的数的最小和，那么$f[i]$就可以由从$i-k+1$到$i-1$中的任意一个$f[j]$转移过来，当然根据题意我们要将一个最小的$f[j]$转移给它，且$i-k+1<=j<i$。很显然我们可以用**单调队列**去维护这个东西。做到$O(n)$的复杂度去DP。

转移方程即为$f[i] = min(f[j])+num$用单调队列去维护。

最后的答案我们可以从$f[n-k]$到$f[n]$去找找最小值然后用所有值和减去就可以了。


## 代码在这里

```cpp
# include <algorithm>
# include <iostream>
# include <cstring>
# include <cstdio>
# include <queue>
# include <cmath>
# include <ctime>
# define R register
# define LL long long

using namespace std;

LL tot,d,n,k;
LL p[100010],head = 1,tail = 1;
LL q[100010],f[100010],ans;

inline void in(R LL &a){
    R char c = getchar();R LL x=0,f=1;
    while(!isdigit(c)){if(c == '-') f=-1; c  =getchar();}
    while(isdigit(c)) x = (x<<1)+(x<<3)+c-'0',c = getchar();
    a = x*f;
}

inline void maxx(R LL &a,const LL b){a>b? 0:a=b;}

inline LL yg(){
    // freopen("bronlily.in","r",stdin);
    // freopen("bronlily.out","w",stdout);
    in(n),in(k);
    for(R int i=1; i<=n; ++i)
    {
        in(d);
        tot += d;
        f[i] = q[head]+1LL*d;
        while(head<=tail&&q[tail]>=f[i]) tail--;
        q[++tail] = f[i],p[tail] = i;
        while(head<=tail&&p[head]<i-k) head++;
    }
    for(R int i=n-k; i<=n; ++i) maxx(ans,1LL*tot-1LL*f[i]);
    printf("%lld",ans);
    return 0;
}

LL youngsc = yg();
int main(){;}
```
（减少代码复制，共创美好洛谷）
