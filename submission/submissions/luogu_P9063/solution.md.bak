# P9063 题解

# [yLOI2023] A 分解只因数

> 出题人小黑子树脂 66

## Description

对一个正整数 $n$，如果它只含奇质因子，则称它是『只因数』。

有 $T$ 组数据，每次给定 $n$，请判定 $n$ 是不是只因数。

$T \leq 9$，$2 \leq n \leq 10^{18}$。

## Analysis

### 算法 0

~~根据生活经验，『只因』常被空耳为『ji』音。于是合理推测『只因数』就是奇数。~~

### 算法 1

$n \leq 10$ 时，手算打表一下就可以。期望得分 $50$ 分。

### 算法 2

$n \leq 10^9$ 时，可以 $O(\sqrt n)$ 暴力枚举质因子然后做判断。以下是一个简单的枚举质因子程序：

```cpp
bool isChicken(const int n) {
  int m = n;
  for (int i = 1; i * i <= n; ++i) while (m % i == 0) {
    m /= i;
    if (isEven(i)) return false; // isEven 判断 i 是不是偶数
  }
  if (isEven(m)) return false;
  return true;
}
```

共 $T$ 组数据，于是总时间复杂度为 $O(T \sqrt n)$。期望得分 $90$ 分。

### 算法 3

考察质数的特点：偶质数有且仅有 $2$ 一个数。

于是只含奇质因子的条件等价为不含偶质因子，也就是不含 $2$ 这个因子。

显然：含有因子 $2$ 的数一定是偶数，不含因子 $2$ 的数一定是奇数。

所以偶数不是只因数，奇数是只因数。~~与生活经验相同~~。

时间复杂度 $O(T)$，期望得分 $100$ 分。需要开 long long。

## Code

```cpp
#include <iostream>

int main() {
  int T;
  for (std::cin >> T; T; --T) {
    long long n; std::cin >> n;
    std::cout << ((n & 1) ? "Yes" : "No") << std::endl;
  }
}
```

## Generator

```cpp
void makedata(int T) {
  int t = std::max(1, T - 1);
  printf("%d\n", t);
  if (T == 1) {
    puts("2");
  } else if (T == 2) {
    puts("3");
  } else if (T == 3) {
    puts("2\n3");
  } else if (T <= 5) {
    for (int i = 1; i <= t; ++i) printf("%d\n", 2 + modx(9));
  } else if (T == 6) {
    for (int i = 1; i <= t; ++i) {
      int x = modx(1000000000);
      while (x <= 2) x = modx(1000000000);
      if ((x & 1) == 0) --x;
      printf("%d\n", x);
    }
  } else if (T == 7) {
    for (int i = 1; i <= t; ++i) {
      int x = modx(1000000000);
      while (x <= 2) x = modx(1000000000);
      if ((x & 1) == 1) --x;
      printf("%d\n", x);
    }
  } else if (T <= 9) {
    for (int i = 1; i <= t; ++i) {
      int x = modx(1000000000);
      while (x == 1) x = modx(1000000000);
      printf("%d\n", x);
    }
  } else {
    for (int i = 1; i <= t; ++i) {
      long long x = modx(1000000000000000000ll);
      while (x == 1) x = modx(1000000000000000000ll);
      printf("%lld\n", x);
    }
  }
}
```