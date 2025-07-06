# P1076 题解

这题嘛，说难，其实就是一个简单的优化模拟。注意：指示牌的数是让你找有门的第ai个。这题数据多，建议用scanf读入优化。当然，从它指示牌x的数据0<x≤10^6就可以看出来，纯模拟逆时针（我怎么看都像顺时针啊）一个一个模拟是不切实际的TLE。于是我们要深入寻找优化方法。再一看，一层楼有楼梯的门就那么几个，找来找去都是它们，这让我想到了周期问题。周期问题取模是关键，我就wrong在这个点上QAQ。原来我用找门次数直接mod该层楼梯门的个数，假设一下，若ai为该层楼梯门个数，就会出现0的情况，而你现在的门又没楼梯，为了保留其原汁原味，可在模之前-1，模之后+1，这样还避免了该层门个数为一的情况。
不说了，上代码！
```cpp
#include<iostream>
#include<fstream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<string>
using namespace std;
int pd[10002][202],a[10002][202];
int main()
{
	//freopen("treasure.in","r",stdin);
	//freopen("treasure.out","w",stdout);
	int n,m,x,i,j,ans=0,l=0;
	scanf("%d%d",&n,&m);//以下的读入不说了
	for(i=1;i<=n;i++)
	{
		l=0;
		for(j=0;j<m;j++)
		{
			scanf("%d%d",&pd[i][j],&a[i][j]);
			if(pd[i][j]==1) l++;//记录该层楼有楼梯的门数
		}
		pd[i][m]=l;
	}
	scanf("%d",&x);
	i=1;
	while(i<=n)
	{
	    ans+=a[i][x];
		ans%=20123;//根据规律，边加边模，值不变，不用long long
	    int k=0;
		for(j=x;;j++)
		{
			if(j==m) j=0;
			if(pd[i][j]==1) k++;
			if(k==(a[i][x]-1)%pd[i][m]+1) break;//最关键的停止条件，循环找对，取模，都靠它。
		}
	    x=j;
		i++;
	}
	printf("%d",ans);//小小的输出优化~
	return 0;
}
```
谢谢大家！！！