# P2487 题解

## 一些闲话

**这是一个忧伤但又振奋人心的故事。**我在做这题的时候栽了不少跟头，也没有人能帮我，网上找不到相似的题解，代码重构了至少三次。一天从早上八九点一直做到接近凌晨。

[十一点的提交](https://www.luogu.org/record/show?rid=9859743)

把做这题的经过写下来，以“贻其后之来者”。

## 题目大意

有$n$个导弹，每个导弹有三个参数$t$，$h$和$v$。你需要求出一个最长的序列${a}$，满足对于所有的$i$，均有$t_i\le t_{i+1}~h_i\ge h_{i+1}~v_i\ge v_{i+1}$。输出最长的序列的长度。由于可能有多种最长的序列的方案，每次随机选一种，你需要求出对于每个导弹，其成为最长序列中的一项的概率。

$n\le 5\times 10^4,1\le h_i,v_i\le 10^9,1\le t_i\le n$

## 解法

记$f1_i$表示以$i$为结尾的最长非生子序列的长度（以后简称LDS），$g1_i$表示这样的LDS的个数。

直接用常规的DP，时间复杂度为$O(n^2)$，需要优化。

条件很显然是个三维偏序的形态。题目中的$t$已经排好了序。

考虑进行CDQ分治。每次将序列分成左和右两部分。每次考虑左边对右边的影响。

递归处理左侧；

更新当前节点的值；

递归求解右侧。

更新当前节点的值时，先将左右两侧按$h$从大到小排好序。因为之前已经按$t$排好序了，所以考虑左边对右侧的影响时，$t$的大小关系一定满足条件。用类似于归并排序的方式，维护两个指针，分别表示当前处理到的左侧区间的位置和右侧区间的位置。如果当前指向右侧区间的$h$值小于等于左边区间指针指向的值，将左指针的$v_i$，$f1_i$和$g1_i$加入数据结构中；反之，查询$v$大于$v_j$的所有数中最大的$f1$和对应的$g1$。

这个数据结构（线段树/树状数组）需要进行两种操作：

1.修改单点的值；

2.查询区间的最大值和对应的数值。

定义$f2_i$和$g2_i$为以$i$为开头的最长非生子序列的长度（以后简称LDS），$g1_i$表示这样的LDS的个数。

将数组逆序，数字取反，即可用同样的过程求解$f2$和$g2$。

最后$max(f1)$即为LDS的最大长度。

$\sum_{i=1}^n g1_i(f1_i=max(f1))$即为所有可能的最长LDS的方案总数，记为$sum$。

对于一个节点$i$，**当且仅当**$f1_i+f2_i-1=max(f1)$时（减去的$1$是重复计算的节点$i$），该节点可能成为LDS上的一点。根据乘法原理，所有经过该节点的LDS方案总数为$g1_i\times g2_i$，那么概率即为$\frac{g1_i\times g2_i}{sum}$。

## 实现细节

用类似于中序遍历的方式进行CDQ过程。

由于$v$较大，而$n$较小，需要对$v$进行离散化，方便进行数据结构。

将左侧对右侧的影响计算完以后，需要**清空数据结构**。直接```memset```可能会超时，需要进行$DFS$并在当前节点没有值时剪枝。

**重要必读！**

$g1_i$，$g2_i$和$sum$必须要用```double```类型存储，否则相加或相乘会爆```long long```。在数字太大的时候，```double```会舍弃一些精度换取存储更大的值。

## 代码展示

这里给出一种用线段树实现的版本。

```cpp
// luogu-judger-enable-o2
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<set>
#include<map>
using namespace std;
typedef long long ll;
const int maxn=50010;
ll n,cnt,maxh,maxx,f1[maxn],f2[maxn];
double sum,g1[maxn],g2[maxn];
struct node{ll t,h,v;}s[maxn];
const bool cmpt(node a,node b){return a.t<b.t;}
const bool cmph(node a,node b){return (a.h==b.h)?(a.t<b.t):a.h>b.h;}
set<ll>st;
map<ll,ll>id;
ll max_[maxn*4];
double cnt_[maxn*4];
void clear(ll o,ll l,ll r)
{
    if(!max_[o])return;
    max_[o]=0;
    if(l==r)return;
    int mid=(l+r)>>1;
    clear(o<<1,l,mid);
    clear(o<<1|1,mid+1,r);
}
void update(ll o,ll l,ll r,ll x,ll v,double v2)
{
    if(l>x||x>r)return;
    if(l==r)
    {
        if(max_[o]<v)max_[o]=v,cnt_[o]=0;
        if(max_[o]==v)cnt_[o]+=v2;
        return;
    }
    ll mid=(l+r)>>1;
    update(o<<1,l,mid,x,v,v2);
    update(o<<1|1,mid+1,r,x,v,v2);
    max_[o]=max(max_[o<<1],max_[o<<1|1]);
    cnt_[o]=0;
    if(max_[o]==max_[o<<1])cnt_[o]+=cnt_[o<<1];
    if(max_[o]==max_[o<<1|1])cnt_[o]+=cnt_[o<<1|1];
}
ll query(ll o,ll l,ll r,ll ql,ll qr,double&cntt)
{
    if(ql>r||l>qr){cntt=0;return 0;}
    if(ql<=l&&r<=qr){cntt=cnt_[o];return max_[o];}
    ll mid=(l+r)>>1;
    double cntl=0,cntr=0;
    ll al=query(o<<1,l,mid,ql,qr,cntl),ar=query(o<<1|1,mid+1,r,ql,qr,cntr);
    cntt=0;
    if(mid>=ql&&max(al,ar)==al)cntt+=cntl;
    if(mid<=qr&&max(al,ar)==ar)cntt+=cntr;
    return max(al,ar);
}
void CDQ1(ll l,ll r)
{
    if(l==r)return;
    ll mid=(l+r)>>1;
    sort(s+l,s+r+1,cmpt);
    CDQ1(l,mid);
    sort(s+l,s+mid+1,cmph);
    sort(s+mid+1,s+r+1,cmph);
    clear(1,1,n);
    for(int i=l,j=mid+1;j<=r;j++)
    {
        while(i<=mid&&s[i].h>=s[j].h)update(1,1,n,s[i].v,f1[s[i].t],g1[s[i].t]),i++;
        double cn=0;
        ll t=query(1,1,n,s[j].v,n,cn);
        if(!t)continue;
        if(f1[s[j].t]<t+1)f1[s[j].t]=t+1,g1[s[j].t]=0;
        if(f1[s[j].t]==t+1)g1[s[j].t]+=cn;
    }
    CDQ1(mid+1,r);
}
void CDQ2(ll l,ll r)
{
    if(l==r)return;
    ll mid=(l+r)>>1;
    sort(s+l,s+r+1,cmpt);
    CDQ2(l,mid);
    sort(s+l,s+mid+1,cmph);
    sort(s+mid+1,s+r+1,cmph);
    clear(1,1,n);
    for(int i=l,j=mid+1;j<=r;j++)
    {
        while(i<=mid&&s[i].h>=s[j].h)update(1,1,n,s[i].v,f2[s[i].t],g2[s[i].t]),i++;
        double cn=0;
        ll t=query(1,1,n,s[j].v,n,cn);
        if(!t)continue;
        if(f2[s[j].t]<t+1)f2[s[j].t]=t+1,g2[s[j].t]=0;
        if(f2[s[j].t]==t+1)g2[s[j].t]+=cn;
    }
    CDQ2(mid+1,r);
}
int main()
{
    scanf("%lld",&n);
    for(int i=1;i<=n;i++)scanf("%lld%lld",&s[i].h,&s[i].v),s[i].t=i,st.insert(s[i].v),maxh=max(maxh,s[i].h);
    for(set<ll>::iterator it=st.begin();it!=st.end();it++)id[*it]=++cnt;
    for(int i=1;i<=n;i++)s[i].v=id[s[i].v];
    for(int i=1;i<=n;i++)f1[i]=f2[i]=1,g1[i]=g2[i]=1.0;
    CDQ1(1,n);
    for(int i=1;i<=n;i++)maxx=max(maxx,f1[i]);
    for(int i=1;i<=n;i++)if(f1[i]==maxx)sum+=g1[i];
    printf("%lld\n",maxx);
    for(int i=1;i<=n;i++)s[i].t=n-s[i].t+1,s[i].h=maxh-s[i].h+1,s[i].v=cnt-s[i].v+1;
    sort(s+1,s+n+1,cmpt);
    CDQ2(1,n);
    for(int i=1;i<=n;i++)
    {
        if(f1[i]+f2[n-i+1]-1!=maxx)printf("%.5lf ",0.0);
        else printf("%.5lf ",g1[i]*g2[n-i+1]/sum);
    }
    return 0;
}
```