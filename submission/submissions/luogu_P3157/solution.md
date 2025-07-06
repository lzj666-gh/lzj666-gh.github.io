# P3157 题解

此题解法颇多，在下略微讲解其二
其一：离线算法(cdq分治)

我们先找出对答案有贡献的点（i,j）对满足的条件：
$Time_{i}<Time_{j},Val_{i}<Val{j},Pos_{i}>Pos_{j}$
或 $Time_{i}<Time_{j},Val_{i}>Val{j},Pos_{i}<Pos_{j}$

那么这个问题就变成了经典的三维偏序问题，可以通过cdq分治来解决。

时间:$O(n log^2 n)$

空间:$O (n)$

```C++
#include<cstdio>
#include<algorithm>
using namespace std;
typedef long long ll;
int read(){
    int x=0,f=1;char ch=getchar();
    while (ch<'0'||ch>'9') ch=='-'&&(f=-1),ch=getchar();
    while (ch>='0'&&ch<='9') x=x*10+ch-'0',ch=getchar();
    return x*f;
}
const int N=1e5+10;
struct AC{int m,v,d,id,t;}e[N<<1];
int n,m,tot;
int pos[N],a[N],c[N];ll ans[N];
bool cmp1(AC x,AC y){return x.d<y.d;}
void add(int x,int k){while (x<=n)c[x]+=k,x+=(x&(-x));}
int query(int x){int su=0;while(x)su+=c[x],x-=(x&(-x));return su;}
void cdq(int l,int r){
    if (l==r) return;
    int mid=(l+r)>>1,j=l;
    cdq(l,mid),cdq(mid+1,r);
    sort(e+l,e+mid+1,cmp1);
    sort(e+mid+1,e+r+1,cmp1);
    for (int i=mid+1;i<=r;++i){
        while (j<=mid&&e[j].d<=e[i].d)add(e[j].v,e[j].m),++j;
        ans[e[i].id]+=e[i].m*(query(n)-query(e[i].v));
    }
    for (int i=l;i<j;++i) add(e[i].v,-e[i].m);
    j=mid;
    for (int i=r;i>mid;--i){
        while (j>=l&&e[j].d>=e[i].d)add(e[j].v,e[j].m),--j;
        ans[e[i].id]+=e[i].m*query(e[i].v-1);
    }
    for (int i=mid;i>j;--i) add(e[i].v,-e[i].m);
}
int main(){
    n=read(),m=read();
    for (int i=1;i<=n;++i)a[i]=read(),pos[a[i]]=i,e[++tot]=(AC){1,a[i],i,0,tot};
    for (int i=1,x;i<=m;++i)x=read(),e[++tot]=(AC){-1,x,pos[x],i,tot};
    cdq(1,tot);
    for (int i=1;i<=m;++i) ans[i]+=ans[i-1];
    for (int i=0;i<m;++i) printf("%lld\n",ans[i]);
    return 0;
}
```

其二：在线算法(树状数组套线段树)

然而cdq分治是一种离线算法，所以为了防止出题人毒瘤，我们需要进一步学习其在线算法。

下面介绍一种树状数组套线段树的做法。

用树状数组访问位置,用线段树访问权值,每个点的贡献就是与其权值和位置大小关系不等的点的个数

线段树需要动态开点,每次访问最多新开$log^2$个新节点,所以空间是$O(n log^2 n)$的

时间:$O(n log ^2 n)$

空间:$O(n log^2 n)$

```c++
#include<cstdio>
#define ll long long
#define low(x) (x&(-x))
int read(){
    int x=0,f=1;char ch=getchar();
    while (ch<'0'||ch>'9') ch=='-'&&(f=-1),ch=getchar();
    while (ch>='0'&&ch<='9') x=x*10+ch-'0',ch=getchar();
    return x*f;
}
const int N=1e5+10,M=3e7+10;
int n,m,tot;ll ans;
int a[N],pos[N],quea[N],queb[N];
int rt[N],t[M],ls[M],rs[M];
void change(int&p,int l,int r,int x,int y){
    if (!p) p=++tot;t[p]+=y;
    if (l==r) return;
    int mid=(l+r)>>1;
    if (x<=mid) change(ls[p],l,mid,x,y);
    else change(rs[p],mid+1,r,x,y);
}
int query(int l,int r,int x,int mode){
    int cnta=0,cntb=0,sum=0,mid;
    for (int i=l-1;i;i-=low(i)) quea[++cnta]=rt[i];
    for (int i=r;i;i-=low(i)) queb[++cntb]=rt[i];
    l=1,r=n;
    while (l!=r){
        mid=(l+r)>>1;
        if (x>mid) {
            if (mode){
                for (int i=1;i<=cnta;++i) sum-=t[ls[quea[i]]];
                for (int i=1;i<=cntb;++i) sum+=t[ls[queb[i]]];
            }
            for (int i=1;i<=cnta;++i) quea[i]=rs[quea[i]];
            for (int i=1;i<=cntb;++i) queb[i]=rs[queb[i]];
            l=mid+1;
        }
        else{
            if (!mode){
                for (int i=1;i<=cnta;++i) sum-=t[rs[quea[i]]];
                for (int i=1;i<=cntb;++i) sum+=t[rs[queb[i]]];
            }
            for (int i=1;i<=cnta;++i) quea[i]=ls[quea[i]];
            for (int i=1;i<=cntb;++i) queb[i]=ls[queb[i]];
            r=mid;
        }
    }
    return sum;
}
int main(){
    n=read(),m=read();
    for (int i=1;i<=n;++i){
        a[i]=read();pos[a[i]]=i;
        ans+=query(1,i-1,a[i],0);
        for (int j=i;j<=n;j+=low(j)) change(rt[j],1,n,a[i],1);
    }
    printf("%lld\n",ans);
    for (int i=1,x;i<m;++i){
        x=read();
        ans-=query(1,pos[x]-1,x,0);
        ans-=query(pos[x]+1,n,x,1);
        printf("%lld\n",ans);
        for (int j=pos[x];j<=n;j+=low(j)) change(rt[j],1,n,x,-1);
    }
    return 0;
}
```