# P1536 题解

题目描述

某市调查城镇交通状况，得到现有城镇道路统计表。表中列出了每条道路直接连通的城镇。市政府“村村通工程”的目标是使全市任何两个城镇间都可以实现交通（**但不一定有直接的道路相连，只要相互之间可达即可**）。请你计算出最少还需要建设多少条道路？



------------


**这一道题可以用并查集的方法做**

**思路：输入两个村庄后就把它们连起来，输入完毕后用i从1循环到n，所以如果i的父亲为它本身的话（它是祖先，它没有父亲），ans+1。答案要减1，因为三个点中只需用两条线连接，无需用三条线连接。**

### 并查集

**并查集是一种树型的数据结构，用于处理一些不交集的合并及查询问题（不交集的意思是两个集合中没有相同的元素）。**

并查集分两个主要步骤——**合并**，**查找**

### 1.find：确定元素属于哪一个子集。它可以被用来确定两个元素是否属于同一子集。


code : 

```cpp
int find(int x) 
{
    if(x != fa[x])//当x不等于它的爸爸时(当它是祖先时，它没有爸爸) 
    {
        fa[x] = find(fa[x]);//继续找他的爸爸的爸爸 
    }
    return fa[x];//返回祖先 
}//查找 

```

### 2.unity：将两个子集合并成同一个集合。

code : 

```cpp
void unity(int x, int y)
{
    int r1 = find(x);//找到x的祖先 
    int r2 = find(y);//找到y的祖先 
    fa[r1] = r2;//祖先和祖先结为父子(谁是父亲谁是儿子都可以) 
}//合并 
```





完整代码如下：


```cpp
#include <bits/stdc++.h>
using namespace std;
int fa[1000001], n, m, x, y;
int find(int x)//并查集(路径压缩) 
{
    if(x != fa[x])//当x不等于它的爸爸时(当它是祖先时，它没有爸爸) 
    {
        fa[x] = find(fa[x]);//继续找他的爸爸的爸爸 
    }
    return fa[x];//返回祖先 
}//查找 
void unity(int x, int y)
{
    int r1 = find(x);//找到x的祖先 
    int r2 = find(y);//找到y的祖先 
    fa[r1] = r2;//祖先和祖先结为父子(谁是父亲谁是儿子都可以) 
}//合并 
int main()
{
	while(true)
	{
		int ans = 0;//ans要在循环中定义为0
		scanf("%d", &n);
		if(n == 0)
		{
			return 0;
		}
		scanf("%d", &m);
	    for(int i = 1; i <= n; i++)
	    {
	        fa[i] = i;//初始化自己的父亲是自己 
	    }
	    for(int i = 1; i <= m; i++)
	    {
	        scanf("%d %d", &x, &y);
	        unity(x, y);//合并x和y 
	    }
	    for(int i = 1; i <= n; i++)
	    {
	    	if(find(i) == i)//自己的父亲等于自己本身
	    	{
	    		ans++;
			}
		}
		printf("%d\n", ans - 1);//答案减一 
	}
    return 0;
}
```

