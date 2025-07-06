# P1427 题解

## 前言

`std::vector` 的常数比普通数组大，所以如果对常数要求特别苛刻的话建议用普通数组。

另外，`int a[n]` 不推荐使用，但 `vector<int> a(n)` 完全可以用。

## 思路 1

由于输入数据没有给出数组的具体大小，所以我们可以使用动态数组 `std::vector`。

`std::vector` 的具体操作如下：
```cpp
vector<int> a; // 初始化，可以在这里预分配空间当静态数组用，'<>'里面是存放的数据类型
a.push_back(10); // 在数组的末尾插入数据，数组大小自动加 1
a.push_back(15);
a.pop_back(); // 删除数组尾部的元素，数组大小自动减 1
for(int i=0;i<a.size();i++){ // 输出数组元素，a.size() 是数组的大小
    cout<<a[i]<<' ';
}
```
所以只需要逐一插入元素，删掉数据尾部的 $0$ 并倒着输出即可。

下面是代码。
```cpp
#include<bits/stdc++.h>
using namespace std;
vector<int> a;
int n;
int main() {
    while(cin>>n){ // 这一行利用了 std::cin 的特性，作用是持续读入数据直至 EOF
        a.push_back(n);
    }
    a.pop_back();
    for(int i=a.size()-1;i>=0;i--){
        cout<<a[i]<<' ';
    }
    return 0;
}
```

## 思路 2

注意到该题具有明显的后进先出特征，所以可以用栈做。

如果不知道什么是栈，可以参考 [OI Wiki](https://oi-wiki.org/ds/stack/)。

那么就只需把所有元素压入栈，弹出末尾的 $0$ 然后依次出栈并输出即可。

下面是代码。
```cpp
#include<bits/stdc++.h>
using namespace std;
stack<int> s; // 这里使用 STL 里的 std::stack
int n;
int main() {
    while(cin>>n){ 
        s.push(n); // 入栈
    }
    s.pop(); // 去掉末尾 0
    while(s.size()){ // 栈的大小大于 0，即栈不为空
        cout<<s.top()<<' '; // 输出栈顶
        s.pop(); // 出栈
    }
    return 0;
}
```