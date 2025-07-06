# P6076 题解

ps:感觉容斥对初学者而言很玄学（至少本人刚开始接触时是这样...），所以想写一篇题解，仔细分析容斥到底如何运用到题目中。


### 容斥

* 容斥解决的是满足多个条件的方案数的问题，这里可以把每个条件转化为集合（如果对集合的运算还不是很了解的同学，可以先了解集合的基本运算，这会对容斥的理解帮助很大），例：

  * $|U|$：所有情况的方案数
  * $S_i$：满足条件$i$的方案数
  * $   \begin{aligned} \left|\bigcup_{i=1}^{n}S_i\right|\end{aligned} $：满足任一一个条件的方案数
  * $ \begin{aligned} \left|\bigcap_{i=1}^{n}S_{i}\right|\end{aligned} $：全部条件都满足的方案数

* 容斥的核心思想是对“至少(至多)”和“恰好（一般是）”之间的转换，重点是弄清楚**哪种方案数容易求**，相关的式子如下：

  * $\begin{aligned} \left|\bigcup_{i=1}^{n}S_i\right|=\sum_{m=1}^n(-1)^{m-1}\sum_{a_i<a_{i+1} }\left|\bigcap_{i=1}^mS_{a_i}\right| \end{aligned}$
  * $  \begin{aligned}\left|\bigcap_{i=1}^{n}S_i\right|=|U|-\left|\bigcup_{i=1}^n\overline{S_i}\right|  \end{aligned}$
  

* 问题描述：

  > 一个$n\times m$的棋盘，用$c$种颜色染色，求满足条件的方案数
  > - 棋盘的每一个小方格既可以染色（染成$c$种颜色中的一种），也可以不染色。
  > - 棋盘的每一行至少有一个小方格被染色。
  > - 棋盘的每一列至少有一个小方格被染色。
  > - 每种颜色都在棋盘上出现至少一次。

  * 看上去很难，既要考虑颜色，又要考虑每一行，每一列，感觉特别不可做...
  * 我们先将颜色单独考虑。
  * 发现“出现至少一次”可以看成每种颜色都要用，即$ \begin{aligned} \left|\bigcap_{i=1}^{n}S_{i}\right|\end{aligned} $，而我们发现如果有某几种颜色不用，其它颜色不考虑用不用的方法好像很好求（（其它颜色数+1）^要填的格子数），即$ \begin{aligned} \left|\bigcap_{i=1}^{n}\overline{S_{i}}\right|\end{aligned} $。通过式子一和式子二共同转化，$  \begin{aligned}\left|\bigcap_{i=1}^{n}S_i\right|=|U|-\left|\bigcup_{i=1}^n\overline{S_i}\right|  =|U|- \sum_{m=1}^n(-1)^{m-1}\sum_{a_i<a_{i+1} }\left|\bigcap_{i=1}^mS_{a_i}\right|  \end{aligned} $
  * $ \begin{aligned} \sum_{a_i<a_{i+1} }\left|\bigcap_{i=1}^m\overline{S_{a_i}}\right| \end{aligned} $的意义是**所有组**$m$个颜色不用的方案数，组数就是$c$种颜色中选$m$种颜色，即$ \binom{C}{m}$组，为了表述方便，我们设$f[i]$表示在棋盘上用最多用$i$种颜色满足要求一、二的方案数（这个待会去求），而一组的答案就为$f[c-m]$，与组数相乘即可，而全集是$f[c]$（最多用$c$种颜色就是所有情况）。所以答案为$ans=f[c]-\sum_{i=1}^{c}f[c-i]*\binom{c}{i}*(-1)^{i-1}$
  * 类似的，计算$f[i]$的时候所要考虑的要求一、二，也可以通过上面的容斥分析得到。还是通过上面的式子转化，不过此时的$ \begin{aligned} \sum_{a_j<a_{j+1} }\left|\bigcap_{j=1}^k\overline{S_{a_j}}\right| \end{aligned} $就是**所有组**$k$列完全不涂色的方案数，一组的答案这么统计：对每一行单独考虑，答案数为$(i+1)^{m-k}$，可是一行不能全为空，就要减去一，$n$行都是独立的，相乘就是$((i+1)^{m-k}-1)^n$。这里全集就是当$k=0$时的值（0列完全不涂色就是所有的情况），所以$f[i]=((i+1)^m-1)^{n}-\sum_{k=1}^{m}*\binom{m}{k}*((i+1)^k-1)^n*(-1)^{k-1}$
  * 综合起来就可以了。
* 代码：
```cpp
#include<bits/stdc++.h>
#define ll long long
using namespace std;
const ll mod=1e9+7;
ll n,m,c,f[410],C[410][410];
ll ksm(ll x,int y){
	ll ans=1;
	while(y){
		if(y&1)ans=ans*x%mod;
		x=x*x%mod,y=y>>1;
	}
	return ans;
}
int main(){
	cin>>n>>m>>c;
	for(int i=0;i<=400;i++){
		C[i][0]=1;
		for(int j=1;j<=i;j++){
			C[i][j]=(C[i-1][j-1]+C[i-1][j])%mod;
		}
	}
	for(ll i=1;i<=c;i++){
		ll st=0,k=1;
		for(int j=m;j>=1;j--,k=k*(i+1)%mod){
			if(j&1)
				st=(st+ksm(k-1,n)*C[m][j])%mod;
			else
				st=(st-ksm(k-1,n)*C[m][j]%mod+mod)%mod;
		}
		f[i]=(ksm(ksm(i+1,m)-1,n)-st+mod)%mod;
	}
	ll ans=f[c],an1=0;
	for(int i=1;i<=c;i++){
		if(i&1)
			an1=(an1+f[c-i]*C[c][i])%mod;
		else
			an1=(an1-f[c-i]*C[c][i]%mod+mod)%mod;
	}
	cout<<(ans-an1+mod)%mod;
	return 0;
}

```
