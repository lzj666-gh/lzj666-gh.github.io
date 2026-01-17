# P4549 题解

据说 NOIP 前发题解会 rp++？我数学这么差当然要让我的数学rp++了！

根据题目可知，这个题目要用裴蜀定理。

## 定理内容
对于任意整数 $a,b,d$，
$$ (a,b)|d \Leftrightarrow \exists \ u,v \ \text{such that}\ ua+vb = d $$

证明可以通过递归构造解来证明：

首先显然当 $u=1,v=0$ 的时候显然成立。

假设存在 $u',v'$,使得 $u'b+v'(a\ mod\ b)=d$.

注意到 $$a\ mod\ b = a-\lfloor\frac{a}{b}\rfloor b$$

可得 $$ u'b + v'(a-\lfloor\frac{a}{b}\rfloor b) = d$$

整理可以得到：
$$ u'b + v'a- v'\lfloor\frac{a}{b}\rfloor b = d$$

$$ v'a + (u'-\lfloor\frac{a}{b}\rfloor v')b = d $$

归纳证明该定理正确。

扩展到求 $ax+by=c$ 的最小非负 $c$,显然 $c$ 要满足 $(a,b)|c$,所以 $c$ 取 $(a,b)$ 是最小的。

扩展到这个题目，如果有多个数字的话，考虑前两个数字 $a_1,a_2$,有 $a_1x+a_2y=S \Rightarrow (a_1,a_2)|d$,$ k(a_1,a_2) =d$

所以把这两个的答案合并直接去取下一个就可以了。

注意到这个题目有负数输入，将其取绝对值就可以了。因为系数的最终答案没有影响。

## 代码
```c++
#include <algorithm>
#include <iostream>
#include <cstring>
#include <climits>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
#define Re register
#define LL long long
#define U unsigned
#define FOR(i,a,b) for(Re int i = a;i <= b;++i)
#define ROF(i,a,b) for(Re int i = a;i >= b;--i)
#define SFOR(i,a,b,c) for(Re int i = a;i <= b;i+=c)
#define SROF(i,a,b,c) for(Re int i = a;i >= b;i-=c)
#define CLR(i,a) memset(i,a,sizeof(i))
#define BR printf("--------------------\n")
#define DEBUG(x) std::cerr << #x << '=' << x << std::endl
namespace fastIO{
    #define BUF_SIZE 100000
    #define OUT_SIZE 100000
    #define ll long long
    bool IOerror=0;
    inline char nc(){
        static char buf[BUF_SIZE],*p1=buf+BUF_SIZE,*pend=buf+BUF_SIZE;
        if (p1==pend){
            p1=buf; pend=buf+fread(buf,1,BUF_SIZE,stdin);
            if (pend==p1){IOerror=1;return -1;}
        }
        return *p1++;
    }
    inline bool blank(char ch){return ch==' '||ch=='\n'||ch=='\r'||ch=='\t';}
    inline void read(int &x){
        bool sign=0; char ch=nc(); x=0;
        for (;blank(ch);ch=nc());
        if (IOerror)return;
        if (ch=='-')sign=1,ch=nc();
        for (;ch>='0'&&ch<='9';ch=nc())x=x*10+ch-'0';
        if (sign)x=-x;
    }
    inline void read(ll &x){
        bool sign=0; char ch=nc(); x=0;
        for (;blank(ch);ch=nc());
        if (IOerror)return;
        if (ch=='-')sign=1,ch=nc();
        for (;ch>='0'&&ch<='9';ch=nc())x=x*10+ch-'0';
        if (sign)x=-x;
    }
    #undef ll
    #undef OUT_SIZE
    #undef BUF_SIZE
};
using namespace fastIO;

int N,gcd;
int main(){
    read(N);
    FOR(i,1,N){
        if(i==1) read(gcd);
        else{
            int x;read(x);x = std::abs(x);
            gcd = std::__gcd(gcd,x);
        }
    }
    printf("%d\n",gcd);
    // system("pause");
    return 0;
}
```