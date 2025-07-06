# P1198 题解

2019.7.28

upd:今天突然发现了一个错误...真的非常抱歉，本人当时很菜（现在也是），请各位见谅

这道题中，st表应该是用$f[i][j]$**表示**区间$[i....i-(2^j)+1]$的最值，否则就不能支持插入一个数这样的修改了。

对此感到很抱歉

---------------------------------------------------

看了很多AC的OIer基本是用**线段树**的。

这里就感觉用线段树有点**大材小用**了。

这里我就讲一下**ST表**的方法。

题目有**插入**和**询问**两个操作。

注意看题面，每次的插入是**无脑在序列的尾端插入**的，所以就可以用ST表了。

那么，这是为什么呢？

我们先看ST表的**定义**：

ST算法是用来求解**给定区间RMQ的最值**，用**f[i][j]**表示**区间[i....i+(2^j)-1]**的最值。

从中我们可以看出，当在尾端插入一个新数时，并不会**影响之前所建立的ST表**。
所以我们就可以用**log(n)的时间复杂度**来修改ST表了。

附上代码。

```cpp
#include <cstdio>
#include <cmath>
#include <iostream>
#include <cstring>
#define ll long long
using namespace std;
ll a[200001],f[200001][21],t,D;
int n,m;
bool flag;
void change(int u){  //用change函数来进行修改
    f[u][0]=a[u];
    for(int i=1;u-(1<<i)>=0;i++) f[u][i]=max(f[u][i-1],f[u-(1<<(i-1))][i-1]);
}
ll find(int x,int y){
    double t=log(y-x+1)/log(2);
    int K=t;
    return max(f[y][K],f[x+(1<<K)-1][K]);
}
int main(){
    memset(f,0,sizeof(f));
    scanf("%d%lld",&m,&D);
    for (int i=1;i<=m;i++){
        char c;
        cin>>c;
        ll x;
        if (c=='A'){  //根据题面的操作，注意细节。
            scanf("%lld",&x);
            a[++n]=(x+t)%D;
            change(n);
        }else{
            int L; scanf("%d",&L);
            ll ans;
            if (L==1){
                printf("%lld\n",a[n]);
                t=a[n]; continue;
            }
            ans=find(n-L+1,n);
            printf("%lld\n",ans); t=ans;
        }
    }
    return 0;
}
```
完结散花