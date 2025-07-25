# P1450 题解

好巧妙的一道dp题！

如果我们就赤裸裸的多重背包那么就是O(10^5\*10^5\*1000)

一周的时间都运行不完（手动滑稽）！

那么怎么办呢？如果没有硬币数量的限制那就多好啊？直接一个完全背包预处理，然后O(1)输出就好了

可是有了硬币的限制怎么办？我们先考虑一个简单一点的情况：只有第一个硬币有限制。

如果我们用类似前缀和的思想（术语叫差分），我们先完全背包预处理好无限制的情况，拿dp[tot]减去dp[tot-c[i]\*(d[i]+1)]就是我们所需的方案数。

这是为什么呢？为什么要弄个c[i]\*(d[i]+1)？其实我们可以这样想，无限制的情况就是没有那个di，而有限制时，不应该计入答案的方案数就是把c[i]这个硬币取了超过d[i]次，对吧？那么我们手动先取出d[i]+1个c[i]的硬币，然后剩下的价值弄个完全背包，这时就是我们所不需要的答案， 把它减掉就行了。

那么对于4个（或更多）的硬币有限制，我们就逐一把4个硬币单独限制的方案数减掉，这时可能会减重了（即同时两个硬币有限制的情况减了两次），所以我们再把4个硬币两两同时限制的方案数加上，可能又加重了，再把4个硬币33同时限制减掉，最后加上4个同时限制的方案数就是我们所需的答案。这就是大名鼎鼎的容斥原理啊！写成位运算就很优美了！

方案数会爆int哟。

参考代码（和楼下不太一样，0表示满足限制，1表示不满足限制）：

```cpp
#include<cstdio>
#include<algorithm>
#include<cstring>
#define REP(i,a,b) for (int i=(a);i<=(b);i++)
#define in(a) scanf("%d",&(a))
using namespace std;
const int N=100001;
long long dp[N+10];
int c[5],d[5];
int main(){
    REP(i,1,4)in(c[i]);
    dp[0]=1;
    REP(i,1,4)REP(j,c[i],N)dp[j]+=dp[j-c[i]];
    int T;in(T);
    while (T--){
        int sum;long long res=0;
        REP(i,1,4)in(d[i]);
        in(sum);
        REP(i,0,15){
            long long t=sum;
            int cnt=0;
            REP(j,1,4)if ((i>>(j-1))&1)t-=c[j]*(d[j]+1),cnt^=1;
            if (t<0)continue;
            if (!cnt)res+=dp[t];else res-=dp[t];
        }
        printf("%lld\n",res);
    }
    return 0;
}
```