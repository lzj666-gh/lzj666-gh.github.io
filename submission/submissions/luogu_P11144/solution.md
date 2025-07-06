# P11144 题解

将题目进一步形式化：

输出 $p_1 $和 $p_2$ ，评测机会给出对应的 $r_1$ 和 $r_2$ 

$m \bmod p_1 = r_1$

$m \bmod p_2 = r_2$

我们令

$p1 = 4 \times 10^8$

$p2 = p1 - 1$

相邻两数必然互素， $p_1 , p_2$ 互素。

构造一组 $k_1,k_2$ 
使得：

$k_1p_2 \bmod p_1 = r_1$

$k_2p_1 \bmod p_2 = r_2$

得：$k_1 = p_1 - r_1,k_2 = r_2$  即可满足

所以 $m = [(p_1 - r_1)p_2 + p_1r_2]  \bmod p_1p_2$

代码：

```cpp
#include <iostream>

typedef long long LL;

const LL Max = 4e8;
const LL mod = (LL)1e17 + 1;

int main(){

    std::cin.tie(0)->sync_with_stdio(0);

    int T;

    for (std::cin >> T;T--;){

        LL res1,res2;

        std::cout << "? " << Max << std::endl;
        std::cin >> res1;
        std::cout << "? " << Max - 1 << std::endl;
        std::cin >> res2;
        std::cout << "! " << (Max * res2 + (Max - 1) * Max - (Max - 1) * res1) % (Max * (Max - 1)) << '\n';

    }

    return 0;
}
```