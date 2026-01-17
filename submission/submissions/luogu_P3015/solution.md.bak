# P3015 题解

题目翻译不完全，这是许多国外oj拿过来的题的通病，所以我来补充翻译一下

输入格式：
```cpp
第一行，n；
接下来n行，每行0或1，0对应“（”；1对应“）”
```
输出格式
```cpp
得分对12345678910取模的结果
```
然后再用一个式子简单推一下样例
```cpp
s（'（（））（）'）=s（'（（））'）+s（'（）'=2*s（'（）'+1=2*1+1=3。
```
英文渣渣，翻译的不好请见谅。

别的东西题目上说的已经很清楚了；

接下来是做题的思路->

我们可以用定义一个整型变量tops来模拟栈顶指针。

当输入为‘（’入栈，tops++；

当输入为“）”出栈，tops--；

若这一位是‘）’但上一位是‘（’进行x_mod，即计算2^tops次方，并累加入tot；

最后输出tot值即可。

需要注意的是：

1.取模的12345678910会爆int，所以开long long。

2.注意每一步都取模，别因为少%而丢失部分分

最后，上代码，自以为还是蛮简洁易懂的。
```cpp
#include<bits/stdc++.h>
#define p 345345
#define h 5001
#define fint register int
#define int long long
#define mods 12345678910
using namespace std;
int a[p],tops,tot;
inline int read();
inline int x_mod(int x,int y);
signed main()
{
	int n;
	n=read();
	for(fint i=1;i<=n;i++)
	a[i]=read();
	for(fint i=1;i<=n;i++)
		if(a[i]==0)
		tops++;
		else
		{
		tops--;
		if(a[i-1]==0)
		tot+=x_mod(1,tops),tot%=mods;
		}
	cout<<tot%mods;
	return 0;
}

inline int read()
{
	int x=0,f=1;
	char ch=getchar();
	while(ch<'0'||ch>'9')
	{
		if(ch=='-')
		f=-1;
		ch=getchar();
	}
	while(ch>='0'&&ch<='9')
	{
		x=(x<<1)+(x<<3)+(ch^48);
		ch=getchar();
	}
	return x*f;
}

inline int x_mod(int x,int y)
{
	for(fint i=1;i<=y;i++)
		x*=2,x%=mods;
	return x;
}
```
总体来说这道题主要还是模拟，只要理解题意难度还是不大的。祝大家AC！