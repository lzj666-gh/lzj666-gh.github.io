# P1042 题解

本题是一道基本语法题。

在本篇题解中，我们将使用 `string` 类进行读入，并利用较新的遍历语法来完成编程。

首先读入字符串，我们一个一个读入字符，并添加到字符串的末尾，一直到读到 `E` 字符为止。

```cpp
while(cin>>C)
{
  if(C=='E')break;
  S+=C;
}
```
其中 `while(cin>>C)` 这一语法利用了 `cin` 的特性，当 `cin` 没能读入到信息的时候，会返回 $0$，那么循环就会终止。

在本地调试的时候，你可以输入 `Ctrl+Z` 来使得循环终止。

读入之后，我们可以利用遍历语法寻找所有的字符，并统计分数，我们可以把结算的条件记作：
- $\max(A,B)>Lim$，$\max$ 表示的是两者中较大的一个数字的数值，其中 $Lim$ 表示的是规则是多少分制。
- $|A-B|\geq 2$，其中 $|x|$ 是求 $x$ 的绝对值，相当于 C++ 中的 `abs(x)`，意思可以理解为，去除数字的正负号。

一局游戏能结算，当且仅当两个条件都成立。

那我们可以得到以下代码。

```cpp
#include<bits/stdc++.h>
using namespace std;
char C;
string S;
int n,A,B;
int main()
{
	while(cin>>C)
	{
		if(C=='E')break;
		S+=C;
	}
	for(char i:S)
	{
		if(i=='W')A++;
		if(i=='L')B++;
		if(max(A,B)>=11&&abs(A-B)>=2)
		{
			cout<<A<<":"<<B<<endl;
			A=0,B=0;
		}
	}
	printf("%d:%d\n",A,B);
	A=B=0;
	puts("");
	for(char i:S)
	{
		if(i=='W')A++;
		if(i=='L')B++;
		if(max(A,B)>=21&&abs(A-B)>=2)
		{
			cout<<A<<":"<<B<<endl;
			A=0,B=0;
		}
	}
	printf("%d:%d\n",A,B);
	return 0;
}
```

我们发现两次统计做的事情是类似的，关键在于参数 $Lim$ 的不同，如果你会函数语法，我们也可以写一个函数 `Work`，并且含有参数 `Lim`，这样代码就更加简短啦！

```cpp
#include<bits/stdc++.h>
using namespace std;
char C;
string S;
int n,A,B;
void Work(int Lim)
{
	for(char i:S)
	{
		if(i=='W')A++;
		if(i=='L')B++;
		if(max(A,B)>=Lim&&abs(A-B)>=2)
		{
			cout<<A<<":"<<B<<endl;
			A=0,B=0;
		}
	}
	printf("%d:%d\n\n",A,B);
	A=B=0;	
}
int main()
{
	while(cin>>C)
	{
		if(C=='E')break;
		S+=C;
	}
	Work(11),Work(21);
	return 0;
}
```

我们通常用时间复杂度来判断代码的运行效率，那么这份代码的时间复杂度是 $\mathcal O(n)$。