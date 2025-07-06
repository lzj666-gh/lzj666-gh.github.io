# P10026 题解

官方题解。

自评难度介于黄和绿之间。

暂时没考虑到其他做法。

------------

## $\text{Subtask 0} $
对于每次询问暴搜。

## $\text{Subtask 1} $
考虑离线处理，将所有询问按 $k$ 从小到大排序，然后一次 dp 出所有答案。

或者直接记忆化搜索。

复杂度为 $\operatorname{O}(n^2)$。

##### 注：以上复杂度中的 $n$ 仅表示题面中 $n,k$ 的数量级。

## $\text{Subtask 2} $
考虑求出达到 $n$ 的最小次数，然后尝试在过程中浪费一些操作以达到 $k$ 次。

首先特判 $n=0,1$ 的情况。

当 $n\ge 1$ 时，我们可以通过 $1\times2-1=1$ 这样的操作浪费掉任意偶数次。

当 $n\ge 2$ 时，我们还可以通过 $2\times 2-1-1=2$ 这样的操作浪费掉 $3$ 次。

显然可以凑出大于 $1$ 的任意整数。

考虑能否浪费 $1$ 次，显然只有 $a\times2-1-1=(a-1)\times2$。

如果 $n$ 的最短操作中不包括 $(a-1)\times2$，以上方案就无法实现。

此时 $n$ 一定为 $2$ 的幂次或 $2$ 的幂次 $-1$（最多只允许最后有一次 $-1$ 操作）。

根据以上条件即可判断是否可行，复杂度 $\operatorname{O}(T\times\log{n})$。

------------

或许您会不知道如何求达到 $n$ 的最小次数，有一种较简单的思考方法。

转换此题为一个本质完全相同的问题（也是出题人最开始想到的问题）。

给定一个整数 $n$，进行 $k$ 次操作，问最终能否为 $1$。

每次操作从以下两种中选一个：

- $a\gets a+1$
- $a\gets\frac{a}{2}$（$a$ 为偶数时可选）

他们的最小次数也是一样的。

考虑尽可能多的 $a\gets\frac{a}{2}$ 即可。

------------
放一下代码吧。

$30pts$：

```cpp
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll maxn=1e5+84,maxm=4e3+23;
struct Query{
    ll k,n,id;
    bool ans;
    inline void read(ll x){
        scanf("%lld%lld",&k,&n);
        id=x;
        return ;
    }
    friend bool operator<(Query xy,Query zb){
        return xy.k<zb.k;
    }
}q[maxn];
ll T,j;
bitset<maxn> ans,Next;
inline bool cmp(Query xy,Query zb){
    return xy.id<zb.id;
}
int main(){
    scanf("%lld",&T);
    for(ll i=1;i<=T;i++)
        q[i].read(i);
    sort(q+1,q+T+1);
    ans[1]=1;
    j=1;
    for(int i=1;i<=q[T].k+2;i++){
        while(j<=T&&i==q[j].k+1){
            q[j].ans=ans[q[j].n]==1;
            j++;
        }
        Next.reset();
        for(int i=ans._Find_first();i!=ans.size()&&i<=maxm;i=ans._Find_next(i)){
            if(i*2<=maxm)
                Next[i*2]=1;
            if(i>=1)
                Next[i-1]=1;
        }
        ans=Next;
    }
    sort(q+1,q+T+1,cmp);
    for(int i=1;i<=T;i++)
        puts(q[i].ans?"Yes":"No");
    return 0;
}
```

$100pts$：

```cpp
// 哀太可爱辣
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll T,k,n,res,ans;
inline ll Q(ll x){
    res=0;
    while(x!=1){
        if(x&1)
            x++;
        else
            x>>=1;
        res++;
    }
    return res;
}
inline bool check(ll x){
    if(x&1)
        x++;
    return (x&(-x))==x;
}
int main(){
    scanf("%lld",&T);
    while(T--){
        scanf("%lld%lld",&k,&n);
        if(!k)
            puts(n==1?"Yes":"No");
        else if(!n)
            puts("Yes");
        else if(n==1)
            puts(k%2==0||k>=5&&k%2?"Yes":"No");
        else{
            ans=Q(n);
            puts(ans>k||ans+1==k&&check(n)?"No":"Yes");
        }
    }
    return 0;
}
```
