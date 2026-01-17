# P5714 题解

# [P5714 【深基 3. 例 7】肥胖问题](https://www.luogu.com.cn/problem/P5714)

## 题目简述

给出 BMI 指数计算公式：$\dfrac{m}{h^2}$，其中 $m$ 是指体重（千克），$h$ 是指身高（米）。\
判定结果如下：

- 小于 $18.5$：体重过轻，输出 `Underweight`；
- 大于等于 $18.5$ 且小于 $24$：正常体重，输出 `Normal`；
- 大于等于 $24$：肥胖，不仅要输出 BMI 值（使用 `cout` 的默认精度），然后换行，还要输出 `Overweight`；

现有 $m$ 和 $h$，按要求输出结果。\
注：结果应保留六位**有效数字**。

## 思路

题目已经给出了计算公式，我们可以直接套用公式，不过结果保留六位有效数字可能吓到大家了。

其实没有那么复杂。

首先，有效数字是指从第一个非零数字开始计算的位数，而非小数点后的位数。

在 C++ 中，用 `cout` 输出 `double` 类型的数字会自动保留六位有效数字，然后我们就可以轻松写出代码啦！

## 代码

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    double z,m,h;
    cin >> m >> h;
    z = (m /(h * h));
    if (z < 18.5) cout << "Underweight";
    else if (z >= 18.5 && z < 24) cout << "Normal";
    else cout << z << endl << "Overweight";
    return 0;
    
}
```

## 拓展

当然如果你不放心的话，C++ 中还有 `fixed` 和 `setprecision`这两个流操作符。

它们两个连用可以控制输出的小数位数，且写一遍后面的输出都会生效，代码如下：

```cpp
double a = 3.1415926, b = 11.4514;

cout << fixed << setprecision(3) << a;
cout << " " << b;

//输出为: 3.142 11.451
```

当 `setprecision` 单独使用时，就可以控制输出的**有效数字位数**，代码如下：

```cpp
double a = 3.1415926, b = 11.4514;

cout << setprecision(3) << a;
cout << " " << b;

//输出为: 3.14 11.5
```

应用在这个题上，我们也可以这样写：

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    double z,m,h;
    cin >> m >> h;
    z = (m /(h * h));
    if (z < 18.5) cout << "Underweight";
    else if (z >= 18.5 && z < 24) cout << "Normal";
    else cout << setprecision(6) << z << endl << "Overweight";
    return 0;
    
}
```

---

完结撒花！

~~话说要不是写这篇题解我都不知道这两个函数还能这么用~~

## UPDATE

2025/5/10：修正了一处表述错误（感谢 @llamn)