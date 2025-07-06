# P1093 题解

一道很好的结构体训练题

我先说一句吧。。。赛场上一般都不手打排序的（C++），一般使用sort，但是sort对结构体的排序就比较麻烦了，需要自己编写一个函数cmp作为sort的第三个参数，具体为：

```cpp
bool cmp(结构体名称 a，结构体名称 b)
{
/*判断a是否大于b的代码块，如果a大于或等于b返回1，否则返回否*/
}
```
那么我们先定义一个结构体stu：

```cpp
struct stu
{
    int num;//编号
    int c,m,e; //分别表示Chinese，math和English的分数
    int sum;//总分
}student[310];//在此顺便定义数组
```
然后开始写cmp函数

```cpp
bool cmp(stu a,stu b)
{
    if(a.sum>b.sum) return 1;//总分大于b就返回1
    else if(a.sum<b.sum) return 0;//否则返回0
    else//相等
    {
        if(a.c>b.c) return 1;//比较语文
        else if(a.c<b.c) return 0;
        else//语文也相等
        {
            if(a.num>b.num) return 0;//比较编号
            else return 1;
        }
    }
}
```
完成了！

之后就可以用sort直接排序具体调用方式为

```cpp
sort(student+1,student+1+n,cmp);
```
那么现在给出完整代码：

```cpp
#include<iostream>
#include<algorithm>
using namespace std;
struct stu
{
    int num;//编号
    int c,m,e; 
    int sum;
}student[310];
bool cmp(stu a,stu b)
{
    if(a.sum>b.sum) return 1;
    else if(a.sum<b.sum) return 0;
    else
    {
        if(a.c>b.c) return 1;
        else if(a.c<b.c) return 0;
        else
        {
            if(a.num>b.num) return 0;
            else return 1;
        }
    }
}
int main()
{
    int n;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        student[i].num=i;//录入编号
        cin>>student[i].c>>student[i].m>>student[i].e;//输入
        student[i].sum=student[i].c+student[i].m+student[i].e;//计算总分
    }
    sort(student+1,student+1+n,cmp);
    for(int i=1;i<=5;i++)
        cout<<student[i].num<<' '<<student[i].sum<<endl;
    return 0;
}
```