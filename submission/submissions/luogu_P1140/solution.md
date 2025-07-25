# P1140 题解

这篇题解原是我的第一篇题解。随着我对 dp 了解更加深入，题解要求更加严格，我决定于2020年1月19日进行一次大更新。

[云剪贴板](https://www.luogu.com.cn/paste/u7l8dqnn)效果更佳。
## 一、题目分析
### 1.dp 基本思路
就我做过的近百道黄绿难度的 dp 来说，dp 题基本这么几个步骤：
1. 定义状态。
2. 写出状态转移式。
3. 根据状态转移式找出递推顺序。
4. 处理递推的边界。
5. 找出结果。

我讲解时不会就题论题，而是讲大部分黄绿难度的 dp 题的方法。

当然，dp 题十分灵活，不会看完这篇题解就会做，关键在于大量的练习。
### 2.状态定义
定义状态是 dp 最重要的步骤之一，状态定义得不好后面全都无法进行。

像这种线性动态规划，定义经常是“$f_i$ 表示前 $i$ 个满足要求时的答案”。

因为这道题有两个串，很容易想到状态的定义是“$f_{i,j}$ 表示 $a$ 串的前 $i$ 个碱基和 $b$ 串的前 $j$ 个碱基的相似度”。
### 3.转移式
通常定义出状态之后转移式就十分好写了。转移式通常只需要考虑最后一点，比如这道题只用考虑最后一对碱基。

最后一对碱基只有以下3种可能：

1. 非空碱基和非空碱基。
2. 非空碱基和空碱基。
3. 空碱基和非空碱基。

注：空碱基和空碱基不能匹配。

去掉最后一对碱基，转化成规模更小的同样的问题，就是转移式的意义。易得如下转移式：
$$\Large{\color{black}{f_{i,j}=max(}\color{red}{f_{i-1,j-1}+d_{a_{i},b_{j}}},\color{green}{f_{i-1,j}+d_{a_{i},5}},\color{blue}{f_{i,j-1}+d_{b_{j},5}}\color{black}{)}}$$
其中 $d_{i,j}$ 表示编号为 $i$ 的碱基和编号为 $j$ 的碱基的相似程度，编号为5的是空碱基，$a_{i}$ 表示第一个基因的第 $i$ 个碱基，$b$ 表示第二个基因的第 $i$ 个碱基。

其中红色代表第一种情况的转移，绿色代表第二种，蓝色代表第三种。

如果还不能明白，就看下面的图吧：

![](https://cdn.luogu.com.cn/upload/image_hosting/tylpht0w.png)

### 4.递推顺序
这步通常挺简单的，看看下标是变大还是变小。如果你要滚动数组的话（这题好像不能用滚动数组），递推顺序就会难一些。

显然，转移时下标不会变大，为了无后效性，应该从小到大递推。至于先枚举 $i$ 还是 $j$，并不重要。
### 5.边界
递推顺序找到，边界就很容易找到了。

既然下标都是不变或变小，那边界就是至少有一个下标为0。如果一个下标为0，另一个下标不为0，上面3种转移只有一种有效，即：
$$\LARGE{f_{i,0}=f_{i-1,0}+d_{a_{i},5}}$$
$$\LARGE{f_{0,i}=f_{0,i-1}+d_{5,b_{i}}}$$
如果两个下标都为0，也就是 $f_{0,0}$，三个转移都会失效。我们应该按照定义赋给它值：0个碱基和0个碱基的相似度应为0。所以得到最后一个式子：
$$\Huge{f_{0,0}=0}$$

### 6.结果
这道题的结果很好找，就是 $f_{l_a,l_b}$（$l_a$，$l_b$分别代表 $a$ 的长度和 $b$ 的长度），但是有些题的结果还得在多个数中找，比较麻烦。
### 7.实现
5个步骤的思维顺序如上，但是代码顺序略有不同，大概是这样的：
1. 状态定义。
2. 输入。
3. 递推边界。
4. 递推顺序。
5. 状态转移式。
6. 找出结果。

我经常在找出转移式后就迫不及待地写，结果代码中第二步就不行了，只能边写边想，最后代码十分混乱，bug 也不好找。所以最好把5个步骤做完再写代码。
## 二、代码
```cpp
#include<iostream>
#include<algorithm>
using namespace std;
int la,lb,a[110],b[110],f[110][110];//状态定义
int d[6][6]=
{
	{0,0,0,0,0,0},
	{0,5,-1,-2,-1,-3},
	{0,-1,5,-3,-2,-4},
	{0,-2,-3,5,-2,-2},
	{0,-1,-2,-2,5,-1},
	{0,-3,-4,-2,-1,0}
};
int main()
{
	//开始输入 
	cin>>la;
	for(int i=1;i<=la;i++)
	{
		char t;
		cin>>t;
		switch(t)
		{
		case'A':
			a[i]=1;break;
		case'C':
			a[i]=2;break;
		case'G':
			a[i]=3;break;
		case'T':
			a[i]=4;break;
		}
	}
	cin>>lb;
	for(int i=1;i<=lb;i++)
	{
		char t;
		cin>>t;
		switch(t)
		{
		case'A':
			b[i]=1;break;
		case'C':
			b[i]=2;break;
		case'G':
			b[i]=3;break;
		case'T':
			b[i]=4;break;
		}
	}
	//输入结束 
	
	//开始处理边界 
	f[0][0]=0;//全局变量自动初始化为0，但是作为题解，还是写上好。
	for(int i=1;i<=la;i++)
		f[i][0]=f[i-1][0]+d[a[i]][5];
	for(int i=1;i<=lb;i++)
		f[0][i]=f[0][i-1]+d[5][b[i]];
	//边界处理结束
	
	//开始 dp
	for(int i=1;i<=la;i++)
		for(int j=1;j<=lb;j++)
			f[i][j]=max(f[i-1][j-1]+d[a[i]][b[j]],max(f[i-1][j]+d[a[i]][5],f[i][j-1]+d[5][b[j]]));
	//dp 结束 
	
	//开始输出结果 
	cout<<f[la][lb]<<endl;
	//输出结果结束
	return 0;
}
```
最后，码字不易，记得点赞 QwQ。