# P3812 题解

## 线性基简介

线性基是一种擅长处理异或问题的数据结构.设值域为$[1,N]$，就可以用一个长度为$\lceil \log_2N \rceil$的数组来描述一个线性基。特别地，线性基第$i$位上的数二进制下最高位也为第$i$位。

一个线性基满足，对于它所表示的所有数的集合$S$，$S$中任意多个数异或所得的结果均能表示为线性基中的元素互相异或的结果，即意，线性基能使用异或运算来表示原数集使用异或运算能表示的所有数。运用这个性质，我们可以极大地缩小异或操作所需的查询次数。

## 插入和判断
我们考虑插入的操作，令插入的数为$x$，考虑$x$的二进制最高位$i$，
- 若线性基的第$i$位为$0$，则直接在该位插入$x$，退出；
- 若线性基的第$i$位已经有值$a_i$，则$x = x\oplus a_i$，重复以上操作直到$x=0$。

如果退出时$x=0$，则此时线性基已经可以表示原先的$x$了；反之，则说明为了表示$x$，往线性基中加入了一个新元素。

很容易证明这样复杂度为$\log_2x$，也可以用这种方法判断能否通过原数列异或得到一个数$x$。

```cpp
void ins(ll x){
    for(reg int i=MN;~i;i--)
        if(x&(1ll<<i))
            if(!a[i]){a[i]=x;return;}
            else x^=a[i];
    flag=true;
}
bool check(ll x){
    for(reg int i=MN;~i;i--)
        if(x&(1ll<<i))
            if(!a[i])return false;
            else x^=a[i];
    return true;
}
```

## 查询异或最值
查询最小值相对比较简单。考虑插入的过程，因为每一次跳转操作，$x$的二进制最高位必定单调降低，所以不可能插入两个二进制最高位相同的数。而此时，线性基中最小值异或上其他数，必定会增大。所以，直接输出线性基中的最小值即可。

考虑异或最大值，从高到低遍历线性基，考虑到第$i$位时，如果当前的答案$x$第$i$位为$0$，就将$x$异或上$a_i$；否则不做任何操作。显然，每次操作后答案不会变劣，最终的$x$即为答案。

同样，我们考虑对于一个数$x$，它与原数列中的数异或的最值如何获得。用与序列异或最大值类似的贪心即可解决。
## 查询$k$小值
我们考虑进一步简化线性基。显然，一个线性基肯定可以表示为若干个形如$2^i$的数。从高到低处理线性基每一位，对于每一位向后扫，如果当前数第$i$位为$0$，且线性基第$i$位不为$0$,则将当前数异或上$a_i$。这一操作可以在$O(\log_2^2 n)$的时间内解决。

经过这一步操作后，设线性基内共有$cnt$个数，则它们共可以表示出$2^{cnt}$个数。当然，对于$0$必须特殊考虑。如果插入的总数$n$与$cnt$相等，就无法表示$0$了。

同样，考虑最小值时，也必须要考虑到$0$的情况。事实上，如果插入时出现了未被加入的元素，就肯定可以表示出$0$。

随后，我们考虑将$k$二进制拆分，用与快速幂类似的方法就可以求出第$k$大值。

学过线性代数的同学应该可以看出，这个过程就是对一个矩阵求解异或意义下的秩的过程。因此，$cnt \leq \lceil \log_2N \rceil$一定成立。而最终，线性基中保存的也是异或意义下的一组极小线性无关组。

同样，有关线性基的一切运算都可以看做矩阵的初等行列变换，也就可以将其看做线性规划问题。同样，可以离线使用高斯消元来构造极小线性基。

```cpp
bool flag;//可以表示0
ll qmax(ll res=0){
    for(reg int i=MN;~i;i--)
        res=max(res,res^a[i]);
    return res;
}
ll qmin(ll res=0){
    if(flag)return 0;
    for(reg int i=0;i<=MN;i++)
        if(a[i])return a[i];
}
ll query(ll k){
    reg ll res=0;reg int cnt=0;
    k-=flag;if(!k)return 0;
    for(reg int i=0;i<=MN;i++){
        for(int j=i-1;~j;j--)
            if(a[i]&(1ll<<j))a[i]^=a[j];
        if(a[i])tmp[cnt++]=a[i];
    }
    if(k>=(1ll<<cnt))return -1;
    for(reg int i=0;i<cnt;i++)
        if(k&(1ll<<i))res^=tmp[i];
    return res;
}
```

## 代码
```cpp
#include<bits/stdc++.h>
#define reg register
using namespace std;
typedef long long ll;
const int MN=60;
ll a[61],tmp[61];
bool flag;
void ins(ll x){
    for(reg int i=MN;~i;i--)
        if(x&(1ll<<i))
            if(!a[i]){a[i]=x;return;}
            else x^=a[i];
    flag=true;
}
bool check(ll x){
    for(reg int i=MN;~i;i--)
        if(x&(1ll<<i))
            if(!a[i])return false;
            else x^=a[i];
    return true;
}
ll qmax(ll res=0){
    for(reg int i=MN;~i;i--)
        res=max(res,res^a[i]);
    return res;
}
ll qmin(){
    if(flag)return 0;
    for(reg int i=0;i<=MN;i++)
        if(a[i])return a[i];
}
ll query(ll k){
    reg ll res=0;reg int cnt=0;
    k-=flag;if(!k)return 0;
    for(reg int i=0;i<=MN;i++){
        for(int j=i-1;~j;j--)
            if(a[i]&(1ll<<j))a[i]^=a[j];
        if(a[i])tmp[cnt++]=a[i];
    }
    if(k>=(1ll<<cnt))return -1;
    for(reg int i=0;i<cnt;i++)
        if(k&(1ll<<i))res^=tmp[i];
    return res;
}
int main(){
    int n;ll x;scanf("%d",&n);
    for(int i=1;i<=n;i++)scanf("%lld",&x),ins(x);
    printf("%lld\n",qmax());
    return 0;
}
```