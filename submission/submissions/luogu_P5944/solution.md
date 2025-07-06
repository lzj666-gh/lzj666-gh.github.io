# P5944 题解

Update：更正代码，修复几个锅。

知道每个人是第几个出圈的作用不大，不如转化为出圈序列。

不难发现，假如当前圈内剩余人数为 $L$，某个人第一次报的数为 $a$，这个人的所有报数均形如 $a+xL$。那么某个人出圈等价于 $a+xL=k$，即 $k\equiv a\pmod L$。

不难发现 $a$ 就是上一个出圈的人到他的距离，暴力找即可。

问题等价于解同余方程组 $\begin{cases}k\equiv a_1\pmod n\\k\equiv a_2\pmod {n-1}\\ \ldots\\k\equiv 0\pmod 1\end{cases}$。

直接 excrt 即可，无解即某次合并时无解。

需要注意的是最后可能会合并出 $k\equiv 0\pmod x$，但显然 $k\ge 1$，因此此时答案为模数 $x$。

```cpp
#include<cstdio>
int cq[31];
int n,ys[31],ms[31];
bool td[31];
long long gcd(long long x,long long y){
	return x%y==0?y:gcd(y,x%y);
}
void exgcd(long long a,long long b,long long &x,long long &y){
	if(!b){
		x=1;y=0;
		return;
	}
	exgcd(b,a%b,x,y);
	long long z=x;
	x=y;
	y=z-a/b*y;
}
int main(){
	int i;
	scanf("%d",&n);
	int p=0,x;
	for(i=1;i<=n;i++){
		scanf("%d",&x);
		cq[x]=i;
	}//cq 存储出圈序列 
	for(i=1;i<=n;i++){
		int ds=0;
		x=cq[i];
		while(p!=x){
			p++;if(p>n)p=1;
			if(!td[p])ds++;
		}
		ms[i]=n-i+1;
		ys[i]=ds%ms[i];
		td[x]=1;
	}
	long long res=ys[1],mod=ms[1];//excrt 流程
	for(i=2;i<=n;i++){
		long long a=mod,b=ms[i],t=((ys[i]-res)%b+b)%b;
		long long x,y,r=gcd(a,b);
		if(t%r)return printf("NIE"),0;
		a/=r;b/=r;t/=r;
		exgcd(a,b,x,y);
		x=x%ms[i]*t%ms[i];
		res+=x*mod;
		mod*=b;
		res=(res+mod)%mod;
	}
	if(!res)res+=mod;
	printf("%lld",res);
}
```