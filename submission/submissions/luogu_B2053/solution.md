# B2053 题解

### upd
21-10-16:修改了一些错误

### 题意
[题目传送门](https://www.luogu.com.cn/problem/B2053)

指定一个方程：$ax^2+bx+c$，现给你 $a、b、c$ 的值让你求这个方程的根。
### 做法
题意简单明了，很明显需要一个东西：$\Delta$，这个东西叫做**判别式**，是用来判断求公式是否成立，我们记 $\Delta=b^2-4ac$，当 $\Delta>0$ 或 $\Delta=0$ 时成立，当 $\Delta<0$ 时不成立，至于为什么可以参考题目中的求根公式：

- $x_1=\dfrac{-b+\sqrt{\Delta}}{2a}$

- $x_2=\dfrac{-b-\sqrt{\Delta}}{2a}$

可以发现因为 $\Delta$ 在根号下所以不能小于零，这样这道题也就解出来了，上代码：
### Code
```cpp
#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;
double a,b,c;

int main() {
    cin>>a>>b>>c;
    double delta=b*b-4*a*c;
    if (delta>0) {
        double x1=(-b+sqrt(delta))/(2*a);
        double x2=(-b-sqrt(delta))/(2*a);
        if (x1>x2) {
            swap(x1,x2);
        }
        printf("x1=%.5lf;x2=%.5lf",x1,x2);
    } else if (delta==0) {//delta为零其根也为零，所以x1=x2
        double x1=(-b+sqrt(delta))/(2*a);
        double x2=(-b-sqrt(delta))/(2*a);
        printf("x1=x2=%.5lf",x1);
    } else {
        cout<<"No answer!";//delta小于零
    }
    return 0;
}
```
