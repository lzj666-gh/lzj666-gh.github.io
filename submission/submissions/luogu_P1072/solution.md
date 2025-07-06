# P1072 题解

- LaTex写公式有点麻烦，所以我用以前写好的代替了

- 想看原版可以戳[这里](http://blog.csdn.net/nuclearsubmarines/article/details/77603154)

- 首先来分析一下这个题目



![](https://i.loli.net/2017/08/26/59a16f6ad2018.png)

证明:



![](https://i.loli.net/2017/08/26/59a16fb56c248.png)

- 把上面的结论推广一下，得到结论$P$


>对于两个正整数$a,b$，设$gcd(a,b)=k$，则存在$gcd(a/k,b/k)=1$

- 应用结论$P$



![](https://i.loli.net/2017/08/26/59a170dc98ec0.png)

- 整理一下式子



![](https://i.loli.net/2017/08/26/59a1711685e4f.png)

用心体会这两个式子，你会发现$x$是$a_1$的整数倍而且是$b_1$的因子


~~好像这个由gcd和lcm也可以得到？~~嗯，就这样


于是得到一种解题思路


>$\sqrt b_1$枚举$b_1$的因子(也就是$x$)，如果这个数是$a_1$的整数倍并且满足那两个式子，则$ans++$

- code

```cpp
#include<cstdio>
using namespace std;
int gcd(int a,int b) {
    return b==0?a:gcd(b,a%b);
}
int main() {
    int T;
    scanf("%d",&T);
    while(T--) {
        int a0,a1,b0,b1;
        scanf("%d%d%d%d",&a0,&a1,&b0,&b1);
        int p=a0/a1,q=b1/b0,ans=0;
        for(int x=1;x*x<=b1;x++) 
            if(b1%x==0){
                if(x%a1==0&&gcd(x/a1,p)==1&&gcd(q,b1/x)==1) ans++;
                int y=b1/x;//得到另一个因子
                if(x==y) continue; 
                if(y%a1==0&&gcd(y/a1,p)==1&&gcd(q,b1/y)==1) ans++;
            }
        printf("%d\n",ans);
    }
    return 0;
}
```