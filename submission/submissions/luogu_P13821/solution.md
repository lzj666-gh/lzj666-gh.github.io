# P13821 题解

感觉挺诈骗的。

就是注意到如果一个点它往下走是墙而无法走到最后一行，那么就一定不能走到。因为操作的方向限定，这个显然是对的。

然后接着把走不到的点填平，相当于把 $a_i$ 减少。

最后填平成满足每一个空点都会被走到的局面，此时容易发现 $a$ 一定是单调不升的。

于是第 $i$ 行的贡献即为后缀最小值。

模拟即可。

```cpp
#include<bits/stdc++.h>
#define int long long
using namespace std;
int ans;
int a[105];
int mini=1e18;
signed main(){
    int n;
    cin>>n;
    for(int i=1;i<=n;i++)
        cin>>a[i];
    for(int i=n;i;i--)
        mini=min(mini,a[i]),ans+=mini;
    cout<<ans;
    return 0;
}
```