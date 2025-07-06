# P3955 题解

将读者的需求码与图书编码配对。

- 把需求码与图书编码配对 = 求图书编码的后 X 位
- 求图书编码的后 X 位 = 把前面的都去掉。


如何把前面的无关数字去掉呢？这时候我们想起了 $\%$ 运算。

对于一个数$a$，很显然它的个位数是：$a \% 10$ 。

但是这是我们人工计算出的结果，而各个需求码的位数不同，这时候就需要找出一个规律。

对此我们发现了规律：对一个数 $a$ 取其后 $n$ 位，就是 $a \% 10^n$ 。

cmath 头文件中带有专门执行幂运算的函数。

其中有一个要注意的点是，pow 函数并不能直接进行 mod 运算，需要将其带入一个变量进行运算。

遍历求最小值即可。

### 最后贴代码

```
#include<iostream>
#include<cmath>
using namespace std;
int n,q,book[6666],len[6666],num[6666];

int main()
{
    cin>>n>>q;
    for(int i=1; i<=n; i++) cin>>book[i];
    for(int i=1; i<=q; i++) {
        cin>>len[i]>>num[i];
        int tmp = pow(10,len[i]),min = 10000001;
        for(int j=1; j<=n; j++) if(book[j] % tmp == num[i] && book[j] < min) min = book[j];
        if(min != 10000001) cout<<min<<endl;
        else cout<<-1<<endl; 
    }
    return 0;
}
```