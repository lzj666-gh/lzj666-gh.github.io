# P7869 题解

## 题解

容易发现，本题就是去寻找输入的字符串里是否含有 $\verb!\r!$ 和 $\verb!\n!$。因为本题保证了文本文件仅在一种系统中产生，因此若仅有前者，则为 $\text{Mac}$ 系统；仅有后者，则为 $\text{Linux}$ 系统；如果都有，则为 $\text{Windows}$ 系统。

- 那么只需要使用 $\verb!getline!$ 函数读入整行字符串，然后使用 $\verb!find!$ 函数查询里面是否含有即可。要注意的是，如果 $\verb!find!$ 函数没能查找到某个需要匹配的字符串，返回值是 $\verb!ULLONG_MAX!$。

- 或者可以选择不断读入字符串，直到读到文件末尾（$\verb!EOF!$），然后对每次读入的字符串使用 $\verb!find!$ 函数。如果使用 $\verb!cin!$，那么读入到文件末尾则会返回 $0$；如果使用 $\verb!scanf!$，那么读入到文件末尾则会返回 $-1$（即 $\verb!EOF!$ 字面量）。

- 或者可以使用 $\verb!fread!$，把输入数据里所有的字符全部读进来（要注意的是，前两种做法都是使用的 $\text{C++}$ 里面特有的字符串（$\verb!string!$），但是 $\verb!fread!$ 属于 $\text{C}$ 风格读入，读入的东西是 $\text{C}$ 风格字符串（$\verb!char []!$））。$\verb!fread!$ 会返回读入的字符的总个数。因此可以直接循环，进行匹配。

- 或者可以直接手写 $\verb!getline!$。具体就是不断地使用 $\verb!getchar!$，一直读到 $\verb!EOF!$。

### 参考代码

```cpp
#include<iostream>
#include<string>
std::string s;
int main(){
    std::getline(std::cin,s); bool f1=0,f2=0;
    if(s.find("\\r")<s.length()) f1=true;
    if(s.find("\\n")<s.length()) f2=true;
    if(f1&&f2) std::cout<<"windows"<<std::endl; else 
    if(f2    ) std::cout<<"linux"<<std::endl; else 
    if(f1    ) std::cout<<"mac"  <<std::endl;
    return 0;
}
```