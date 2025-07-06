# P1757 题解

正如题目名所说，这是一道分组背包的题

只要在板子上改动一点：求背包的组数（直接在输入时求就行了）

板子的输入：
```cpp
for(i=1;i<=n;i++){
    cin>>w[i]>>z[i]>>x;      //x表示第i个物品的小组编号
    b[x]++;      //小组x的物品+1
    g[x][b[x]]=i;      //g[i][j]表示存储小组i中的第j个物品的编号
}
```
**改动后**的输入：
```cpp
for(i=1;i<=n;i++){
    cin>>w[i]>>z[i]>>x;
    t=max(t,x);      //求小组组数
    b[x]++;
    g[x][b[x]]=i;
    }
```
本题**精髓**：
```cpp
for(i=1;i<=t;i++){      //小组
    for(j=v;j>=0;j--){      //容量
        for(k=1;k<=b[i];k++){      //小组中的物品
            if(j>=w[g[i][k]]){      //小组i中物品k的容量
                dp[j]=max(dp[j],dp[j-w[g[i][k]]]+z[g[i][k]]);      //状态转移方程
            }
        }
    }
}
```
无注释的完整代码:
```cpp
#include<bits/stdc++.h>
using namespace std;
int v,n,t;
int x;
int g[205][205];
int i,j,k;
int w[10001],z[10001];
int b[10001];
int dp[10001];
int main(){
    cin>>v>>n;
    for(i=1;i<=n;i++){
        cin>>w[i]>>z[i]>>x;
        t=max(t,x);
        b[x]++;
        g[x][b[x]]=i;
    }
    for(i=1;i<=t;i++){
        for(j=v;j>=0;j--){
            for(k=1;k<=b[i];k++){
                if(j>=w[g[i][k]]){
                    dp[j]=max(dp[j],dp[j-w[g[i][k]]]+z[g[i][k]]);
                }
            }
        }
    }
    cout<<dp[v];
    return 0;
}
```