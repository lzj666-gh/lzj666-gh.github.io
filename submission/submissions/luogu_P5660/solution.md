# P5660 题解

$\textbf{FFT}$.  
首先这个题目可以转化为给出字符串和 `1` 这个字符串有多少个点可以匹配，那么我们可以用 `P4173 残缺的字符串` 的思路（见 [Link](https://www.luogu.org/blog/Venus/solution-p4173)），分做三次 $\textbf{FFT}$，就可以通过此题了。  
（这个题解说明过少被 ban 了，那就多讲一点）  
我们定义字符串 $S,T$ 的“距离”为  
$$d(S,T)=\sum_{i=1}^n(S_i-T_i)^2\times S_i\times T_i$$
那么可以匹配的条件就是
$$f_i=d(S,T)=0$$
那么我们令 $T$ 为 `1`，对于 $S$ 中每个位置都求出一个 $f_i$，那么问题就是这个 $f_i$ 怎么求。显然可以将距离的式子拆开，变为由三个 $\sum$ 组成的式子，而这三个式子正好是多项式的形式，那么我们就可以用 $\textbf{FFT}$ 分别做三次来求出每个 $f_i$ 的值，最后统计一下就可以出解了。  
（md我在写什么）  
（实测可过，常数巨大）  
代码如下
```cpp
#pragma GCC optimize("Ofast")
#include<bits/stdc++.h>
#define MAXN 2000005
#define reg register
#define inl inline
#define db double
#define eps 1e-6
using namespace std;
const int Mod=998244353;
const db Pi=acos(-1.0);
struct Complex
{
    db x,y;
    friend Complex operator + (const Complex &a,const Complex &b)
    {
        return ((Complex){a.x+b.x,a.y+b.y});
    }
    friend Complex operator - (const Complex &a,const Complex &b)
    {
        return ((Complex){a.x-b.x,a.y-b.y});
    }
    friend Complex operator * (const Complex &a,const Complex &b)
    {
        return ((Complex){a.x*b.x-a.y*b.y,a.x*b.y+a.y*b.x});
    }
    friend Complex operator * (const Complex &a,const db &val)
    {
        return ((Complex){a.x*val,a.y*val});
    }
}f[MAXN],g[MAXN],p[MAXN];
int n,m,lim=1,maxn,rev[MAXN],a[MAXN],b[MAXN],ans;
char S[MAXN],T[MAXN];
bool used[MAXN];
inl void FFT(reg Complex *A,reg int opt)
{
    for(reg int i=0;i<lim;i++) if(i<rev[i]) swap(A[i],A[rev[i]]);
    for(reg int mid=1;mid<lim;mid<<=1)
    {
        reg Complex Wn=((Complex){cos(Pi/(db)mid),(db)opt*sin(Pi/(db)mid)});
        for(reg int j=0;j<lim;j+=(mid<<1))
        {
            reg Complex W=((Complex){1,0});
            for(reg int k=0;k<mid;k++,W=W*Wn)
            {
                reg Complex x=A[j+k],y=W*A[j+k+mid];
                A[j+k]=x+y;
                A[j+k+mid]=x-y;
            }
        }
    }
}
int main()
{
	n=8,m=1,T[1]='1';
    scanf("%s",S+1);
    for(reg int i=1;i<=m;i++) if(T[i]!='*') a[i-1]=T[i]-'0'+1;
    for(reg int i=1;i<=n;i++) if(S[i]!='*') b[i-1]=S[i]-'0'+1;
    while(lim<=(n+m))
    {
        lim<<=1;
        maxn++;
    }
    for(reg int i=0;i<lim;i++) rev[i]=((rev[i>>1]>>1)|((i&1)<<maxn-1));
    reverse(a,a+m);
    for(reg int i=0;i<m;i++) f[i]=((Complex){a[i]*a[i]*a[i],0});
    for(reg int i=0;i<n;i++) g[i]=((Complex){b[i],0});
    FFT(f,1);FFT(g,1);
    for(reg int i=0;i<lim;i++) p[i]=p[i]+f[i]*g[i];
    for(reg int i=0;i<lim;i++) f[i]=g[i]=((Complex){0,0});
    for(reg int i=0;i<m;i++) f[i]=((Complex){a[i]*a[i],0});
    for(reg int i=0;i<n;i++) g[i]=((Complex){b[i]*b[i],0});
    FFT(f,1);FFT(g,1);
    for(reg int i=0;i<lim;i++) p[i]=p[i]-f[i]*g[i]*2.0;
    for(reg int i=0;i<lim;i++) f[i]=g[i]=((Complex){0,0});
    for(reg int i=0;i<m;i++) f[i]=((Complex){a[i],0});
    for(reg int i=0;i<n;i++) g[i]=((Complex){b[i]*b[i]*b[i],0});
    FFT(f,1);FFT(g,1);
    for(reg int i=0;i<lim;i++) p[i]=p[i]+f[i]*g[i];
    FFT(p,-1);
    for(reg int i=m-1;i<n;i++) if(!(int)(p[i].x/(db)lim+0.5)) ans++;
    printf("%d\n",ans);
    return 0;
}
```