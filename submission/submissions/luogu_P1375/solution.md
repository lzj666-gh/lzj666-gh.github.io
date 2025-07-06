# P1375 题解

这道题感觉有点卡python啊!!!,最后两个点始终过不去.

![](https://cdn.luogu.com.cn/upload/image_hosting/nxqhlmuc.png)

最后只好换上c++.

从题目内容来看，我们~~易知这是一道卡特兰数的模板题~~,卡特兰数一般有以下几个考法(摘自百度)：
```cpp
1：括号化

2：出栈次序

3：凸多边形三角划分

4：给定节点组成二叉搜索树

5：n对括号正确匹配数目
```


**本题属于凸多边形三角划分**

**证明过程**：(我抄我自己的另外一篇题解，也是卡特兰数，只不过是出栈次序，差不多，题目是[P1044 栈](https://www.luogu.org/problem/P1044))

我们已经知道，栈有两种操作，入栈和出栈.对此，我们可以建立一个坐标系.

像这样:

![](https://cdn.luogu.com.cn/upload/image_hosting/n6qtja5n.png)

我们可以把

**黄色的线作为入栈操作，由$(x,y)$变成$(x+1,y+1)$**

**绿色的线作为出栈操作,由$(x,y)$变成$(x+1,y-1)$**

这样，我们就可以把问题抽象为从(0,0)到(2n,0),有多少种合法方案数

我们先来考虑这样一个问题，因为我每一次操作都可以让x+1,那么我总共要进行2n次操作，考虑到最后的栈要为空，所以**入栈次数等于出栈次数=n**,所以方案数则为$C_{2n}^n$.

**但是！！！**
我们这样，会出现非法的情况，也就是线越过x轴的情况（栈已经空了，但是还在弹出元素），也就是这种情况:

![](https://cdn.luogu.com.cn/upload/image_hosting/zgt6vmfu.png)

对于这种情况，我们可以设k为第一次与y=-1那条图线的交点，然后把交点以后的点都关于y=-1对称（即，交换操作1和操作2）

![](https://cdn.luogu.com.cn/upload/image_hosting/z5r69x8g.png)

由于我们现在的终点变成了$(2n,-2)$,所以我们的入栈次数肯定等于出栈次数-2,入栈次数加出栈次数等于2n,所以入栈为n-1次，出栈n+1次，则有不合法的总方案数为$C_{2n}^{n-1}$,所以最终结果为$C_{2n}^{n}$-$C_{2n}^{n-1}$.

根据组合数的定义，

![](https://cdn.luogu.com.cn/upload/image_hosting/xtfqh80e.png)


化简可以得到最终答案为$\frac{(2n)!}{(n+1)!(n)!}$,完结

证明过程大致就这样，最后输出答案的时候记得用乘法逆元，~~乘法逆元应该都会吧~~

**Code**:(自己加了个快乘的板子，怕爆long long)

c++:

```cpp
/**
*    author:  a2954898606
*    created: 2019/10/21 15:20:24
**/
#include<bits/stdc++.h>
#define REP(A,B,I) for(int I=(A);I<=(B);I++)
#define PER(A,B,I) for(int I=(A);I>=(B);I--)
#define LL long long
#define N 1000010
#define M 100
#define mod 1000000007
using namespace std;
long long quickmul(long long a,long long b){///快乘
    a%=mod;b%=mod;
    long long c=(long long)a*b/mod;
    long long ans=a*b-c*mod;
    if(ans<0)ans+=mod;
    else if(ans>=mod)ans-=mod;
    return ans;
}
long long quickpow(long long a,long long b){///快速幂
    long long ret=1;
    while(b){
        if(b&1)ret=ret*a%mod;
        a=a*a%mod;
        b>>=1;
    }
    return ret;
}
long long n;
int main(){
    //read(1)
    //write(1)
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin>>n;
    long long ans1=1,ans2=1,ans3=1,fina=1;
    REP(1,2*n,i){
        if(i<=n)ans2=quickmul(ans2,i);
        if(i<=n+1)ans3=quickmul(ans3,i);
        ans1=quickmul(ans1,i);
    }
    ans2=quickmul(ans2,ans3);
    fina=quickmul(ans1,quickpow(ans2,mod-2));
    cout<<fina<<endl;
    return 0;
}


```

python(只能得80，本人太弱，不能想到什么好的优化方法了):

```python
n=int(input())
m=2*n
m=m+1
a=1
b=1
c=1
for i in range(1,m):
    a=a*i
    if(i<=n):
        b=b*i
    if(i<=n+1):
        c=c*i
b=b*c
b=pow(b,1000000005,1000000007)
ans=int(a*b%1000000007)
print(ans)
```



