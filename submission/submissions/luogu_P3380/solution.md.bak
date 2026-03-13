# P3380 题解

大家好，我非常喜欢暴力数据结构，于是我就用分块过了这道题。

# 并且可能比大多数人的树套树都块

~~其实这题就是P4119的弱化版~~

## 本体题解

这题让我们实现4个操作，区间kth，区间前驱，区间后继，区间查询排名

那么如果你对基本的数据结构足够熟练的话会知道这些其实可以这些问题都可以用可持久化线段树在$O(log(n))$的时间内解决

但是这题还多一个操作，那就是单点修改点权，此时我们的问题可能就会变得比较辣手了，该怎么解决这个问题呢?

~~树状数组套权值线段树，此题完结~~

当然这可能也是这道题的树套树解法之一，而且跑的并不慢

~~但是我们就是喜欢分块~~

在这道题的一篇题解当中介绍了一种乱七八糟的二分+分块做法……

问题来了，**分块这个算法和二分法根本不契合**

为什么我们在可持久化线段树上会使用二分法？因为线段树这个东西本身就和二分的算法流程相当像，所以我们在线段树上使用二分就可以在$O(logn)$的时间内出解

但是现在支持二分的底层数据结构变成了分块，众所周知，二分的思想是分治,而分块的思想是暴力之间的平衡，这两个算法之间明显不搭调，因此我们的复杂度会凭空多个log出来变成了$O(\sqrt{N} logn)$

那么对于kth问题我们其实还有一个算法是基于对值域分块的算法

假设我们现在需要知道一些数字中的第k大,并且仅仅要求在$O(\sqrt{N})$的时间内出解，我们可以采取这样一种算法，将值域分成$O(\sqrt{N})$块

然后设两个数组$cnt1(i)$表示第i个值域块有几个点，$cnt2(i)$表示第i这个值出现了多少次

那么我们思路就是暴力的for循环

对于查询元素排名的操作，假设这个元素在第i块而值为x，我们先暴力的把$cnt1(1)$到$cnt1(i-1)$的值加到答案当中去,然后再把和x在同一个值域块的数字加到答案中去，这个东西可以查$cnt2$得到

对于查询kth的操作，我们枚举这个元素在第几块，这个可以从左到右扫一遍$cnt1$得到，将kth定位在某一个块内之后，在这个值域块内从左到右扫一遍，通过查$cnt2$就可以得知kth到底是哪个元素了

对于查询前驱和后继的操作，我们通过查$cnt2$可以查询它自己值域块有没有它的前驱和后继，如果有的话直接输出结果，否则找到这个点左侧或者右侧第一个非空的块然后在这个块内暴力找前驱后继即可

这样我们就在$O(\sqrt{N})$的时间内解决了这个问题

你可能会问，这东西有什么用呢？二分直接完爆这个垃圾算法

但是不知道你发现没有发现一个事实，二分法要求我们快速回答这个问题

**在这个数字集合当中有几个数字比x大**

但是刚才的算法我们仅仅需要回答这个问题

**在这个数字集合当中有几个数字恰好为x，以及在这个数字集合当中有几个数字恰好落在了第i个值域块里**

显然维护这两个信息的难度是相当不一样的

_________________

现在让我们来考虑如何用分块来解决这道题

首先将整个序列分成$O(\sqrt{N})$块，然后将出现的值全部离散化这样值域也变成$O(N+M)$级别的了，然后将值域分成$O(\sqrt{N+M})$块

接下来我们打两个表出来$cnt1(i,j)$表示前i块落在第j个值域块的数字有几个,$cnt2(i,j)$表示前i个块值恰好为j的数字有几个，这两个表显然可以在$O(N\sqrt{N})$的时间内预处理出来

那么修改的时候相当简单，把x改成y就直接暴力修改这两个表就行了，复杂度显然$O(\sqrt{N})$

对于其他的询问操作，其实我们就是想要得到这个区间的cnt1和cnt2数组长什么样,那么我们可以暴力的处理出来边角点的cnt1和cnt2数组，然后对于第i个块和第j块之间的cnt1和cnt2数组我们可以用$cnt1(j,...)-cnt1(i-1,...)$和$cnt2(j,...)-cnt2(i-1,...)$来得到，这样我们就可以在$O(\sqrt{N+M})$的时间内解决这个问题了，至于4个操作的具体流程已经在上面写的相当清楚了此处就不在赘述，如果还不明白可以看我代码

上代码~

```C
#include<cstdio>
#include<algorithm>
#include<map>
using namespace std;const int N=5*1e4+10;const int M=1e5+10;
const int B=260;const int B2=300;int a[N];//维护的表格 
int cnt1[N/B+3][M/B2+3];int cnt2[N/B+3][M];int n;int m;int bi[N];int bi1[M];
int tr1[M];int tr2[M];map <int,int> mp;int S;int Pr[M];int Pl[M];int val[M];
inline int frk(int l,int r,int va)//查询元素的排名 
{
    int p1=bi[l];int p2=bi[r];int ret=0;
    if(p1==p2){for(int i=l;i<=r;i++)ret+=(a[i]<va);return ret+1;}
    for(int i=l;bi[i]==p1;i++)ret+=(a[i]<va);
    for(int i=r;bi[i]==p2;i--)ret+=(a[i]<va);p2--;
    for(int i=1;i<bi1[va];i++)ret+=cnt1[p2][i];
    for(int i=1;i<bi1[va];i++)ret-=cnt1[p1][i];
    for(int i=va-1;bi1[i]==bi1[va];i--)ret+=cnt2[p2][i];
    for(int i=va-1;bi1[i]==bi1[va];i--)ret-=cnt2[p1][i];return ret+1;
}
inline int ckth(const int& p1,const int& p2,int k)//辅助函数，查询kth 
{
    int ret=B2;int cur=0;
    for(int t=1;cur<k;ret+=B2,t++)cur+=cnt1[p2][t]-cnt1[p1][t]+tr1[t];ret-=B2;
    for(;cur>=k;ret--)cur-=cnt2[p2][ret]-cnt2[p1][ret]+tr2[ret];return ret+1;
}
inline int cpre(const int& p1,const int& p2,int k)//辅助函数，查询前驱 
{
    for(int i=k-1;bi1[i]==bi1[k];i--)
        if(cnt2[p2][i]-cnt2[p1][i]+tr2[i])return i;
    int p;for(p=bi1[k]-1;(cnt1[p2][p]-cnt1[p1][p]+tr1[p])==0;p--);
    for(int i=Pr[p];;i--)if(cnt2[p2][i]-cnt2[p1][i]+tr2[i])return i;
}
inline int csuf(const int& p1,const int& p2,int k)//辅助函数，查询后继 
{
    for(int i=k+1;bi1[i]==bi1[k];i++)
        if(cnt2[p2][i]-cnt2[p1][i]+tr2[i])return i;
    int p;for(p=bi1[k]+1;(cnt1[p2][p]-cnt1[p1][p]+tr1[p])==0;p++);
    for(int i=Pl[p];;i++)if(cnt2[p2][i]-cnt2[p1][i]+tr2[i])return i;
}
# define ins(x) tr1[bi1[x]]++,tr2[x]++
# define del(x) tr1[bi1[x]]--,tr2[x]--
inline int calc(int l,int r,int k,int(*f)(const int& p1,const int& p2,int k))//这里用了个函数指针 
{
    int p1=bi[l];int p2=bi[r];int ret=0;//直接处理出区间的cnt1,cnt2数组 
    if(p1==p2)
    {
        for(int i=l;i<=r;i++)ins(a[i]);ret=f(p1,p2,k);
        for(int i=l;i<=r;i++)del(a[i]);return val[ret];
    }
    for(int i=l;bi[i]==p1;i++)ins(a[i]);
    for(int i=r;bi[i]==p2;i--)ins(a[i]);ret=f(p1,p2-1,k);
    for(int i=l;bi[i]==p1;i++)del(a[i]);
    for(int i=r;bi[i]==p2;i--)del(a[i]);return val[ret];//记得还原回离散化之前的值 
}
inline void modify(int pos,int y)//暴力修改 
{
    int p=bi1[a[pos]];for(int i=bi[pos];i<=bi[n];i++)cnt1[i][p]--;
    p=a[pos];for(int i=bi[pos];i<=bi[n];i++)cnt2[i][p]--;
    p=bi1[y];for(int i=bi[pos];i<=bi[n];i++)cnt1[i][p]++;
    for(int i=bi[pos];i<=bi[n];i++)cnt2[i][y]++;a[pos]=y;
}
struct opt{int tp;int l;int r;int k;}op[N];
int main()
{
    scanf("%d%d",&n,&m);mp[-2147483647]=1;mp[2147483647]=1;
    for(int i=1;i<=n;i++)scanf("%d",&a[i]),mp[a[i]]=1;
    for(int i=1;i<=m;i++)
    {
        scanf("%d",&op[i].tp);
        if(op[i].tp!=3)scanf("%d%d%d",&op[i].l,&op[i].r,&op[i].k);
        else scanf("%d%d",&op[i].l,&op[i].k);if(op[i].tp!=2)mp[op[i].k]=1;	
    }
    S=mp.size();map <int,int> :: iterator it,it1;//离散化 
    for(it=mp.begin(),it1=it,++it1;it1!=mp.end();++it,++it1)it1->second+=it->second;
    for(it=mp.begin();it!=mp.end();++it)val[it->second]=it->first;
    for(int i=1;i<=n;i++)a[i]=mp[a[i]];
    for(int i=1;i<=m;i++)if(op[i].tp!=2)op[i].k=mp[op[i].k];
    for(int i=1;i<=n;i++)bi[i]=(i-1)/B+1;for(int i=1;i<=S;i++)bi1[i]=(i-1)/B2+1;
    for(int i=1;i<=S;i++)Pr[bi1[i]]=i;for(int i=S;i>=1;i--)Pl[bi1[i]]=i;
    for(int i=1;i<=n;i++)
    {
        int p=bi1[a[i]];for(int j=bi[i];j<=bi[n];j++)cnt1[j][p]++;
        p=a[i];for(int j=bi[i];j<=bi[n];j++)cnt2[j][p]++;
    }ins(1);ins(S);//插入哨兵 
    for(int i=1;i<=m;i++)
        switch(op[i].tp)
        {
            case 1:{printf("%d\n",frk(op[i].l,op[i].r,op[i].k));break;}
            case 2:{printf("%d\n",calc(op[i].l,op[i].r,op[i].k+1,ckth));break;}
            case 3:{modify(op[i].l,op[i].k);break;}
            case 4:{printf("%d\n",calc(op[i].l,op[i].r,op[i].k,cpre));break;}
            case 5:{printf("%d\n",calc(op[i].l,op[i].r,op[i].k,csuf));break;}
        }return 0;//拜拜程序~ 
}


```








