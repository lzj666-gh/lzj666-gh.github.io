# P9373 题解

- 出题人题解。

------------

第一档暴力枚举，第二档枚举因数，这里就不详细阐述了，下面讲正解。

考虑这样一个结论：


- 对于任意正整数 $x,y$，若 $x \leq y$，则有 $y \bmod x \leq \lfloor \frac{y-1}{2} \rfloor$。

证明的话分两种情况：

1. $x \leq \lfloor \frac{y}{2} \rfloor$，显然答案小于模数，结论成立。

2. $x > \lfloor \frac{y}{2} \rfloor$，不难发现 $y \bmod x \ = \ y-x$，结论也成立。

所以当给定的 $n,k$ 满足 $k > \lfloor \frac{n-1}{2} \rfloor$ 时无解，否则就一定有 $k \leq \lfloor \frac{n-1}{2} \rfloor$，此时输出 $k$ 和 $n-k$ 即可。

至此这道题解决完毕，时间复杂度 $O(T)$。下附代码：

```cpp
#include<bits/stdc++.h>
using namespace std;

int T;
long long n,k;
int main()
{
	scanf("%d",&T);
	while(T--)
	{
		scanf("%lld%lld",&n,&k);
		if(k<=(n-1)>>1)	printf("%lld %lld\n",k,n-k);
		else printf("-1\n");
	}
	return 0;	
} 
```


