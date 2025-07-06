# P4688 题解

不得不说bitset套莫队还是相当套路的……

不过这道题放到ynoi里就显得相当亲民了……(45行的ynoi题啊!)
_________________________________

首先这道题的询问看样子基本没法用数据结构维护……

因为你相当于说要维护不同区间权值数组的最小值，这个东西使用数据结构显然是没法做的

那么智商不够压位来凑，我们可以考虑使用bitset乱搞一波

那么我们可以很快的发现一个询问$(l_{1},r_{1},l_{2},r_{2},l_{3},r_{3})$的答案是

$$(r_{1}-l_{1}+1)+(r_{2}-l_{2}+1)+(r_{3}-l_{3}+1)-3×size$$

其中$size$表示这3个区间里面出现了多少个公共的颜色

问题来了，如果我们使用一个bitset来标记这个区间里出现过什么颜色的话，我们最多知道这个3个区间出现了**多少种公共的颜色**，而不是出现了**多少个公共的颜色**

此时情况开始变得辣手起来……

仔细分析一下我们会发现,问题的瓶颈在于，我们的目标是求公共颜色个数，相当于每种颜色的出现次数取一个min，可是bitset却只是支持集合取交集

但是我们又发现一个性质是所有颜色的出现次数之和=区间长度

所以我们发现我们可以以这样的方式存储一个区间

首先我们在给数字离散化的时候做下手脚

我们令这个数字离散化之后的值=这个序列里小于等于这个值的数字个数

(实现起来很简单，用map求出每种值的出现次数做一遍前缀和就行)

接下来我们要用一个bitset存储一个区间了

假设我们现在向这个区间里加一个颜色p

一般的做法是令bitset的p这一位为1

但是我们现在不这样了，假如说这个区间里p这个值已经出现$cnt_{p}$次了

我们就令bitset里面$(p-cnt_{p})$这一位为1

因为这个数字离散化之后的值是所有小于等于这个值的数字个数

换句话说离散化之后，相邻两个值p1,p2的值的差，刚好是p1的出现次数

这意味着我们这样存储颜色也不会出现将一个颜色存到另外一个颜色地方去

那么此时我们发现这样存储元素有一个好处是

我们现在能算两个区间或者多个区间之间有多少个公共的颜色了

只要把这几个区间取一下交集然后看交集的size就行了

为什么此时取交集就可以起到取min的效果呢……？

因为我们插入颜色的方式决定了假如某个颜色p在区间内出现了$cnt_{p}$次的话

那么bitset里面第$p$到第$p-cnt_{p}+1$位是连续的一段1，也就存储下了$cnt_{p}$的信息

而取交集的时候，对于一个颜色p，交集里从第p位向前连续1的长度恰好就是每一个集合$cnt_{p}$中的min(不懂的话自己画个图还是相当好理解的)

 _如果你熟悉后缀数组的话会发现这种存储方式和后缀数组里的计数排序的行为非常向(都是做一遍前缀和然后倒着排布元素)_ 

所以我们就成功使用取交集完成了取min的操作了

好了那么我们的算法就大致定型了:通过某种奇技淫巧求出这个区间的bitset，然后三个bitset取一下交即可

然后你发现一件事情是这样的bitset似乎并没有办法通过线段树这种常用的处理区间问题的工具来求出来

这个时候我们就可以考虑请出莫队这种泛用更强的区间处理算法了

那么我们发现我们求这个区间的bitset还是很资瓷快速插入和删除的

因此我们可以使用莫队算法以$O(N\sqrt{N})$的复杂度求出每一个区间的bitset

然后你需要做的就是把这个bitset和对应的询问的bitset&一下就可以了

最后的问题是我们开不起1e5个长度为1e5的bitset

~~很简单把询问拆成3组，每组莫队一次就行了~~

上代码~

```C
#include<cstdio>
#include<algorithm>
#include<map>
#include<bitset>
using namespace std;const int N=1e5+10;const int M=34010;typedef long long ll;
int a[N];int n;int m;map <int,int> mp;bitset <N> ans[M];int nans[M];bitset <N> nb;
struct qry{int l;int r;int t;}q[3*M];int tp;int tot=1;int cnt[N];
inline bool cmp1(const qry& a,const qry& b){return a.l<b.l;}
inline bool cmp2(const qry& a,const qry& b){return a.r<b.r;}
inline void ins(int p){nb[p-cnt[p]]=1;cnt[p]++;}
inline void del(int p){cnt[p]--;nb[p-cnt[p]]=0;}
inline void solve()
{
    if(tot>=m)return;
    for(int i=1;i<=M-10&&tot<=m;i++,tot++)
    {
        ++tp;scanf("%d%d",&q[tp].l,&q[tp].r);q[tp].t=i;nans[i]+=q[tp].r-q[tp].l+1;
        ++tp;scanf("%d%d",&q[tp].l,&q[tp].r);q[tp].t=i;nans[i]+=q[tp].r-q[tp].l+1;
        ++tp;scanf("%d%d",&q[tp].l,&q[tp].r);q[tp].t=i;nans[i]+=q[tp].r-q[tp].l+1;
    }for(int i=1;i<=tp/3;i++)ans[i].set();sort(q+1,q+tp+1,cmp1);int nl=0;int nr=0;
    for(int i=1;i<=tp;i+=320){int r=min(tp,i+319);sort(q+i,q+r+1,cmp2);}
    for(int i=1;i<=tp;i++)
    {
        if(nr<q[i].l)
        {
            for(int j=nl;j<=nr;j++)del(a[j]);nl=q[i].l;nr=q[i].r;
            for(int j=nl;j<=nr;j++)ins(a[j]);
        }
        else 
        {
            while(nl<q[i].l)del(a[nl]),nl++;while(nl>q[i].l)nl--,ins(a[nl]);
            while(nr<q[i].r)nr++,ins(a[nr]);while(nr>q[i].r)del(a[nr]),nr--;
        }ans[q[i].t]&=nb;
    }for(int i=nl;i<=nr;i++)del(a[i]);
    for(int i=1;i<=tp/3;i++)printf("%lld\n",nans[i]-ans[i].count()*3);
    for(int i=1;i<=tp/3;i++)nans[i]=0;tp=0;
}
int main()
{
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++)scanf("%d",&a[i]);
    for(int i=1;i<=n;i++)mp[a[i]]++;map <int,int> :: iterator it,it1;
    for(it=mp.begin(),it1=it,++it1;it1!=mp.end();++it,++it1)it1->second+=it->second;
    for(int i=n;i>=1;i--)a[i]=mp[a[i]];
    solve();solve();solve();return 0;
}
```