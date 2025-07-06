# P9982 题解

### 题目概述

给定一个长度为 $n$ 的序列 $\{x_n\}$，有 $Q$ 组询问，每组询问给定常数 $a,b$，请选择最优的 $d$，使得 $\sum\limits_{i=1}^{k} a(y-x_i)+ \sum\limits_{i=k+1}^{n} b(x_i-y)$ 最小，并求出最小值，其中 $k$ 满足 $x_k\le y<x_k+1$。

对于 $100\%$ 的数据，满足 $1\le n,Q\le 2\times 10^5$。

### 思路分析

题解区中已经给出了使用二分/三分的做法，这里给出一种偏数学的做法。

我们观察一组询问。

为了方便讨论，我们设 $p_i$ 为 $x_i$ 对答案的贡献。即当 $x_i\le d$ 时 $p_i=a(y-x_i)$，当 $d<x_i$ 时 $p_i=b(x_i-y)$。

我们考虑先设 $y=1$。接着，对于 $d_0$ 和 $d_0+1$，观察每一个 $p_i$ 的变化量，我们发现所有的满足 $x_i\le d$ 的 $p_i$ 会增加 $a$，所有的满足 $x_i\le d$ 的 $p_i$ 会增加 $a$，所有的满足 $d<x_i$ 的 $p_i$ 会减少 $b$。

这说明，如果 $d$ 从 $d_0$ 变化到 $d_0+1$，那么答案增加 $\Delta= k_0\times a-(n-k_0)\times b$。其中 $k_0$ 是 $d=d_0$ 满足 $x_i\le d$ 的 $i$ 的数量。随着 $d$ 的增加，$k_0$ 增加，$\Delta$ 也从负数单调递增至非负数。所以，答案随 $d$ 的增加而先减少后增加。

为了找到最小的答案，我们只需要找到第一个使 $\Delta\ge0$ 的 $k_1$，这个 $k_1$ 对应的结果即为答案。即我们就是要找到满足 $\Delta= k\times a-(n-k)\times b\ge0$ 的最小的 $k$ 对应的 $d$。

对这个式子进行恒等变形：$\Delta= k\times (a+b)\ge n\times b$。

故最小的满足条件的 $k$ 即 $k_1=\lceil \frac{n\times b}{a+b}\rceil$，同时我们根据 $k_1$ 就可以计算出答案。

请注意，对于每一组询问，需要将时间复杂度降到 $O(1)$，故您应当在读入后预处理**前缀和**。

### 代码

```cpp
#include<bits/stdc++.h>
using namespace std;

#define MAXN 200005

int n,q,u;
long long x[MAXN],sum[MAXN];
long long a,b;

int main(){
	cin>>n;
	for(int i=1;i<=n;i++){
		cin>>x[i];
	}	
	sort(x+1,x+n+1);
   
	for(int i=1;i<=n;i++){ // 预处理前缀和
		sum[i]=sum[i-1]+x[i];
	}
   
	cin>>q;
	for(int i=1;i<=q;i++){
		cin>>a>>b;
		u=(int)(ceil((long double)b*n/(a+b))); // 为了保证精度如此操作
		cout<<(x[u]*(u)-sum[u])*a+(sum[n]-sum[u]-x[u]*(n-u))*b<<endl;
		// 此处计算答案时带入前缀和
	}
	
	return 0;
}
```