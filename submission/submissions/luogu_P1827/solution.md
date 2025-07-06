# P1827 题解

这里利用到一个最重要的知识点——二叉树遍历。

* **前序遍历：根左右**

* **中序遍历：左根右**

* **后序遍历：左右根**

前序遍历是先遍历根节点，再遍历根节点的左右子树。

那么，前序序列的第一个节点，一定是根节点。

找到根节点，再确定根节点在中序序列中的位置，就可以分出左右两棵子树。

这道题我们不需要建树，只要通过递归不断切割字符串就好了。

**字符串切割时应注意的问题**

那便是切割位置。STL的string类型自带切割方法substr，但搞不清参数就会导致WA甚至RE。

首先我们搞清楚substr方法的使用方法。

```cpp
string s;
s.substr(order,k);
```
参数传入一个order，一个k。

函数将会从下标为order的位置开始，连续截取k个字符。返回截取后的字符串。

order显然不能超出0~`s.size()-1`的范围。

但是，如果order+k超过了`s.size()-1`，函数会自动只截取到s的末尾。

如果不传入k，那么默认截取到末尾。

**这个函数是返回一个字符串，而不是对s进行改动。**

那么我们现在就开始寻找参数规律。

见下面的图（样例）

![](https://img41.pixhost.to/images/89/143577901_1.png)

看到前序序列的第一个字符是 C ，那么根节点就是 C ，找到中序中对应的位置，数下标，发现 C 在 5 处
**（注意字符串下标从0开始）**。

然后在先序序列中把C删掉。

![](https://img41.pixhost.to/images/89/143578227_2.png)

这是因为我们后面不会用到了。

（下面的数字是下标）

中序序列中C在5处，那么左右子树分别就是ABEDF(0~4)和HG(6~7)。

设在中序序列中根节点的位置是k，

很容易发现：

* 中序序列中左子树就是从0开始切割到k-1，也就是切割了k个字符；

* 中序序列中右子树就是从k+1开始，一直切割到最后。

然后找前序序列切割的规律。

中序序列中左子树是ABEDF，右子树是HG，对应在前序序列中就是BADEF(0~4)和GH(5~6)。

那么

* 前序序列中左子树是从0开始切割到k-1，也就是切割了k个字符；

* 前序序列中右子树就是从k开始，一直切割到最后。

另外仍需补充的几点，是关于查找和删除。

```cpp
s.find(c);
//在字符串s中查找第一个字符c的位置，返回下标，如果没有返回string::npos

s.erase(it);
//在字符串中删除指针it所指向的字符

s.begin();
//返回s的首字符的指针（迭代器）

```

那么我们现在就可以开始写代码了！

**（注意代码中的pre是前序，inor是中序）**

```cpp
#include<string>
#include<cstring>
#include<iostream>
#include<cstdio>
using namespace std;
string pre,inor;
void work(string pre,string inor)
{
    if(pre.empty())return;
    //如果序列空了，就没必要继续了
    char root=pre[0];
    //取到前序序列的首字母，即根节点
    int k=inor.find(root);
    //找到中序序列中根节点的位置
    pre.erase(pre.begin());
    //删去前序序列中的根节点
    string leftpre=pre.substr(0,k);
    //从0开始切割k个
    string rightpre=pre.substr(k);
    //从k开始切割到最后
    string leftinor=inor.substr(0,k);
    //从0开始切割k个
    string rightinor=inor.substr(k+1);
    //从k+1开始切割到最后
    work(leftpre,leftinor);
    work(rightpre,rightinor);
    printf("%c",root);
    //因为要输出后序序列，所以是左右根
    //先遍历左子树，再右子树，再根节点
}
int main()
{
    cin>>inor>>pre;
    work(pre,inor);
    putchar('\n');
    return 0;
}
```
结束！






