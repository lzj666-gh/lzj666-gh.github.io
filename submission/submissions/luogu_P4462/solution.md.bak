# P4462 题解

### 闲话

- 博主更新给管理员带来的不便请谅解

- UPD 20200207 - 添加了一些归纳过的计算公式

- UPD 20200210 - 更正了将块取小的原因。

这是一篇 ***在线算法*** 的题解！！！

用了分块，虽然比莫队差一点点点点，但怎么说也是一种优美的解法。

只是比较考验细节，调了好几个小时啊啊啊啊啊。。。

![1sovFJ.png](https://s2.ax1x.com/2020/02/05/1sovFJ.png)

wtcl...

## 正片

### 数列分块的思想（熟悉的可以略过）

数列分块又被称作数列的平方分割。

数列分块是将整段数列分为均匀的几块，使得每块长度为$b$（末块的最后一个是第$n$个，并不是直接向后$+b$个，注意特判）。这里，$b$常取$\sqrt{n}$。

然后对每个块都维护一些必要的信息。

比如：[P3372 【模板】线段树 1](https://www.luogu.com.cn/problem/P3372)这一题就可以用分块做。

我们维护一下每个块的原数字之和，加法标记即可。

查询或修改时，并不一定目标区间一定包含整块。对于边角块，暴力。对于整块，取其现成维护的信息即可。

由于散块中的元素不超过$2\sqrt{n}$个，整块一个不超过$\sqrt{n}$块，所以这样的分块算法复杂度为$O(m\sqrt{n})$。

如果仅仅对分块了解至此，对于本题而言还是远远不够的。详细的教程请自行到网上学习。这里不再赘述。

本题中，这里认为$n,m,k$同阶。

### 下面算法基于的技巧

在下面的算法中，我们要做到快速求得某一段的异或和。

我们知道，异或的逆运算即为异或。

所以我们定义$s_i=a_1\oplus a_2\oplus ... \oplus a_i$，其中$\oplus$代表异或，$a$为原数组。

那么$a_l\oplus a_{l+1}\oplus ... \oplus a_{r}$就等于$s_{r}\oplus s_{l-1}$。

现在问题成了：给定$l,r$，求区间$[l-1,r]$中有多少对二元组$(i,j)$满足$l-1\le i\le j\le r$且$s_i\oplus s_j=k$。

注意，由于实际使用时，$l$是要减一的，因此不能从一开始，而是0。

### 对于此题需要维护的信息

我们现在使用$s$取代一无是处的$a$。

- $pre[i][j]$表示前$i$个块之内，数字$j$出现的次数。

- $ans[i][j]$表示第$i$个到第$j$块（包括$i,j$）的 ***答案***。

至于为什么做这些，请继续阅读。

这里我们暂时仍用$\sqrt{n}$作块的大小。

### 预处理——$pre,ans$的求法。

先是$pre$，这个简单。我们在$s$上一路扫去直到$B|i$时，即应该是下一个块的开始时，我们将这个块的$pre$的信息copy到下一个块中。扫的时候顺便处理一下第$i$个位置的所属块的编号。

下面的代码优化了一下，就是先求出最大的$s$的元素，以其为边界进行copy。注意不要漏掉0。

```cpp
memset(pre[0],0,sizeof(pre[0]));
limits=*max_element(s,s+1+n);
for(register int i=0,j=0;i<=n;i++)
{
	if(i%B==0)
	{
		block=++j;
		for(register int val=0;val<=limits;val++)
			pre[j][val]=pre[j-1][val];
	}
	belong[i]=j,pre[j][s[i]]++;
}
```

这部分的复杂度为$O(\max\limits_{i\in [0,n]}{s_i}\times \sqrt{n})$。

然后是$ans$，这个是第一个难点。为了求出所有的$ans$，我们分两步做。

1. 计算$ans[i][i]$：

这个不难，只要暴力计算就行了。复杂度$O((\sqrt{n})^3)=O(n\sqrt{n})$。

2. 计算$ans[i][j](j>i)$

上面我们计算的$ans[i][i]$即将会用到！

我们假设我们已经求得了$ans[i][j-1]$的值，那么$ans[i][j]$的值就是$ans[i][j-1]+ans[j][j]$······

Wrong!

上面，我们相当于只计算了区间的左右端点（这里左右端点指“下面算法基于的技巧”中的$(i,j)$的二元组）都在$[\text{第i块，第j-1块}]$和都在$\text{第j块}$的情况，而很有可能左右端点并不在上述两个区间之中的同一个，可能左端点在$[\text{第i块，第j-1块}]$，而右端点在$\text{第j块}$。这种情况我们漏掉了。

那怎么计算呢？我们可以枚举上述2部分的其中一部分的所有元素，另一部分可以利用已经求得的$pre$来计算与之对应的元素的个数。

那么枚举那一部分呢？显然是第二部分。因为第二部分是一个块，最多$\sqrt{n}$个元素，而第一部分指不定有多少块呢。。复杂度$O(2(\sqrt{n})^3)=O(n\sqrt{n})$

$$ans[i][j]=ans[i][j-1]+ans[j][j]+\sum\limits_{p\in\text{第
j块}}(pre[j-1][s_p\oplus k]-pre[i-1][s_p\oplus k])$$

处理$ans$的算法大致明朗了，代码：

```cpp
for(register int i=1;i<=block;i++)
	for(register int j=(i-1)*B;j<=min(n,i*B-1);j++)
		for(register int p=j+1;p<=min(n,i*B-1);p++)
			if((s[j]^s[p])==k) ans[i][i]++;
for(register int i=1;i<=block;i++)
	for(register int j=i+1;j<=block;j++)
	{
		ans[i][j]=ans[i][j-1]+ans[j][j];
		for(register int p=(j-1)*B;p<=min(n,j*B-1);p++)
			ans[i][j]+=pre[j-1][s[p]^k]-pre[i-1][s[p]^k];
	}
```

预处理工作就这么愉快的结束啦！预处理总复杂度为$O(n\sqrt{n})$。

### 在查询时利用好预处理的信息

查询时，输入是$l,r$，但查询时我们要将$l$减一，方便处理。

那么查询怎么做呢？别急，我们暂且讨论一下如何在$O(\text{区间长度})$的时间内求得一个询问的答案。

定义$rec[i]$为数字$i$出现的次数。

#### 快速计算散块

我们先扫一边区间，并处理好$rec$。然后再扫一遍，扫到第$i$位的时候，先将$rec[s_i]$减一，再将$s_i\oplus k$的数的个数，即$rec[s_i\oplus k]$的值加到答案上即可。

代码：

```cpp
LL ret=0ll;
for(register int i=l;i<=r;i++)
	__rec[s[i]]++;
for(register int i=l;i<=r;i++)
	__rec[s[i]]--,ret+=__rec[s[i]^k];
return ret;
```

对于散块，或者$(l,r)$之间（ ***不包括两个端点，便于判断*** ）并没有整块的情况，我们直接这样暴力即可。

由于这两种情况扫描的长度不超过$2\sqrt{n}$，所以单次操作的复杂度为$O(\sqrt{n})$。

#### 包含整块的情况

这是本题的第二个难点。

当时智障的我：这不就散块暴力，中间直接取$ans$就行了嘛......

Wrong！

还是那个问题：我们不能保证左右端点都在（这里左右端点指“下面算法基于的技巧”中的$(i,j)$二元组）左散块或都在右散块或都在整块。

所以麻烦的来了：我们不仅要计算三个独立的块，还有以下三种情况：

- 左端点在左散块，右端点在整块

- 左端点在左散块，右端点在右散块

- 左端点在整块，右端点在右散块

不急，慢慢来。

> 以下使用$X$表示整块的第一块，用$Y$表示整块的最后一块。

1. 三个独立的部分：

左右散块像上面一样暴力，整块部分直接取$ans$。

2. 左端点在左散块，右端点在整块

我们枚举左散块的所有元素，枚举至$s_i$时，在整块中查找$s_i\oplus k$的个数加入答案，这可以利用$pre$数组轻松做到。

$\text{答案}+=\sum\limits_{p\in \text{左散块}}(pre[Y][s_p\oplus k]-pre[X-1][s_p\oplus k])$

3. 左端点在左散块，右端点在右散块

先扫一遍左散块的所有元素，记录好左散块中每个元素出现的次数，即$rec$数组。

然后枚举右散块的所有元素，枚举至$s_i$时，在左散块中查找$s_i\oplus k$的个数，即$rec[s_i\oplus k]$的值加入答案。

4. 左端点在整块，右端点在右散块

整块不好枚举，所以我们枚举右端点。其他的操作与情况2的处理方式基本相同。

$\text{答案}+=\sum\limits_{p\in \text{右散块}}(pre[Y][s_p\oplus k]-pre[X-1][s_p\oplus k])$

以上就是处理包含整块情况的查询的全部内容啦！

代码：

```cpp
int X=belong[l]+1,Y=belong[r]-1;
LL ret=0ll;
/*整块*/
ret+=ans[X][Y];
/*左散块*/
for(register int i=l;belong[l]==belong[i];i++)
	__rec[s[i]]++;
for(register int i=l;belong[l]==belong[i];i++)
	__rec[s[i]]--,ret+=__rec[s[i]^k];
/*右散块*/
for(register int i=r;belong[r]==belong[i];i--)
	__rec[s[i]]++;
for(register int i=r;belong[r]==belong[i];i--)
	__rec[s[i]]--,ret+=__rec[s[i]^k];
	
/*左散块 -> 右散块*/
for(register int i=l;belong[l]==belong[i];i++)
	__rec[s[i]]++;
for(register int i=r;belong[r]==belong[i];i--)
	ret+=__rec[s[i]^k];
for(register int i=l;belong[l]==belong[i];i++)
	__rec[s[i]]--;
	
/*左散块 -> 整块*/
for(register int i=l;belong[l]==belong[i];i++)
	ret+=pre[Y][s[i]^k]-pre[X-1][s[i]^k];
	
/*整块 -> 右散块*/
for(register int i=r;belong[r]==belong[i];i--)
	ret+=pre[Y][s[i]^k]-pre[X-1][s[i]^k];
return ret;
```

复杂度：还是取决于散块的最大长度，为$O(\sqrt{n})$

## 时空复杂度

再次注明：此处认为$n,m,k$同阶。

时间：$O(n\sqrt{n})$

空间：$O(n\sqrt{n})$（$pre$数组）

## 完整代码

```cpp
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

inline int read(){int x=0,f=1;char c=getchar();while(c<'0'||c>'9'){if(c=='-')f=-1;c=getchar();}while(c>='0'&&c<='9'){x=x*10+c-'0';c=getchar();}return f*x;}

const int N=1e5+5;
const int K=1e5+5;
const int B=150;
const int T=N/B+5;

int s[N];
int n,m;
int k;

namespace SqrtDiv
{
	typedef long long LL;
	int belong[N];
	int pre[T][K<<1];
	LL ans[T][T];
	int limits;
	int block; 
	
	inline void init()
	{
		memset(ans,0,sizeof(ans));
		memset(pre[0],0,sizeof(pre[0]));
		limits=*max_element(s,s+1+n);
		for(register int i=0,j=0;i<=n;i++)
		{
			if(i%B==0)
			{
				block=++j;
				for(register int val=0;val<=limits;val++)
					pre[j][val]=pre[j-1][val];
			}
			belong[i]=j,pre[j][s[i]]++;
		}
		for(register int i=1;i<=block;i++)
			for(register int j=(i-1)*B;j<=min(n,i*B-1);j++)
				for(register int p=j+1;p<=min(n,i*B-1);p++)
					if((s[j]^s[p])==k) ans[i][i]++;
		for(register int i=1;i<=block;i++)
			for(register int j=i+1;j<=block;j++)
			{
				ans[i][j]=ans[i][j-1]+ans[j][j];
				for(register int p=(j-1)*B;p<=min(n,j*B-1);p++)
					ans[i][j]+=pre[j-1][s[p]^k]-pre[i-1][s[p]^k];
			}
	}
	
	int __rec[K<<1];
	inline LL query(int l,int r)
	{
		LL ret=0ll;
		if(belong[r]-belong[l]<=1)
		{
			for(register int i=l;i<=r;i++)
				__rec[s[i]]++;
			for(register int i=l;i<=r;i++)
				__rec[s[i]]--,ret+=__rec[s[i]^k];
			return ret;
		}
		int X=belong[l]+1,Y=belong[r]-1;
		
		/*整块*/
		ret+=ans[X][Y];
		/*左散块*/
		for(register int i=l;belong[l]==belong[i];i++)
			__rec[s[i]]++;
		for(register int i=l;belong[l]==belong[i];i++)
			__rec[s[i]]--,ret+=__rec[s[i]^k];
		/*右散块*/
		for(register int i=r;belong[r]==belong[i];i--)
			__rec[s[i]]++;
		for(register int i=r;belong[r]==belong[i];i--)
			__rec[s[i]]--,ret+=__rec[s[i]^k];
			
		/*左散块 -> 右散块*/
		for(register int i=l;belong[l]==belong[i];i++)
			__rec[s[i]]++;
		for(register int i=r;belong[r]==belong[i];i--)
			ret+=__rec[s[i]^k];
		for(register int i=l;belong[l]==belong[i];i++)
			__rec[s[i]]--;
			
		/*左散块 -> 整块*/
		for(register int i=l;belong[l]==belong[i];i++)
			ret+=pre[Y][s[i]^k]-pre[X-1][s[i]^k];
			
		/*整块 -> 右散块*/
		for(register int i=r;belong[r]==belong[i];i--)
			ret+=pre[Y][s[i]^k]-pre[X-1][s[i]^k];
		return ret;
	}
}

signed main()
{
	n=read(),m=read(),k=read();
	for(register int a,i=1;i<=n;i++)
		a=read(),s[i]=s[i-1]^a;
	SqrtDiv::init();
	while(m--)
	{
		int l=read()-1,r=read();
		printf("%lld\n",SqrtDiv::query(l,r));
	}
	return 0;
}
```

## 注意事项

- $ans$数组记得开```long long```。

- 注意询问时要将$l$减一，预处理时从0开始。

- 虽然原数字中的元素不超过$10^5$，但是$\oplus$之后可能会超过这个值。$10^5$的二进制是```1 1000 0110 1010 0000‬```，共17位，值域应该开到$2^{18}$，也就是```1<<18```。这里直接开到了$2\times 10^5$。

- 注意暴力计算散块时，$rec[s_i]$要先减去一再加入答案。最后清空$rec$时不能草率地```memset```，因为这样时$O(n)$的复杂度会原地爆炸。应当怎么加过来，怎么减回去，具体操作上面的代码有所体现。

## 未考虑到的问题

### 块的大小，真的最好是$\sqrt{n}$吗？

有人已经发现了：上面代码中块的大小我调小了。

如果把块的大小设成$\sqrt{n}$，即$\sqrt{10^5}\approx 316$，那么只能拿到70pts：https://www.luogu.com.cn/record/30177145

这是咋回事呀？？

观察以下我们的算法，会发现预处理做的干净利落，但询问有一坨循环，虽说复杂度正确，但常数还是有点大。减少询问时间的方式就是减小块长。（效率只与块长有关的说法并不正确，因为预处理的第一步就是$\text{块的数量}\times k$，更正一下。）

因此我调小了块的大小（150），虽然空间需求大了，但是果然快了不少：https://www.luogu.com.cn/record/30185458

注：块的大小为200时开O2才可以过。

### 是否存在更高效的算法

双倍经验：[CF617E XOR and Favorite Number](https://www.luogu.com.cn/problem/CF617E)

然而这份代码过不了。。。

上面，我们假设$n,m,k$同阶，但这里不行，因为值域$k\le 10^6$。这样复杂度就是$O((m+k)\sqrt{n})$，非常的菜。而且$pre$数组也是关于值域$k$的，直接$MLE$了。

难道就只有莫队可解了吗？对此本人持怀疑的态度。如果强大的你找到了更好的分块（可以是线段树）方法，欢迎私信（或评论）。

-----------------------

### 后记

wtcl这一题调了半天。。。

码字不易，留个赞叭QwQ。

[$\colorbox{yellow}{\texttt{cnblogs:https://www.cnblogs.com/-Wallace-/}}$](https://www.cnblogs.com/-Wallace-/)

[$\colorbox{greenyellow}{\texttt{luogu blog:https://strncmp.blog.luogu.org/}}$](https://strncmp.blog.luogu.org/)