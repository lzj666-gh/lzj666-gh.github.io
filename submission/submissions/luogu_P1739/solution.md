# P1739 题解

我的满分题解（历尽千辛万苦啊！）（解释在题解中）：

```cpp
#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>//头文件
using namespace std;//不加这个会出错（告诉一些新人的，大佬勿喷）
int ok=0;//状态的变量（大佬千万别改bool）
char a;//记录字符
int i=0;//之后的特判要用
int main()
{
    for (;;i++)//很无脑对不对，但是很有用
    {
        a=getchar();//读入
        if (i==0&&a==')') {printf ("NO");return 0;}//特判：第一个为‘）’，结束，不对，自己想想看
        if (a=='(') ok++;//是左括号就++
        if (a==')') ok--;//是有括号就--
        if (ok<0) {printf ("NO");return 0;}//特判：多了右括号，结束（多了左没事，但不可以多右，想想看）
        if (a=='@') {if (!ok) printf ("YES");else printf ("NO");return 0;}
//特判无效：比较ok是不是为0（是0表示左右括号都一样多，结束）
    }
}

```