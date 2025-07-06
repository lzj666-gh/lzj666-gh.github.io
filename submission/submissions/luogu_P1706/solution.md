# P1706 题解

## c++朝这看！！！

看了这么多大佬的文章，小生忍不住也来写一篇题解；

你知道吗，在#include <algorithm>里有一个函数，全排列函数：
  
 ### next_permutation！

小生管他叫字典排函数；
  
这个函数每运行一次就可以把数组排成下一个字典排数列；与之对应的是prev_permutation，即排出上一个字典序； <algorithm>里有好多实用的函数，建议大家百度一下；
  
回到题上，我们怎样求出所有的组合呢？这是个组合排列问题，形如下图：

![](https://cdn.luogu.com.cn/upload/pic/27420.png)
  
那么现在我们做的就是从n个数种拿n个数排列；也就是有n！种排列；理论完毕，代码如下：

```
#include<iostream>//P1706
#include<cstdio>
#include<cstring>
#include<string>
#include<iomanip>
#include <algorithm>
#include<cmath>
#include<vector>
#include<set>
using namespace std;
int a[10];
int main()
{
	int n,i,j=1,k;
	cin>>n;
	for(i=1;i<=n;i++)
	 {a[i]=n-i+1;j*=i;}//题目好像没说要从小到大输出
     //但保险起见还是初始赋值为最大序列
     //即a[1~n]=n~1;顺便计算n!
	for(i=1;i<=j;i++)
	 {next_permutation(a+1,a+n+1);
	  for(k=1;k<=n;k++)
	   cout<<"    "<<a[k];//排一次输出一次
       //空格建议复制
	  cout<<endl;
	 }
	 return 0;
}
```

观此题解小生不胜荣幸，请顺手留赞，感谢<^~^>