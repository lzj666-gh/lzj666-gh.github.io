# P2240 题解

~~这道题不是贪心吗？为什么题目是背包？~~
## 思路
千万不要被题目给误导了，这道题是贪心。

所有金币都可以分开，也就是说只要按照性价比最高的取一定得到的价值最大。

性价比就是这堆金币的价值除以重量。

只需要把这$n$堆金币按性价比排序就行了。

然后依次遍历，如果背包中剩余可以拿的重量大于等于这堆金币的重量，就全拿，否则直接装满。

直接装满这里注意一下整型转浮点的细节就好了。
## 代码
这道题没什么细节，也比较简单，就直接放代码——

（~~我知道你们只看这里~~）
```cpp
#include<cstdio>
#include<algorithm>//用到sort
using namespace std;
struct Node{//金币结构体
	int w,v;//w表示重量，v表示价值
}a[110];
int read(){//普通的快读，不解释
	int x=0,f=1;
	char c=getchar();
	while(c<'0'||c>'9'){
		if(c=='-') f=-1;
		c=getchar();
	}
	while(c>='0'&&c<='9'){
		x=x*10+c-'0';
		c=getchar();
	}
	return x*f;
}
bool cmp(Node aa,Node bb){//定义排序方法
	return aa.v*bb.w>aa.w*bb.v;//按性价比从高到低排序，为防止精度问题直接交叉相乘
}
int main(){//主函数
	int n=read(),m=read();
	double ans=0;//记录答案
	for(int i=1;i<=n;i++) a[i].w=read(),a[i].v=read();
	sort(a+1,a+n+1,cmp);//排序
	for(int i=1;i<=n;i++){//一次遍历
		if(a[i].w<=m) ans+=a[i].v,m-=a[i].w;//够就全拿
		else{//不够
			ans+=a[i].v*m*1.0/(a[i].w*1.0);//拿上能拿的部分，注意强转double
			break;//直接退出循环
		}
	}
	printf("%.2lf",ans);//保留2位小数
	return 0;//华丽结束
}
```
看我在比赛刚刚结束就发了一篇题解，总得点个赞再走呀~