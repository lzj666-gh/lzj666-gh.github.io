# P1116 题解

- 我看了其他题解都是做了排序，可是题目只是问需要多少次移动，没问排序结果啊！！！

- 所以我没有做排序，只是迭代去计算每个数字前有几个数字比它大，这意味着它必须要移动几次。

- 没有做冒泡排序，双层循环写法也和冒泡无关。没人发布这种思路的题解，望管理员通过。

```cpp
#include <iostream>
using namespace std;
int n, sum;
int main()
{
    cin >> n;
    int a[n];
    for (int i = 0; i < n; ++i)
        cin >> a[i];
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < i; ++j)
            if (a[j] > a[i])
                ++sum;
    cout << sum;
    return 0;
}

```