# P5715 题解

三位数排序，基础题目就不用说了

---

## 第一种方法

```cpp
#include <iostream>
#include <algorithm>

using namespace std;

int a[4];

int main()
{
    cin>>a[1]>>a[2]>>a[3];
    sort(a+1,a+4);
    cout<<a[1]<<' '<<a[2]<<' '<<a[3];
    return 0;
}
  
```
但这里利用了自带的排序函数

初学者不适合使用

## 第二种方法

正常的选择排序简化版

```cpp
#include <iostream>

using namespace std;

int main()
{
    int a,b,c;
    cin>>a>>b>>c;
    if(a>b)swap(a,b);
    if(b>c)swap(b,c);
    if(a>b)swap(a,b);
    cout<<a<<' '<<b<<' '<<c;
}
```
-----

学完这道题建议去学：

- 选择排序

- 冒泡排序

- 插入排序

# 感谢管理员审核！