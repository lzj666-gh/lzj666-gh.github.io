# P1634 题解

```cpp
#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
 long long x,n,sum=1,i;//long long定义大点
 cin>>x>>n;
 for(i=0;i<n;i++)
  {
   sum=sum+sum*x;//这里是关键,一轮后感染总数为原来总数+新感染的总数                             
  }   
 cout<<sum;   
 return 0;   
}
```