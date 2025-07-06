# B2007 题解

输入两个数，并将它们的和输出。
由于不知道数据范围，所以变量开了 long long。
```cpp
#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long a,b,c=0;
    scanf("%lld%lld",&a,&b);
    c=a+b;
    printf("%lld",c);
}
```