# P1191 题解

# 本蒟蒻只会$n^3$

唉，还是太弱了，靠刷点水题过日子


------------
# 思路：

我们枚举出矩形左下角的点，坐标为$(i,j)$，并且枚举这个点向右的长度$k$，那么以$(i,j)$为左下角，宽度为$k-j+1$的矩形自然就是能向上扩展的高度最小值了，光说可能不太清楚，下面模拟一下（有图哦$qwq$）

我们以下面为例子，粗略讲一下（不会全部模拟）

样例：

$4$

$WWWW$

$WWBW$

$WWWW$

$WWWW$

那么假设我们枚举$i,j$分别为$4,1$，也就是第四行第一列，那么我们向右枚举$k$

当$k=1$时，我们求出以$i,j$为左下角，宽度为$k-j+1$也就是$1$的矩形有多少个，我们可以看到有$4$个，分别是:

![](https://i.loli.net/2019/02/12/5c62baaac721d.png)
![](https://i.loli.net/2019/02/12/5c62baee7c52f.png)
![](https://i.loli.net/2019/02/12/5c62bb6bbdcf1.png)
![](https://i.loli.net/2019/02/12/5c62bba2a8f1e.png)

我们其实可以发现就是能向上扩展的高度个矩形

当$k=2$时,我们发现以$i,j$为左下角，宽度为$2$的矩形也有$4$个，分别为：

![](https://i.loli.net/2019/02/12/5c62bc64a2f0b.png)
![](https://i.loli.net/2019/02/12/5c62bc88ce1fb.png)
![](https://i.loli.net/2019/02/12/5c62bca0b5c98.png)
![](https://i.loli.net/2019/02/12/5c62bcbbbd140.png)

当$k=3$时，我们发现以$i,j$为左下角，宽度为$3$的矩形有$2$个，分别为：

![](https://i.loli.net/2019/02/12/5c62bd1f2eb35.png)
![](https://i.loli.net/2019/02/12/5c62bd37ac4c3.png)

当$k=4$时，我们发现以$i,j$为左下角，宽度为$4$的矩形有$2$个，分别为：

![](https://i.loli.net/2019/02/12/5c62bd9e0c7ac.png)
![](https://i.loli.net/2019/02/12/5c62bdbb22180.png)

那么到这里我们就枚举出了左下角为$4,1$的所有矩形

而且我们可以发现，矩形个数就是能向上扩展的高度

那么我们会枚举$i,j$，让每一个点作为矩形左下角，同时枚举宽度，一层一层下来，最后就是不遗漏的所有矩形个数，具体证明就省略了，自己想想就知道了

时间复杂度$O(n^3)$

下面是美滋滋的代码时间~~~

~~~cpp
#include<iostream>
#include<cstdio>
#include<cstring>
#define N 157
using namespace std;
int n,now,ans;
int high[N];
int main()
{
	scanf("%d",&n);
	for(int i=1;i<=n;++i)
	{
		for(int j=1;j<=n;++j)
		{
			char in;
			scanf(" %c",&in);
			if(in=='W')
				++high[j];
			else
				high[j]=0;
		}
		for(int j=1;j<=n;++j)
		{
			now=high[j];
			for(int k=j;k<=n;++k)
			{
				if(!high[k])
					break;
				now=min(now,high[k]);
				ans+=now;
			}
		}
	}
	printf("%d",ans);
	return 0;
}
~~~