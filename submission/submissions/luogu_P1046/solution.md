# P1046 题解

这个题目很简单，但是可以对代码进行多次优化。

首先，常规读入高度和身高，这个没什么可优化的。

接下来分两步，一个是比较，一个是计算。

常规做法基本上是 if(height[i] <= H + 30)s++;

但是，对于部分要卡常的题目来说，可能会爆掉，而且每次都调用寄存器来计算 H+30，很显然是一种浪费。

首先我们可以像多数题解那样，在读入 H 之后，直接对它进行 +=30的操作。

但是实际上，比较的行为也可以简化。

if(height[i] <= H )s++; 电脑计算的时候分为三步：

1. 计算 height[i] <= H 的值 （true | false）

2. 调用if判断里面表达式的值是否为真

3. 若真，对s进行s+=1的运算。

我们简化时可以发现，s每次加的值都是恒定的 1 。

联想到 ： true == 1 , false == 0 , 我们可以直接将逻辑值的结果加给s。

也即 **s+=!(H<height[i]);**

CPP代码如下

```cpp
#include <iostream>
using namespace std;
int height[20],H,s;
int main()
{
    for(int i=0;i<10;i++)cin >> height[i];
    cin >> H;
    H += 30;
    for(int i=0;i<10;i++)s+=!(H<height[i]);
    cout << s;
}
```