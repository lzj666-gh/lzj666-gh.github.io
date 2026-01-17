# P4316 题解

## 题解 P4316 【绿豆蛙的归宿】

题目传送门：

https://www.luogu.org/problemnew/show/P2801

这题是道**期望dp经典模型**~~（水积分题）~~

可能这是我做过的第二道比较正经的期望题了。。。

但是个人感觉。。。好像做的顺序不太对？

这题看完了可以去看看这题：

[luogu p1850 换教室](https://www.luogu.org/problemnew/show/P1850)

（也是一道期望dp~~毒瘤~~题）

=========================================================

上面都是没什么用的。。。下面才是正题

一看这题。。。肯定是个**DAG**（别问我怎么看出来的QWQ）

根据题目要求，我们很自然的可以想到：

**设状态$f[x]$表示点x到终点n的期望路径总长**

显然，要求的**答案为f[1]**,**而且有$f[n]=0$**

（终点到自己的期望距离肯定为0啊。。。）

发现这时就是期望dp的套路了。。。

正好要将期望dp，不妨我们先来说说**期望dp的具体~~sao~~操作**

**期望dp，也加概率dp**

一般来说，期望dp找到正确的状态后，转移是比较容易想到的。

但一般情况下，**状态一定是“可数”的**

事实上，**将问题直接作为dp的状态**是最好的。

如，问**“n人做XX事的期望次数”**，那么不妨设计**状态为f[i]表示i个人做完事的期望**。

**转移一般是递推**，通常分两种，一种是从上一个状态转移得（填表法），另一种是转移向下一个状态（刷表法）。

有时期望dp需以最终状态为初始状态转移，即**逆推**。

如f[i]表示期望还要走f[i]步到达终点。这种状态的转移是**刷表法**

形如$f[i]=∑p[i→j]*f[j]+w[i→j]$，其中**p表示转移的概率**，**w表示转移对答案的贡献**。

一般来说，**初始状态确定时可用顺推，终止状态确定时可用逆推。**

大概期望dp的套路就是这样了吧。。。~~（我还是菜讲得不太好）~~

现在我们回到本题

上面提到了，我们**设状态f[x]表示点x到终点n的期望路径总长**，那么显然有f[n]=0

那么这正好符合了**“终止状态确定时可用逆推”**的策略~~套路~~

具体来说：

对于一条有向边,我们假设它由 $x->y$

那么有$f[x]=(\dfrac{1}{degree[x]})*∑f[y]+w[x->y]$

其中$degree[x]$表示x点的度（结合一下上面给出的式子你就懂了）

仔细观察题目其实你会发现,  $(\dfrac{1}{degree[x]})$其实就是概率(p)

同时又有一个问题，那就是**转移时的过程怎么实现**

不妨这样想：既然是个DAG，那么我们可以“倒过来”想

具体来讲，我们反向连边，进行一遍拓扑排序，在拓扑排序的时候进行期望dp的转移

这时候要注意上面的x和y要反过来（因为我们反向连边了）

那么我们转移方程就设计完啦

~~（其实还是挺好理解的是不是）（逃~~

**分析一下复杂度**

dp转移是与拓扑排序有关的，每次计算几乎是$O(1)$的

那么时间复杂度瓶颈就是拓扑排序，故时间复杂度为$O(n+m)$

下面放代码吧

PS：代码里也有解释

```cpp
#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<queue>
#include<cstring>
using namespace std;
typedef long long ll;
const int inf=1e9+7;
inline int read()//读优
{
    int p=0,f=1;char c=getchar();
    while(c<'0'||c>'9'){if(c=='-')f=-1;c=getchar();}
    while(c>='0'&&c<='9'){p=p*10+c-'0';c=getchar();}
    return f*p;}
const int maxn=100003;
const int maxm=200003;
struct Edge
{
	int from,to,w;
}p[maxm];
int n,m,cnt,head[maxm],in[maxn],dg[maxn];
double f[maxn];//f[x]表示x点到终点n的期望路径总长 
inline void add_edge(int x,int y,int W)//加边
{
	cnt++;
	p[cnt].from=head[x];
	head[x]=cnt;
	p[cnt].to=y;
	p[cnt].w=W;
}
inline void toposort()//拓扑排序
{
	queue <int> q;
	q.push(n);
	while(!q.empty())
		{
			int x=q.front();
			q.pop();
			for(int i=head[x];i;i=p[i].from)
				{
					int y=p[i].to;
					f[y]+=(f[x]+p[i].w)/dg[y];//dp转移 
					if(!(--in[y]))q.push(y);
				}
		}
}
int main()
{
	/*这是我做这题的时候写的QAQ
	分析:不妨设f[x]表示x点到终点的期望路径总长度
	显然有f[n]=0
	那么对于一条有向边,连接着x和y点(x->y)
	那么显然有f[x]=sigma(f[y]+w[i])/degree[x] 
	其中degree[x]表示x点的出度,w[i]表示这条边的边权 
	那么假设我们已经知道了f[y]
	我们就可以反推f[x]
	显然只需要反向建边之后跑个拓扑排序就行了
	那么最后答案即为f[1]
	时间复杂度O(n+m) 
	*/
	n=read(),m=read();
	for(int i=1;i<=m;i++)
		{
			int x=read(),y=read(),w=read();
			add_edge(y,x,w);//反向建图 
			in[x]++,dg[x]++;
		}
	toposort();
	printf("%.2lf\n",f[1]);
	return 0;
}
```
这题就算讲完了吧。。。

本人思维比较跳跃，可能写的不是太好，请见谅

感谢你的阅读！

最后~~无耻的~~推一波我的blog：

https://www.luogu.org/blog/new2zy/

拜拜~~~
















