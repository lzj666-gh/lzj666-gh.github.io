# P7381 题解

一道动规题，我第一次一遍过绿题。

## 思路

我们定义一个数组 $\mathit{dp}_{i,j}$，表示在第 $i$ 支球队已经用了 $j$ 张照片，它分数的一个最大值。

那么 $i$ 就从 $1\backsim n$，$j$ 要从 $0\backsim K$，因为前 $i$ 支球队可以都不用送的照片，所以有 $0$。

那么状态转移方程是什么呢？$\mathit{dp}_{i,j}=\operatorname{max}(\mathit{dp}_{i,j},\mathit{dp}_{i-1,p_{i}+j-k})$

那么为什么呢？$k$ 表示第 $i-1$ 支球队可能已经用了多少张照片，而 $j$ 表示前 $i$ 支球队会用多少张照片。

由于我们已经加过这个 $k$ 了，而这个 $k$ 包含在 $j$ 里，所以要减去 $k$。

说了这么多，上代码！

## 代码

```cpp
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
int n,m,k,p[505],b[505],dp[505][505];
int main(){
	cin>>n>>m>>k;
	for(int i=1;i<=n;i++)
		cin>>p[i];
	for(int i=0;i<=m;i++)
		cin>>b[i];
	for(int i=1;i<=n;i++){
		for(int j=0;j<=k;j++){
			for(int kk=0;kk<=j;kk++){
				dp[i][j]=max(dp[i-1][kk]+b[p[i]+j-kk],dp[i][j]);
			}
		}
	}
	cout<<dp[n][k];//毋庸置疑，dp[n][k]肯定是最优方案 
	return 0;
}
```
