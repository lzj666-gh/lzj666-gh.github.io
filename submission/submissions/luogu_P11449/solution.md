# P11449 题解

### 前言：
MnZn 第一次打 USACO，降智降到用数位 dp 过了这个题。

喜提洛谷最劣解。

有一说一在理解数位 dp 的前提下还是非常好懂（doge）。
### 题意：
求在 $[2,n]$ 中 **逐位四舍五入** 和 **直接四舍五入** 不同的数的个数。
### 思路：
首先逐位四舍五入肯定不小于直接四舍五入。

容易发现，如果想要两者不同的话，只能是逐位四舍五入多进了一些位。

怎么样才能达到呢？只有一串 $4$ 后面跟上 $\ge 5$ 的数才行。

数位 dp 即可。判当前的有效位数并记录是否填过 $\ge 5$ 的数，按照一串 $4$ 后跟一个 $\ge 5$ 来填，后面的数随便填就可以了。

代码里有详细注释。

### 代码：
```cpp
#include<bits/stdc++.h>
using namespace std;
#define ll long long
const ll N=11;
ll T,n,dp[N][N][2];
vector<ll> p;
ll dfs(ll x,bool up,bool z,ll wei,bool wu){
    // x 表示位数（从大到小），up 表示当前是否取满（即当前位是能取到 9 还是只能取到 p[x]）
    // z 表示是否有前导零，wei 表示当前有效位的位数（即去除前导零），wu 表示是否存在 4...4 (>=5)
    if(!~x) return wu;
    if(!up&&!z&&~dp[x][wei][wu]) return dp[x][wei][wu];// 记忆化
    ll ct=0;// 答案
    if(!wei) ct+=dfs(x-1,0,1,0,0);// 前导零特判
    for(int i=0;i<=(up?p[x]:9);i++)
        if((!wei&&i==4)||(wei>=1&&!wu&&i>=4)||wu)
            ct+=dfs(x-1,up&&i==p[x],z&&(!i),wei+1,wu|(i>=5));
            // !wei&&i==4 ：第一位填 1
            // wei>=1&&!wu&&i>=4 ：一串 4 后面填 >=5 的数
            // wu ：前面已经满足条件了，这位可以随便填（只要在范围内）
            // up&&i==p[x] ：下一位是否取满
            // z&&(!i) ：下一位是否还都是前导零
            // wei+1 ：有效位 +1
            // wu|(i>=5)：是否存在 4...4 (>=5)
    if(!up&&!z) dp[x][wei][wu]=ct;// 记忆化
    return ct;
}
ll C(ll n){// 将 n 拆成一位一位
    p.clear();
    while(n) p.push_back(n%10),n/=10;// 十进制拆分
    return p.size()-1;
}
ll solve(ll n){memset(dp,-1,sizeof dp);return dfs(C(n),1,1,0,0);}
int main(){
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    cin>>T;while(T--) cin>>n,cout<<solve(n)<<"\n";
    return 0;
}
```