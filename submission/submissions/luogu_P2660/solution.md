# P2660 题解

一个数学迭代，类似于GCD。

具体详见代码和注释。

```cpp
#include<bits/stdc++.h>
using namespace std;
int main(){
    long long x,y,ans=0;
    cin>>x>>y;
    while(x&&y){                          //如果x,y中有一个为0，就结束了
                swap(x,y);                        //交换x和y，为什么？马上就知道了
                ans+=4*y*(x/y);              //种完剩下的所有最大的正方形。很像GCD是不是？
                x%=y;                             //然后x就只剩下x%y了，因为x%y<y，所以之前需要交换
    }
    cout<<ans;
    return 0;
}
```