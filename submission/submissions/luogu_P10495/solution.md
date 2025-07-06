# P10495 题解

[题目传送门](https://www.luogu.com.cn/problem/P10495)

这道题目其实很好理解。

举个例子：求 $10$ 的阶乘中有几个 $2$ 和几个 $3$。

首先看 $2$ 的个数，$2$，$4$，$6$，$8$，$10$ 各有一个 $2$，而 $4$ 和 $8$ 中还各有一个 $2$，最后 $8$ 还有一个 $2$。也就是说，$2$ 有 $10 \div 2^1+10 \div 2^2+10 \div 2^3$ 个。

$3$ 同理。$3$，$6$，$9$ 各有一个 $3$，$9$ 还有一个 $3$，所以 $3$ 有 $10 \div 3^1+10 \div 3^2$ 个。

所以思路就很清楚了：先求质数，再按上面的方法求个数。

代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
int s,cnt,st[1000005],pr[1000005];
int p(int n)//线性筛,此处不具体分析 
{
    for(int i=2;i<=n;i++)
    {
        if(!st[i])
		{
		    pr[cnt++]=i;//是质数 
		}
        for(int j=0;pr[j]<=n/i;j++)
        {
            st[pr[j]*i]=true;//不是质数 
            if(i%pr[j]==0)break;
        }
    }
    return cnt;
}
int main()
{
	int n;
	scanf("%d",&n);
	p(n);
	for(int i=0;i<cnt;i++)
	{
		s=0;
		for(int j=1;pow(pr[i],j)<=n;j++)//确保i的j次方不超过n 
		{
			s+=n/pow(pr[i],j);
		}
		printf("%d %d\n",pr[i],s);
	}
	return 0;
}
```