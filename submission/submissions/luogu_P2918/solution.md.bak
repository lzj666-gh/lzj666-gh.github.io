# P2918 题解

## 一、看题
  很明显，这是一道~~USACO~~的原题，所以我们得先看题面，小心被坑（本蒟蒻就被坑了！！！）
  
 广大群众都看出来这是一道完完全全的完全背包，但还是有些不一样，这里不是单一的装入，还要考虑什么什么情况下有特殊情况（下面会说明）
 
## 二、构思
大部分朋友听到这里后就不会做了，这恰好就中了出题人的下怀，其实啊，我们不妨直接按题目中的条件去试试，没准就过了呢（AC的魔力）

这道题的坑在于，当重量大于等于h，小于等于h与价格最大值的和时，最小值都有可能出现，不仅存于重量等于h时！

所以，根据题面所说的，可以看出状态转移方程，其实这道题蛮单纯的

**状态转移方程**如下：

$$f[j]=min(f[j],f[j-weight[i]]+val[i]);$$

即少载i头奶牛再加上载i头奶牛的时间

## 三、AC代码呈现

```cpp
#include <bits/stdc++.h> //万能的头文件 
using namespace std;

const int maxn=55005; // maxn是用来存数组大小的，可以忽视 
const int Max=5000; // Max是考虑有可能买更多的干草包但花费的钱却更小，只需加上单个开销的最大值即可 

int weight[105],val[105]; //weight数组相当于是存这种干草包有多少磅，val数组存这种干草包一袋花费多少钱 
int f[maxn]; //当需要i磅时，最小花费是多少 
int Min=0x3f3f3f3f; //最小值首先赋成无穷大，以免出错 
int n,h; 

int main()
{
    scanf("%d%d",&n,&h);
    
    for (register int i=1;i<=n;i++) //日常卡常 
    {
    	scanf("%d%d",&weight[i],&val[i]);
	}
	
	for (register int i=1;i<=h+Max;i++)
	{
		f[i]=Min; //先把每个赋成无穷大，由此可见，Min一箭双雕 
	}
	
	for(register int i=1;i<=n;i++)
    {
    	for(register int j=weight[i];j<=h+Max;j++) //典型的完全背包 
        {
        	f[j]=min(f[j],f[j-weight[i]]+val[i]); //美丽的状态转移方程！ 
		}
	}
	
	for (register int i=h;i<=h+Max;i++)
	{
		Min=min(Min,f[i]); //在合理范围内找最小花费 
	}
	
	printf("%d",Min);
	return 0;
}


```

## 四、请求
本人是中学生，这是我第三次发题解，请大家多多支持，留下你们宝贵的赞，顶我！！！
