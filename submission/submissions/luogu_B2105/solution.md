# B2105 题解

## 题目分析
此题的新矩阵只需按题目中所说，再加一重循环来把新矩阵的点当作计数器计算，注意矩阵的换行。
## 代码实现
```cpp
#include<bits/stdc++.h>
using namespace std;
int a[110][110],b[110][110],c[110][110],m,n,k;
double s;
int main()
{
	cin>>n>>m>>k;
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)
			cin>>a[i][j];
	for(int i=1;i<=m;i++)
		for(int j=1;j<=k;j++)
			cin>>b[i][j];
	for(int i=1;i<=n;i++)
		for(int j=1;j<=k;j++)
			for(int l=1;l<=m;l++)
				c[i][j]+=a[i][l]*b[l][j];//将新矩阵的每一个点都看作计数器来计算
	for(int i=1;i<=n;i++){
		for(int j=1;j<=k;j++)
			cout<<c[i][j]<<" ";
		cout<<endl;//注意换行
	}
	return 0;
}
```
