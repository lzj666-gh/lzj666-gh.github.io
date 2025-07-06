# P2831 题解

### upd on 2019.1.29：

感谢@老QB 和@小梁 的提醒，似乎数组是得开大一点……

表示很抱歉，现在才看到这条消息……

---
### 前言：
我好像在已有的题解中看到的都是 $O(T\text{玄学})$ 的暴搜和 $O(Tn^22^n)$ 的状压。

暴搜如果数据强一点就过不了了，$O(Tn^22^n)$ 的状压在考场也只有75分。

在此发一篇严格 $O(Tn2^n)$ 的完全严谨正解。

（感谢[这篇博客](https://www.cnblogs.com/Sakits/p/6440722.html)让我会了这种状压）

---
### 设计dp状态：
$n\le 18$？不是暴搜就是状压。

$dp[S]$ 表示已经死了的猪的集合状态为 $S$ 时最少要发射的鸟数。

明显有
- $dp[0]=0$
- $dp[S|line[i][j]]=\min(dp[S]+1)$
- $dp[S|(1<<(i-1)]=\min(dp[S]+1)$


其中 $line[i][j]$ 表示经过 $i,j$ 两点的抛物线能经过的所有点的集合。

这就是网上大多流传的 $O(Tn^22^n)$ 算法。优化？

---
### 优化1：
发现当 $i\in S$ 或者 $j\in S$ 时**没有必要转移**。

证明：
- 若这条线只经过至多三个点，因为其中一个点已被打到，所以可以通过另外两个点的状态转移。如果 $i,j$ 都被打到，则可以通过转移3（单独一个点）转移。
- 若这条线经过多于三个点，则可以通过其它任选两个点转移。

但是这只能算是常数优化。

---
### 优化2：
若令 $x$ 为满足 $S\&(1<<(x-1))=0$ 的最小正整数，则由 $S$ 扩展的转移的**所有线都要经过 $x$。**

为什么？这个是对的吗？不经过 $x$ 就会慢吗？

你想一想，先打 $1,4$，再打 $2,3$，和先打 $2,3$，再打 $1,4$ 是不是一样的？

如果这一次转移不打 $x$，那以后还要再回过头来打 $x$。这就是多余的转移。

因为经过 $x$ 的线数量是 $n$，所以每次转移涉及到的线就从 $n^2$ 变成了 $n$。

只要预处理一下 $0-2^{18}$ 的对应的 $x$ 就能做到 $O(Tn2^n)$ 了，这才是考场的正解。

似乎比暴搜还快一点~

---
### 代码
```cpp
#include<bits/stdc++.h>
using namespace std;
const double eps=1e-8;
int t,n,m,lines[20][20],lowunbit[1<<20],dp[1<<20];	//lowunbit就是题解中的x
double x[20],y[20];
void equation(double &x,double &y,double a1,double b1,double c1,double a2,double b2,double c2){	//解方程
	y=(a1*c2-a2*c1)/(a1*b2-a2*b1);
	x=(c1-b1*y)/a1;
}
int main(){
	for(int i=0;i<(1<<18);i++){	//预处理lowunbit
		int j=1;
		for(;j<=18 && i&(1<<(j-1));j++);
		lowunbit[i]=j;
	}
	scanf("%d",&t);
	while(t--){
		memset(lines,0,sizeof(lines));	//各种初始化
		memset(dp,0x3f,sizeof(dp));
		dp[0]=0;
		scanf("%d%d",&n,&m);
		for(int i=1;i<=n;i++) scanf("%lf%lf",x+i,y+i);
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++){	//处理所有抛物线
				if(fabs(x[i]-x[j])<eps) continue;	//x坐标相同，不可能有解
				double a,b;
				equation(a,b,x[i]*x[i],x[i],y[i],x[j]*x[j],x[j],y[j]);
				if(a>-eps) continue;	//解出a和b
				for(int k=1;k<=n;k++)
					if(fabs(a*x[k]*x[k]+b*x[k]-y[k])<eps) lines[i][j]|=(1<<(k-1));
			}
		for(int i=0;i<(1<<n);i++){	//重点！状压开始！
			int j=lowunbit[i];	//必须经过lowunbit这个点
			dp[i|(1<<(j-1))]=min(dp[i|(1<<(j-1))],dp[i]+1);	//单独转移
			for(int k=1;k<=n;k++) dp[i|lines[j][k]]=min(dp[i|lines[j][k]],dp[i]+1);	//所有经过lowunbit的抛物线
		}
		printf("%d\n",dp[(1<<n)-1]);	//答案
	}
}
```