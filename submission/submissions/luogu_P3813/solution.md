# P3813 题解

表示正解为什么是$O(4^{n})$啊……

明明可以做到$O(3^n)$啊……

感觉那个dp做法十分奇怪……同时凭借$O(2^{n})$的空间复杂度拿了rk1？

# 容斥原理

看到计数想容斥……基本来讲这种玄学的计数题就是容斥定理没跑了……

首先我们发现矩阵中一个点肯定有一个取值范围

范围是$[1,min(min(v_{i}),m)]$其中i是覆盖了这个点的矩阵，因为呢，如果这个点的取值大过了v的最小值，对应子矩阵的限制就不满足了

然后值域相同的点会连成一些奇形怪状的图案(当然，不一定全部相连)

我们仔细观察这个图形，**发现值域不同的点之间的取值无关。**

这个是什么意思呢？

如果两个点a,b值域不同的话，a取到值域的max，所满足的子矩阵(们)，和b取到值域的max所满足的子矩阵(们)肯定不同，没有什么既然a取了max那么b就可以随便取了这个说法。

所以a取什么值和b取什么值根本没有任何关系~

那么既然是独立事件就可以使用乘法原理~

因此分别求出每个值域的方案数，最后乘起来就是答案了！

### 求某一个值域的方案数

(我知道胡乱设一堆变量十分难理解，但是的确不是很好说)

那么我们会发现呢，可能有多个矩阵的值域相同，那么设值域最大值为k的**点**构成一个集合$S_{k}$，里面的点可以满足的子矩阵暂且记为1，2，3……号矩阵

那么我们可以先让所有的点随便取，那么总方案数就是$k^{|S_{k}|}$

然后我们发现明显多算了

所以减去1号子矩阵取不到max的情况，记$S_{k}$中属于i号矩阵的点构成了集合$T_{k,i}$那么总方案数为$(k-1)^{|T_{k,1}|}k^{|S_{k}|-|T_{k,1}|}$，就是属于一号矩阵的点不可以取max，其他的点随便取

然后减去2号子矩阵取不到max的情况，3号子矩阵取不到max的情况，等等……

发现1，2号子矩阵同时取不到max的情况被多减了，所以减去1，2同时取不到max的情况，2，3同时取不到max的情况，1，3同时取不到max的情况……等等

发现此时1，2，3号子矩阵同时取不到max的情况被多加了，所以减去1，2，3同时取不到max的情况，……等等……

然后这样就可以大力容斥出每一个值域的方案数了

大概就是枚举v值相同的矩阵集合的子集，然后加加减减什么的

问题来了，上面要求我们要求出S集合和T集合的siz……

其实就是可以理解成v值相同子矩阵矩阵的并集∪所有值小于当前v的子矩阵并集-所有值小于v的矩阵的并集

T集合的话差不多，就是把上面的“所有”改成子集就可以了，然后就可以求出这个集合的siz了。

问题是如何求出所有并集的siz？

显然所有并集的siz是可以容斥原理暴力做的，直接枚举子集就好……然后$O(3^{n})$暴力的枚举子集大力容斥就可以了

所以当然非常快了……就酱

上代码~

```C

// luogu-judger-enable-o2
#include<cstdio>
#include<algorithm>
using namespace std;const int N=15;const int M=1050;typedef long long ll;const ll mod=1e9+7;
inline ll po(ll a,ll p){ll r=1;for(;p;p>>=1,a=a*a%mod){if(p&1){r=r*a%mod;}}return r;}
int n;int m;ll h;ll w;ll s[M];ll u[M];int up;int siz[M];ll res;int T;
struct retc//矩形类 
{
    ll x;ll y;ll x1;ll y1;int v;
    inline void rd(){scanf("%lld%lld%lld%lld%d",&x,&y,&x1,&y1,&v);}
    inline bool ck(){return (x>x1)||(y>y1);}//是否为空 
    inline ll calcs(){return (x1-x+1)*(y1-y+1);}//求面积 
    void operator &=(const retc& a)//交 
    {x=max(x,a.x);y=max(y,a.y);x1=min(x1,a.x1);y1=min(y1,a.y1);}
    friend bool operator <(retc a,retc b){return a.v<b.v;}
}r[N],tr;
inline void solve()
{
    scanf("%lld%lld%d%d",&h,&w,&m,&n);
    for(int i=0;i<n;i++){r[i].rd();}sort(r,r+n);up=(1<<n)-1;
    for(int i=1;i<=up;i++)//暴力求交集面积 
    {
        tr.x=1;tr.y=1;tr.x1=h;tr.y1=w;
        for(int p=i,j=0;p;p>>=1,j++){if(p&1){tr&=r[j];if(tr.ck()){s[i]=0;goto ed;}}}
        s[i]=tr.calcs();ed:;
    }
    for(int i=1;i<=up;i++)//暴力求并集面积 
    {
        for(int j=i;j;j=(j-1)&i)
        {if(siz[j]%2){u[i]+=s[j];}else {u[i]-=s[j];}}
    }
    int ns=0;int ls=0;res=1;
    for(int i=0;i<n;i++)//分值域统计方案数 
    {
        ns|=(1<<i);if(r[i].v==r[i+1].v){continue;}
        ll tot=u[ns|ls]-u[ls];ll st=tot;ll ret=po(r[i].v,tot);
        for(int k=ns;k;k=(k-1)&ns)
        {
            tot=u[k|ls]-u[ls];
            ll del=po(r[i].v-1,tot)*po(r[i].v,st-tot)%mod;
            if(siz[k]%2){ret=(ret+mod-del)%mod;}
            else {ret=(ret+del)%mod;}
        }res=res*ret%mod;ls|=ns;ns=0;//乘起来	
    }printf("%lld\n",res*po(m,h*w-u[up])%mod); 
}
inline void clear(){for(int i=0;i<=up;i++){u[i]=0;}}
int main()
{
    for(int i=1;i<=1023;i++){siz[i]=siz[i>>1]+(i&1);}scanf("%d",&T);
    for(int z=1;z<=T;z++){solve();clear();}return 0;//拜拜程序~ 
}

```






