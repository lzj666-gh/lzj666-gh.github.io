# P2858 题解

区间dp

1、
普通的搜索54分。

每一次的抉择是取当前区间的左边还是右边，搜索的边界条件是取到最后只剩下一个元素

代码:




```cpp
#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int n,ans,v[2020];
void dfs(int ste,int l,int r,int sum){
    if(l==r){
        ans=max(ans,sum+v[l]*ste);
        return;
    }
    dfs(ste+1,l+1,r,sum+ste*v[l]);
    dfs(ste+1,l,r-1,sum+ste*v[r]);
}
int main(){
    scanf("%d",&n);ans=0;
    for(int i=1;i<=n;i++)scanf("%d",&v[i]);
    dfs(1,1,n,0);
    cout<<ans<<endl;
    return 0;
}
```
2、记忆化搜索
我们发现之前取的抉择可能不完全一样，但是现在面临同样的状态，那么我们就不需要搜索

多遍，开一个f[l][r]数组，表示区间[l,r]能提供的最大价值，边界条件为取完时，即数列为空时。

代码：




```cpp
#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int n,ans,v[2020],f[2020][2020];
int dfs(int ste,int l,int r){
    if(r<l)return 0;
    if(f[l][r])return f[l][r];
    f[l][r]=max(dfs(ste+1,l+1,r)+ste*v[l],dfs(ste+1,l,r-1)+ste*v[r]);
    return f[l][r];
}
int main(){
    scanf("%d",&n);
    for(int i=1;i<=n;i++)scanf("%d",&v[i]);
    dfs(1,1,n);
    printf("%d",f[1][n]);
    return 0;
}
```
3、记忆化搜索中我们已经看出dp转移方程了。
第一层循环枚举区间长度，第二层循环枚举左端点。

代码：


```cpp
#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int n,f[2017][2017],v[2017];
int main(){
    scanf("%d",&n);
    for(int i=1;i<=n;i++)scanf("%d",&v[i]);
    for(int i=1;i<=n;i++)f[i][i]=v[i]*n;//一开始初始化忘记乘以n 
    for(int i=2;i<=n;i++){
        for(int l=1;l<=n;l++){
            int r=l+i-1;
            if(r>n)break;
            f[l][r]=max(f[l][r-1]+v[r]*(n-i+1),f[l+1][r]+v[l]*(n-i+1));
        }
    }
    printf("%d\n",f[1][n]);
    return 0;
}
```
这篇题解希望能帮助到区间dp入门的同学。