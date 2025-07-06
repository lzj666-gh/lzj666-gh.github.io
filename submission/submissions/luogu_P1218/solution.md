# P1218 题解

## 重要的事情说三遍

# 此解绝对不是正解！
# 此解绝对不是正解！！
# **此解绝对不是正解！！！**

好了，其实这道题暴力就可以过。
怎么个暴力法。。。。 
# 八重循环！！！

我们开一个$N$重循环，检测一共的$N-1$个数是不是素数，如果是，则输出

然而，这种做法肯定会超时。所以我们需要优化

* 优化一，我们可以肯定，第一位肯定是2,3,5,7。不然它不可能是素数

  我们可以开一个数组$A[4]$，分别存储$2,3,5,7$。

* 优化二，第$2$位到第$ N-1$位中，每一位都必须是奇数，不然也满足不了素数的调节
  我们开一个数组$b[5]$，分别存储$1,3,5,7,9$。

## 以下高能！
## 以下高能！！
## 以下高能！！！
```cpp
#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
#include<queue>
#include<cmath>
#include<set>
#include<list>
#include<stack>
#include<vector>
#include<cstdlib>
#include<iterator>
#include<deque>
#include<ctime>
#include<iomanip>
#include<map>
#include<bitset>
#include<utility>
#include<sstream>
using namespace std;
bool prime(int n)
{
    if(n==1)return false;
    for(int i=2;i*i<=n;i++)
    {
    	if(n%i==0)return false;
    }
    return true;
}
inline void write(int x)
{
     if(x<0) putchar('-'),x=-x;
     if(x>9) write(x/10);
     putchar(x%10+'0');
    
}
int a[5]={0,2,3,5,7};
int b[6]={0,1,3,5,7,9};
int main()
{
	int n,i,j,k,q,w,e,r,t;
	scanf("%d",&n);
	if(n==1)
		for(i=1;i<=4;i++)
			if(prime(a[i]))
				{write(a[i]);putchar('\n');}
	if(n==2)
		for(i=1;i<=4;i++)
			for(j=1;j<=5;j++)
				if(prime(a[i]*10+b[j]))
					{write(a[i]*10+b[j]);putchar('\n');}
	if(n==3)
		for(i=1;i<=4;i++)
			for(j=1;j<=5;j++)
				for(k=1;k<=5;k++)
					if(prime(a[i]*100+b[j]*10+b[k])&&prime(a[i]*10+b[j])&&prime(a[i]))
						{write(a[i]*100+b[j]*10+b[k]);putchar('\n');}
	if(n==4)
		for(i=1;i<=4;i++)
				for(j=1;j<=5;j++)
					for(k=1;k<=5;k++)
						for(q=1;q<=5;q++)
							if(prime(a[i]*1000+b[j]*100+b[k]*10+b[q])&&prime(a[i]*100+b[j]*10+b[k])&&prime(a[i]*10+b[j])&&prime(a[i]))
								{write(a[i]*1000+b[j]*100+b[k]*10+b[q]);putchar('\n');}
	if(n==5)
		for(i=1;i<=4;i++)
			for(j=1;j<=5;j++)
				for(k=1;k<=5;k++)
					for(q=1;q<=5;q++)
						for(w=1;w<=5;w++)
							if(prime(a[i]*10000+b[j]*1000+b[k]*100+b[q]*10+b[w])&&prime(a[i]*1000+b[j]*100+b[k]*10+b[q])&&prime(a[i]*100+b[j]*10+b[k])&&prime(a[i]*10+b[j])&&prime(a[i]))
								{write(a[i]*10000+b[j]*1000+b[k]*100+b[q]*10+b[w]);putchar('\n');}
	if(n==6)
		for(i=1;i<=4;i++)
			for(j=1;j<=5;j++)
				for(k=1;k<=5;k++)
					for(q=1;q<=5;q++)
						for(w=1;w<=5;w++)
							for(e=1;e<=5;e++)
								if(prime(a[i]*100000+b[j]*10000+b[k]*1000+b[q]*100+b[w]*10+b[e])&&prime(a[i]*10000+b[j]*1000+b[k]*100+b[q]*10+b[w])&&prime(a[i]*1000+b[j]*100+b[k]*10+b[q])&&prime(a[i]*100+b[j]*10+b[k])&&prime(a[i]*10+b[j])&&prime(a[i]))
									{write(a[i]*100000+b[j]*10000+b[k]*1000+b[q]*100+b[w]*10+b[e]);putchar('\n');}
	if(n==7)
		for(i=1;i<=4;i++)
			for(j=1;j<=5;j++)
				for(k=1;k<=5;k++)
					for(q=1;q<=5;q++)
						for(w=1;w<=5;w++)
							for(e=1;e<=5;e++)
								for(r=1;r<=5;r++)
									if(prime(a[i]*1000000+b[j]*100000+b[k]*10000+b[q]*1000+b[w]*100+b[e]*10+b[r])&&prime(a[i]*100000+b[j]*10000+b[k]*1000+b[q]*100+b[w]*10+b[e])&&prime(a[i]*10000+b[j]*1000+b[k]*100+b[q]*10+b[w])&&prime(a[i]*1000+b[j]*100+b[k]*10+b[q])&&prime(a[i]*100+b[j]*10+b[k])&&prime(a[i]*10+b[j])&&prime(a[i]))
										{write(a[i]*1000000+b[j]*100000+b[k]*10000+b[q]*1000+b[w]*100+b[e]*10+b[r]);putchar('\n');}
	if(n==8)
		for(i=1;i<=4;i++)
			for(j=1;j<=5;j++)
				for(k=1;k<=5;k++)
					for(q=1;q<=5;q++)
						for(w=1;w<=5;w++)
							for(e=1;e<=5;e++)
								for(r=1;r<=5;r++)
									for(t=1;t<=5;t++)
										if(prime(a[i]*10000000+b[j]*1000000+b[k]*100000+b[q]*10000+b[w]*1000+b[e]*100+b[r]*10+b[t])&&prime(a[i]*1000000+b[j]*100000+b[k]*10000+b[q]*1000+b[w]*100+b[e]*10+b[r])&&prime(a[i]*100000+b[j]*10000+b[k]*1000+b[q]*100+b[w]*10+b[e])&&prime(a[i]*10000+b[j]*1000+b[k]*100+b[q]*10+b[w])&&prime(a[i]*1000+b[j]*100+b[k]*10+b[q])&&prime(a[i]*100+b[j]*10+b[k])&&prime(a[i]*10+b[j])&&prime(a[i]))
											{write(a[i]*10000000+b[j]*1000000+b[k]*100000+b[q]*10000+b[w]*1000+b[e]*100+b[r]*10+b[t]);putchar('\n');}
	return 0;
}


```
