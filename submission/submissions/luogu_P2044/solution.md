# P2044 题解

## 矩阵快速幂 + 龟速乘

$$ X_{n+1}=(aX_n+c) \mod m $$

题目给了我们一个递推式，让我们求$X_n$.

看到$1e18$的数据范围，明显是不能直接递推的，考虑矩阵加速。

-------------------------

### 构造矩阵

首先设初始矩阵为

$$\begin{bmatrix}

X_{i-1} \\

c

\end{bmatrix}$$

要求一个转移矩阵使得相乘之后可得到

$$\begin{bmatrix}

X_i\\

c

\end{bmatrix}$$

（以下暂不考虑取模）

$$X_i=a×X_{i-1}+1×c$$

$$c=0×X_{i-1}+1×c$$


那么容易得出转移矩阵为

$$\begin{bmatrix}

a & 1\\

0 & 1

\end{bmatrix}$$

在本题中，初始矩阵即为

$$\begin{bmatrix}

X_0\\

c

\end{bmatrix}$$

经过一次转移

$$\begin{bmatrix}

a & 1\\

0 & 1

\end{bmatrix} 

×

\begin{bmatrix}

X_0\\

c

\end{bmatrix}

=

\begin{bmatrix}

X_1\\

c

\end{bmatrix}

$$ 

显然，对于 $n$ 次转移，得到的矩阵就是

$$

\begin{bmatrix}

X_n\\

c

\end{bmatrix}

$$ 

-----------------------


那么 $n$ 次转移后得到的矩阵的第一行第一列位置的数，就是我们要求的答案，最后对 $g$ 取模。

由于矩阵乘法满足结合律，所以先把转移矩阵进行矩阵快速幂 $n$ 次方，然后乘上初始矩阵。

-------------------------------

但是仅仅打上一个矩阵快速幂是无法$\color{green}AC$此题的，考虑到数据范围过大以至于会爆掉$longlong$，~~可以写高精~~，可以使用龟速乘。

---------------------------

### 龟速乘

顾名思义，龟速乘就是一种速度超慢的乘法，但是可以保证不爆$longlong$.

首先考虑为什么我们每一步都取模还是会爆呢？那就是因为我们在乘的时候先乘再取模，还没等到取模就已经溢出了，然后再执行取模，就相当于亡羊补牢。

龟速乘的原理是什么呢？

考虑乘法的本质。大家都学过，乘法就是连加的一种缩写。

举个栗子， 

$5×4=5+5+5+5$

$3×6=3+3+3+3+3+3$

那我们如果对于 $x × y$，循环 $y$ 次，累加 $y$ 个 $x$ ，每一步都取模，不就可以避免这个问题了吗？

确实，但很慢……肯定是不行的。

使用和快速幂相似的思想，对乘法进行拆分。

对于 $a × b$，

当 $a$ 为偶数时，$a × b = a × (b÷2) + a × (b÷2)$

当 $a$ 为奇数时，$a × b = a × (b÷2) + a × (b÷2)+a$

跟快速幂像极了……

```cpp
long long Wuguidechengfa(long long x,long long y)
{
	long long ans=0;
	while(y)
	{
		if(y&1) (ans+=x)%=mod;
		(x+=x)%=mod;
		y>>=1;
	}
	return ans;
}
```

这样就解决了长整型溢出的问题。

-----------------------------

完整代码

```cpp
#include<bits/stdc++.h>
#define mul(x,y) Wuguidechengfa(x,y)
using namespace std;
typedef long long ll;
const int N=40;
inline ll read()
{
	char c;ll res=0;
	for(;!isdigit(c);c=getchar());
	for(;isdigit(c);c=getchar())res=(res<<3)+(res<<1)+(c^48);
	return res;
}
ll mod,a,c,x0,n,g;
ll Wuguidechengfa(ll x,ll y)
{
	ll ans=0;
	while(y)
	{
		if(y&1) (ans+=x)%=mod;
		(x+=x)%=mod;
		y>>=1;
	}
	return ans;
}
//龟速乘
struct Mat
{
	ll a[N][N];
	//矩阵
	int n,m;
	//行、列
	Mat(){n=m=0;memset(a,0,sizeof a);}
	//构造空矩阵
	Mat(int k){n=m=k;memset(a,0,sizeof a);for(int i=1;i<=k;i++)a[i][i]=1;}
	//构造k*k的单位矩阵
	Mat(int x,int y){n=x,m=y;memset(a,0,sizeof a);}
	//构造x*y的空矩阵
	Mat operator *(Mat b)
	{
		Mat c(n,b.m);
		for(int i=1;i<=c.n;i++)
		{
			for(int j=1;j<=c.m;j++)
			{
				for(int k=1;k<=m;k++)
				{
					c.a[i][j]=(c.a[i][j]+mul(a[i][k],b.a[k][j]))%mod;
					//注意这里用龟速乘而不是直接写乘号
				}
			}
		}
		return c;
	}
	Mat operator *=(Mat b)
	{
		return *this=*this*b;
	}
	//重载乘法
	Mat operator ^(ll k)
	{
		Mat ans(n),t=*this;
		while(k)
		{
			if(k&1) ans*=t;
			t*=t;
			k>>=1;
		}
		return ans;
	}
	Mat operator ^=(ll k)
	{
		return *this=*this^k;
	}
	//矩阵快速幂
};
int main()
{
	mod=read();a=read();c=read();x0=read();n=read();g=read();
	if(!n)return printf("%d\n",x0)&0;
	//特判n==0的情况
	Mat res(4,4);
	res.a[1][1]=a,res.a[1][2]=1,res.a[2][2]=1;
	//构造转移矩阵
	Mat p(2,1);
	p.a[1][1]=x0,p.a[2][1]=c;
	//构造初始矩阵
	res^=n;
	res*=p;
	//注意乘法顺序，矩阵乘法不满足交换律
	printf("%lld\n",res.a[1][1]%g);
	//注意答案对g取模
    return 0;
}
```
结束！