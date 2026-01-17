# P5726 题解

本题大概思路：

注意此题答案类型为`double`，读入后快排一下，第 $1$ 位和第 $n$ 位就分别是最小值和最大值，那求和时就从 $2$ 开始一直到 $n-1$ 位。最后输出分数和除以总人数 $-2$（因为去掉了最大值和最小值），注意用`printf`的`.2lf`输出，保留 $2$ 位小数。

$Code:$

```cpp
#include<bits/stdc++.h>
using namespace std;
int n,a[10001];
double ans;
int main()
{
	cin>>n;
	for(int i=1;i<=n;i++) cin>>a[i];
	sort(a+1,a+n+1);
	for(int i=2;i<=n-1;i++) ans+=a[i];
	printf("%.2lf",ans/(n-2));
	return 0;
}
```