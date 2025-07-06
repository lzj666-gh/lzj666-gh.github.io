# P1106 题解

我们的思路是这样的：要删m个数，一开始m=k，在左边m+1个数中，找到其中最小的数（如果有多个则选最左边的），记它的位置为t，显然，t左边的l个数都可以删掉，此时还需要删m-l个数，m重新赋值为m-l，而t右边的数是一个新的数列，进行同样的操作，直到选出了n-k个数为止。

证明？我们希望从左开始在尽量大的范围内找到一个最小的数作为结果的第一位，但范围不能超过m+1，否则可能把左边全部m个数删了也无法把找到的数作为第一位，第一位找到后是第二位，同理。。可以，这很贪心

这样做可以每找出一个数就**直接输出**，但还要考虑前导0的问题。以及，若循环结束什么都没输出（意味着答案是0）就在程序结束前输出0。

以下是代码，思路如上：

```cpp
#include<iostream>
#include<string>
using namespace std;
int n,k,a[257],rest,t=1,minp,cnt=0;
bool flag=0;
string num;
int main(){
    cin>>num>>k;
    n=num.length();
    for(int i=1;i<=n;++i)a[i]=num[i-1]-'0';
    rest=n-k;
    while(cnt<rest){
        minp=t;
        for(int i=t;i<=k+t;++i)if(a[minp]>a[i])minp=i;
        if(a[minp])flag=1;
        if(flag)cout<<a[minp];
        k-=minp-t;
        t=minp+1;
        cnt++;
    }
    if(!flag)cout<<0;
    return 0;
}
```