# AT_joisc2014_c 题解

## 回滚莫队
适用范围：
* 问题可以莫队。（询问可以离线，不带修改）
* 区间伸长的时候很好维护信息
* 区间缩短的时候不太好维护信息（如最大值，删除以后不知道次大值是多少)

怎么做呢？
* 首先，我们把询问按照莫队的顺序排序
* 这样询问被分成了若干个段落。每段内，询问的左端点在同一个块，右端点递增。
* 我们分段来处理：（设这一段的左端点为L[i],右端点是R[i]
* 每一段开始时，$l\leftarrow R[i]+1,r\leftarrow R[i]$，表示初始的空区间。
* 若左右端点都在这个块内的询问，我们直接暴力，显然$O(\sqrt n)$
* 现在，我们可以假定对于所有询问，均有$Q[j].r>R[i]$
* 每处理一个询问，我们先将r移动到该询问的右端点，保存下来此时的信息。
* 将l移动到询问的左端点，此时可以求出答案。
* $l\leftarrow R[i]+1$,用刚才保存的信息来恢复现场。
  
每段内，右端点单调递增，移动的时间复杂度$O(n)$,一共有$\sqrt n$段。左端点在同一块内，移动时间复杂度$O(\sqrt n)$，一共有n个左端点。暴力处理小段询问复杂度$O(\sqrt n)$。所以总的时间复杂度为$O(n\sqrt n)$，不变。而且可以看到，所有的操作都是在扩张区间，避免了收缩区间的麻烦，可以更方便地维护信息。

例题：[AtCoder 1219 历史研究](https://www.luogu.org/problemnew/show/AT1219)
代码在这里~
```cpp
#include <cstdio>
#include <cmath>
#include <cstdint>
#include <cstring>
#include <algorithm>

using std::sort;
using std::unique;
using std::lower_bound;

const int maxn=2e5+100;

int a[maxn],b[maxn];
int L[maxn],R[maxn],blo[maxn];

struct Qry
{
    int l,r,id;
    bool operator< (const Qry& q){return blo[l]==blo[q.l]?r<q.r:l<q.l;}
}Q[maxn];

template<class T>inline T max(T a,T b){return a<b?b:a;}
template<class T>inline T min(T a,T b){return a<b?a:b;}

int cnt[maxn];
int64_t tmp;

inline void add(int x,int val=1)
{
    cnt[a[x]]+=val;
    tmp=max(tmp,(int64_t)cnt[a[x]]*b[a[x]]);
}

inline int64_t brute_force(int l,int r)
{
    static int c[maxn];
    int64_t ans=0;
    for (int i=l;i<=r;++i) ++c[a[i]];
    for (int i=l;i<=r;++i) ans=max(ans,(int64_t)c[a[i]]*b[a[i]]);
    for (int i=l;i<=r;++i) --c[a[i]];
    return ans;
}

int main()
{
    int n,q;
    scanf("%d%d",&n,&q);
    for (int i=1;i<=n;++i)
        scanf("%d",a+i),b[i]=a[i];
    for (int i=1;i<=q;++i)
        scanf("%d%d",&Q[i].l,&Q[i].r),Q[i].id=i;
    sort(b+1,b+n+1);
    int tot=unique(b+1,b+n+1)-b-1;
    // for (int i=1;i<=tot;++i) printf("%d ",b[i]);
    // putchar('\n');
    // printf("%d\n",tot);
    for (int i=1;i<=n;++i)
        a[i]=lower_bound(b+1,b+tot+1,a[i])-b;
    int T=sqrt(n),bl=n/T;
    for (int i=1;i<=bl;++i)
        L[i]=R[i-1]+1,R[i]=L[i]+T-1;
    if (R[bl]<n) ++bl,L[bl]=R[bl-1]+1,R[bl]=n;
    for (int i=1;i<=n;++i)
        blo[i]=(i-1)/T+1;
    sort(Q+1,Q+q+1);
    static int64_t ans[maxn];
    for (int i=1,lp=1,r=0,l=0;i<=bl;++i)
    {
        memset(cnt,0,sizeof(cnt));
        r=R[i];
        tmp=0;
        // for (l=L[i];l<=R[i];++l) add(l,-1);
        while (blo[Q[lp].l]==i)
        {
            l=R[i]+1;
            if (Q[lp].r-Q[lp].l<=T)
            {
                ans[Q[lp].id]=brute_force(Q[lp].l,Q[lp].r);
                ++lp;
                continue;
            }
            while (Q[lp].r>r) add(++r);
            int64_t now=tmp;
            while (l>Q[lp].l) add(--l);
            ans[Q[lp].id]=tmp;
            tmp=now;
            while (l<=R[i]) --cnt[a[l++]];
            ++lp;
        }
    }
    for (int i=1;i<=q;++i) printf("%lld\n",ans[i]);
}
```
