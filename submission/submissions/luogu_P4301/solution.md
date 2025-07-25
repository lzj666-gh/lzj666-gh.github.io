# P4301 题解

貌似题解区的某几位dalao太巨了，寥寥几笔就写完了题解，然而我觉得那几篇实在太简略了些，于是便写了这篇题解

## [$\color{black}\text{原题链接}$](https://www.luogu.com.cn/problem/P4301)

~~相信你们都做过nim游戏的模板，知道先手的必胜/败条件~~

那么，本题中，先手要胜利，则必须让后手无论拿掉哪几堆都弄不出异或和为0的情况。显然，这要用到线性基。

在插入线性基时，如果没成功插入，即最后x=0，那么意味着会出现异或和为0的情况，这时就要把x取走。显然，~~聪明的~~先手一定必胜，所以这题输出-1是不可能得分的了，我们只用考虑如何让取走的数量最小。

这时我们就要用到贪心思想：从大到小来试，能插入就插入，不能则取走。

那为啥这样结果最小呢？

粗略的证明一下，因为异或是**不进位**加法，那么，如果不是从大到小，假设a^b^…=x(a≤b≤...≤x)，由于中途没有进位，因此，**a^b^…≤a+b+...**,所以显然取走x比取走那几堆更优。

如果并不是a≤b≤...≤x呢？排个序呗。

~~于是就大致的说明了为毛要这样贪心了。~~

**但显然这样是不严谨的。因此想看严谨的证明还请去看[Jaihk662大佬的文章](https://blog.csdn.net/Jaihk662/article/details/75050313)。**

代码如下：
```cpp
#include<bits/stdc++.h>
#pragma GCC optimize(3)
#define LL long long
int n,a[101],d[31];LL ans;
int main(){
	scanf("%d",&n);
	for(int i=1;i<=n;++i)
		scanf("%d",&a[i]);
	std::sort(a+1,a+n+1);
	for(int x=a[n];n;--n,x=a[n]){
		for(int j=30;j>=0;--j)
			if((x>>j)&1)
				if(d[j])x^=d[j];
				else{d[j]=x;break;}
		if(!x)ans+=a[n];
	}
	return printf("%lld\n",ans)*0;
}
```
_谢君曾共霜雪 不辞生死长约_