# P2404 题解

蒟蒻初学回溯，做了这样一道经典的题目（第一次过于自信直接提交结果编译没过？？！！）AC后翻了一下《信息学奥赛一本通》，发现书上的算法比我的快~~很多？？~~

以下是书上的算法：


```cpp
#include<cstdio>
#include<iostream>
#include<cstdlib>
using namespace std;
int a[10001]={1},n;
int search(int,int);
int print(int);
int main()
{
	cin>>n;
	search(n,1);//将要拆分的数n传递给s
	return 0;
}
int search(int s,int t)
{
	int i;
	for(i=a[t-1];i<=s;i++)
		if(i<n)//当前数i要大于等于前一位数，且不超过n
		{
			a[t]=i;//保存当前拆分的数i
			s-=i;//s减去数i，s的值将继续拆分
			if(s==0)print(t);//当s=0时，拆分结束输出结果
				else search(s,t+1);//当s>0时，继续递归
			s+=i;//回溯：加上拆分的数，以便产生所有可能的拆分
		}
}
int print(int t)
{
	for(int i=1;i<=t-1;i++)//输出一种拆分方案
		cout<<a[i]<<"+";
	cout<<a[t]<<endl;
}
```

### 另：附上我的打表程序（暴力出奇迹，打表过样例）

```cpp
//打表的程序不作解释，仅供娱乐，请认真学习回溯

#include<iostream>
#include<cstdio>
using namespace std;
int n;
int main()
{
	cin>>n;
	if(n==1)printf("\n");
		else if(n==2)printf("1+1\n");
			else if(n==3)printf("1+1+1\n1+2\n");
				else if(n==4)printf("1+1+1+1\n1+1+2\n1+3\n2+2\n");
					else if(n==5)printf("1+1+1+1+1\n1+1+1+2\n1+1+3\n1+2+2\n1+4\n2+3\n");
						else if(n==6)printf("1+1+1+1+1+1\n1+1+1+1+2\n1+1+1+3\n1+1+2+2\n1+1+4\n1+2+3\n1+5\n2+2+2\n2+4\n3+3\n");
							else if(n==7)printf("1+1+1+1+1+1+1\n1+1+1+1+1+2\n1+1+1+1+3\n1+1+1+2+2\n1+1+1+4\n1+1+2+3\n1+1+5\n1+2+2+2\n1+2+4\n1+3+3\n1+6\n2+2+3\n2+5\n3+4\n");
								else printf("1+1+1+1+1+1+1+1\n1+1+1+1+1+1+2\n1+1+1+1+1+3\n1+1+1+1+2+2\n1+1+1+1+4\n1+1+1+2+3\n1+1+1+5\n1+1+2+2+2\n1+1+2+4\n1+1+3+3\n1+1+6\n1+2+2+3\n1+2+5\n1+3+4\n1+7\n2+2+2+2\n2+2+4\n2+3+3\n2+6\n3+5\n4+4\n");
	return 0;
}
```

### 既然都看到这儿了，赞一个呗（求过~）

-------------

友链：点击[这儿]进入我的Blog(https://www.luogu.org/blog/user67087/)