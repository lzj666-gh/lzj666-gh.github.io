# P5721 题解

## [P5721 【深基4.例6】数字直角三角形](https://www.luogu.com.cn/problem/P5721)

### 思路

首先可以知道要输出的是一个第一行为 $n$ 个数，第二行输出 $n-1$ 个数，第三行输出 $n-2$ 个数，最后一行输出 $1$ 个数。一共有 $n$ 行，所以我们可以用两层循环，第一层是遍历第几行的，因为第一行有 $n$ 个数，所以从 $n$ 开始遍历。第二层则是每行有几个数。还要判断前导 $0$ 哦。

### Code


```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    int c=1;
    for (int i=n;i>=1;i--){
        for (int j=1;j<=i;j++){
            if (c<10){
                cout<<"0"<<c;
            }
            else{
                cout<<c;
            }
            c++;
        }
        cout<<endl;
    }
    return 0;
}

```