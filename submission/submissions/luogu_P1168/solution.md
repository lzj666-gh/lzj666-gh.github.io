# P1168 题解

$vector$轻松水过

或成此题最短代码？

首先介绍一下$STL$容器$vector$

$vector$基本操作：

$vc.push\_back()$在$vector$末尾插入一个数据

$vc.insert()$在$vecter$中插入一个元素

$vc.erase()$在$vector$中删除一个元素

$vc.at()$在$vector$中获取某个元素($vc[a]$等价于$vc.at(i)$)

因为每次插入后排序时间代价太大，则插入采用$lower\_bound$来二分大于等于该数的数的指针，使得每次插入完都是已经排好序

然后每次插入后，直接输出当前容器内第$\frac{size()-1}{2}$项即可($vector$是从第$0$项开始存储的)

好了，上代码
```
#include <bits/stdc++.h>
using namespace std;
int n;
vector<int>a;
int main()
{
    cin>>n;
    for(int i=1,x;i<=n;i++)
    {
        scanf("%d",&x);
        a.insert(upper_bound(a.begin(),a.end(),x),x);//二分插入保证单调性
        if(i%2==1)
        {
        	printf("%d\n",a[(i-1)/2]);//是奇数个就输出
        }
    }
    return 0;
}
```