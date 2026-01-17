# P2617 题解

类似算法总结

**1、静态整体Kth**

滑稽吧...sort一遍就好了。

时间复杂度$O(nlogn)$    空间复杂度$O(n)$

**2、动态整体Kth**

离散化后开一棵权值线段树，每个位置的值表示这个位置对应的那个数（离散化后的）有多少个，向上维护和；

查询时先查询左子树和sum，比较k和sum的大小：若k<=sum则说明第k小数在左子树中，递归查询左子树；

否则，这个数对应的就是右子树中第k-sum小的数，k-=sum，递归查询右子树。

时间复杂度$O(nlogn)$    空间复杂度$O(n)$

**3、静态区间Kth**

对每个点以其前缀开一棵权值线段树，那么任意一段区间均可以表示成为两棵权值线段树作差，即R位置的线段树减去L-1位置上的线段树

每个点开一棵线段树空间复杂度$O(n^2)$，MLE，考虑到后一个位置相比于前一个位置的更改只有$logn$个节点，所以使用主席树

时间复杂度$O(nlogn)$    空间复杂度$O(nlogn)$

**4、动态区间Kth**(就是本题辣)

还是要想办法维护前缀和。如果只是同3、的前缀和的话，就要对前缀和进行$O(nlogn)$的单次修改，显然TLE。

这里考虑用树状数组维护前缀和。修改时，可以只修改$logn$个位置，复杂度$O(log^2n)$；

查询时，依旧是R位置减去L-1位置，这时候不再是两棵线段树作差，而是log棵线段树与log棵线段树作差；跳的时候，log个节点一起跳到左子树/右子树

时间复杂度$O(nlog^2n)$    空间复杂度$O(nlogn)$

```cpp
#include<cstdio>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
using namespace std;
const int MAX=10005;
struct segment_tree{int v;int ls,rs;}t[MAX*400];//线段树开nlogn大小
struct operation{bool b;int l,r,k;int pos,t;}q[MAX];//因为要离散花所以要把所有数据输进来离线搞
int n,m,a[MAX],o[MAX<<1],rt[MAX],len,tot,temp[2][20],cnt[2];
char opt;
void Modify(int &now,int l,int r,int pos,int val)
{
    if (!now) now=++tot;
    t[now].v+=val;
    if (l==r) return;
    int mid=l+r>>1;
    if (pos<=mid) Modify(t[now].ls,l,mid,pos,val);
    else Modify(t[now].rs,mid+1,r,pos,val);
}
void prepare_Modify(int x,int val)
{
    int k=lower_bound(o+1,o+len+1,a[x])-o;
    for (int i=x;i<=n;i+=i&-i) Modify(rt[i],1,len,k,val);//处理出需要修改哪log棵主席树
}
int Query(int l,int r,int k)
{
    if (l==r) return l;
    int mid=l+r>>1,sum=0;
    for (int i=1;i<=cnt[1];i++) sum+=t[t[temp[1][i]].ls].v;
    for (int i=1;i<=cnt[0];i++) sum-=t[t[temp[0][i]].ls].v;
    if (k<=sum)
    {
        for (int i=1;i<=cnt[1];i++) temp[1][i]=t[temp[1][i]].ls;
        for (int i=1;i<=cnt[0];i++) temp[0][i]=t[temp[0][i]].ls;
        return Query(l,mid,k);
    }
    else
    {
        for (int i=1;i<=cnt[1];i++) temp[1][i]=t[temp[1][i]].rs;
        for (int i=1;i<=cnt[0];i++) temp[0][i]=t[temp[0][i]].rs;
        return Query(mid+1,r,k-sum);
    }
}
int prepare_Query(int l,int r,int k)
{
    memset(temp,0,sizeof(temp));//同修改，处理出需要进行相减操作的是哪log棵主席树
    cnt[0]=cnt[1]=0;
    for (int i=r;i;i-=i&-i) temp[1][++cnt[1]]=rt[i];
    for (int i=l-1;i;i-=i&-i) temp[0][++cnt[0]]=rt[i];
    return Query(1,len,k);
}
int main()
{
    ios::sync_with_stdio(false);
    cin>>n>>m;
    for (int i=1;i<=n;i++) cin>>a[i],o[++len]=a[i];
    for (int i=1;i<=m;i++)
    {
        cin>>opt;
        q[i].b=(opt=='Q');
        if (q[i].b)    cin>>q[i].l>>q[i].r>>q[i].k;
        else cin>>q[i].pos>>q[i].t,o[++len]=q[i].t;
    }
    sort(o+1,o+len+1);
    len=unique(o+1,o+len+1)-o-1;//离散 —— 排序 + 去重
    for (int i=1;i<=n;i++) prepare_Modify(i,1);
    for (int i=1;i<=m;i++)
    {
        if (q[i].b)    printf("%d\n",o[prepare_Query(q[i].l,q[i].r,q[i].k)]);
        else
        {
            prepare_Modify(q[i].pos,-1);
            a[q[i].pos]=q[i].t;
            prepare_Modify(q[i].pos,1);
        }
    }
    return 0;
}
```