# P10472 题解

[题目传送门](https://www.luogu.com.cn/problem/P10472)
## 解题思路
我们注意到 $n\le 10^4$，那就可以暴力了！

先用 $i$ 遍历字符串，选择左端点；再用 $j$ 从 $i$ 到最后一个字符选择右端点，$j$ 一边增加，一边用栈维护。

- 当 $a_j$ 是 `(`，`[` 或 `{` 时，把 $a_j$ 压入栈中；
- 当 $a_j$ 是 `)`，`]` 或 `}` 时：
	- 如果栈顶是 `(`，`[`，`{` 中与它对应的那个时，把 `)`，`]` 或 `}` 弹出栈，并让计数器 $now\gets now+1$； 
   - 否则，不是美观的括号序列，`break`，退出循环。
- 当栈是空的时，是美观的括号序列，$maxn\gets \max(maxn,now\times 2)$（括号都是成双成对的，所以要乘 $2$）。

最后输出 $maxn$ 即可。
## Code
```cpp
#include<bits/stdc++.h>
#define int long long
using namespace std;
char st[114514];
signed main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	string a;
	int n,maxn=0;
	cin>>a;
	n=a.size();
	for(int i=0;i<n;i++)
	{
		int now=0,top=0;
		for(int j=i;j<n;j++)
		{
			if(a[j]=='('||a[j]=='['||a[j]=='{')st[++top]=a[j];
			if(a[j]==')')if(st[top]=='(')top--,now++;else break;
			if(a[j]==']')if(st[top]=='[')top--,now++;else break;
			if(a[j]=='}')if(st[top]=='{')top--,now++;else break;
			if(top==0)maxn=max(maxn,now*2);
		}
	}
	cout<<maxn;
	return 0;
}

```