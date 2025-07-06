# P9868 题解

## 题面
[P9868 [NOIP2023] 词典](https://www.luogu.com.cn/problem/P9868)
## 分析
建议手搓一下样例，以便更好的理清思维。

我们对于每一个字符串，可以存储一个 $k$ 和 $k_2$ 分别表示这个字符串包含的字符中的字典序最小字符与字典序最大字符，这一步可以初始就处理好。

然后判断每一个字符串是否成立时，我们可以直接判断该字符串的 $k$ 是否绝对小于任意其他字符串的 $k_2$（注意这里不能等于，注意到题目中 $w'_i$ 的字典序比 $w'_j$ 都要**小**，而不是**小于等于**，如果当前 $k=k_2$，那只可能当前字符串的字典序大于等于另外的字符串，不符合题意）。

时间复杂度 $O(n^2)$，可以通过此题。

## Code
```cpp
#include<bits/stdc++.h>
using namespace std;
int read()
{
	int x=0,f=0;
	char c=getchar();
	while(!isdigit(c))
	{
		f|=c=='-';
		c=getchar();
	}
	while(isdigit(c))
	{
		x=(x<<3)+(x<<1)+(c^48);
		c=getchar();
	}
	return f?-x:x;
}
int n,m;
char c[3010];
int k[3010],k2[3010];
int main()
{
//	freopen("dict.in","r",stdin);
//	freopen("dict.out","w",stdout);
	n=read(),m=read();
	for(int i=1;i<=n;i++)
	{
		scanf("%s",c);
		for(int j=0;j<m;j++)
		{	
			if(j==0)
				k[i]=k2[i]=c[j]-'a';
			else 
			{
				k[i]=min(k[i],c[j]-'a');
				k2[i]=max(k2[i],c[j]-'a');
			}
		}
	}
	for(int i=1;i<=n;i++)
	{		
		int flag=1;
		for(int j=1;j<=n;j++)
		{
			if(i==j)continue;
			if(k[i]<k2[j])
				continue;
			else{//不符合性质，直接输出，且直接跳出循环 
				flag=0;
				printf("0");
				break;			
			}
		}
		if(flag==1)//如果其他所有字符都满足 k<k2,那表示性质成立 
			printf("1");
	}
	return 0;
}
```
