# P5657 题解

考虑答案的每一位

第`0`位为`011001100110...`

第`1`位为`0011110000111100...`

发现第`i`位即$k\oplus \lfloor\frac k2\rfloor$的第`i`位


```cpp
#include<iostream>
int n;
unsigned long long k;
int main(){
   	std::cin>>n>>k;
    k^=k>>1;
    while(~--n)std::cout<<(k>>n&1);
}
```