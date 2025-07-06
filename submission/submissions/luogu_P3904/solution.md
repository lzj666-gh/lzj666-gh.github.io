# P3904 题解

最优解第四来水一发（~~虽然开了o2~~）

(~~不点赞也无所谓，~~只要不照抄)

我们考虑将第n只小猪塞进m个房子里（记做f[n][m]）：

显然答案分为两部分：

第一部分：

将这只猪扔到一个新房间，共有方案数：f[n-1][m-1]

第二部分：

将这只猪扔进之前的房间,乘法原理知共有方案数:m*f[n-1][m]

综上：有状态转移方程：f[n][m]=f[n-1][m-1]+m*f[n-1][m]

特别的：f[1][1]=1

这种数就是将n个不同的元素拆分成m个集合的方案数，又称：第二类斯特林数。

同时由于数据范围较大，考虑使用高精加和高精乘。

那么我们令f[i][j][0],表示f[i][j]的位数，之后为f[i][j]每一位。

```cpp
#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include<algorithm>
using namespace std;
int f[60][60][60];
int _ans[60],_size;
int n,m;
void _change(int x,int y)
{
	if(y>x)return;
	if(x==1&&y==1)return;
	for(int i=1;i<=_size;i++)
	_ans[i]=0;
	_size=1;
	int _x=0;
	for(int i=1;i<=f[x-1][y][0];i++)
	{
		_ans[i]=f[x-1][y][i]*y+_x;
		_x=_ans[i]/10;
		_ans[i]%=10;
	}
	_size=f[x-1][y][0];
	if(_x!=0)
	_ans[++_size]=_x;
	f[x][y][0]=1;
    _x=0;
    while(f[x][y][0]<=f[x-1][y-1][0]||f[x][y][0]<=_size)
    {
        f[x][y][f[x][y][0]]=f[x-1][y-1][f[x][y][0]]+_ans[f[x][y][0]]+_x;
        _x=f[x][y][f[x][y][0]]/10;
        f[x][y][f[x][y][0]]%=10;
        f[x][y][0]++;
    }
    f[x][y][f[x][y][0]]=_x;
    if(f[x][y][f[x][y][0]]==0&&f[x][y][0]!=1)
    f[x][y][0]--;
}
int main()
{
	scanf("%d%d",&n,&m);
	if(m>n)
	{
		cout<<0;
		return 0;
	}
	f[1][1][0]=1;
    f[1][1][1]=1;
	for(int i=2;i<=n;i++)
	for(int j=1;j<=min(i,m);j++)
	_change(i,j);
	if(f[n][m][0]==1&&f[n][m][1]==0)
	{
		cout<<0;
		return 0;
	}
	for(int i=f[n][m][0];i>=1;i--)
	printf("%d",f[n][m][i]);
}
```