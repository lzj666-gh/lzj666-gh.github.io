# CF1881C 题解

## 题意：
给定一个 $n\times n$ 大小的矩阵，每次操作可以将一个字母变成字母表序中下一个字母。求最小操作次数使矩阵旋转 $90^\circ$ 仍保持不变。

注意：本题有多组数据。
## 思路：
要将点 $(i,j)$ 任意旋转 $90^\circ$ 的字母都保持不变，则要找到点 $(i,j)$ 的三个对应点：$(j,n-i+1)$、$(n-j+1,i)$、$(n-i+1,n-j+1)$。既然要将这四个点变为相同的点，则变成的字母一定是这四个点中字母表序最大的一个字符，其操作次数即为 $\max\{a_{i,j},a_{j,n-i+1},a_{n-j+1,i},a_{n-i+1,n-j+1}\}\times4-a_{i,j}-a_{j,n-i+1}-a_{n-j+1,i}-a_{n-i+1,n-j+1}$，其中 $a_{i,j}$ 表示从字符 `a` 变成第 $i$ 行第 $j$ 列的字符的操作次数。

设 $cnt_{i,j}$ 表示点 $i,j$ 的操作次数，则最后答案即为：
$$\sum\limits_{i=1}^{n/2}\sum\limits_{j=1}^{n/2}cnt_{i,j}$$
## 代码：
```cpp
#include<bits/stdc++.h>
using namespace std;
const int N=1e3+5;
int t,n,a[N][N],ans;
char c;
int main(){
	for(cin>>t;t;ans=0,t--){
		cin>>n;
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)cin>>c,a[i][j]=c-'a';
		for(int i=1;i<=n/2;i++)
			for(int j=1;j<=n/2;j++){
				int maxi=max({a[i][j],a[n-j+1][i],a[j][n-i+1],a[n-i+1][n-j+1]});
				int cnt=a[i][j]+a[n-j+1][i]+a[j][n-i+1]+a[n-i+1][n-j+1];
				ans+=maxi*4-cnt;//累加每个点的操作次数 
			}
		cout<<ans<<"\n";//多测换行不要用 endl，"\n" 快得多 
	}
	return 0;
}
```