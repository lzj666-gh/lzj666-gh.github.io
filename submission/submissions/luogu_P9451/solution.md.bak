# P9451 题解

[题目传送门](https://www.luogu.com.cn/problem/P9451)

直接分类讨论：

- 如果数 $a$ 满足 $\operatorname{popcount}(a)\ge3$，直接报告无解；

- 如果数 $a$ 满足 $\operatorname{popcount}(a)=1$，则直接输出 $a+1$ 即可，因为这样最多才使 $\operatorname{popcount}(a)=2$；

- 如果数 $a$ 满足 $\operatorname{popcount}(a)=2$，就稍微麻烦一些。我们先设数 $a$ 在二进制表示下为 $a'$，则可以找到 $a'$ 最右侧的 $1$，然后将其“加 $1$”即可。通俗地讲，就是找到最右侧的 $01$，将其变为 $10$。例如：$1010$ 的下一个合法数字为 $1100$。请注意，这个过程并不是真正的加 $1$。
   
   这里可以使用 [$\operatorname{lowbit}$](https://oiwiki.com/ds/fenwick/#%E7%AE%A1%E8%BE%96%E5%8C%BA%E9%97%B4) 函数来找到二进制数最右侧的 $1$。例如，$\operatorname{lowbit}(x)$ 就是 $x\operatorname{and}-x$。注意 $\operatorname{lowbit}$ 函数返回的值是一个 $k$ 位的二进制数 $\begin{matrix}1\ \underbrace{000\cdots000}\\\ \ \ k-1\text{个}\end{matrix}$，也就是十进制数 $2^k$，所以最后将其再加上 $n$ 即为答案。
   
得代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
#define int long long
#define pop __builtin_popcountll
int lowbit(int x)
{
	return x&-x;
}
signed main()
{
	int t;
    cin>>t;
    while(t--)
	{
		int n;
    	cin>>n;
    	if(pop(n)>=3)
    	{
    		puts("No,Commander");
		}
    	else if(pop(n)==1)
    	{
    		cout<<n+1<<endl;
		}
    	else
		{
    		cout<<n+lowbit(n)<<endl;
		}
	}
	return 0;
}
```