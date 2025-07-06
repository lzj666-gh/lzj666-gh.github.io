# P4195 题解

## 前言
clockwhite 写了一篇此题题解。

~~我也要写！~~

## 问题

求出使 $a^x\equiv b\pmod p$ 成立的最小 $x$，或判断方程无解。

## 解法与证明
同一般 BSGS 做法进行根号平衡，设 $t=\lceil \sqrt{2\varphi(p)} \rceil,x=pt-q(0\le q<t)$ ，考虑对原式进行变形：

$$
a^{pt-q}\equiv b\pmod {p}
$$
$$
a^{pt} \equiv ba^q\pmod p
$$

注意到两步间并非等价变形，后者是前者的必要条件。预先将 $a^{pt}(0\le p\le t)$ 的值存入散列表，之后枚举 $a^q$ 并在散列表中查询 $ba^q$ 的值是否存在。若存在，则所对应的 $pt-q$ 即为 $x$ 的一个可能值，代入原式可知是否确实能成为 $x$。

事情至此尚未解决，这是由于$a^{pt}$ 的值可能出现重复。对于重复的值，仅前两个出现的位置可能成为答案。查询时两值均进行检验即可。

时间复杂度为 $\operatorname{O}(\sqrt{\varphi(p)})$。

然后是正确性证明。

首先证明答案上界。前文设 $t=\lceil \sqrt{2\varphi(p)} \rceil$，意味着 $2\varphi(p)$ 是答案的上界。事实上确实如此。根据扩展欧拉定理 $a^{x}\equiv a^{x\bmod {\varphi(p)}+\varphi(p)}$，若 $x>2\varphi(p)$，必然有 $x\bmod {\varphi(p)}+\varphi(p)$ 是更优的答案。上界得证。

之后证明仅保留前两个相等的值的正确性。由扩展欧拉定理，形象化地说，$a^x$ 的值形成了一个 $\rho$ 形，即在经过长度不超过 $\varphi(p)$ 的非循环数后进入长度不超过 $\varphi(p)$ 的循环节。若一个值出现多次，则它的每一次出现均在循环节上。由于 $q<t$，某一个值第二次出现时对应的 $a^{p't-q}$ 必然大于第一次出现时对应的 $a^{pt}$，这意味着只有第一次出现某一个值时 $a^{pt-q}$ 才可能在非循环数中。由于在循环节中得到的答案不会产生差异，取前两次必定能考虑到答案的所有情况。

## 代码
update: 再加快读即可通过，懒得加了。希望以后不会再有这么无聊的 hack。

加强数据后已通过。

先取模再跑即可。
```cpp
#include<algorithm>
#include<cmath>
#include<cstdio>
#include<cstring>
using namespace std;
const long long maxn=1e5,mod=1145141,inf=0xffffffffffffffll;
long long base,rest,prime,baby[maxn+1],giant[maxn+1],key[mod],comment[2][mod],stk[mod<<1|1];
long long Hash(long long value)
{
	long long now=value*value%mod;
	while(key[now]&&key[now]!=value)
		now=(now+1)%mod;
	if(!key[now])
		stk[++stk[0]]=now;
	key[now]=value;
	return now;
}
long long phi(long long x)
{
	long long res=x;
	for(long long i=2;i*i<=x;++i)
		if(x%i==0)
		{
			res=res/i*(i-1);
			while(x%i==0)
				x/=i;
		}
	if(x>1)
		res=res/x*(x-1);
	return res;
}
long long exBSGS(void)
{
	long long res=inf,block=ceil(sqrt(2*phi(prime)));
	baby[0]=1;
	for(long long i=1;i<=block;++i)
		baby[i]=baby[i-1]*base%prime;
	comment[0][Hash(1)]=0;
	giant[0]=1;
	for(long long i=1;i<=block;++i)
	{
		giant[i]=giant[i-1]*baby[block]%prime;
		long long now=Hash(giant[i]);
		if(!comment[0][now])
			comment[0][now]=i;
		else if(!comment[1][now])
			comment[1][now]=i;
	}
	for(long long i=0;i<=block;++i)
	{
		long long now=Hash(rest*baby[i]%prime),t0=comment[0][now],t1=comment[1][now];
		if(t0&&giant[t0-1]*baby[block-i]%prime==rest)
			res=min(res,t0*block-i);
		else if(t1&&giant[t1-1]*baby[block-i]%prime==rest)
			res=min(res,t1*block-i);
	}
	return res;
}
signed main()
{
	while(scanf("%lld%lld%lld",&base,&prime,&rest)!=EOF)
	{
		while(stk[0])
		{
			key[stk[stk[0]]]=comment[0][stk[stk[0]]]=comment[1][stk[stk[0]]]=0;
			--stk[0];
		}
		if(!prime&&!base&&!rest)
			break;
		base%=prime;
		rest%=prime;
		long long res=exBSGS();
		if(res==inf)
			puts("No Solution");
		else printf("%lld\n",res);
	}
	return 0;
}
```

