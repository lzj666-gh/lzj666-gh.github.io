# P1308 题解

## 读取部分
c 版本的字符串处理确实比较不友好。

+ 第一行的单词读取比较简单，使用`scanf()`读取即可；
+ 第二行的字符串有一个测点有行首空格，所以开始用`gets()` 读取一行的时候会漏掉，改用`getchar()`挨个处理即可。

读取部分代码如下：
```c
    // input
    scanf("%s", w);
    c = getchar();
    while((c = getchar()) != EOF && i < MAX_LINE){  
        if(c == '\n') break;
        s[i++] = c;
    } s[i] = '\0';
```

## 处理部分
处理部分比较简单，考虑周全一点即可。

+ 首先定义大小写转换，此处全部转成小写：
```c
#define val(a) (a<'a' ? (a-'A'+'a') : a)
```

+ 然后维护两个扫描头，$i$ 对应文章字符串，$j$ 对应单词字符串，一旦是单词头（`i==0`或`s[i-1]==' '`）或者之前保持匹配 (`j>0`此处略写为`j`)，那么继续判断匹配：
	+ `++j`  判断单词的下一个字母，如果下一个为空`w[j]=='\0'` 并且文章的下一个字母为空或空格 `s[i+1]=='\0' || s[i+1]==' '`，则有一次完整的字符匹配。
    + 否则继续判断下一个字母（什么也不做）
+ 否则清空 $j$，从头继续扫描

处理部分代码：

```c
    // calculate
    for(i=0,j=0; s[i]!='\0'; ++i){
        if((i==0 || s[i-1]==' ' || j) && val(s[i])==val(w[j]) && ++j>-1){
            if(w[j]=='\0' && (s[i+1]=='\0' || s[i+1]==' ')){
                if(first==-1) first = i+1-j;
                count++;
            }
        }else j=0;
    }
```

## AC代码

``` c
#include <stdio.h>

#define MAX_LINE 1000001
#define val(a) (a<'a' ? (a-'A'+'a') : a)

int main()
{
    // declaration
    int i=0, j, count=0, first=-1;
    char c, w[11], s[MAX_LINE];

    // input
    scanf("%s", w);
    c = getchar();
    while((c = getchar()) != EOF && i < MAX_LINE){  
        if(c == '\n') break;
        s[i++] = c;
    } s[i] = '\0';

    // calculate
    for(i=0,j=0; s[i]!='\0'; ++i){
        if((i==0 || s[i-1]==' ' || j) && val(s[i])==val(w[j]) && ++j>-1){
            if(w[j]=='\0' && (s[i+1]=='\0' || s[i+1]==' ')){
                if(first==-1) first = i+1-j;
                count++;
            }
        }else j=0;
    }

    // output
    if(count==0) printf("-1\n");
    else printf("%d %d\n", count, first);
    return 0;
}

```

> PS: 到底要写多详细才能给过呢= =