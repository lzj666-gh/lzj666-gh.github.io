# P5664 题解

#### 给管理员的更新说明：这是一篇广受好评的题解，我近日对选手们提到的代码问题作了修订，并不是故意提出重复解法的题解，希望在重新提交审核的过程中可以通过，为更多的选手带来好的帮助，非常感谢！

又来水题解了~

这个题作为d2t1比往年偏难，但完全在可以接受和预见的范围。

首先考虑列的限制，发现若有不合法的列，则必然有且只有一列是不合法的：因为不可能有不同的两列数量都超过总数的一半。

于是发现列的限制容易容斥计算：每行选不超过一个的方案数 - 每行选不超过一个，且某一列选了超过一半的方案数。

那么考虑枚举不合法的一列。假设我们已经枚举了不合法的列为$col$，接下来会发现我们只关心一个数的位置是否在当前列；如果属于在其他列的情况，那么它具体在哪一列对当前列的合法性并无影响，我们并不需要考虑。

接下来设计状态。$f_{i,j,k}$表示对于$col$这一列，前$i$行在$col$列中选了$j$个，在其他列中选了$k$个，那么令$s_i$为第$i$行的总和，则有转移：
$$f_{i,j,k} = f_{i-1,j,k}\ +\ a_{i,col}* f_{i-1,j-1,k}\ +\ (s_i-a_{i,col})* f_{i-1,j,k-1}$$
状态数$O(n^3)$，转移$O(1)$，算上枚举$col$，这一步复杂度是$O(mn^3)$的。统计如下和式的值并对每一列求和即可得到不合法的方案数：
$$\sum_{j>k} f_{n,j,k}$$

接下来考虑计算总方案数：和之前相似，只需设$g_{i,j}$为前$i$行共选了$j$个数的方案数，则有转移：
$$g_{i,j} = g_{i-1,j}\ +\ s_i*g_{i-1,j-1}$$

那么$\sum\limits_{i=1}^n g_{n,i}$就是总方案数，
这一步是$O(n^2)$的。所以现在可以在$O(mn^3)$的总复杂度内完成这题，获得84分。

考虑进一步优化，剪去无用状态：注意到在不合法情况的计算过程中，也就是$f_{i,j,k}$的转移过程中，我们实际上并不关心$j,k$的具体数值，而只关心相对的大小关系；所以我们可以将状态变为$f_{i,j}$，表示前$i$行，当前列的数比其他列的数多了$j$个，则有转移：
$$f_{i,j} = f_{i-1,j}\ +\ a_{i,col}* f_{i-1,j-1}\ +\ (s_i-a_{i,col})* f_{i-1,j+1}$$

转移仍然是$O(1)$的，但总复杂度降为$O(mn^2)$，可以通过此题。

（考试的时候我好像数组开小了？？？）

（沦为和暴力老哥同分）

代码：

```cpp
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#define mod 998244353

using namespace std;
typedef long long ll;
const int MAXN = 105, MAXM = 2005;
int n,m,a[MAXN][MAXM],sum[MAXN][MAXM];
ll f[MAXN][MAXN*2],g[MAXN][MAXN];

int main()
{
	cin >> n >> m;
	for(int i = 1; i<=n; i++)
	    for(int j = 1; j<=m; j++)
	    {
	        scanf("%d",&a[i][j]);
	        sum[i][0] = (sum[i][0]+a[i][j])%mod;
		}
    for(int i = 1; i<=n; i++)
        for(int j = 1; j<=m; j++)
            sum[i][j] = (sum[i][0]-a[i][j]+mod)%mod;
    ll ans = 0;
    for(int col = 1; col<=m; col++)
    {
        memset(f,0,sizeof(f));
        f[0][n] = 1;
        for(int i = 1; i<=n; i++)
            for(int j = n-i; j<=n+i; j++) 
                f[i][j] = (f[i-1][j]+f[i-1][j-1]*a[i][col]%mod+f[i-1][j+1]*sum[i][col]%mod)%mod;
        for(int j = 1; j<=n; j++)
            ans = (ans+f[n][n+j])%mod;
	}
	g[0][0] = 1;
	for(int i = 1; i<=n; i++)
	    for(int j = 0; j<=n; j++) 
		    g[i][j] = (g[i-1][j]+(j>0?g[i-1][j-1]*sum[i][0]%mod:0))%mod;
    for(int j = 1; j<=n; j++)
	    ans = (ans-g[n][j]+mod)%mod;  
	cout << ans*(mod-1)%mod << endl;
	return 0;
}
```
