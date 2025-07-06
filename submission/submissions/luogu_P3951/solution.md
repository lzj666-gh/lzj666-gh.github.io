# P3951 题解

### 题目描述


小凯手中有两种面值的金币，两种面值均为正整数且彼此互素。每种金币小凯都有无数个。在不找零的情况下，仅凭这两种金币，有些物品他是无法准确支付的。现在小凯想知道在无法准确支付的物品中，最贵的价值是多少金币？注意：输入数据保证存在小凯无法准确支付的商品。


### 题目链接


[NOIP2017 小凯的疑惑](https://www.luogu.org/problemnew/show/3951)


### 题解


不妨设 $ a < b $


假设答案为 $ x $


若

$$ x \equiv ma \pmod b (1 \leq m \leq b - 1) $$


即

$$ x = ma + nb (1 \leq m \leq b - 1) $$


显然当 $ n \geq 0 $ 时 $ x $ 可以用 $ a, b $ 表示出来，不合题意。


因此当 $ n = -1 $ 时 $ x $ 取得最大值，此时 $ x = ma - b $。


显然当 $ m $ 取得最大值 $ b - 1 $ 时 $ x $ 最大，此时 $ x = (b - 1)a - b = ab - a - b $


因此 $ a, b $ 所表示不出的最大的数是 $ ab - a - b $


### 代码


```cpp
#include <cstdio>

typedef long long ll;

int main(int argc, char *argv[]) {
    freopen("math.in", "r", stdin);
    freopen("math.out", "w", stdout);

    int a, b;
    scanf("%d %d", &a, &b);
    printf("%lld\n", a * b - a - b);
    
    fclose(stdin);
    fclose(stdout);
    return 0;
}
```