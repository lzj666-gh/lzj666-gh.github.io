# P1423 题解

数学方法



O(1)时间复杂度

等比数列求和公式


![](https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=1747555526,1280050457&fm=58)


每次游的距离为上一次的0.98倍，构成一个公比为0.98的等比数列


现要使其前ans项大于等于一个值


只要代入公式并向上取整即可


下附超短代码



```cpp
#include<bits/stdc++.h>
double x;
int main()
{
    std::cin>>x;
    std::cout<<ceil(log(1-x/100)/log(0.98));
    return 0;
}

```