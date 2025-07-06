# P7199 题解

一些 wyy 的基础骗分的算法就不讲了，这里就简单的说说一个普通的算法：

solution：

对于 $100\%$ 的数据，如果我们使用 $\mathcal{O}(Q\times(r-l+1))$ 的算法会 TLE ，现在给出一种算法：

对于一个数 $\overline{abcd}$ 来说，我们可以令该算法为 $g(x)$ ，其实就是不断的相加：$a+b+c+d \cdots$ 加到一个 **个位数** 为止。（最后发现 $g(\overline{abcd})$ 的所有数字之和为 $g(x)\in[1,9]$）。

因此我们只需要知道：$\sum\limits_{i=1}^9 i=45$ ，因此只需要找出 $\div 9$ （取整）的数量加上额外的数量即可。

注意因为本题数据范围 $>2^{60}$ ，因此需要使用 $\texttt{long long}$。

代码如下：

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
	int n;
	cin>>n;
	while(n--) {
		long long l, r;
		cin>>l>>r;
		long long times=(r-l+1)/9;//周期统计的个数
		long long sum=times*45; 
		for(long long i=l+times*9;i<=r;i++)//计算从l之后的不完整周期的选择，注意在这里的数据是有规律可循的，因此 /9 即可
			sum+=(i-1)%9+1;	
		cout<<sum<<endl;
	}
	return 0;
}
```

复杂度为 $\mathcal{O}(q \times \dfrac{r-l-\text{次数}}{9})$