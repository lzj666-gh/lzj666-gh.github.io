# P6032 题解

# 第一篇绿题题解
首先，读题可以发现，这道题相对于[P1311 选择客栈](https://www.luogu.com.cn/problem/P1311)唯一的差别就是数据范围大了，未加强过的题目可以用$O(Nlog n)$的算法**勉强**过，但是这道题应该是会$TLE$几个点的，所以如果要$AC$的朋友们，就要用到$O(N)的算法。$~~那么恭喜您，找对题解了~~！

来说一下思路，既然是$O(N)$的解法，自然只能有循环，那么当然是$i=1$~$N$了，那么括号内放什么呢？听博主慢慢道来：

大致思路是这样的：循环一层$i=1$~$N$，接着找最近的一个价格小于等于$P$的咖啡厅，所以前面的所有同色客栈都可以为一个方案

三个关键数组$aft[i]$存最后一个颜色为$i$的客栈的坐标，$tot[i]$表示同个颜色每次的方案数，$numb[i]$存颜色为 $i$的客栈的总数。

代码：
```cpp
#include <bits/stdc++.h>
using namespace std;

const int maxn=200005;

long long n,k,p;
long long col,pri;
long long aft[maxn],tot[maxn],numb[maxn],bef;

long long ans;

int main()
{
	//freopen("hotel.in","r",stdin); 这里由于是考试时打的，
	//freopen("hotel.out","w",stdout); 所以用了文件输入输出 

    scanf("%lld%lld%lld",&n,&k,&p);
    
    for (register int i=1;i<=n;++i)
    {
    	scanf("%lld%lld",&col,&pri); //再循环内输入，节约一点点时间 
    	
    	if (pri<=p) bef=i; //满足就赋值 
    	
    	if (bef>=aft[col]) tot[col]=numb[col]; //最大值重新命值 
    	
    	ans+=tot[col]; //答案加上暂时储存 
    	
		aft[col]=i; //最后客栈位置也要改变 
    	
    	numb[col]++; //暂时储存的加上一 
	}
	
	printf("%lld",ans); // 愉快的输出 

	return 0;
}
```
希望对大家有帮助$ ! ! !$
# 谢谢观看! ! !
 
 