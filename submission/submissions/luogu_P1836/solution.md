# P1836 题解


### $\text{环顾整个题解区,都没有我写的简单}$ $QwQ$
[进我的博客浏览](https://www.luogu.org/blog/LZSY01-xzy-blog/solution-p1836)

我的想法是这样的：

$\text{分别考虑个位，十位，百位，千位，万位...}$

可以发现$sum($第$i$位$)$ $=10^i*(\sum_{i=1}^{9}*(n/10^i)+$ $\sum_{i=1}^{n\mod10^i/10^{i-1}-1})+(n\mod10^i/10^{i-1})*(n\mod10^i)+1$
### 故代码如下：
```cpp
#include <cstdio>
using namespace std;
long long n;
int sum[10]={0,1,3,6,10,15,21,28,36,45};

int get(int n)
{
	if(n<0)return 0;
	return n;
}

long long get_ans(long long n)
{
	long long res=0,a=1,b=0;	
	while(n>0)
	{
		res=res+a*(45*(n/10)+sum[get(n%10-1)])+(n%10)*(b+1);
		b=b+(n%10)*a;a*=10;
		n/=10;
	}
	return res;	
}

int main()
{
	scanf("%lld",&n);
	printf("%lld\n",get_ans(n));
	return 0;
}
```
我的代码里对$\sum_{i=1}^{k}$打了表

~~觉得不错的话点个赞欧~~