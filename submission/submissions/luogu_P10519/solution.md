# P10519 题解

### 1.思路

首先，我们考虑 $\alpha = (t \times v - \lfloor t \times v \rfloor) \times 2 \times \pi$，即衣服转的角度化成弧度制。

再考虑 $dis = \sqrt{x^2+y^2}$，即圆的半径。

那么我们要求的就是以 $dis$ 为腰，以 $\alpha$ 为顶角的等腰三角形的底边 $ans$。

根据[余弦定理](https://baike.baidu.com/item/%E4%BD%99%E5%BC%A6%E5%AE%9A%E7%90%86/957460?fr=ge_ala)，我们有 $ans = \sqrt{dis ^ 2 + dis^2 - 2 \times dis \times dis \times \cos{\alpha}}$。

又因为 STL 里的 ```cos``` 里面的角要填弧度制，所以上文中我们把 $\alpha$ 换算成弧度制。

### 2.代码

```cpp
#include<bits/stdc++.h>
using namespace std;
double x,y,t;
double v;
signed main()
{
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    cin>>x>>y>>t>>v;
    double angle = (t * v - (double)(floor(t * v))) * 2 * 3.1415926535897,dis = sqrt(x * x + y * y);
	cout<<setprecision(10)<<fixed<<sqrt(dis * dis + dis * dis - 2 * dis * dis * cos(angle)); 

    
    return 0;
}
```