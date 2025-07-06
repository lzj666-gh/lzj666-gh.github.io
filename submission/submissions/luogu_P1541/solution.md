# P1541 题解


[P1541 乌龟棋](https://www.luogu.org/problemnew/show/P1541)

这个题可以说运用了背包的思想:

开的主要变量：

1.F[a][b][c][d]:表示你出了a张爬行牌1，b张爬行牌2，c张爬行牌3，d张爬行牌4时的得分

2.g[x]:表示牌x一共有多少张

题干中说如何出牌,那我们就不妨DP一下每一种牌的出牌张数

初始化：

```
F[0][0][0][0]=num[1];
```

显然,乌龟开始时在num[1],题中说乌龟棋子自动获得起点格子的分数,故未出牌时（F[0][0][0][0]）分数为num[1]

之后边输入边存每一种牌的张数（输入数据第3行:M个整数，b1b2……bM，表示M张爬行卡片上的数字,故卡1~卡4张数一定）:

```cpp
for(int i=1;i<=m;i++)
{
	cin>>x;
	g[x]++;
}
```

之后便可以开始DP了:

起始状态F[0][0][0][0]=num[1]，即不出任何爬行卡;之后对于每一张卡片，我都可以选择放与不放，
E:设当前放的卡1数量为a，卡2数量为b，卡3数量为c，卡4数量为d（以下出现a~d均为这个意思），则对于卡一:

比较卡一的放与不放,只需决策卡一的放与不放，即取F[a][b][c][d],F[a-1][b][c][d]+num[r]的最大值。又由于a有一定数量,所以我们可以得出关于a的转移方程:

```cpp
	F[a][b][c][d]=max(F[a][b][c][d],F[a-1][b][c][d]+num[r])
```
其中r=1+a+b*2+c*3+d*4(至于r在a+b*2+c*3+d*4加一原因见后)

DP 数量a：

```cpp
for(int a=0;a<=g[1];a++)
{
	int r=1+a+b*2+c*3+d*4;
	if(a!=0)	F[a][b][c][d]=max(F[a][b][c][d],F[a-1][b][c][d]+num[a+b*2+c*3+d*4])
}
```
这不就是个“物品占的空间”为1，“价值”为num[r]的多重背包嘛！！
 
 至于这个(a!=0)，显然，你要是调用F[a-1][b][c][d]，肯定得保证a-1>=0吧。a显然作为卡1个数不可能<0,故取(a!=0)即可
    
根据多维背包的思想，背包DP几个“价值”（即爬行牌种类）开几维即可,故
转移方程为:
```cpp
		F[a][b][c][d]=max(F[a-1][b][c][d],F[a][b-1][c][d],F[a][b][c-1][d],F[a][b][c][d-1])+num[1*a+2*b+3*c+4*d]
```

最后DP出来的F[g[1]][g[2]][g[3]][g[4]]即为答案。


DP代码如下：
```cpp
	for(int a=0;a<=g[1];a++)
		for(int b=0;b<=g[2];b++)
			for(int c=0;c<=g[3];c++)
				for(int d=0;d<=g[4];d++)
				{
					int r=1+a+b*2+c*3+d*4;//千万千万别忘了加一,因为乌龟从num[1]出发,设前进i步，则到达num[i+1],我就是因为这调了一个小时死活没找出毛病 
					if(a!=0)	F[a][b][c][d]=max(F[a][b][c][d],F[a-1][b][c][d]+num[r]); //a!=0原因见上
					if(b!=0)    F[a][b][c][d]=max(F[a][b][c][d],F[a][b-1][c][d]+num[r]);
					if(c!=0)    F[a][b][c][d]=max(F[a][b][c][d],F[a][b][c-1][d]+num[r]);
					if(d!=0)	F[a][b][c][d]=max(F[a][b][c][d],F[a][b][c][d-1]+num[r]);
				}	
```

在for循环中将F[a][b][c][d]与F[a-1][b][c][d]+num[1*a+2*b+3*c+4*d],F[a][b-1][c][d]+num[1*a+2*b+3*c+4*d],F[a][b][c-1][d]+num[1*a+2*b+3*c+4*d],F[a][b][c][d-1]+num[1*a+2*b+3*c+4*d]逐个比较，实现了转移方程的更新(c++中max函数貌似只能比较两个数)

当然，我们知道总牌数n和每种卡的张数，则实际写代码时我们完全可以考虑减一维,可我至今还是没想起来。。。。。。（我还是个蒟蒻）

AC代码:

```
#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
const int MAXN=41;
int F[MAXN][MAXN][MAXN][MAXN],num[351],g[5],n,m,x;
int main()
{
    ios::sync_with_stdio(false);
    cin>>n>>m;
    for(int i=1;i<=n;i++)
        cin>>num[i];
    F[0][0][0][0]=num[1];
    for(int i=1;i<=m;i++)
    {
        cin>>x;
        g[x]++;
    }
    for(int a=0;a<=g[1];a++)
        for(int b=0;b<=g[2];b++)
            for(int c=0;c<=g[3];c++)
                for(int d=0;d<=g[4];d++)
                {
                    int r=1+a+b*2+c*3+d*4;
                    if(a!=0)	F[a][b][c][d]=max(F[a][b][c][d],F[a-1][b][c][d]+num[r]);
                    if(b!=0)    F[a][b][c][d]=max(F[a][b][c][d],F[a][b-1][c][d]+num[r]);
                    if(c!=0)    F[a][b][c][d]=max(F[a][b][c][d],F[a][b][c-1][d]+num[r]);
                    if(d!=0)	F[a][b][c][d]=max(F[a][b][c][d],F[a][b][c][d-1]+num[r]);
                }	
    cout<<F[g[1]][g[2]][g[3]][g[4]];
    return 0;
}
```


