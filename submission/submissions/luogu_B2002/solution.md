# B2002 题解

这是一个程序员用来测试编译环境是否正常的代码。

首先我们来简单介绍一下输出。

常用的有`cout`，`printf`，`puts`这三种。

`cout`所属的库为`iostream`。

剩下两个都属于`cstdio`库。

对于库的调用，我们要在程序开始时输入`#include<库名>`，并独自占据一行。

我会在下面的程序中加上注释，就是`//`之后的文字，不影响程序的运行。

我们现在用三种输出来做这道题。

上代码：


```
#include<iostream>
using namespace std;
int main() {//表示主函数
	cout<<"Hello,World!"<<endl;//<<endl表示换行
	return 0;//表示结束程序
}
```

```
#include<cstdio>
using namespace std;
int main() {
	printf("Hello,World!\n");//\n同样表示换行
	return 0;
}
```

```
#include<cstdio>
using namespace std;
int main() {
	puts("Hello,World!");//puts自带换行
	return 0;
}
```

完结撒花~