# P2249 题解

~~比赛刚结束，我来水一发题解~~

## 暴力解法

这个暴力解法还是蛮好想的。

对于每个询问，从头到尾搜一遍，找到就输出并 ```break``` ，如果一直找不到最后输出 $-1$ 。

然而这个的时间复杂度是 $O(nm)$，显然过不了。（代码就不贴了）

## 正解

~~这个正解好像也挺好想的~~

题目说序列**单调不减**，于是很容易就想到**二分**。

然而，~~我很懒~~，显然不会写二分，那就只能用 ```STL``` 自带的二分函数—— ```upper_bound``` 和 ```lower_bound```。

这两个函数的作用是二分查找一个数在数组中出现的位置。区别是 ```upper``` 返回第一个大于搜索数的位置，而 ```lower``` 是第一个大于等于的数的位置。显然这道题用的是 ```lower```。

函数的用法：```lower_bound(a.begin(),a.end(),x)``` 返回第一个大于等于 $x$ 的数的地址。而由于是地址，在最后要 $-a$（也就是减去地址）。

会了这个函数，还有一个问题：怎么判断 $-1$ 的情况？

其实也很简单。如果满足，那么一定有 $x=a[ans]$，所以如果不等那么输出 $-1$ 就行了。

说了这么多，代码也就非常好写了。

## 代码

下面是完整 AC 代码——

（~~不能只看这里啊~~）

```cpp
#include<cstdio>
#include<algorithm>//用到lower_bound
using namespace std;
const int MAXN=1e6+10;//注意范围
int read(){//快读
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
int a[MAXN];
int main(){
	int n=read(),m=read();//读入
	for(int i=1;i<=n;i++) a[i]=read();
	while(m--){
		int x=read();
		int ans=lower_bound(a+1,a+n+1,x)-a;//二分搜，注意-a
		if(x!=a[ans]) printf("-1 ");//没有，输出-1
		else printf("%d ",ans);//有，输出ans
	}
	return 0;//华丽结束
}
```
看我这么晚还发题解，总得点个赞再走呀~