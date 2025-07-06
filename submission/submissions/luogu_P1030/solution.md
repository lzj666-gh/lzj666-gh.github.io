# P1030 题解

首先，一点基本常识，给你一个后序遍历，那么最后一个就是根（如ABCD，则根为D）。

因为题目求先序，意味着要不断找根。

那么我们来看这道题方法：（示例）

中序ACGDBHZKX，后序CDGAHXKZB，首先可找到主根B；

那么我们找到中序遍历中的B，由这种遍历的性质，可将中序遍历分为ACGD和HZKX两棵子树，

那么对应可找到后序遍历CDGA和HXKZ（从头找即可）

从而问题就变成求1.中序遍历ACGD，后序遍历CDGA的树 2.中序遍历HZKX，后序遍历HXKZ的树；

接着递归，按照原先方法，找到1.子根A，再分为两棵子树2.子根Z，再分为两棵子树。

就按这样一直做下去（先输出根，再递归）；

模板概括为step1:找到根并输出

step2:将中序，后序各分为左右两棵子树；

step3:递归，重复step1,2；

代码如下

```cpp
#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
void beford(string in,string after){
    if (in.size()>0){
        char ch=after[after.size()-1];
        cout<<ch;//找根输出
        int k=in.find(ch);
        beford(in.substr(0,k),after.substr(0,k));
        beford(in.substr(k+1),after.substr(k,in.size()-k-1));//递归左右子树；
    }
}
int main(){
    string inord,aftord;
    cin>>inord;cin>>aftord;//读入
    beford(inord,aftord);cout<<endl;
    return 0;
}
```