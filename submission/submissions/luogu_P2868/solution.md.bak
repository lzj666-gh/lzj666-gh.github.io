# P2868 题解

题解里似乎都没有提到这么一种情况，如果环里经过一个点两次（去一次，回来一次），点的`fi`只会被计算一次，但是如果按照题解里的算法的话，这个点的`fi`会被计算两次。

如果一个点被计算两次的话，分子上的东西就比分母上的东西少，以下推导都没法进行。

（这个bug让我在模拟赛里面不敢写0/1规划算法，最后此题0分QwQ

现在就要证明，如果环上的比率最优，则必然不会有一个点被经过两次。

首先，如果一个环经过一个点两次，则必然可以通过那个点（设为$P_x$）分成两个没有相交点的环。方便起见，设两个环的快乐值总和分别为$F_1$和$F_2$，用时总和分别为$T_1$和$T_2$，x点的快乐值为$F_x$

我们的目标就是证明：

$$\frac{F_1}{T_1}\geq\frac{F_1+F_2-F_x}{T_1+T_2}\space\space\space or\space\space\space\frac{F_2}{T_2}\geq\frac{F_1+F_2-F_x}{T_1+T_2}$$

由于右式含有`T1+T2`作为分母，因此就可以考虑将两环求平均数。即，只需要证明：

$$\frac{F_1}{2\times T_1}+\frac{F_2}{2\times T_2} \geq \frac{F_1+F_2-F_x}{T_1+T_2}$$

$$\frac{F_1T_2+F_2T_1}{2(T_1+T_2)}\geq\frac{F_1+F_2-F_x}{T_1+T_2}$$

因为我们分的两个都是环，至少要经过两条边，同时题目保证$T_i\geq1$，所以可以得出$T_1\geq2$且$T_2\geq2$。

因此，可得：

$$\frac{F_1T_2+F_2T_1}{2(T_1+T_2)}\geq\frac{F_1+F_2}{T_1+T_2}> \frac{F_1+F_2-F_x}{T_1+T_2}$$

Q.E.D.

因此，我们可以得出，该算法只适用于$T_i\geq1$的题目，如果允许边权等于0或者为小于1的小数的话，就得另找算法。

（很有可能是爆搜了QwQ）

其他部分题解的各位神仙已经讲得很清楚了，为了内容的完整性，还是写完吧QwQ。

首先，原题可以转化为，求一个环，使得$\frac{\sum F_i}{\sum T_i}$最小。由于上面花了几行证明上下齐项，可以应用0/1分数规划。

对于0/1分数规划，考虑二分。二分可将一个最优化问题转化为一个判定问题。如果二分出来的`mid`为$L$，则问题就转化为是否存在一个$\frac{\sum F_i}{\sum T_i}> L$

分数乘过去（保证$T_i>0$），减回来，得：

$$\sum(F_i-L\times T_i) > 0$$

由于左式不好搞，考虑变换。如果将左式乘以-1，原式变为：

$$\sum(L\times T_i-F_i)>0$$

既然所有边成一个环，那不就是一个负环的方程嘛？？

于是算法就出来了，先二分答案，然后对于一个`mid`，将边权变为边权乘`mid`再减去一个端点的`F[i]`（随便入端点还是出端点，反正是个环），最后`stacked spfa`找负环判定。

附AC代码：

```cpp
#include <stack>
#include <cmath>
#include <cstdio>
using namespace std;

inline double lfabs(double x)
{
	return x<0?-x:x;
}

int beg[1005];
int ed[5005];
int nxt[5005];
int len[5005];
int top;

void addedge(int a,int b,int c)
{
	++top;
	ed[top] = b;
	len[top] = c;
	nxt[top] = beg[a];
	beg[a] = top;
}
int n;
int fi[5005];
int inq[5005];
int inqn[5005];
double dist[5005];

bool spfa(int s,double delta)
{
	dist[s] = 0;
	inq[s] = 0;
	
	stack<int> stk;
	stk.push(s);
	
	while(!stk.empty())
	{
		int th = stk.top();
		stk.pop();
		inq[th] = 0;
		
		for(int p=beg[th]; p; p=nxt[p])
		{
			if(dist[th] + (delta*len[p]-fi[th]) < dist[ed[p]])
			{
				dist[ed[p]] = dist[th] + (delta*len[p]-fi[th]);
				
				if(!inq[ed[p]])
				{
					stk.push(ed[p]);
					++inqn[ed[p]];
					inq[ed[p]] = 1;
					
					if(inqn[ed[p]] > n+10)
					{
						return true;
					}
				}
			}
		}
	}
	
	return false;
}

int main()
{
	int p;
	scanf("%d%d",&n,&p);
	for(int i=1; i<=n; ++i)
	{
		scanf("%d",fi+i);
	}
	for(int i=1; i<=p; ++i)
	{
		int a,b,t;
		scanf("%d%d%d",&a,&b,&t);
		addedge(a,b,t);
	}
	
	double l = 0;
	double r = 1005;
	while(lfabs(r-l) >= 0.0001)
	{
		double mid = (l+r)/2;
		
		for(int i=1; i<=n; ++i)
		{
			dist[i] = 99999999;
			inq[i] = inqn[i] = 0;
		}
		
		for(int i=1; i<=n; ++i)
		{
			if(!inqn[i])
			{
				if(spfa(i,mid))
				{
					l = mid;
					goto die;
				}
			}
		}
		
		r = mid;
		
		die:;
	}
	
	printf("%.2lf",l+0.00005);
}
```