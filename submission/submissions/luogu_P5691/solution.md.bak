# P5691 题解

# P5691 [NOI2001] 方程的解数

updated 修复了一点点乱码

## 前言

最近在复习折半搜索。

其实折半搜索除了这个还有一些好题的：

[P4799 [CEOI2015 Day2]世界冰球锦标赛](https://www.luogu.com.cn/problem/P4799)

[P3067 [USACO12OPEN]Balanced Cow Subsets G](https://www.luogu.com.cn/problem/P3067)

[CF888E Maximum Subsequence](https://www.luogu.com.cn/problem/CF888E)

## 题意

求方程 $\sum \limits_{i=1}^n k_ix_i^{p_i}=0, x_i \in [1,m](i\in [1,n])$ 的整数解的个数。

最为朴素的方法是枚举 $x_i$，然后复杂度就是 $O(m^n)$ 的。~~GG~~

想办法降复杂度。

首先 $x_i$ 是肯定要枚举的，但是肯定又不能直接枚举。

于是考虑怎样把指数降下去。

可以用 折半搜索（_meet in middle_）.

## 折半搜索

做法为将整个搜索的过程分为两部分，然后每部分分别进行搜索，最后将得到两个答案序列，再将答案序列进行合并，即可得到最终的答案。

可以发现，当状态非常之多的时候，这种优化还是非常明显的，最优情况下可以直接把复杂度开个根号。

需要注意的是，折半搜索应用的时候需要满足以下条件：

- 搜索各项不能相互干扰。

- 需要满足搜索状态可逆，就是说一个状态可以从两个方向都得到。

折半搜索其实还是用的比较广泛的。

BFS ,DFS 还有状压 DP 都有类似的应用。

折半搜索一般的难点就在于最后的答案序列合并。（可能会使用一些奇奇怪怪的高深的玩意才能搞得出来）

实现非常灵活，需要按照题目来进行选择。

一般比较常见的排序后二分，双指针还有哈希表（自然还有一些我没见过的）。

逐个分析一下（以下的代码均不是本题的，只是提供一下大概的板子长啥样）：

排序后二分 复杂度肯定是带 $\log$ 的。

为什么正确？

在一个有序的序列中，如果我们可以找到一个位置可以做到对答案有贡献，那么这个位置之前的所有位置都是可以对答案有贡献的。

所以直接统计就好。

```cpp
sort(a+1,a+1+cnta);
for(re int i=1;i<=cntb;i++)
    ans+=upper_bound(a+1,a+1+cnta,m-b[i])-a-1;
```

双指针一般是线性的，效果很不错，代码比较好写。

缺点就是比较难想，需要考虑一些问题（例如单调性）。

```cpp
int l=cnta,r=1;
for(r=1;r<=cntb;r++){
	while(a[l]+b[r]>m)l--;//m是一个限制条件
	if(a[l]&&b[r])ans+=(l-1);  
} 
```

哈希表也是线性，至于具体如何就要看脸了。

如果不被卡的话哈希表确实是一种非常不错的选择。

具体就是先处理一半，然后把搜到的答案存到哈希表里，然后搜另一半，之后再去哈希表里找，把结果合并就可以了。

```cpp
void dfs1(){//搜索一半 
	if (到达边界){
		add(hash(x)); 
		return;
	} 
	... 
}

void dfs2(){//处理另一半 
	if (到达边界){
		ans+=sum[hash(x)];
		return;
	} 
	... 
}

```

## 本题解法

观察这个式子，想办法把 $n$ 的规模降为原来的一半。

$\sum \limits_{i=1}^n k_ix_i^{p_i}=0$

把左边拆开得：

$\sum \limits_{i=1}^{\lfloor n/2 \rfloor} k_ix_i^{p_i}+\sum \limits_{\lfloor n/2 \rfloor}^{n} k_ix_i^{p_i}=0$

移项得：

$\sum \limits_{i=1}^{\lfloor n/2 \rfloor} k_ix_i^{p_i}=-\sum \limits_{\lfloor n/2 \rfloor}^{n} k_ix_i^{p_i}$

于是这样就可以折半搜索了。

接下来确定一下是否满足性质：

- $x_i$ 的不同取值不会影响别的答案，方程的解数量不会发生改变。

- 因为是要枚举 $x_i$ 的取值，所以无论怎么搜，答案都是一样的，所以满足状态可逆。

考虑合并。

可以发现，等号两边的区别在于有一个负号。

于是我们可以搜一半，然后找另一半中满足 与它相加等于 $0$ 的数，也就是相反数。

之后合并答案就可以了。

关于哈希的合并方法和排序后二分别的题解已经说的很清楚了，这里主要说一下双指针的统计方法。

首先将两个答案数组排序。

然后找到两个相加满足条件的第一个位置，然后统计左半部分一样的有多少个，右半部分一样的有多少个，然后运用乘法原理合并起来就好了。

```cpp
sort(a+1,a+1+cnta);
sort(b+1,b+1+cntb);
	
int l=1,r=cntb;
for (;l<=cnta&&r>=1;l++){
	while (a[l]+b[r]>0)r--;//找到满足条件的第一个位置
	int x=1,y=0;
	for(int j=r;a[l]+b[j]==0&&j>0;j--)y++;//计算第二个部分有多少个满足的的
	while(l<cnta&&a[l]==a[l+1])x++,l++;//计算左半部分有多少一样的
	ans+=x*y;//乘法原理
} 
```

## CODE：

```cpp
//#define LawrenceSivan

#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
#define re register
const int maxn=4e6+5;
#define INF 0x3f3f3f3f

int n,m;

int k[10],p[10];

int a[maxn],b[maxn],cnta,cntb,ans;

int qpow(int a,int b){
	int res=1,x=a;
	for(;b;b>>=1,x=x*x){
		if(b&1)res=res*x;
	}
	return res;
}

void dfs(int l,int r,int sum,int *arr,int &cnt){
	if(l>r){
		arr[++cnt]=sum;
		return;
	}
	for(re int i=1;i<=m;i++)
		dfs(l+1,r,sum+k[l]*qpow(i,p[l]),arr,cnt);
	
}

inline int read(){
    int x=0,f=1;char ch=getchar();
    while(!isdigit(ch)){if(ch=='-')f=-1;ch=getchar();}
    while(isdigit(ch)){x=x*10+(ch^48);ch=getchar();}
    return x*f;
}

int main(){
#ifdef LawrenceSivan
    freopen("aa.in","r",stdin);
    freopen("aa.out","w",stdout);
#endif
	n=read();m=read();
	for(re int i=1;i<=n;i++){
		k[i]=read();p[i]=read();
	}
	
	int mid=(1+n)>>1;
	dfs(1,mid,0,a,cnta);
	dfs(mid+1,n,0,b,cntb);

	sort(a+1,a+1+cnta);
	sort(b+1,b+1+cntb);
	
    
	int l=1,r=cntb;
	for (;l<=cnta&&r>=1;l++){
	    while (a[l]+b[r]>0)r--;
	    int x=1,y=0;
	    for(re int j=r;a[l]+b[j]==0&&j>0;j--)y++;
	    while(l<cnta&&a[l]==a[l+1])x++,l++;
	    ans+=x*y;
	} 
	 
	 
	printf("%lld\n",ans);
	
    return 0;
}

```

 
