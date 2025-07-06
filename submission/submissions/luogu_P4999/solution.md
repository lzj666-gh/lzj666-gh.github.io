# P4999 题解

数位 dp。

设 $dp_{q,i}$（$i\in\{0,1,2,3,4,5,6,7,8,9\}$）为 $1\sim q$ 中 $i$ 出现的次数，$1\sim q$ 的数字和显然就是 $dp_{q,0}\times 0+dp_{q,1}\times 1+\cdots+dp_{q,i}\times i\cdots+dp_{q,9}\times 9$。

所以我们只需要求出 $1\sim q$ 中 $i$ 出现的次数就能解决这个问题了。

这个问题看起来很好解决，但是注意**前导零会影响结果**，所以不能有前导零。

这该怎么办呢？

有前导零的式子很容易推出。有 $q$ 位数字，$i$ 数码的出现次数对于 $x\in\{s\mid s\in \mathbb N,10^q\le s\le10^{q+1}\}$ ，$f(q,i)$ 的数量都是相等的（设 $f(q,i)$ 为 $q$ 位数 $i$ 数码的出现次数）。

具体求法罢，是：  
$\begin{cases}f(q,i)=0&q=0\\f(q,i)=10f(q-1)+10^{q-1}&q>0\end{cases}$

我们考虑减去多余的 $0$。

我们先设数字为 $\overline{A_1A_2A_3\dots A_n}$

我们首先考虑求 $\overline{A_100\dots 0}$，将 $\overline{A_100\dots 0}$ 分割为区间 $[0000,1000),[1000,2000),\dots,[\overline{(A_1-1)00\dots 0},\overline{A_100\dots 0})$，所以答案就为 $10^{n-1}A_1$，注意 $<A_1$ 的每个数还出现了 $10^{n-1}$ 次，所以要加上。

首位 $A_1$ 出现了 $\overline{A_2A_3\dots A_n}+1$ 次，答案还要加上 $\overline{A_2A_3\dots A_n}+1$，

当然还需要处理前导 $0$，用排列组合算一下会知道 $i$ 位 $q$ 个前导零的数量就是 $10^q$（$q\in\{s\mid s\in\mathbb N,0\le s\le i-1\}$），把它们加起来会发现一共出现了 $10^{i-1}+10^{i-2}+...10$（$\sum\limits_{k=0}^{i-1}10^k$） 次，减一下即可。

Code:
```cpp
#include<iostream>
#include<cstring>
using namespace std;
typedef long long ll;
const int N=51,MOD=1e9+7; //注意能 MOD 的地方都要 MOD，不然会 WA 0pts。
ll pow10[N],dp[N],a[N],count[N],tmpcount[N],ans;
// pow10    : 字面意思，10^n
// dp       : 不考虑前导零的状况
// count    : 统计 0~9 出现次数
// tmpcount : 暂时保存 count，用来减
// ans      : 累加答案
void init() //预处理 pow10 和 dp。
{
	pow10[0]=1;
	for (int i=1;i<30;i++) dp[i]=(dp[i-1]*10%MOD+pow10[i-1])%MOD,pow10[i]=10*pow10[i-1]%MOD;
}
void solve(ll x)
{
	int len=0;
	while (x){a[++len]=x%10;x/=10;} //数位分离
	for (int i=len;i>=1;i--)        //从高到低遍历
	{
		for (int j=0;j<10;j++) count[j]+=dp[i-1]*a[i],count[j]%=MOD;  //分割区间
		for (int j=0;j<a[i];j++) count[j]+=pow10[i-1],count[j]%=MOD; //加上 10^(n-1)
		ll lastnum=0;
		for (int j=i-1;j>=1;j--) lastnum=lastnum*10+a[j],lastnum%=MOD; //求出 A2A3A4...An
		count[a[i]]+=lastnum+1,count[a[i]]%=MOD;
		count[0]-=pow10[i-1],count[0]=(count[0]+MOD)%MOD; //减去前导零
	}
}
int main()
{
	init();
	ll l,r,T;
	cin>>T;
	for (int q=0;q<T;q++)
	{
		ans=0; cin>>l>>r;
		solve(r); //前缀和思想相减 r 和 l-1。
		for (int i=0;i<10;i++) (tmpcount[i]=count[i]),count[i]=0; //复制 count，记得清零
		solve(l-1);
		for (int i=0;i<10;i++) ans=(ans+i*(tmpcount[i]-count[i]+MOD)%MOD)%MOD,count[i]=0; //累加答案，记得清零 count。
		cout<<ans<<'\n';
	}
	return 0;
}
```

Refence [求数字 $i$ 出现的次数](https://www.luogu.com.cn/blog/mak2333/solution-p2602)。