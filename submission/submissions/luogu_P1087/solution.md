# P1087 题解

## 一个函数也没有的代码来啦！
在输入的过程中，对于第 k*(2^n) 个数， 我们可以直接把它和兄弟节点“合并”之后**直接输出直接替换**作为父节点
![箭头表示与兄弟节点“合并”为父节点](https://cdn.luogu.com.cn/upload/pic/61476.png)
##### 在一条链上（用箭头表示）的元素都用同一个变量存储

替换的具体方法是：当节点本身与兄弟节点不同时， 父亲节点为F ~~显而易见~~

否则， 两个节点相同，则父节点就是右子节点（即不变）

因为是后序遍历，所以输出两个子节点就可以直接输出父亲啦！

```
#include<bits/stdc++.h>
using namespace std;
int fbi[1025], n;
int p2[11] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024}; // 打表2的次方
int main() {
    cin >> n; char t;
    for(int i = 1; i <= p2[n]; ++i) {
        cin >> t; 
        fbi[i] = t - '0';
        if(fbi[i] == 0)printf("B"); 
  		else if(fbi[i] == 1)printf("I"); 
  		else printf("F");
        for(int k = 1; k < 11; ++k) {//合并过程
            if(i % p2[k] == 0){
                if(fbi[i] != fbi[i - p2[k - 1]])fbi[i] = 2;
                if(fbi[i] == 0)printf("B"); 
  		else if(fbi[i] == 1)printf("I"); 
  		else printf("F");
            }
        }
    }
    return 0;
}
```
要注意的是合并过程中k的初值**千万不能设为0**~~不然节点1和谁合并呢~~

还有就是不要不小心输入整数类型，而且千万不要用getchar()（看我的提交记录就知道了）