# P4051 题解

## [题面](https://www.luogu.org/problemnew/show/P4051)

## 思路：

作为一个**后缀数组**的初学者，当然首先想到的是**后缀数组**

把$s$这个串首尾相接，扩展为原来的两倍，就能按后缀数组的方法处理

### 证明：

~~神仙一眼就看出这是后缀的裸题，我这个蒟蒻想了半天想不出来~~

如果我们只对$s$串进行后缀排序，明显无法处理如下的情况，~~于是就拿了30分~~

> $s=bnabn$
>
> $bn$会在$bnabn$前面，而实际$bn$对应的应该是$bnbna$，比$bnabn$要大

那么应该这么处理这些缺少的串呢？

我们可以尝试一下把原来的$s$变成两倍

> $s=bnabn+bnabn$
>
> 后缀$bnabnbnabn$在后缀$bnbnabn$前面，而实际上$bnabn$也同样在$bnbna$前面

这样扩展了一倍之后，也就是说题目中变化得到的$len(s)$个串都出现过，但是多出来的部分会不会影响结果呢？

答案是不会

比如说：

> $s=abcd$
>
> 扩展后$ \to s=abcdabcd$
>
> 对于原串的一种变化结果$bcda$
>
> 包含在扩展后的$s$中，而$bcda$对应的后缀就是$bcdabcd$，后缀中多出的$bcd$对于$bcda$来说，它实际上是$bcda$的前缀，也就是说它对$bcda$的影响由$bcda$决定，~~这不就是没有影响吗~~

Code：

```cpp
#include<bits/stdc++.h>
#define N 1000010
using namespace std;
int n,m,x[N],y[N],c[N],sa[N],p,t;
char s[N];
int main()
{
	int i,k;
	scanf("%s",s);
	t=strlen(s);m=300;n=t<<1;//t是原来s的长度，n是扩展后长度，m初始值实际不用300
	for(i=t;i<n;i++) s[i]=s[i-t];
	for(i=0;i<n;i++) c[x[i]=s[i]]++;
	for(i=1;i<m;i++) c[i]+=c[i-1];
	for(i=0;i<n;i++) sa[--c[x[i]]]=i;
	for(k=1;k<=n;k<<=1)
	{
		p=0;
		for(i=n-k;i<n;i++) y[p++]=i;
		for(i=0;i<n;i++) if(sa[i]>=k) y[p++]=sa[i]-k;
		for(i=0;i<m;i++) c[i]=0;
		for(i=0;i<n;i++) c[x[y[i]]]++;
		for(i=1;i<m;i++) c[i]+=c[i-1];
		for(i=n-1;i>=0;i--) sa[--c[x[y[i]]]]=y[i];
		swap(x,y);p=1;x[sa[0]]=0;
		for(i=1;i<n;i++)
			x[sa[i]]=(y[sa[i-1]]==y[sa[i]]&&y[sa[i-1]+k]==y[sa[i]+k])?p-1:p++;
		if(p>=n) break;
		m=p;
	}//都是后缀数组的模板
	for(i=0;i<n;i++) if(sa[i]<t) printf("%c",s[(sa[i]+t-1)]);//也就是一个后缀开始的前一位
	return 0;
}
```

