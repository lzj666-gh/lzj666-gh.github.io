# P8865 题解

AFO 了，考场上四十分钟打完 T1，以为自己一等稳了，但是有一个地方忘记取模，以为自己今年完了，想不到 CCF  数据能让我过（。

## 考场思路

只讲思路，没有代码，配合下边代码详解食用。

考试的时候一看题面，看着像是一个 DP ， 但是细想一下，貌似不是，只是一个很简单的前缀和优化计数问题。

首先，先考虑 $C$ 因为 $F$ 是  $C$ 下边随便加一个点，所以只要求出 $C$ 就求出了  $F$  。下边来考虑如何求 $C$ 。

注意到，他并没有要求上下行一样，唯一的要求是 $C$ 的两个横要隔一行，这就是问题的突破点，这题很明显的计数，计数用到什么？乘法原理，加法原理。

假设上边的有  $a$ 个合法的横，那考虑这一行每一个合法的横（这里说的不同是长度不同）给答案的贡献是什么？是不是每一个贡献  $a$ ，那这一行有  $b$ 个不同的合法的横，那么答案就增加了  $a  \times  b$，那每一行都这么处理，然后处理完一样就加上上一行的合法的方案数（因为他要求两个横之间至少隔一行）。当遇到土坑的时候就把记录数组清零即可。

 $C$ 解决了，那就是 $F$ 了、
 
 想要求出 $F$ ，只要求出这一列上有多少合法的 $C$ 就行了（因为 $F$ 是由  $C$ 下边加上一个竖构成的），所所以我们只要复制过来记录  $C$ 的公式然后把他存在另一个数组里到时候每找到一个能种花的地方 $F$ 的答案加上这个数组就好了。
 

那问题来了，怎么 $\Theta (1)$ 查询每一行有多少个合法的横？只需要预处理就 解决了。

## 代码

这里吧不同部分代码分开，并且删掉了取模部分（我觉得加上取模不雅观，去掉更方便看，打代码的时候别忘了加上），更容易食用。

### 初始化

多少大佬损兵折将在此处。这是最重要的部分了（，希望以后的 OIer 能记得有一年 NOIP T1 因为初始化干掉了很多大佬。

`memset(f,0,sizeof f);`

多测不清空，十年 OI 一场空。

### 预处理

预处理前缀和，让我们在 $\Theta (1)$ 下查询到每一行有多少合法的横。

```
for(int i=1;i<=n;i++)
	for(int j=m-1;j>=1;j--)
	{
		if(Map[i][j]=='1') f[i][j]=-1;//如果不能种花，就变成-1 
		else  if(Map[i][j+1]=='0') f[i][j]=f[i][j+1]+1;//能种花，就加上前缀和 
	}
```

### 求 $C$ 的数量

前边讲的很清楚了，不具体说了。

```
for(int j=1;j<m/*最后一列就不用枚举了*/;j++)//j是枚举每一列 
{
	jis=jil=jilf=0;
	for(int i=1;i<=n;i++)//每一行 
	{
		if(f[i][j]==-1){jis=jilf=jil=0;continue ;}//清空答案 
		ansc+=f[i][j]*jil;
		//乘法原理应用（上文讲了C如何求 
		jil+=max(0,f[i-1][j]);//因为我设置的初值是-1，所以取max 
		//加上上一行的，因为要保证每两个横之间隔一行 
	}
}
```

### 求 $F$ 的数量

```
for(int j=1;j<m;j++)//j是枚举每一列 
{
	jis=jil=jilf=0;
	for(int i=1;i<=n;i++)//每一行 
	{
		if(f[i][j]==-1){jis=jilf=jil=0;continue ;}
		ansf+=jilf;//因为当这个是可以种花的，那只要加上之前有多少C就是F的数量了 
		jilf+=f[i][j]*jil;//求出到当前这一行有多少合法的C
      //注意这上下两行不能换，因为要保证两横之间差一行
		jil+=max(0,f[i-1][j]);//和C的一样 
	}
}
```


然后把求 $C$ 和 $F$ 得循环结合在一起就行了

## 总代码

```
#include<bits/stdc++.h>
#define ll int
#define max(A,B) (A<B?B:A)
#define min(A,B) (A<B?A:B)
#define bug cout<<"I AK NOIP!"<<'\n';
#define gc getchar
using namespace std;
const int N=1005,mod=998244353;
inline ll read(){ll res=0,f=0;char ch=gc();for(;!isdigit(ch);ch=gc()) f=(ch=='-'?1:0);for(;isdigit(ch);ch=gc()) res=(res<<3)+(res<<1)+(ch^'0');return f?-res:res;}

long long ansc,ansf,c,F;
int n,m,id,T;
int f[N][N],jil,jilf,jis;
char Map[N][N];

signed main()
{
	T=read(),id=read();
	while(T--)
	{
		memset(f,0,sizeof f);
		n=read(),m=read();c=read(),F=read();
		for(int i=1;i<=n;i++) for(int j=1;j<=m;j++) cin>>Map[i][j];
			for(int i=1;i<=n;i++)
				for(int j=m-1;j>=1;j--)
				{
					if(Map[i][j]=='1') f[i][j]=-1;//如果不能种花，就变成-1 
					else  if(Map[i][j+1]=='0') f[i][j]=f[i][j+1]+1;//能种花，就加上前缀和 
				}
		for(int j=1;j<m;j++)
		{
			jis=jil=jilf=0;
			for(int i=1;i<=n;i++)
			{
				if(f[i][j]==-1){jis=jilf=jil=0;continue ;}
				ansc=ansc%mod+(1ll*f[i][j]*(jil%mod))%mod;
				ansf=(ansf%mod+jilf%mod)%mod;
				jilf=(jilf+(1ll*f[i][j]*(jil%mod))%mod)%mod;
				jil+=max(0,f[i-1][j]);
			}
		}
		cout<<(c*ansc)%mod<<' '<<(F*ansf)%mod<<'\n';
		ansc=ansf=0;
	}
	return 0;
}
```