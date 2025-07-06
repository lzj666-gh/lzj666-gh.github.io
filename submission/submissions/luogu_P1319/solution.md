# P1319 题解

[更好的阅读体验。](https://blog.csdn.net/Hymmeishili/article/details/148436283?sharetype=blogdetail&sharerId=148436283&sharerefer=PC&sharesource=Hymmeishili&spm=1011.2480.3001.8118)

## 题目分析
我们需要根据给定的压缩码还原出原始的 $n\times n$ 的 **01** 点阵图案。压缩码的第一个数字是 $n$，后续数字交替表示连续的 0 和 1 的个数。

## 解决思路
根据**数字序列**交替填充 0 和 1，第一个数字表示连续的 0 的个数，第二个数字表示连续的 1 的个数，依此类推。

此思路需要双重循环，时间复杂度为 $O(n^2)$，可以接受。

## 代码实现
```cpp
#include <bits/stdc++.h>
using namespace std;
int n,sum,cnt,ct,ans;
int main(){
    cin>>n;
    sum=n*n;
    while(ans<sum){
        cin>>ct;
        for(int i=0;i<ct;i++){
            cout<<cnt;
            ans++;
            if(ans%n==0){
                cout<<endl;
            }
        }
        cnt=1-cnt;// 切换 0 和 1。
    }
    return 0;
}
```