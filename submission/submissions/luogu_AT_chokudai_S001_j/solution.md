# AT_chokudai_S001_j 题解

## 这道题就是求逆序对的个数

### 什么是逆序对？

逆序对就是在数列中满足`i<j` 且`a[i]>a[j] `的一对数

我们都会冒泡排序，事实上在冒泡排序的过程中，我们就是不断找逆序对，交换他们

所以只要模拟一遍冒泡排序就可以统计出来逆序对的数量

根据逆序对的定义，很容易写出$O(n^2)$算法

```cpp
for(int i=1;i<=n;i++)
{
	for(int j=i+1;j<=n;j++)
	{
		if(a[i]>a[j])
		{
			ans++;
		}
	}
}
```
但一定会超时的，考虑更优方法

常用的求逆序对的方法有两种，一种是归并排序，一种是利用树状数组

我看了下现有的题解，大部分都是归并排序，有一个树状数组的题解不好理解，所以我写一个题解

### 树状数组求逆序对

#### 注意，此题解适合已有树状数组基础的朋友

我们可以先开一个大小为$a$的最大值的树状数组$c$

每当读入一个数时，我们可以用桶排序的思想，将`c[a[i]]`加上$1$

然后我们统计`c[1]-c[a[i]]` 的和ans

$ans - 1$（除掉这个数本身）就是在这个数前面有多少个数比它小

遍历 $i$ 从 $1$ 到 $n$ 我们只要用 `i-ans` 就可以得出前面有多少数比它大，也就是逆序对的数量

#### 但是！

#### 有时候，a的最大值可能到达你开c数组会直接炸掉的地步

那我们就要引入一个奇技淫巧——离散化

（在这里不详细介绍离散化，只是作为一个技巧来使用，如果想学习的建议去百度）

我们可以在读完数数据后对他进行从小到大排序

我们用排完序的数组的下标来进行运算

这样可以保证小的数依旧小，大的数依旧大

话不多说，上代码

```cpp
#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
using namespace std;
struct Number
{
	int order;//序号
	int value;//值
}a[100005];
int lsh[100005];//离散化后的数组
int c[100005];
int n;
int lowbit(int x)//熟悉的lowbit
{
	return x&-x;
}
void update(int x,int k)//熟悉的增值函数
{
	for(int i=x;i<=n;i+=lowbit(i))
	{
		c[i]+=k;
	}
}
int getSum(int x)//熟悉的求和函数,求前面和多少就是小于它数的个数
{
	int res=0;
	for(int i=x;i>0;i-=lowbit(i))
	{
		res+=c[i];
	}
	return res;
}

/*
以上我相信不用多说，只要有树状数组的基础就可以明白
如果不熟悉的，其实没必要看这篇题解
*/
bool cmp(Number x,Number y)
{
	return x.value<y.value;
}
//排序函数
int main()
{
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		cin>>a[i].value;
		a[i].order=i;//记录原序
	}
	sort(a+1,a+n+1,cmp);//快排
	for(int i=1;i<=n;i++)
	{
		lsh[a[i].order]=i;//离散化的过程
	}
	long long ans=0;//不开longlong见祖宗
	for(int i=1;i<=n;i++)
	{
		update(lsh[i],1);
		ans+=i-getSum(lsh[i]);//减去小于的数即为大于的数即为逆序数
	}
	cout<<ans<<endl;
	return 0;
}
```
不过，据说这题不用离散化也能过，我没试
### 温馨提示：不开$long long$见祖宗
写题解不易，求多支持，谢谢各位