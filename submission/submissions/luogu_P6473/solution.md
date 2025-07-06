# P6473 题解

这里是民间数据 std。

思路其实很简单。我们应该是先用在后面触发的魔法，再用在前面触发的魔法，这样触发次数才会尽可能少。

因此我们上来对 $a_i$ 排序，然后做个前缀和，那么 $s_i$ 就是触发 $i$ 次后所用的最大时间，显然单调递增。

我们就可以在 $s_i$ 上进行二分查找，使用 `C++ STL` 中的 `upper_bound()` 函数可以帮助我们完成实现。

时间复杂度 $O(q \log n)$，足以通过本题。

```
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <queue>
#include <vector>

using namespace std;

inline int read()
{
	int x=0,f=1;char ch=getchar();
	while (!isdigit(ch)){if (ch=='-') f=-1;ch=getchar();}
	while (isdigit(ch)){x=x*10+ch-48;ch=getchar();}
	return x*f;
}

int n,L,v;

long long a[200050],s[200050];

inline bool cmp(double a,double b)
{
	return a>b;
}

int main()
{
	n=read(),L=read(),v=read();
	for (int i=1;i<=n;i++)
		a[i]=read();
	sort(a+1,a+n+1,cmp);
	for (int i=1;i<=n;i++)
		s[i]=s[i-1]+a[i];
	int q=read();
	while (q--)
	{
		long long t=read();
		t=t*v-L;
		if (t<0)
			puts("0");
		else if (s[n]>t)
			cout << upper_bound(s+1,s+n+1,t)-s << endl;
		else
			puts("-1");
	}
	return 0;
}
```