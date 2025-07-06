# P3868 题解

####明明是中国剩余定理裸题竟然没有中国剩余定理题解

[中国剩余定理讲解](https://blog.csdn.net/niiick/article/details/80229217)

由题意知


 $$\left\{\begin{aligned}(n-a_1)\mid b_1 \\ (n-a_2)\mid b_2\\ ...\\ (n-a_k)\mid b_k\end{aligned}\right.$$ 

变换成同余方程组得

$$\left\{\begin{aligned}n-a_1\equiv 0(\mod b_1) \\ n-a_2\equiv 0(\mod b_2)\\ ...\\ n-a_k\equiv 0(\mod b_k)\end{aligned}\right.$$ 

根据同余式变换法则，

如果有$a\equiv b(\mod m)$，
则$a+c\equiv b+c(\mod m)$成立

将上述方程组变形得
\begin{cases}
n\equiv a_1(\mod b_1)\quad \\
n\equiv a_2(\mod b_2)\quad \\
...\quad \\
n\equiv a_k(\mod b_k)\quad \\
\end{cases}

 $$\left\{\begin{aligned}n\equiv a_1(\mod b_1)\\ n\equiv a_2(\mod b_2)\\ ...\\ n\equiv a_k(\mod b_k)\end{aligned}\right.$$ 

到这里就是裸得中国剩余定理了
不过要注意计算前要将所有$a[i]=(a[i]\mod b[i]+b[i])\mod b[i];$

另外这题出题人用(sang)心(xin)良(bing)苦(kuang)
要用快速乘，不然最后一个点爆long long
**********************

```
#include<iostream>
#include<cstdio>
#include<vector>
#include<queue>
#include<algorithm>
#include<cstring>
using namespace std;
typedef long long lt;

lt read()
{
    lt f=1,x=0;
    char ss=getchar();
    while(ss<'0'||ss>'9'){if(ss=='-')f=-1;ss=getchar();}
    while(ss>='0'&&ss<='9'){x=x*10+ss-'0';ss=getchar();}
    return x*f;
}

int k;
lt a[20],b[20];

lt qmul(lt a,lt b,lt mod)
{
    lt ans=0;
    while(b>0)
    {
        if(b&1) ans=(ans+a)%mod;
        a=(a+a)%mod;
        b>>=1;
    }
    return ans;
}

void exgcd(lt a,lt b,lt &x,lt &y)
{
    if(b==0){ x=1; y=0; return;}
    exgcd(b,a%b,x,y);
    int tp=x;
    x=y; y=tp-a/b*y;
}

lt china()
{
    lt ans=0,lcm=1,x,y;
    for(int i=1;i<=k;++i) lcm*=b[i];
    for(int i=1;i<=k;++i)
    {
        lt tp=lcm/b[i];
        exgcd(tp,b[i],x,y);
        x=(x%b[i]+b[i])%b[i];
        ans=(ans+qmul(qmul(tp,x,lcm),a[i],lcm))%lcm;//记得快速乘
    }
    return (ans+lcm)%lcm;
}

int main()
{
    k=read();
    for(int i=1;i<=k;++i) a[i]=read();
    for(int i=1;i<=k;++i) b[i]=read();
    for(int i=1;i<=k;i++) a[i]=(a[i]%b[i]+b[i])%b[i];
    cout<<china();
    return 0;
    //niiick
}
```