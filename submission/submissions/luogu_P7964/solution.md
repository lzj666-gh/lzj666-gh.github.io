# P7964 题解

## 题意
给定 $n$ 组命令及标题名称，输出所有标题序号及其名称。

命令：

- `section` 一级标题；

- `subsection` 二级标题；

- `subsubsection` 三级标题。

## 思路
每次统计，判断有没有开新的一列标题，若没有，序号就加上 $1$，反之，统计数据归 $0$，开个新的。

当然，为了方便，每次操作均把其后面的统计数据归 $0$。
## 代码
```cpp
#include<iostream>
using namespace std;
int main(){
    int t,a=0,b=0,c=0;
    cin>>t;
    while(t--){
        string d,s;
        cin>>d>>s;
        if(d=="section"){ //一级标题
            b=0,c=0,a++;
            cout<<a<<' '<<s<<endl;
        }
        if(d=="subsection"){ //二级标题
            c=0,b++;
            cout<<a<<'.'<<b<<' '<<s<<endl;
        }
        if(d=="subsubsection"){ //三级标题
            c++;
            cout<<a<<'.'<<b<<'.'<<c<<' '<<s<<endl;
        }
    } 
}
```
[AC记录](https://www.luogu.com.cn/record/63767712)