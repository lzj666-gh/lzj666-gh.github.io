# P4331 题解

正好一年前做的这道题，趁着自己快退役了翻了翻记录，找到了这题。

看了一圈题解都是可并堆……我捉摸着这也不需要这么复杂的数据结构呀。

于是有了这篇题解，使用STL的堆就可以完成此题。

首先是一个显然的DP。

$f[i][j]$表示前i个数字，其中最后一个数字小于等于j，最优答案是多少。

考虑转移，考虑转移

首先让$f[i][j] = f[i-1][j] + |a[i] - j|$

然后再让$f[i][j] = min(f[i][j],f[i][j-1])$

如果我们得到这个dp数组，用一般的方法就可以倒着推回去得到方案。

其实$f[i][j]$其实是一个斜率单调以1递减的折线。我们只需要知道拐点就可以了。

考虑加入一个绝对值函数，如果在之前斜率为0的直线上，相当于这个左边斜率减一，否则相当于右边的斜率都加一（这时候斜率为为-1的就没啦，和右边并起来了）。

我们用堆来维护折线的拐点的横坐标即可。

一年前的代码，有点丑见谅。
```C++
#include<bits/stdc++.h>
#pragma comment(linker, "/stack:200000000")
#pragma GCC optimize("Ofast")
#pragma target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
using namespace std;
typedef long long ll;
#define Rep(i,a,b) for(register int i=(a);i<=int(b);++i)
#define Dep(i,a,b) for(register int i=(a);i>=int(b);--i)
#define rep(i,a,b) for(register int i=(a);i<int(b);++i)
#define mem(x,v) memset(x,v,sizeof(x))
#define fi first
#define se second
#define debug(x) cout << #x" = " << x << endl;
#define pp(x,y) cout << "pp: " << x << " " << y << endl;
namespace IO{
    const int L=1<<15;char ibuf[L|1],*iS=ibuf,*iT=ibuf,obuf[L|1],*oS=obuf,*oT=obuf+L,c,st[66];int tp=0,f;
    inline char gc(){if(iS==iT) iT=(iS=ibuf)+fread(ibuf,sizeof(char),L,stdin);return (*iS++);}
    inline void flush(){fwrite(obuf,sizeof(char),oS-obuf,stdout);oS = obuf;}
    inline void pc(char c){*oS++=c;if(oS==oT) flush();}
    inline ll read(){ll x=0;f=1,c=gc();for(;!isdigit(c);c=gc())if(c=='-')f=-1;for(;isdigit(c);c=gc())x=(x<<1)+(x<<3)+(c&15);return x*f;}
    inline void write(ll x){if(!x) pc('0');if(x<0) pc('-'),x=-x;while(x) st[++tp]=x%10+'0',x/=10;while(tp) pc(st[tp--]);}
    inline void writeln(ll x){write(x);pc('\n');}
    struct IOflusher{~IOflusher(){flush();}}_ioflusher_;
}using IO::read;using IO::write;using IO::writeln;using IO::gc;using IO::pc;
int n,m,ans,x;
priority_queue<int>q;
int a[1000005],b[1000005];
signed main(){
    n=read();q.push(b[1] = read()-1);
    a[1] = q.top();
    Rep(i,2,n){
        x=read()-i;
        q.push(b[i] = x);
        if (q.top()>x){
            ans+=q.top()-x;
            q.pop();q.push(x);
        }
        a[i] = q.top();
    }
    for(int i=n-1;i>=1;i--) a[i]=min(a[i],a[i+1]);
    ll res = 0;
    for(int i=1;i<=n;++i) res += abs(a[i]-b[i]);
    writeln(res);
    for(int i=1;i<=n;i++)
        write(a[i]+i),pc(' ');
    return 0;
}

```