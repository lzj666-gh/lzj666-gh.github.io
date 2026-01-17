# P4035 题解

## A Solution For P4035 Problem ##
写了两天终于搞懂了！！！  
坚持写小白都能看懂的题解！！！  
  
说实话，本蒟蒻是第一次学习高斯消元，写这篇题解旨在加深自己的理解，以及帮助一下打算学习高斯消元的同学。  
以下一部分来自李煜东老师的《算法竞赛——进阶指南 0x35》（详见P155）



* ## 什么是高斯消元  
高斯消元是一种求解线性方程组的方法。  
所谓线性方程组，是由M个N元一次方程共同构成的。  
我们可以利用每个方程的所有系数及等号右侧的常数，  
写成一个M行N+1列的“**增广矩阵** ”。  
然后对这个矩阵进行一系列操作得到方程组的解所用到的方法  
我们称之为：高斯消元  
* ## 举个栗子 ##
给定一个三元一次方程组：  
$ x_1+2x_2-x_3=-6 $  
$ 2x_1+x_2-3x_3=-9 $  
$ -x_1-x_2+2x_3=7 $   
变形为增广矩阵：  
![](https://cdn.luogu.com.cn/upload/pic/61850.png)
凑活着看吧，不太精通Markdown和LaTeX（抱歉了，客官们~）  
求解这种增广矩阵我们有三种操作：  
1.用一个非零的数乘上某一行。  
2.把其中的一行的若干倍加到另一行上。  
3.交换两行的位置。  
这三种操作呗称作叫初等行变换  
同样的，我们可以定义初等列变换  
那么上面的表格就动了起来，像这样  
![](https://cdn.luogu.com.cn/upload/pic/61845.png)  


![](https://cdn.luogu.com.cn/upload/pic/61847.png)  


![](https://cdn.luogu.com.cn/upload/pic/61848.png)


![](https://cdn.luogu.com.cn/upload/pic/61849.png)


![](https://cdn.luogu.com.cn/upload/pic/61867.png)


![](https://cdn.luogu.com.cn/upload/pic/61867.png)

至此，我们最后得到的是“**阶梯型矩阵**”  
该矩阵表达的是：  
$ x_1+2x_2-x_3=-6 $  
$ x_2+x_3=1 $  
$ x_3=3 $  
我们已经知道了$ x_3 $的值，所以能够代入求解  
如果我们对方程组进一步化简，能够得到下面的表格：  
![](https://cdn.luogu.com.cn/upload/pic/61868.png)

最后： 
![](https://cdn.luogu.com.cn/upload/pic/61869.png)  
这个最终的矩阵叫“**简化阶梯型矩阵**”  
引出定义：  
**通过初等行变换把增广矩阵变为简化阶梯型矩阵的线性方程组求解算法就是高斯消元算法**  
* ## 特例 ## 
$ x_1+2x_2-x_3=3 $  
$ 2x_1+4x_2-8x_3=0 $  
$ -x_1-2x_2+6x_3=2 $  
对这个方程组手模一遍（懒得打表了QAQ）得到：  
$ x_1=4-x_2 $  
$ x_3=1 $  
可见，$ x_2 $取任何值都有一个对应的$x_1$，并且使原方程组成立  
也就是说，该方程组有无穷多个解  
我们把$x_1,x_3$这样的未知量称为“**主元**”  
而$x_2$叫“**自由元**”  

**综上所述，可以大致分为三种情况：**   
**1.高斯消元完成后，若存在系数全为0、常数不为0的行，则方程组无解。**  
**2.若系数不全为0的行恰好有$n$个，则主元有$n$个，方程组有唯一解。**  
**3.若系数不全为0 的行有$k<n$个，则主元有$k$个，自由元有$n-k$个，方程组有无穷多个解  **  

到这里，我们的基础知识就讲完了，你，看懂了吗？  


------------

* ## 来看例题[P4035球形空间产生器](https://www.luogu.org/problemnew/show/P4035)  
一个球体上的所有点到球心距离相等，因此我们只需求出一个点（$x_1,x_2,x_3……x_n$），使得：  
$  \sum_{j=0}^{n} $ $ (a_{i,j}-x_j)^2=C $  
其中C为常数，$a_{i,j}$是点的坐标。  
改方程组由$n+1$个$n$元二次方程构成，当然不是线性的，怎么办呢？？  
我们可以通过相邻两个方程做差，变成$n$个$n$元一次方程组，消去常数C  
有点像数学中数列求通项公式或者前$n$项和  
于是有：  
$ \sum_{j=1}^{n} $ $ (a_{i,j}^2-a_{i+1,j}^2-2x_j(a_{i,j}-a_{i+1,j}))=0 $  
把变量放左边，常数放右边：  
$ \sum_{j=1}^{n} $ $ 2(a_{i,j}-a_{i+1,j})x_j$ = $ \sum_{j=1}^{n}(a_{i,j}^2-a_{i+1,j}^2)$  $ (i=1,2,3……n) $
    
    
so,我们要对这个增广矩阵进行高斯消元：  
![](https://cdn.luogu.com.cn/upload/pic/61894.png)


下面就是代码时间啦：
```cpp
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

inline int read(){
	int x=0,w=1;
	char ch=getchar();
	for(;ch>'9'||ch<'0';ch=getchar()) if(ch=='-') w=-1;
	for(;ch>='0'&&ch<='9';ch=getchar()) x=x*10+ch-'0';
	return x*w;
}

double a[20][20],b[20],c[20][20];//c:矩阵系数  b:常数  两者构成增广矩阵  
int n;

int main(){
	n=read();
	for(int i=1;i<=n+1;i++)
		for(int j=1;j<=n;j++)
			scanf("%lf",&a[i][j]);
	for(int i=1;i<=n;i++)
		for(int j=1;j<=n;j++){
			c[i][j]=2*(a[i][j]-a[i+1][j]);
			b[i]+=a[i][j]*a[i][j]-a[i+1][j]*a[i+1][j];
		}
	//高斯消元（数据保证有唯一解）
	for(int i=1;i<=n;i++){//找到x[i]系数不为0的一个方程
		for(int j=i;j<=n;j++){
			if(fabs(c[j][i]>1e-8)){
				for(int k=1;k<=n;k++)
					swap(c[i][k],c[j][k]);
				swap(b[i],b[j]);
			}
		}
	//消去其他方程x[i]的系数
		for(int j=1;j<=n;j++){
			if(i==j) continue;
			double rate=c[j][i]/c[i][i];
			for(int k=i;k<=n;k++) c[j][k]-=c[i][k]*rate;
			b[j]-=b[i]*rate;
		}
	}
	for(int i=1;i<n;i++)
		printf("%0.3lf ",b[i]/c[i][i]);
	printf("%.3lf\n",b[n]/c[n][n]);
	return 0;
}
```
emmmm，终于写完啦，希望讲懂了（逃~
    
    
