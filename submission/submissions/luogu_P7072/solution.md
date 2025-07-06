# P7072 题解

# P7072 直播获奖 题解

$update:$
优化了代码的风格



蒟蒻的第一篇题解 求过

此题动态维护第K大数，显然对顶堆

****

先来看几种错误解法：

## 1. 每读入一个就sort排序一次（$50pts$）

这种解法最好想，相应的分也就最少

代码如下
```c++
scanf("%d%d", &n, &w);
for (int p = 1; p <= n; p++)
{
	now=max(1,p*w/100);
	scanf("%d", &a[p]);
	sort(a+1, a+p+1, greater<int>());
	printf("%d ", a[now]); 
}
return 0;
```




结果如下

![](https://cdn.luogu.com.cn/upload/image_hosting/ubknm6ij.png)

## 2. 整体做一次插入排序，边读边做插入排序边输出（$85pts$）

复杂度$O(n^2)$,神奇地过了n=10^4的数据

代码如下

```c++
scanf("%d%d", &n, &w);
a[0]=0x7fffffff;
for (int p = 1; p <= n; p++)
{
	now=max(1,p*w/100);
	scanf("%d", &num);
	for (int i = p; i >= 0; i--)
	{
		if (num < a[i])
		{
			a[i+1]=num;
			break;
		}
		else
		{
			a[i+1]=a[i];
		}
	} 
	printf("%d ", a[now]); 
}
```

结果如下

![](https://cdn.luogu.com.cn/upload/image_hosting/cv5ce27q.png)

****
接下来，我们来了解对顶堆

## 1.什么是对顶堆？
通俗的说，对顶堆是一种简单好用的**动态维护单调区间第k大数或第k小数的数据结构** ~~（好像也不怎么通俗啊）~~,
由一个大顶堆和一个小顶堆构成

 先看图（由于题意降序排列，小顶堆在上， 大顶堆在下。反之亦然 ）：

![](https://cdn.luogu.com.cn/upload/image_hosting/wgonylvh.png)



**不言而喻，一目了然**

*********

## 2. 基本操作

1. 插入元素
```c++
void push(int num)
{
	if (num >= ma_hp.top())
   		mi_hp.push(num);
	else ma_hp.push(num);
	qwq();//调整小顶堆元素个数
}
```

2. 在两个堆之间交换元素:



大->小（下->上）:
```c++
mi_hp.push(ma_hp.top());
ma_hp.pop();
```


小->大（上->下）:
```c++
ma_hp.push(mi_hp.top());
mi_hp.pop();
```

3. 查询
```c++
mi_hp.top();
```


注意：插入元素时应注意整个序列的单调性，判断应插入上面还是下面
于是题目就变成一个动态维护序列第p\*w%大数的题目啦~
****

## 3. 代码

递上一份蒟蒻写的蒟蒻代码

$code:$

```c++
#include <bits/stdc++.h>

using namespace std;

priority_queue<int> ma_hp;//大顶堆 
priority_queue<int, vector<int>, greater<int> > mi_hp;//小顶堆 

int n, w, now, num;

void qwq()//调整获奖人数（小顶堆元素个数）
{
	if (mi_hp.size()<now)
	{
		mi_hp.push(ma_hp.top());
		ma_hp.pop();
	} 
	if (mi_hp.size() > now)
	{
		ma_hp.push(mi_hp.top());
		mi_hp.pop();
	}
	
} 

void push(int num)
{
	if (num >= ma_hp.top()) mi_hp.push(num);
		else ma_hp.push(num);
	qwq();
}

int main()
{
	scanf("%d%d", &n, &w);
	ma_hp.push(0);//避免边界判断 
	for (int p = 1; p <= n; p++)
	{
		now=max(1,p*w/100);;//实时获奖人数 
		scanf("%d", &num);
		push(num);
		printf("%d ", mi_hp.top()); 
	}
	return 0;
}
```

*result：*
![](https://cdn.luogu.com.cn/upload/image_hosting/9fivymje.png)

PS：由于数据范围较小，官方正解应该是桶排序。但是对顶堆可以应对数据更大的题目，并且代码也非常短，是一种非常好用的数据结构呢。

对顶堆练手题目：[P3871](https://www.luogu.com.cn/problem/P3871)

### 点个赞再走吧
### 谢谢

