# P1372 题解

此题简化后，求的是：从1~n中取k个数，使这k个数的最大公约数最大

因为两个数成倍数关系时，它们的最大公因数是两数中的较小数，也就是相对来说最大公因数较大

返回题目，这k个数其实就是：x\*1,x\*2......x\*k，及x的1~k倍，但必须保证x\*k小于n，在上述条件下，能知道，符合条件的最大的x就是答案，为了找出最大的x，必须使x\*k尽量接近n，因为c++的整数除法有自动取整的功能，所以所有情况下，n/k都是最终答案

```cpp
#include<iostream>
#include<cstdio>
using namespace std;
long long n,k;
int main()
{
    cin>>n>>k;
    cout<<n/k;
    return 0;
}
```