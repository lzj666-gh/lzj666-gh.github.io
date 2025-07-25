# P1259 题解

我们先分析一下样例
```
ooooooo*******--

oooooo--******o*
oooooo******--o*

ooooo--*****o*o*
ooooo*****--o*o*

oooo--****o*o*o*
oooo****--o*o*o*

ooo--***o*o*o*o*

ooo*o**--*o*o*o*
o--*o**oo*o*o*o*
o*o*o*--o*o*o*o*
--o*o*o*o*o*o*o*
```
每两行分一组的时候,可以很明显地看到规律.

- 中间的 "o*" 与 "--" 交换
- 最左边的 "**" 与 "--" 交换

然而后四行我并没有发现什么规律,于是无耻地打了一个表.

打表原理:

```
ooo*o**--* o*o*o*
o--*o**oo* o*o*o*
o*o*o*--o* o*o*o*
--o*o*o*o* o*o*o*
后6个字符为固定的"o*o*o*"
于是只要记录
	ooo*o**--*,
	o--*o**oo*,
	o*o*o*--o*,
	--o*o*o*o*
```
代码如下

```cpp
#include <cstdio>
#include <iostream>
using namespace std;
int n;
char ch[205];//存储棋子的状态
void swap(char &a, char &b)//交换函数
{
    char t = a;
    a = b;
    b = t;
}
void output(){//输出
    for (int i = 0; i < 2 * n + 2; i++)
        putchar(ch[i]);
    putchar('\n');
}
void movechess(int start, int end)
{//移动棋子
    swap(ch[start], ch[end]);
    swap(ch[start + 1], ch[end + 1]);
    output();
}
string out[4] = {"ooo*o**--*", "o--*o**oo*", "o*o*o*--o*", "--o*o*o*o*"};
//打表qwq
int main()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        ch[i] = 'o';
    for (int i = n; i < 2 * n; i++)
        ch[i] = '*';
    ch[2 * n] = '-';
    ch[2 * n + 1] = '-';
    //打印初始状态
    output();
    int len = n;
    //需要移动的黑/白棋子
    while (true)
    {
        movechess(len - 1, 2 * len);
        //中间的 "o*" 与 "--" 交换
        len--;
        if (len == 3)
        //不符合上述规律,开始输出打表内容
            break;
        movechess(len, 2 * len);
        //最左边的 "**" 与 "--" 交换
    }
    string ss;
    for (int i = 0; i < n - 4; i++)
        ss += "o*";
    for (int i = 0; i < 4; i++)
        cout << out[i] << ss << endl;
}
```