# P3759 题解

大家好，我用$O(n^2)$**暴力**过了这道题，特地来分享一波卡常技巧。不喜请轻喷。


首先看到数据范围只有$5W$，而且时间居然开了$5s$，这是我们暴力的前提。

这里默认大家都理解了这道题的意思，然后就是我的一些经验了。

1、++i 比 i++ 要快。

2、语句数量要尽量少，能压成一句话就要压。

3、能不用$ long\;long $就别用，只有在需要的地方开。

4、$while$ 循环速度要比 $for$ 循环速度快好多。

5、**尽量不要取模!!**，先估算一下时机，到快要爆$long\;long$ 的时候再取模！（会快很多）

6、别忘了打开各种优化开关。以下是模板。

```cpp
%:pragma GCC optimize(3)
%:pragma GCC optimize("Ofast")
%:pragma GCC optimize("inline")
%:pragma GCC optimize("-fgcse")
%:pragma GCC optimize("-fgcse-lm")
%:pragma GCC optimize("-fipa-sra")
%:pragma GCC optimize("-ftree-pre")
%:pragma GCC optimize("-ftree-vrp")
%:pragma GCC optimize("-fpeephole2")
%:pragma GCC optimize("-ffast-math")
%:pragma GCC optimize("-fsched-spec")
%:pragma GCC optimize("unroll-loops")
%:pragma GCC optimize("-falign-jumps")
%:pragma GCC optimize("-falign-loops")
%:pragma GCC optimize("-falign-labels")
%:pragma GCC optimize("-fdevirtualize")
%:pragma GCC optimize("-fcaller-saves")
%:pragma GCC optimize("-fcrossjumping")
%:pragma GCC optimize("-fthread-jumps")
%:pragma GCC optimize("-funroll-loops")
%:pragma GCC optimize("-fwhole-program")
%:pragma GCC optimize("-freorder-blocks")
%:pragma GCC optimize("-fschedule-insns")
%:pragma GCC optimize("inline-functions")
%:pragma GCC optimize("-ftree-tail-merge")
%:pragma GCC optimize("-fschedule-insns2")
%:pragma GCC optimize("-fstrict-aliasing")
%:pragma GCC optimize("-fstrict-overflow")
%:pragma GCC optimize("-falign-functions")
%:pragma GCC optimize("-fcse-skip-blocks")
%:pragma GCC optimize("-fcse-follow-jumps")
%:pragma GCC optimize("-fsched-interblock")
%:pragma GCC optimize("-fpartial-inlining")
%:pragma GCC optimize("no-stack-protector")
%:pragma GCC optimize("-freorder-functions")
%:pragma GCC optimize("-findirect-inlining")
%:pragma GCC optimize("-fhoist-adjacent-loads")
%:pragma GCC optimize("-frerun-cse-after-loop")
%:pragma GCC optimize("inline-small-functions")
%:pragma GCC optimize("-finline-small-functions")
%:pragma GCC optimize("-ftree-switch-conversion")
%:pragma GCC optimize("-foptimize-sibling-calls")
%:pragma GCC optimize("-fexpensive-optimizations")
%:pragma GCC optimize("-funsafe-loop-optimizations")
%:pragma GCC optimize("inline-functions-called-once")
%:pragma GCC optimize("-fdelete-null-pointer-checks")
```
当你把上面的优化都用到之后，你的程序就可以轻松 $AC$ 这道题了。最慢一个点只跑了 $4s$。

```cpp
#include<bits/stdc++.h>
#define N 50001
using namespace std;

inline void rd(int &X){
    X=0;char ch=0;
    while(!isdigit(ch))ch=getchar();
    while( isdigit(ch))X=(X<<3)+(X<<1)+(ch^48),ch=getchar();
}

int n,m,p=1e9+7,i;
long long l1,r1,ans;
int f[N],g[N],x[N],y[N],l,r;

inline void add(int x,int y){
    for(;x;x-=x&-x) f[x]+=y,g[x]++;
}
inline void ask(int x){
    for(l1=r1=0;x<=n;x+=x&-x) l1+=f[x],r1+=g[x];
}
signed main()
{
    rd(n);rd(m);
    for(i=1;i<=n;++i) rd(x[i]),rd(y[i]),ask(x[i]),add(x[i],y[i]),ans+=l1+r1*y[i];
    while(m--)
    {
          rd(l);rd(r); if(l>r) swap(l,r); i=l+1;
          while(i<r)
          {
              if(x[i]>x[l]) ans+=y[i]+y[l];
              if(x[i]<x[r]) ans+=y[i]+y[r];
              if(x[i]<x[l]) ans-=y[i]+y[l];
              if(x[i]>x[r]) ans-=y[i]+y[r];
              ++i;
          }
          if(x[l]>x[r]) ans-=y[l]+y[r];
          if(x[l]<x[r]) ans+=y[l]+y[r];
          swap(x[l],x[r]);swap(y[l],y[r]);
          printf("%lld\n",ans=(ans%p+p)%p);
        }
}
```
**后记：**

暴力过数据结构题，你并不会收获什么，~~只能获得成就感~~。所以有时候还是需要自己手敲代码的，这片题解仅供大家娱乐和参考。

不过，反正快乐就行了呗（逃~