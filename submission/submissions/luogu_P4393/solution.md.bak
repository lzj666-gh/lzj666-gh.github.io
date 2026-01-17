# P4393 题解

~~给没想通贪心的~~

先上超简洁代码
```
#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;
int n;
long long ans, a[1000100];
int main()
{
    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }
    for (int i = 1; i < n; i++){
        ans += max(a[i - 1], a[i]);
    }
    cout << ans;
}
```

刚做这道题的时候没看出来是贪心

~~蒟蒻啊蒟蒻~~


时隔这么久，跟机房小伙伴回顾这道题

终于（他）得到了一个比较满意的解释

~~我太菜了，解释老有漏洞~~

“把图呈上来！”~~假装画外音~~

-----=_=废话分割线------------


![](https://cdn.luogu.com.cn/upload/pic/39455.png)


事实上每个数最多只可能被有效加两次（~~想一想，为什么~~）

合并一次后被另一个数合并，或者两边的数都比他小（如图a3）

而看每一边的情况

当一边的数都比a[i]小，最终一定会使a[i]被加一次，如果如图中a3，一侧有a1比a3大，显然在加上a1前会先和a3合并使得结果更优

另一边同理

