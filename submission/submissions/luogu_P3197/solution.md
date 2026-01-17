# P3197 题解

# 广告

[蒟蒻的blog](http://www.luogu.com.cn/blog/111990/#)

# 正文

~~本蒟蒻又一次写题解，好激动。。。~~

其实这题是这样的：

有n个人，还有m种信仰，然后在所有信仰情况中找出有相邻两个人的信仰是相同的。~~我懒，不想说太多，希望读者大大是读了题思考过了来看的。。。~~

一看难度：
# 绿标签！还是数论！看我dfs切了它！
然后看数据范围：

M<=10000000（10的8次方）

N<=1000000000000（10的12次方）

~~笑容逐渐消失~~

然后开始想正解。

首先，第一种思路肯定是搞一个公式可以直接算出有相邻两个人信仰相同的情况数，but。。。**没有万能公式啊！！！**

~~教大家一招，绿标数论题如果没有找到公式，换一种思路，继续找公式。要相信，这种难度的题肯定有公式~~

然后换一种思路。

我们可以倒过来想，我们只需要算出不越狱的情况，再用总情况减掉就行了！！！

所以。。。第一个人有m种选择，第二个人为了不与第一个人不重复，只有m-1个选择，第三个人为了不与第二个人重复，也只有m-1个选择。。。最后总情况有m^n个，那么。。。

## $ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ ans=m^n-m*(m-1)^{n-1}$

## code

```cpp
#include<cstdio>
#define ll long long
using namespace std;
const ll mod=100003ll;
inline int read()
{
	char ch=getchar();
	int x=0,f=1;
	while(ch>'9'||ch<'0'){if(ch=='-')f=-1;ch=getchar();}
	while(ch>='0'&&ch<='9')
	{
		x=(x<<1)+(x<<3)+ch-'0';
		ch=getchar();
	}
	return x*f;
}
inline ll pow(ll a)
{
	return (a*a)%mod;
}
ll n,m;
inline ll qmi(ll a,ll b)
{
	if(b==0)return 1;
	return (b&1)?pow(qmi(a,b>>1))*(a%mod)%mod:pow(qmi(a,b>>1));
}
int main()
{
	scanf("%lld%lld",&m,&n);
	ll ans=qmi(m,n)-(m%mod)*qmi(m-1,n-1)%mod;
	while(ans<0)ans+=mod;
	ans%=mod;
	printf("%lld",ans);
	return 0;
}
```

最后希望各位读者大大可以ak ioi！！！