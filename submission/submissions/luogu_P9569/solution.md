# P9569 题解

### 思路

只需求出每一个气球在 $m$ 时刻的高度，再取最大值即可。

这里有一个坑点，那就是如果在 $x$ 时放飞气球，那么它在 $x$ 时高度是已经达到了 $v_i$ 的，易得高度计算式：

$$( T - t_i + 1 ) \times v_i$$

## ACCODE

```cpp
#include<bits/stdc++.h>
using namespace std;
int n , m , p , ans ;
signed main(){
    cin >> n >> m ;
    for( int i = 1 ; i <= n ; i ++ ){
        int u , v ;
        cin >> u >> v ;
        int e = ( m - v + 1 ) * u ;
        if( e > p ){
            p = e ;
            ans = i ;
        }
    }
    cout << ans;
    return 0 ;
}
```