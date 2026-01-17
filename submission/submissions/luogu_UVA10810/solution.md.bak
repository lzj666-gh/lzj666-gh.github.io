# UVA10810 题解

这就是一道求**逆序对**的模板吧

为了使代码的常数不要太辣鸡，所以要用~~金坷垃~~，

呸，要用**树状数组**。

#### 首先对于树状数组，当前的理解是

```
对于一个1~n的序列，一共有n个前缀和，每个前缀的下标都有唯一的二进制分解形式

```
通过这个性质我们可以在分解前缀下标log的时间内，分解前缀加和的过程

加的时候，比如算1~10，我们知道10=2+8,先算9~10，长度为2，然后再算1~8，长度为8，分解完成，两步算出

那么递归地减小要算的前缀和，我们发现它总是对的

那么如何更新它呢，那我们就要看在统计和的过程中，要更新的位置对树状数组的哪些节点有贡献，很显然他一定对于

x-lowbit(x)进行若干次变换得到他当前的下标的值有贡献，那么它就对于cur+lowbit(cur)进行若干次迭代有贡献

直到它超过我们统计的范围N，因此范围N我们一定要知道，因此离散化使得N变小是很必要的，或者处理一些负值

 

### 如何统计逆序对呢

一种方法是，我们每插入一个数就计算插入时间在它前面但是值比他大的数有多少，很显然这是一个区间和sum(a+1,N)

另外一种方法是，按照原插入序列的倒序插入，这样我们需要检测的是时间在它后面但是值比它小的数有多少，很显然这是一个前缀和sum(a-1)


```
#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#define ll long long
using namespace std;
const ll maxn=1000000+5;
ll n,m,ans;
ll A[maxn],C[maxn]/*Tree[]*/,D[maxn]/*离散化*/;
string s;
ll x,y;
inline ll read()
{
    ll x=0;
    char c=getchar();
    bool f=false;
    while(!isdigit(c))
	{
        if(c=='-') f=true;
        c=getchar();
    }
    while(isdigit(c))
	{
        x=(x<<1)+(x<<3)+(c^48);
        c=getchar();
    }
    return f?-x:x;
}
inline ll LowBit(ll k){return k&(-k);}//lowbit技术
ll Get_Sum(ll x)//求和操作
{
	ll ans=0;
	for(ll i=x;i>0;i-=LowBit(i))ans+=C[i];
	return ans;
}
inline void Update(ll x,ll d)//更新操作
{for(ll i=x;i<=n;i+=LowBit(i))C[i]+=d;}
void Discretize()
{
    sort(D+1,D+1+n);
    unique(D+1,D+1+n)-D-1;
    for(ll i=1;i<=n;i++)A[i]=lower_bound(D+1,D+1+n,A[i])-D;
}
int main()
{
	ll i,j;
	while(1)
	{
		ans=0;
		n=read();
		if(n==0)break;
		for(i=1;i<=n;i++)A[i]=read(),D[i]=A[i];
		Discretize();
		for(i=1;i<=n;i++)C[i]=0;
		for(i=n;i>=1;i--)//倒叙
		{
			Update(A[i],1);
			ans+=Get_Sum(A[i]-1);//比它小的数的个数
		}
		printf("%lld\n",ans);
	}
	return 0;
}
```