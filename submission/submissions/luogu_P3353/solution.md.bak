# P3353 题解

题目好甜啊……虽然是个女孩子可是还是被甜到了呢……~~（话说要是有这么个小哥哥追我就好了……）~~

↑以上为题解作者的幻想

下面开始正题

~~话说这题真的甜~~，这道题的题意就是给定一条数轴，我们把数轴简化为一个数组，然后求规定大小的区间内的最大和

一看到就是树状数组码码码

这里的添加星星的操作就对应树状数组的update操作，求区间最大值就对应树状数组的sum操作

### 顺便安利一下树状数组

# 树状数组

一听到有树就很牛逼对不对，其实树状数组是一种很接地气的数据结构，然后比线段树好码多了

树状数组一般有三种操作（算上lowbit）

#### 1.lowbit操作

也就是一层一层往下找的操作，然后具体为什么这么写请问度娘

[树状数组](https://baike.baidu.com/item/%E6%A0%91%E7%8A%B6%E6%95%B0%E7%BB%84/313739?fr=aladdin)

#### 2.update操作

也就是更新节点的值的操作，注意这里的更新指的是加上一个数，也就是如果要变为0那么就要update原数的相反数

#### 3.sum操作

也就是区间求和操作，当然这里的sum指的是从下标为1到下标为n进行求值，树状数组能够高效的求sum的原因就是因为有lowbit操作的存在

注意！前方丑能！

蒟蒻我自己用画图画的图

![](https://cdn.luogu.com.cn/upload/pic/39124.png)

初学树状数组的话，可以先写模板

[树状数组模板1](https://www.luogu.org/problemnew/show/P3374)

[树状数组模板2](https://www.luogu.org/problemnew/show/P3368)

然后巩固可以写写逆序对

[逆序对](https://www.luogu.org/problemnew/show/P1908)

[红色的幻想乡](https://www.luogu.org/problemnew/show/P3801)

然后给一发代码，代码中值得注意的地方是

1.区间求值的时候边界不要写错了……（咕了一次）

2.树状数组代码一定要记牢（咕了一次）


代码太过简单所以注释比较少
```cpp
#include<bits/stdc++.h>
using namespace std;
const int N=100005;
int c[N];//树状数组，这道题只是区间求和，不用存星星，所以不用再开一个星星数组
int n;
int w;
int Max=-1;//等下区间求和的时候比较最大值用
int x,y,z;
int lowbit(int x)//lowbit操作
{
	return x&(-x);
}
void update(int x,int v)//update操作
{
	while(x<=n)
	{
		c[x]+=v;
		x+=lowbit(x);
	}
}
int sum(int x)//区间求和操作
{
	int res=0;
	while(x>0)
	{
		res+=c[x];
		x-=lowbit(x);
	}
	return res;
}
int main()
{
	scanf("%d%d",&n,&w);
	for(int i=1;i<=n;i++)//读入
		scanf("%d%d",&x,&y),update(x,y);
	for(int i=w;i<=100000;i++)//因为这里不想写n，于是我写了100000
	{
		Max=max(Max,sum(i-1)-sum(i-w-1));//区间最大值
	}
	printf("%d\n",Max);//输出
	return 0;
}
```