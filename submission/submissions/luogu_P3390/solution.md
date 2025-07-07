# P3390 题解


$update:2019-9-2$

非常抱歉图炸了，现在应该修复了，管理员给个通过吧（我也不知道为啥图莫名其妙挂了，难道我把图片挂在博客园上不天天访问就会失活？）

$update:2019-2-23$

忽然意识到没有说单位矩阵这个重要的东西，尴尬，现在补上了

-----

嗯，这玩意看着很难对吧，昨天我还是这样想的。。直到今天看到了[**斐波那契公约数**](https://www.luogu.org/problemnew/show/P1306)这道题

这道题一看我这种辣鸡就不会做啊，然后rqy告诉我这是傻逼题啊，我忽然就想起了以前听说过的矩阵乘。。然后懒惰的DDOSvoid大佬告诉我要做这道题，得先做[**斐波那契数列**](https://www.luogu.org/problemnew/show/P1962),要做斐波那契数列，得先做[**矩阵加速**](https://www.luogu.org/problemnew/show/P1939),要做矩阵加速，得先做[**矩阵快速幂**](https://www.luogu.org/problemnew/show/P1939)。。于是，一个上午就这么过去了

----------------

(想看代码直接翻到最下面，本文主要为入门讲解)

回归正题

# 定义

什么是矩阵运算呢？

在理解这个问题前，我们先要知道什么是矩阵

百度百科给的定义如下

> 矩阵是一个按照长方阵列排列的复数或实数集合 

复数实数什么的我们先不管，总之，矩阵就是一堆数，按照矩形排列形成的集合

那么，我们所需要记录的也就是它的长、宽以及矩阵中存储的元素

特殊的，长宽相等的矩阵我们定义它为方阵

当两个矩阵的长宽相等时，我们认为这两个矩阵为同型矩形

# 基本运算

矩阵的运算我们可以类比实数的运算来理解

在实数运算中，一般由进行运算的实数和运算符组成，运算符决定了运算类型

那么同样的，矩阵运算也是如此

## 加法运算

首先，我们来看加法运算

两个矩阵进行**一般的**加法运算的前提是两个矩阵为**同型矩阵**

我们只需要将对应位置的元素相加即可，如下图

![](https://cdn.luogu.com.cn/upload/image_hosting/hioa90k3.png)

在矩阵的加法运算中，满足交换律和结合律，也就是

### $A+B=B+A$

### $(A+B)+C=A+(B+C)$

也许有人想问了，如果我想让两个非同型矩形进行相加可不可以实现呢？

答案是可以的，这种运算是被支持的，我们称这种运算为直和

但由于这种运算使用较少，且与本文关系不大，我们在此不多做解释，感兴趣的朋友可以阅览下面的链接，相信它会给你一个满意的答复

[矩阵加法](https://baike.baidu.com/item/%E7%9F%A9%E9%98%B5%E5%8A%A0%E6%B3%95/12641418?fr=aladdin)

## 减法运算

在实数运算中，减法为加法的逆运算，同样的，在矩阵运算中也是如此，如下图

![](https://cdn.luogu.com.cn/upload/image_hosting/b2rkuxwg.png)

## 数乘

在实数运算中我们并没有数乘这种运算（毕竟本身就是数，直接叫乘法了）

所以在数乘运算中，我们类比向量来进行理解

在数乘向量运算中，只需要将向量中的每个元素乘上那个数就可以了

数乘矩阵也是如此，如图

![](https://cdn.luogu.com.cn/upload/image_hosting/39krazdf.png)

数乘矩阵运算中，满足如下运算律

$(\lambda\mu)A=\lambda(\mu A)$

$(\lambda+\mu)A=\lambda A+\mu A$

$\lambda(A+B)=\lambda A+\lambda B$

## 矩阵乘法（矩阵乘矩阵）

在向量乘向量的运算中，是将每个元素与它对应的元素相乘，求所有乘积之和

那么矩阵乘矩阵是不是就是两个同型矩阵的对应元素相乘呢？

~~**图样图森破**~~

两个矩阵相乘的前提是前一个矩阵的列数等于后一个矩阵的行数

举个栗子，$A$为$n*k$矩阵，$B$为$k*m$矩阵，$C$为$m*n$矩阵，那么$A$可以与$B$相乘，$B$可以与$C$相乘，$C$可以与$A$相乘，其他均不成立

我们知道了什么情况下两个矩阵可以相乘，那么他们怎么相乘呢？不讲每个对应位置相乘还能怎么乘呢？

设$A$为$n*k$矩阵，$B$为$k*m$矩阵,那么它们的乘积$C$则为一个$n*m$矩阵

### $C_{i,j}=\sum_{r=1}^kA_{i,r}*B_{r,j}$

是不是不太好理解，没关系看看图就知道了

![](https://cdn.luogu.com.cn/upload/image_hosting/9zfncisd.png)

在矩阵乘法中满足以下运算律： 

### $(AB)C=a(BC)$

### $(A+B)C=AC+BC$

### $C(A+B)=CA+CB$

在普通的乘法中，一个数乘1还是等于它本身，在矩阵乘法中也有这么一个“1”，它就是单位矩阵

不同于普通乘法中的单位1，对于不同矩阵他们的单位矩阵大小是不同的

对于$n*m$的矩阵，它的单位矩阵大小为$m*m$，对于$m*n$的矩阵，它的单位矩阵大小为$n*n$

也就是说单位矩阵都是正方形的，这是因为只有正方形的矩阵能保证结果和前一个矩阵形状相同

单位矩阵的元素非0即1，从左上角到右下角的对角线上元素皆为1，其他皆为0

-------------

了解了这么多，我们开始看题，矩阵快速幂，由于矩阵乘法满足结合律，所以我们只需要把它按照一般的快速幂打，再重载一下运算符就可以了，好了我们直接放代码

```c++
#include<algorithm>
#include<iostream>
#include<cstring>
#include<cstdio>
#include<cctype>
#define ll long long
#define gc() getchar()
#define maxn 105
#define mo 1000000007
using namespace std;

inline ll read(){
	ll a=0;int f=0;char p=gc();
	while(!isdigit(p)){f|=p=='-';p=gc();}
	while(isdigit(p)){a=(a<<3)+(a<<1)+(p^48);p=gc();}
	return f?-a:a;
}
int n;

struct ahaha{
	ll a[maxn][maxn];     //一定要用long long存矩阵，否则在过程中会爆掉
	ahaha(){
		memset(a,0,sizeof a);
	}
	inline void build(){     //建造单位矩阵
		for(int i=1;i<=n;++i)a[i][i]=1;
	}
}a;
ahaha operator *(const ahaha &x,const ahaha &y){     //重载运算符
	ahaha z;
	for(int k=1;k<=n;++k)
		for(int i=1;i<=n;++i)
			for(int j=1;j<=n;++j)
				z.a[i][j]=(z.a[i][j]+x.a[i][k]*y.a[k][j]%mo)%mo;
	return z;
}

ll k;
inline void init(){
	n=read();k=read();
	for(int i=1;i<=n;++i)
		for(int j=1;j<=n;++j)
			a.a[i][j]=read();
}

int main(){
	init();
	ahaha ans;ans.build();
	do{     //递推快速幂，与普通的递推快速幂无异，但*不能缩写为*=
		if(k&1)ans=ans*a;
		a=a*a;k>>=1;
	}while(k);
	for(int i=1;i<=n;putchar('\n'),++i)
		for(int j=1;j<=n;++j)
			printf("%d ",ans.a[i][j]);
	return 0;
}
```
最后打一下广告  [**我的博客**](http://www.cnblogs.com/hanruyun/)

## 感谢您的阅览