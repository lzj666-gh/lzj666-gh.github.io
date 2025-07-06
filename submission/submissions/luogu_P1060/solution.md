# P1060 题解

背包问题主要是背模板，这里收录了一些模板

一些复杂的背包问题（如泛化物品）未收录

01背包问题：

无优化

```cpp
for(int i=1;i<=n;i++)
{
    for(int c=0;c<=m;c++)
    {
        f[i][c]=f[i-1][c];
        if(c>=w[i])
        f[i][c]=max(f[i][c],f[i-1][c-w[i]]+v[i]);
    }
}
```
一维数组优化：
```cpp
for(int i=1;i<=n;i++)
{
    for(int c=m;c>=0;c--)
    {
        if(c>=w[i])
        f[c]=max(f[c],f[c-w[i]]+v[i]);
    }
}
```
更进一步的常数优化：
```cpp
for(int i=1;i<=n;i++)
{
    sumw+=w[i];
    bound=max(m-sumw,w[i]);
    for(int c=m;c>=bound;c--)
    {
        if(c>=w[i])
        f[c]=max(f[c],f[c-w[i]]+v[i]);
    }
}
```
完全背包问题：
```cpp
for(int i=1;i<=n;i++)
{
    for(int c=0;c<=m;c++)
    {
        if(c>=w[i])
        f[c]=max(f[c],f[c-w[i]]+v[i]);
    }
}
```
多重背包问题：
```cpp
for(int i=1;i<=n;i++)
{
    if(w[i]*a[i]>m)
    {
        for(int c=0;c<=m;c++)
        {
        if(c>=w[i])
        f[c]=max(f[c],f[c-w[i]]+v[i]);
        }
    }
    else
    {
         k=1;amount=a[i];
         while(k<amount)
         {
             for(int c=k*w[i];c>=0;c--)
             {
                 if(c>=w[i])
                 f[c]=max(f[c],f[c-w[i]]+k*v[i]);
             }
             amount-=k;
             k<<=1;
         }  
         for(int c=amount*w[i];c>=0;c--)
         {
             f[c]=max(f[c],f[c-w[i]]+amount*v[i]);
         }
    } 
}
```
下面来到我们的正题：
首先判断是否为背包问题，可见其背包就是money的总数，质量就是重要度\*money

可以套用背包问题

有根据其特性可知这是01背包

到此建模完成，思考+读题用时3min

c++代码：

```cpp
#include<iostream>
#include<algorithm>
using namespace std;
int w[30],v[30],f[50000];//w数组为重要度，v数组为money，f是用来dp的数组
int n,m;//n是总物品个数，m是总钱数
int main()
{
    cin>>m>>n;//输入
    for(int i=1;i<=n;i++)
    {
        cin>>v[i]>>w[i];
        w[i]*=v[i];//w数组在这里意义变为总收获（重要度*money）
    }
       //01背包（参照第二类模板“一维数组优化”）
    for(int i=1;i<=n;i++)
    {
        for(int j=m;j>=v[i];j--)//注意从m开始
        {
            if(j>=v[i])
            {
                f[j]=max(f[j],f[j-v[i]]+w[i]);//dp
            }
        }
    }
    cout<<f[m]<<endl;//背包大小为m时最大值
    return 0;
} 
湖南衡阳OI
```