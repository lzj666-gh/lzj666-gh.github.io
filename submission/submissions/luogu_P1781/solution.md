# P1781 题解

upd - 19 - 02 - 28，现在在洛谷可以编译通过了

---

其实对于只要比较大小的题，写高精度没必要

直接用 string 记录一个 max 每次比较很简单啊

---
原理：string的比较 保存数字的字符串=高精度版比较大小

和字典序什么的有关系

---
代码
```cpp
#include <iostream>
#include <cstring>
using namespace std;
int main() {
    int n, id; // id 记录当上总统的人的号数
    string max = ""; // 赋初值，这个 max 不可以作为全局变量（会重名）
    // 如果一定要把 string max 放到全局变量去，应去掉 using namespce std;
    string in;
    cin >> n;
	for (int i = 1; i <= n; i++) {
        cin >> in;
        int inSize = in.size();
        int maxSize = max.size();
        if (inSize > maxSize || (inSize >= maxSize && in > max)) {
            max = in;
            id = i;
        }
    }
    cout << id << endl << max << endl;
    return 0;
}
```