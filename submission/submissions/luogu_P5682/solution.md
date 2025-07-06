# P5682 题解

其实这题还是有很多要考虑的点的 稍微说一说解题过程  

首先它要求严格次大值 所以有两个相同的数没有意义...先排序+去重  
假设原序列去重后剩下的序列为$a_1,a_2,...,a_n$

由于 $a\ mod\ b < a$ 所以最大值一定是$a_{n-1}\ mod\ a_n$  
简单证明:  
- 1.对于$a_1$到$a_{n-2}$ 使其**取模比它们大的数** 就是本身 一定比$a_{n-1}$小  
- 2.如果一个数**模比它小的数** 被模的数不可能是$a_n$ 那么最后值一定小于$a_{n-1}$  

然后我们可以想到 很明显$a_{n-2}\ mod\ a_n$是所有**一个数模比它大的数**中次大值$x$  
我们还要找出**一个数模比它小的数**中次大值 和刚才的值$x$比较  
看起来得枚举了 其实不必  
假设这个选择是$a_j\ mod\ a_i$ 那么如果$i\leq n-2$ 这个值一定小于$x$  
于是$i\geq n-1$ 只剩下一种取法:$j=n,i=n-1$  

这两个比较 取较大的 必定就是次大值  
代码也很简短  

```cpp
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
typedef long long LL;

int n;
int a[300005];

int main(){
	cin >> n;
	for(int i = 1;i <= n;i ++) cin >> a[i];
	sort(a + 1,a + 1 + n); n = unique(a + 1,a + 1 + n) - a - 1;
	// 排序+去重
   a[0] = 0;
	if(n <= 1) printf("-1\n");
   // 无解特判
	else printf("%d\n",max(a[n - 2],a[n] % a[n - 1]));
	return 0;
}
```