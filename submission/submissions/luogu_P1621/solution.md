# P1621 题解

大家都是先筛素数再合并？其实用埃氏筛法的话筛的同时就可以合并了，因为每个数都被它的所有质因数各筛了一遍，直接在用每个质因数筛的时候把被筛掉的数合并就好了。

```
#include <iostream>

using namespace std;

int find(int x);

int f[100010],a,b,p,ans;
bool np[100010];

int main()
{
	int i,j;
	
	cin>>a>>b>>p;
	
	ans=b-a+1; //将答案初始化为a~b间数的个数，每合并一次减1就可以了
	
	for (i=a;i<=b;++i)
	{
		f[i]=i;
	}
	
	for (i=2;i<=b;++i) //埃氏筛
	{
		if (!np[i])
		{
			if (i>=p) //如果当前质数大于p才合并
			{
				for (j=i*2;j<=b;j+=i)
				{
					np[j]=true;
					if (j-i>=a&&find(j)!=find(j-i)) //将当前被筛的数与上一个被筛的数合并（第一个被筛的数和质因数本身合并），注意这两个数都要在a~b之间才合并
					{
						f[find(j)]=find(j-i);
						--ans;
					}
				}
			}
			else
			{
				for (j=i*2;j<=b;j+=i)
				{
					np[j]=true;
				}
			}
		}
	}
	
	cout<<ans;
	
	return 0;
} 

int find(int x)
{
	return x==f[x]?x:f[x]=find(f[x]);
}
```