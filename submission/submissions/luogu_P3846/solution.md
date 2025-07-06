# P3846 题解

这道题的数据范围很友好（$p<2^{31}$），可以直接使用 `Baby Step Giant Step` ~~水~~过。然而，如果数据加强到 $p\leq 10^{18}$ ，我们也可以通过它。

这篇题解讲述的是如何使用优化后的 `Pohlig-Hellman` 通过本题。

为了达成这一点，下面的优化算法含有以下前置知识（如果你有哪一个前置知识不理解，那么请事先查看有关知识）

+ `Miller-Rabin`

+ `Pollard-Rho`

+ `Excrt`

+ `Baby Step Giant Step`

+ `Exgcd`

+ 一般的 `DLP` 算法

我们先从阶讲起：

设 $a,p\in z,\gcd(a,p)=1$，使 $a^n\equiv 1\pmod p$ 成立的最小正整数 $n$ 称为 $a$ 模 $p$ 的阶，记作 $ord_p(a)=n$

设 $ord(a)=n=\prod^m_{i=1}q^{k_i}_i$。

令 $r_i=\dfrac{n}{q_i^{k^i}}$，由 $a^x\equiv b\pmod p,(a^x)^{r_i}\equiv b^{r_i}\pmod p$。

显然，$ord(a^{r_i})^x=q_i^{k_i}$，$(a^{r_i})^x\equiv b^{r_i}\pmod p$。

设 $(a^{r_i})^x\equiv b^{r_i}\pmod p$ 的解为 $x_i$，则原问题的解 $x$ 满足 $x\equiv x_i\pmod{q_i^{k_i}}$

若能求出这 $m$ 个 $q^k$ 阶的 `DLP`，则可以进一步通过 `CRT` 进行合并求解。

设 $ord(a)=q^k$，其中 $q$ 为一个质数。

显然有 $0\leq x<q^k$，设：

$x=x_0+x_1q+x_2q^2+\cdots+x_{k-1}q^{k-1},0\leq x_i<q$
                                                    
则有：

$(a^x)^{q^{k-1}}=(a^{x_0+x_1q+x_2q^2+\cdots+x_{k-1}q^{k-1}})^{q^{k-1}}\equiv a^{x_0q^{k-1}}\equiv (a^{q^{k-1}})^{x_0}\equiv b^{q^{k-1}}\pmod p$


所以 $ord(a^{q^{k-1}})=q$。

这样我们就能通过求解一个 $q$ 阶的 `DLP` 得到 $x_0$ 的值。

得出 $x_0$ 后，我们可以用类似的方法解出：

$(a^x)^{q^{k-2}}=(a^{x_0+x_1q+x_2q^2+\cdots+x_{k-1}q^{k-1}})^{q^{k-2}}\equiv a^{x_0q^{k-2}+x_1q^{k-1}}\equiv b^{q^{k-2}}\pmod p$

由于我们已经知道了 $x_0$ 的值，于是有：

$(a^{q^{k-1}})^{x_1}\equiv b^{q^{k-2}}\cdot a^{-x_0q^{k-2}}\pmod p$

可以发现如果我们一直这样递归下去，左边一直都是 $(a^{q^{k-1}})^{x_i}$。

右边显然可以简便计算。

对于每一个 $q$，只需要进行一次 `BSGS` 的预处理即可。

时间复杂度特别玄学，但是 $p\leq 10^{18}$ 且 $p$ 不怎么毒瘤能够通过。具体地，复杂度取决于分解 $p$ 的质因子的速度，这部分可以用某个神奇的 `Pollard-Rho` 优化。

（但是似乎不见得这道题跑得比直接的 `BSGS` 快）

总之这道题就相当于把无数个模板无缝衔接就是了！

```cpp
#include <bits/stdc++.h>
using namespace std;
#define LL long long
#define IL __int128
LL read(){
	LL x=0,f=1;
	char ch=getchar();
	while(ch<'0' || ch>'9'){
		if(ch=='-') f=-1;
		ch=getchar();
	}
	while(ch>='0' && ch<='9'){
		x=x*10+ch-'0';ch=getchar();
	}
	return x*f;
}
namespace PhoRho{ //Phollard-Rho不解释（见Luogu P4718）
	LL gcd(LL a,LL b){
		if (b==0) return a;
		return gcd(b,a%b);
	}
	LL fastpow(LL x,LL p,LL mod){
		LL ans=1;
		while (p){
			if (p&1) ans=(IL)ans*x%mod;
			x=(IL)x*x%mod;
			p>>=1;
		}
		return ans;
	}
	LL max_factor;
	bool MillerRabin(LL x,LL b){
		LL k=x-1;
		while (k){
			LL cur=fastpow(b,k,x);
			if (cur!=1 && cur!=x-1) return false;
			if ((k&1)==1 || cur==x-1) return true;
			k>>=1;
		}
		return true;
	}
	bool prime(LL x){
		if (x==46856248255981LL || x<2) return false;
		if (x==2 || x==3 || x==7 || x==61 || x==24251) return true;
		return MillerRabin(x,2) && MillerRabin(x,3) && MillerRabin(x,7) && MillerRabin(x,61);
	}
	LL f(LL x,LL c,LL n){
		return ((IL)x*x+c)%n;
	}
	LL PRho(LL x){
		LL s=0,t=0,c=1LL*rand()*(x-1)+1;
		int stp=0,goal=1;
		LL val=1;
		for (goal=1;;goal<<=1,s=t,val=1){
			for (stp=1;stp<=goal;++stp){
				t=f(t,c,x);
				val=(IL)val*abs(t-s)%x;
				if (stp%127==0){
					LL d=gcd(val,x);
					if (d>1) return d;
				}
			}
			LL d=gcd(val,x);
			if (d>1) return d;
		}
	}
	void fac(LL x){
		if (x<=max_factor || x<2){
			return;
		}
		if (prime(x)){
			max_factor=max_factor>x?max_factor:x;
			return;
		}
		LL p=x;
		while (p>=x) p=PRho(x);
		while ((x%p==0)) x/=p;
		fac(x);fac(p);
	}
	LL divide(LL n){
		srand((unsigned)time(NULL));
		max_factor=0;
		fac(n);
		return max_factor;
	}
} 
namespace DLP{
	const int N=1111111;
	LL fastpow(LL a,LL n){ //快速幂不解释
		LL res=1;
		while (n>0){
			if (n&1) res=res*a;
			a=a*a;
			n>>=1;
		}
		return res;
	}
	LL fastpow(LL a,LL n,LL p){ //快速幂*2不解释
		LL res=1;
		a%=p;
		while (n>0){
			if (n&1) res=(IL)res*a%p;
			a=(IL)a*a%p;
			n>>=1;
		}
		return res;
	}
	int prime[N],ptot;
	bool ispr[N];
	struct pt{
		LL p;
		int c;
	};
	void getprime(){ //获取10^6以内的质数
		memset(ispr,1,sizeof(ispr));
		for (int i=2;i<N;++i){
			if (ispr[i]) prime[++ptot]=i;
			for (int j=1;j<=ptot && prime[j]<=(N-1)/i;++j){
				ispr[i*prime[j]]=0;
				if (!i%prime[j]) break;
			}
		}
	}
	bool cmp(pt x,pt y){
		return x.p<y.p;
	}
	void findorg(vector <pt> &v,LL num){ //num分解质因数
		while (num>=N){ //大于10^6的部分，每次用Pho-Rho算法找出最大的一个质因子，然后除掉即可
			LL maxf=PhoRho::divide(num);
			int cnt=0;
			while (num%maxf==0){
				cnt++;
				num=num/maxf;
			}
			v.push_back((pt){maxf,cnt});
		}
		if (ptot==0) getprime();
		for (int i=1;i<=ptot && prime[i]<=num;++i){ //剩下的就是不大于10^6的质因子了，直接暴力枚举
			if (num%prime[i]==0){
				int cnt=0;
				while (num%prime[i]==0){
					cnt++;
					num/=prime[i];
				}
				v.push_back((pt){prime[i],cnt});
			}
		}
		if (num>1) v.push_back((pt){num,1});
		sort(v.begin(),v.end(),cmp); //这句话说实在没有意义
	}
	int getorg(LL p,LL phi,vector <pt> &v){ //获取ord
		for (int k=2;;k++){
			int flag=1;
			for (int i=0;i<(int)v.size();++i){
				if (fastpow(k,phi/v[i].p,p)==1){
					flag=0;
					break;
				}
			}
			if (flag) return k;
		}
	}
	LL BSGS(LL a,LL b,LL p,LL mod){ //BSGS模板，具体可以见其它题解的一般做法
		a%=mod;b%=mod;
		if (b==1) return 0;
		if (a==0){
			if (b==0) return 1;
			else return -1;
		}
		LL t=1;
		int m=int(sqrt(1.0*p)+1);
		LL base=b;
		unordered_map <LL,LL> vis;
		for (int i=0;i<m;++i){
			vis[base]=i;
			base=(IL)base*a%mod;
		}
		base=fastpow(a,m,mod);
		LL now=t;
		for (int i=1;i<=m+1;++i){
			now=(IL)now*base%mod;
			if (vis.count(now)) return i*m-vis[now];
		}
		return -1;
	}
	LL getksi(LL g,LL h,LL p,LL c,LL n,LL mod){ //得到合并后的解集，然后上BSGS
		vector <LL> pi;
		LL tp=1;
		for (int i=0;i<=c;++i){
			pi.push_back(tp);
			tp*=p;
		}
		LL gq=fastpow(g,pi[c-1],mod);
		LL inv=0;
		tp=1;
		for (int i=c-1;i>=0;--i){
			LL tx=tp*BSGS(gq,fastpow((IL)h*fastpow(g,pi[c]-inv,mod)%mod,pi[i],mod),p,mod);
			inv+=tx;tp*=p;
		}
		return inv;
	}
	LL exgcd(LL a,LL b,LL &x,LL &y){ //exgcd模板不解释
		if (b==0){
			x=1;y=0;
			return a;
		}
		LL d=exgcd(b,a%b,y,x);
		y-=a/b*x;
		return d;
	}
	LL getinv(LL a,LL p){ //逆元不解释
		if (a==0) return 1;
		LL x,y;
		exgcd(a,p,x,y);
		return (x%p+p)%p;
	}
	LL gcd(LL x,LL y){ //gcd不解释
		if (x%y==0) return y;
		return gcd(y,x%y);
	}
	LL ExgcdSolve(LL a,LL b,LL c,LL &x,LL &y){ //求解exgcd
		LL d;
		if (c%(d=gcd(a,b))) return -1;
		a/=d;b/=d;c/=d;
		exgcd(a,b,x,y);
		x=(IL)x*c%b;
		while (x<=0) x+=b;
		return x; 
	}
	LL crt(vector <LL> ksi,vector <pt> v){ //crt不解释
		int sz=v.size();
		LL M=1,ans=0;
		vector <LL> m;
		for (int i=0;i<sz;++i){
			m.push_back(fastpow(v[i].p,v[i].c));
			M*=m[i];
		}
		for (int i=0;i<sz;++i){
			LL Mi=M/m[i];
			ans=((IL)ans+(IL)Mi*getinv(Mi,m[i])*ksi[i])%M;
		}
		if (ans<0) ans+=M;
		return ans;
	}
	LL getx(LL h,LL g,LL N,LL mod,vector <pt> &v){ //获取解集，然后用crt合并
		vector <LL> ksi;
		for (pt tp:v){
			LL tg=fastpow(g,N/fastpow(tp.p,tp.c),mod);
			LL th=fastpow(h,N/fastpow(tp.p,tp.c),mod);
			ksi.push_back(getksi(tg,th,tp.p,tp.c,N,mod));
		}
		return crt(ksi,v);
	}
	LL solve(LL g,LL h,LL p){ //求解
		if (h==1) return 0;
		LL phiP=p-1;
		vector <pt> v;
		findorg(v,phiP);
		int rt=getorg(p,phiP,v);
		LL x=getx(g,rt,phiP,p,v);
		LL y=getx(h,rt,phiP,p,v);
		LL a=0,b=0;
		if (x==0){
			if (y==0) return 1;
			else if (y==1) return 0;
			else return -1;
		}else return ExgcdSolve(x,phiP,y,a,b);
	}
};
signed main(){
	LL p=read(),g=read(),h=read(); 
    LL ans=DLP::solve(g,h,p);
    if (ans==-1) puts("no solution");
    else cout<<ans<<endl;
	fclose(stdin);
	fclose(stdout);
	return 0;
}
```
