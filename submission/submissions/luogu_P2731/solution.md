# P2731 题解

~~简单的开始~~ 
## 完美の开始
这里数组什么的用来干什么后面标注的清楚了

------------
```cpp
#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int map[10001][10001];//记录两个点之间的路径个数 
int du[10001];//辅助记录奇点 
int lu[10001];//记录路径 
int n,x,y,js=0;//输入的数据和计数器
int maxn=0;
```
------------
## 正题开始QWQ
先说思路：
很简单和一本通上的例题一笔画没什么差别就是多了一个点可能会重复出现罢了。


------------
可以按正常的输入然后存入map数组（PS：如果你用的是万能头就不要定义map数组啦，可以定义一个f数组什么的)这里就出现和一本通上一笔画的差距了，是累减，每次记录就加一而不是赋值为1
。。。。因为后面很多地方需要用到点的个数，但是却没有输入所以专门定义一个maxn来找输入的最大值就是点的个数啦

------------

注意这里要定义一个数组记录出现次数，在输入的时候每次一出现就加一然后在后面单独找，看看谁不是2的倍数记录下来结束循环

------------
```cpp
scanf("%d",&n);
	for(int i=1;i<=n;++i)
	{
		scanf("%d%d",&x,&y);
		map[x][y]++;
		map[y][x]++;
		du[x]++;
		du[y]++;//记录出现的次数 
		maxn=max(maxn,max(x,y));
	}
	int start=1;//默认奇点是1 
	for(int i=1;i<=maxn;++i)
	{
		if(du[i]%2)//找到奇点 
		{
			start=i;//记录奇点
			break;//然后结束循环 
		}
	}
	find(start);//从奇点开始找 
	for(int i=js;i>=1;i--)
	{
		printf("%d\n",lu[i]);//挨个输出路径并且换行 
	}
	return 0;
```

------------
然后就说函数部分了，也就是上面的find函数QWQ.这里很好想的，就是模板改一下，变为0改为减一QWQ简单的我不想多说
函数代码


------------

```cpp
void find(int i)//
{
	int j;
	for(j=1;j<=maxn;++j)//而且这里不是n而是maxn因为n不是点的个数而是下面有多少行 
	{
		if(map[i][j]>=1)
		{
			map[i][j]--;//删去边一次吗避免重复 
			map[j][i]--;//z这里和一笔画不一样这里是累减而一笔画直接变成0 
			find(j);
		}
	}
	lu[++js]=i;
}
```


------------

## 话不多说完整代码

------------

```cpp
//防伪标识
#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int map[10001][10001];//记录两个点之间的路径个数 
int du[10001];//辅助记录奇点 
int lu[10001];//记录路径 
int n,x,y,js=0;
int maxn=0;
void find(int i)//
{
	int j;
	for(j=1;j<=maxn;++j)//而且这里不是n而是maxn因为n不是点的个数而是下面有多少行 
	{
		if(map[i][j]>=1)
		{
			map[i][j]--;//删去边一次吗避免重复 
			map[j][i]--;//z这里和一笔画不一样这里是累减而一笔画直接变成0 
			find(j);
		}
	}
	lu[++js]=i;
}
int main()
{
	scanf("%d",&n);
	for(int i=1;i<=n;++i)
	{
		scanf("%d%d",&x,&y);
		map[x][y]++;
		map[y][x]++;
		du[x]++;
		du[y]++;//记录出现的次数 
		maxn=max(maxn,max(x,y));
	}
	int start=1;//默认奇点是1 
	for(int i=1;i<=maxn;++i)
	{
		if(du[i]%2)//找到奇点 
		{
			start=i;//记录奇点
			break;//然后结束循环 
		}
	}
	find(start);//从奇点开始找 
	for(int i=js;i>=1;i--)
	{
		printf("%d\n",lu[i]);//挨个输出路径并且换行 
	}
	return 0;
}
```

综上所述，已AC
# 完美の结束
（看的这么累，不点个赞再走QWQ）