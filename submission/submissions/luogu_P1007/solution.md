# P1007 题解

此题可以用排序做（高档一点的模拟）

核心思想：两个人相遇转身，相当于交换灵魂后继续走

最大值：最靠近端点两个人各自向对方走,时间较长的那个人的时间

最小值：所有人中走完桥最小值中的最大值

详细见代码：


    
    
    
    
                                 
```cpp
#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;
const int size = 5005;
int a[size];
int main()
{
    int L,N;
    cin>>L>>N;
    if (!N) //特判 N==0的情况 
    {
        cout<<"0 0"<<endl;
        return 0;
    }
    for (int i=1;i<=N;i++) cin>>a[i]; //输入
    sort(a+1,a+N+1); //从小到大排序（算最长时间时可能方便一些）
    int max_time,min_time;
    for (int i=1;i<=N;i++)
        min_time=max(min(a[i],L+1-a[i]),min_time); //最短时间就是所有人中走完桥最小值中的最大值 
    max_time=max(L+1-a[1],a[N]); //最长时间就是最靠近端点两个人各自向对方走,
                                 //时间较长的那个人的时间 （排序的好处）
    cout<<min_time<<' '<<max_time<<endl;
    return 0;
}
还是一道不错的模拟
```