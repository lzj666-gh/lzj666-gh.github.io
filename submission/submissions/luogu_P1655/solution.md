# P1655 题解

## 算法分析

- 简单的动态规划，但是要加上高精度运算，不然只能得 $20$ 分。本题和 **[放苹果](https://www.luogu.org/problem/show?pid=2386)** 有些类似，但是盒子不能空着不放，也就是楼下所说的 **Stirling数**，应用于组合数学领域

- ### 状态转移方程：$f[i][j]=f[i-1][j-1]+f[i-1][j]\times j$

## 示例代码

```cpp
#include <bits/stdc++.h>
using namespace std;
const int L = 1001;//调整字符串长度，本题1000足矣
string add(string a,string b)//只限两个非负整数相加
{
    string ans;
    int na[L]={0},nb[L]={0};
    int la=a.size(),lb=b.size();
    for(int i=0;i<la;i++) na[la-1-i]=a[i]-'0';
    for(int i=0;i<lb;i++) nb[lb-1-i]=b[i]-'0';
    int lmax=la>lb?la:lb;
    for(int i=0;i<lmax;i++) na[i]+=nb[i],na[i+1]+=na[i]/10,na[i]%=10;
    if(na[lmax]) lmax++;
    for(int i=lmax-1;i>=0;i--) ans+=na[i]+'0';
    return ans;
}
int na[L];
string mul(string a,int b)//高精度a乘单精度b模板
{
    string ans;
    int La=a.size();
    fill(na,na+L,0);
    for(int i=La-1;i>=0;i--) na[La-i-1]=a[i]-'0';
    int w=0;
    for(int i=0;i<La;i++) na[i]=na[i]*b+w,w=na[i]/10,na[i]=na[i]%10;
    while(w) na[La++]=w%10,w/=10;
    La--;
    while(La>=0) ans+=na[La--]+'0';
    return ans;
}
int n, m;
string f[101][101];
int main(){
    for ( int i = 1; i <= 100; i++ )
    f[i][1] = "1";//初始化，一个盒子（m=1）的时候只有一种放法
    for ( int i = 2; i <= 100; i++ )
    for ( int j = 1; j <= i; j++ )
    f[i][j] = add ( f[i-1][j-1], mul ( f[i-1][j], j ) );//带上高精度运算的状态转移
    while ( cin >> n >> m ){
        if ( n < m ) printf ( "0\n" );//特判输出0
        else cout << f[n][m] << endl;//输出每个n，m对应的答案f[n][m]
    }
    return 0;//华丽落幕
}
```