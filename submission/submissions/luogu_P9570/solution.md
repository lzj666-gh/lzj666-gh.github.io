# P9570 题解

[原题](https://www.luogu.com.cn/problem/P9570)

[更好的阅读体验](https://www.cnblogs.com/thenyu/p/17649810.html)

直接遍历字符串，如果当前字符为 `N` ,就判断编号 $1 \sim n$ 是否有冰川没有第一次融化。如果有，就将这个冰川的编号存到记录答案的数组中；如果没有，则输出 `No solution` 并结束程序。

如果当前字符为 `Y` ，因为题目要求字典序最小，所以直接判断编号 $1$ 的冰川是否已经第一次融化，如果没有就输出 `No solution` 并结束程序，有就直接把编号为 $1$ 的冰川存到记录答案的数组中。

```cpp
#include<bits/stdc++.h>
using namespace std;
const int N=1e6;
int n,m,a[N+5],cnt,tmp;//tmp用来记录已经融化的冰川数量
string s;
int main()
{
	scanf("%d%d",&n,&m);
	cin>>s;
	for(int i=0;i<m;++i)
	{
		if(s[i]=='N')
		{
			if(tmp==n){printf("No solution");return 0;}//如果所有冰川已经第一次融化了，那么就没有符合条件的冰川 
			a[++cnt]=++tmp;//有符合条件的冰川，存到数组a中 
		}
		else
		{
			if(cnt==0){printf("No solution");return 0;}//如果数组a中没有冰川第一次融化，那就没有符合条件的冰川 
			a[++cnt]=1;
		}
	}
	for(int i=1;i<=cnt;++i)
		printf("%d ",a[i]);
	return 0;
}
```
