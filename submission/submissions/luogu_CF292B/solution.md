# CF292B 题解

[传送门](https://www.luogu.com.cn/problem/CF292B)

这个题其实很简单啦~~，只需要分清楚三种图性质就行啦。

### 链形结构：

![](https://cdn.luogu.com.cn/upload/image_hosting/qsrx04hj.png)

如上图，就是一个非常明显的链形结构。

根据上图，我们可以发现：

**链形结构有且只有两个入度和出度之和（以下简称出入和）为 $1$ 的点，剩余点出入和皆为 $2$。**

根据这个性质，我们就可以判断是否是链形结构：

```cpp
bool bus()//链形结构
{
	int cnt1=0,cnt2=0;
	for(int i=1;i<=n;i++)
	{
		if(a[i].size()>=3) return 0;//出入和不是1或2
		else if(a[i].size()==1) ++cnt1;//出入和为1
		else ++cnt2;//出入和为2
	}
	return cnt1==2;//判断出入和为1的点是否有两个
}
```

### 环形结构

![](https://cdn.luogu.com.cn/upload/image_hosting/7cgxt5n7.png)

如上图，就是一个基本的环形结构。

我们就能发现：

**当所有点得出入和皆为 $2$ 时，它是环形结构。**

根据环形结构的特点我们就能判断它了：

```cpp
bool ring()//环形结构
{
	for(int i=1;i<=n;i++)
	{
		if(a[i].size()!=2) return 0;//出入和不为2
	}
	return 1;//出入和皆为2
}
```

### 星形结构

![](https://cdn.luogu.com.cn/upload/image_hosting/bu9sno2y.png)

见上图，很明显就是一个星形结构

我们能够发现：

**当所有点都围绕着其中一个点时，即有一个点出入度为 $n - 1$ 其他所有点出入度为 $1$ 时，它是星形结构。**

写出如下代码：

```cpp
bool star()//星型结构
{
	int cntn=0,cnt1=0;
	for(int i=1;i<=n;i++)
	{
		if(a[i].size()!=1 && a[i].size()!=n-1) return 0;//出入度不为1或n-1
		else if(a[i].size()==n-1) ++cntn;//中间那个点
		else ++cnt1;//分散在两边的点
	}
	return cnt1==n-1 && cntn==1;//只能有1个和n-1个
}
```

### 完整代码：

```cpp
#include<bits/stdc++.h>
using namespace std;

#define LL long long
#define LI long long int
#define UI unsigned int
#define UL unsigned long long
#define ULI unsigned long long int

const int MAXN=100000+5;
vector<int>a[MAXN]; //用vector存图
int n,m;

bool bus()//链形结构
{
	int cnt1=0,cnt2=0;
	for(int i=1;i<=n;i++)
	{
		if(a[i].size()>=3) return 0;//出入和不是1或2
		else if(a[i].size()==1) ++cnt1;//出入和为1
		else ++cnt2;//出入和为2
	}
	return cnt1==2;//判断出入和为1的点是否有两个
}

bool ring()//环形结构
{
	for(int i=1;i<=n;i++)
	{
		if(a[i].size()!=2) return 0;//出入和不为2
	}
	return 1;//出入和皆为2
}

bool star()//星型结构
{
	int cntn=0,cnt1=0;
	for(int i=1;i<=n;i++)
	{
		if(a[i].size()!=1 && a[i].size()!=n-1) return 0;//出入度不为1或n-1
		else if(a[i].size()==n-1) ++cntn;//中间那个点
		else ++cnt1;//分散在两边的点
	}
	return cnt1==n-1 && cntn==1;//只能有1个和n-1个
}

int main()
{
    ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	cin>>n>>m;
	for(int i=1;i<=m;i++)
	{
        //存图
		int u,v;
		cin>>u>>v;
		a[u].push_back(v);
		a[v].push_back(u);
	}
	if(bus()) return cout<<"bus topology\n",0;//满足链形结构
	if(ring()) return cout<<"ring topology\n",0;//满足环形结构
	if(star()) return cout<<"star topology\n",0;//满足星型结构
	cout<<"unknown topology\n";//什么都不满足
    return 0;
}

```