# P4074 题解

## [题意](https://blog.csdn.net/BeNoble_/article/details/79770456)

给你一棵树,每个点有个颜色

每次询问你一条路径求$\sum_{c}val_c\sum_{i=1}^{cnt_c}worth_i$

>$val$表示该颜色的价值,$cnt$表示其出现的次数,$woeth_i$表示第$i$次出现的价值

带修改

---

## 题解

先求出$dfs$序把树变成序列

考虑向右扩展一个点,这个贡献我们是可以$O(1)$算出来的

>假设扩展出的点是的颜色是$c,$那么$\Delta=val_c\times worth_{cnt_{c+1}}$

所以可以考虑用带修改~~树上~~莫队来求

但是直接用$dfs$序去扩展的话显然会出问题

因为他会先去扫完起点的子树,产生多余的贡献

考虑怎么去掉多余的贡献,把树变成一个长$2n$括号序列

这样的话扫的过程中起点的子树里的点肯定会被扫两次(一进一出)

连续做两次之后贡献为$0$,我们可以想到异或

>即开一个$vis$数组,每次访问就一个点$u$,就$vis_u$^$=1$

但是注意到几个问题

$1.$如果$lca$不是路径端点是不会被计算的

>考虑样例的括号序列$12443321$

>询问$4\to3$,那么我们得到的区间是$[3,5]$

>发现$2$没有被算进来,这个要特判

>当然如果起点就是$lca$就不需要管了

$2.$如果起点不是$lca$,那么他的贡献是不会被计算的

>同样是上面那个例子

>我们可以看到$4$的贡献被算两次抵消掉了

>所以这种情况也要特判

修改和普通带修改莫队一样,只要加一维时间即可

```
#include<bits/stdc++.h>
#define fp(i,a,b) for(register int i=a,I=b+1;i<I;++i)
#define fd(i,a,b) for(register int i=a,I=b-1;i>I;--i)
#define go(u) for(register int i=fi[u],v=e[i].to;i;v=e[i=e[i].nx].to)
#define file(s) freopen(s".in","r",stdin),freopen(s".out","w",stdout)
template<class T>inline bool cmax(T&a,const T&b){return a<b?a=b,1:0;}
template<class T>inline bool cmin(T&a,const T&b){return a>b?a=b,1:0;}
using namespace std;
char ss[1<<17],*A=ss,*B=ss;
inline char gc(){return A==B&&(B=(A=ss)+fread(ss,1,1<<17,stdin),A==B)?-1:*A++;}
template<class T>inline void sd(T&x){
    char c;T y=1;while(c=gc(),(c<48||57<c)&&c!=-1)if(c==45)y=-1;x=c-48;
    while(c=gc(),47<c&&c<58)x=x*10+c-48;x*=y;
}
char sr[1<<21],z[20];int C=-1,Z;
inline void Ot(){fwrite(sr,1,C+1,stdout),C=-1;}
template<class T>inline void we(T x){
    if(C>1<<20)Ot();if(x<0)sr[++C]=45,x=-x;
    while(z[++Z]=x%10+48,x/=10);
    while(sr[++C]=z[Z],--Z);sr[++C]='\n';
}
const int N=2e5+5;
typedef int arr[N];
typedef long long ll;
struct Q{
    int l,r,x,y,z,id;
    inline bool operator<(const Q b)const{
        if(x^b.x)return x<b.x;
        if(y^b.y)return x&1?y<b.y:y>b.y;
        return (x^y)&1?z<b.z:z>b.z;
    }
}q[N];
struct T{int x,c;}t[N];
struct eg{int nx,to;}e[N];
int n,m,ce,dft,Sz,Sq,St,L,R,G;arr fa,fi,sz,val,wor,pos,lis,dep,son,top,col,vis,cnt;ll Now,ans[N];
void dfs(int u){
    dep[u]=dep[fa[u]]+(sz[u]=1);
    go(u)if(v^fa[u]){
        fa[v]=u;dfs(v),sz[u]+=sz[v];
        if(sz[v]>sz[son[u]])son[u]=v;
    }
}
void dfs(int u,int t){
    top[u]=t;lis[pos[u]=++dft]=u;
    if(son[u])dfs(son[u],t);
    go(u)if(v^fa[u]&&v^son[u])dfs(v,v);
    lis[++dft]=u;
}
inline int lca(int u,int v){
    for(;top[u]^top[v];dep[top[u]]>dep[top[v]]?u=fa[top[u]]:v=fa[top[v]]);
    return dep[u]<dep[v]?u:v;
}
inline void add(int u,int v){e[++ce]={fi[u],v},fi[u]=ce;}
inline void sol(int x){int c=col[x];
    (vis[x]^=1)?Now+=(ll)wor[++cnt[c]]*val[c]:Now-=(ll)wor[cnt[c]--]*val[c];
}
inline void mdy(int i){
    int u=t[i].x,x=t[i].c,y=col[u];
    vis[u]?Now+=(ll)wor[++cnt[x]]*val[x]-(ll)wor[cnt[y]--]*val[y]:0;
    t[i].c=y,col[u]=x;
}
int main(){
    #ifndef ONLINE_JUDGE
        file("s");
    #endif
    sd(n),sd(m);int x,y,u,v,g=0;sd(x);
    fp(i,1,m)sd(val[i]);
    fp(i,1,n)sd(wor[i]);m=x;
    fp(i,2,n)sd(u),sd(v),add(u,v),add(v,u);
    fp(i,1,n)sd(col[i]);
    dfs(1),dfs(1,1);
    while(m--){
        sd(x);
        if(x){
            sd(x),sd(y);if(pos[x]>pos[y])swap(x,y);
            q[++Sq]={x,y,pos[x],pos[y],St,Sq};
        }else sd(x),sd(y),t[++St]={x,y};
    }Sz=pow(n,St?2.0/3:1.0/2);
    fp(i,1,Sq)q[i].x/=Sz,q[i].y/=Sz;
    sort(q+1,q+Sq+1);L=pos[q[1].l],R=L-1;
    fp(i,1,Sq){
        x=pos[u=q[i].l],y=pos[v=q[i].r],g=q[i].z;
        while(L>x)sol(lis[--L]);
        while(R<y)sol(lis[++R]);
        while(L<x)sol(lis[L++]);
        while(R>y)sol(lis[R--]);
        while(G<g)mdy(++G);
        while(G>g)mdy(G--);
        int p=lca(u,v);
        if(u^p){sol(u);if(v^p)sol(p);}
        ans[q[i].id]=Now;
        if(u^p){sol(u);if(v^p)sol(p);}
    }
    fp(i,1,Sq)we(ans[i]);
return Ot(),0;
}
```