# P1455 题解

[题面](https://www.luogu.com.cn/problem/P1455)~~(卖云朵的怕不是个骗子)~~

[博客内食用更佳](https://flysong.blog.luogu.org/solution-p1455)。

我的第一印象：**01背包**。

### 问：什么是01背包?
答：一种~~背包~~动态规划题目。

追问：什么是动态规划?

追答：你不知道动态规划你干嘛做这题?请先康康[这位老兄的博客](https://www.cnblogs.com/zyacmer/p/9961710.html)。

$WA$ $Code(+30)$
```cpp
for(int i=1;i<=n;i++)//DP
{
	for(int v=w;v>=c[i];v--)
	{
	   f[v]=max(f[v],f[v-c[i]]+d[i]);
	}
}
cout<<f[w]

```

错误原因：~~(事情并不这么简单)~~没有读题。

“一些云朵要搭配起来买才卖，也就是说买一朵云则与这朵云有搭配的云都要买”

	       --商店老板

商店老板告诉我们买一朵云则与这朵云有搭配的云都要买。由此，我们可以想到另一个算法：**并查集**。

### 问：什么是并查集?

答：一种图论算法。

追问：详细一点。

追答：并查集可以快速的判断两个点是否连通。

原理：并查集将一个点作为与这个点连通的所有点的代表。判断两个是否连通，只需要判断他们的代表是否一样。举个栗子：如下图，设有3个询问：

![](https://s2.ax1x.com/2020/01/20/1PvRCd.png)

~~(不要嫌弃图丑)~~

+ $a$与$b$是否连通?
+ $c$与$e$是否连通?
+ $e$与$f$是否连通?

我们暂且现将$a$、$e$作为与他们连通的所有点的代表。

先看第一个询问：

#### d与b是否连通?

我们观察上图，可以发现$d$的代表为$a$，$b$的代表为$a$。因此，$d$与$b$连通。

再看第二个询问：

#### c与e是否连通?

我们观察上图，可以发现$c$的代表为$a$，$e$的代表为$e$。因此，$c$与$e$不连通。

最后再看第三个询问：

#### e与f是否连通?

我们观察上图，可以发现$e$的代表为$e$，$f$的代表为$e$。因此，$e$与$f$连通。

通过上面三个询问，我们就可以知道并查集判断两个点是否连通的方法。

接下来我们再举个栗子：

我们已知$a$与$b$连通，$b$与$c$连通，$d$与$c$连通，问$a$是否与$d$连通？

我们暂且先把前一个节点作为后一个节点的代表。

第一次，我们知道$a$与$b$连通，那么，$a$为$b$的代表。第二次，我们知道$b$与$c$连通，那么，我们设$b$为$c$的代表。第三次，我们知道$d$与$c$连通，那么，我们设$d$为$c$的代表……

似乎有点不对劲？

事实上，我们已经设$b$为$c$的代表了，不能再设$d$为$c$的代表了。

那么，我们如果把$d$设为$c$的代表的代表。事情不就好办了？

通过这一个栗子，我们就可以知道如何用程序合并两个集合。

但是，$c$的代表$b$也有代表了。

那么，我们再往上找。$b$的代表是$a$,那么，我们就把$a$的代表设为$d$。

根据上面这个栗子，我们就可以写出一个基本的并查集。

但是，如果并查集的长度过长：

![](https://s2.ax1x.com/2020/01/20/1iFRPK.png)

就会翻车。

那么，我们就要使用路径压缩。

我们在找$7$的终极代表的过程中把途中经过的所有点的代表都设为$7$的终极代表。那么，这个并查集就成了这个亚子：

![](https://s2.ax1x.com/2020/01/20/1iFW8O.png)

至此，我们已经掌握了并查集………………的一部分。对付这道题够用了。

我们只需把并查集与01背包一结合：

我们就得到了AC代码：

$AC$ $Code$
```cpp
#include<bits/stdc++.h>
using namespace std;

inline int read()//快读
{
	int num=0,f=1;
	char ch=getchar();

	while(!isalnum(ch))
	{
		if(ch=='-')
		{
			f=-1;
		}
		ch=getchar();
	}
	while(isalnum(ch))
	{
		num=num*10+(ch-'0');
		ch=getchar();
	}
	return num*f;
}

int father[10001];//并查集数组

int find(int x)//并查集函数
{
	if(father[x]==x)
	{
		return x;
	}
	return father[x]=find(father[x]);
}

int c[10001],d[10001],f[10001];//DP数组

int main()
{
	int n=read(),m=read(),w=read();
	for(int i=1;i<=n;i++)//初始化并查集
	{
		father[i]=i;
	}
	for(int i=1;i<=n;i++)
	{
		c[i]=read();
		d[i]=read();
	}

	int x,y;
	for(int i=1;i<=m;i++)//并查集
	{
		x=read(),y=read();
		father[find(x)]=find(y);
	}

	for(int i=1;i<=n;i++)//将同集合的云朵的价钱与价值都划到一个云朵里
	{
		if(father[i]!=i)
		{
			d[find(i)]+=d[i];
			d[i]=0;
			c[find(i)]+=c[i];
			c[i]=0;
		}
	}

	for(int i=1;i<=n;i++)//DP
	{
	    for(int v=w;v>=c[i];v--)
	    {
	    	f[v]=max(f[v],f[v-c[i]]+d[i]);
		}
	}
	cout<<f[w];
	return 0;
}

```
麻烦点个免费的赞再走呀。