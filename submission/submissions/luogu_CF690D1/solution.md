# CF690D1 题解

# [CF690D1 The Wall(easy)](https://www.luogu.com.cn/problem/CF690D1)
- [更好的阅读体验](https://www.cnblogs.com/wanguan/p/17008864.html)

## 正文

很显然啊，这是在考一个叫连通块的东东，于是~~蒟蒻的~~我马上想到了连通块必备：并查集。

如果一个块四边连通了其它的块，那么合并这两个块。

当然，并查集要用二维的：

```cpp
typedef pair<int,int> pii;
pii f[1005][1005];
void init(){//初始化并查集
	for(int i=1;i<=n;i++)	for(int j=1;j<=m;j++)
		f[i][j]={i,j};
}
pii fd(pii a){//查找根
	if(f[a.fi][a.sc]==a)	return a;
	return f[a.fi][a.sc]=fd(f[a.fi][a.sc]);
}
void unio(pii a,pii b){//合并a和b所在的集合
	f[a.fi][a.sc]=fd(b);
}
```

最后就是查重，这里我用了手打的哈希表 `set`。

遍历并查集数组，将每个子节点的根节点放入 `set`，去重，最后看 `set` 的元素数就可以。

```cpp
struct set{
	int s[1000005];
	void insert(pii a){
		s[a.fi*105+a.sc]++;
	}
	int size(){
		int ret=0;
		for(int &i:s)
			if(i)	ret++;
		return ret;
	}
};
```

最后综合：

```cpp
#include<iostream>
#include<bits/stl_pair.h>
#define fi first
#define sc second
using namespace std;
typedef pair<int,int> pii;
pii f[1005][1005];
int n,m;
char a[1005][1005];
struct set{
	int s[1000005];
	void insert(pii a){
		s[a.fi*105+a.sc]++;
	}
	int size(){
		int ret=0;
		for(int &i:s)
			if(i)	ret++;
		return ret;
	}
};
set s;
void init(){
	for(int i=1;i<=n;i++)	for(int j=1;j<=m;j++)
		f[i][j]={i,j};
}
pii fd(pii a){
	if(f[a.fi][a.sc]==a)	return a;
	return f[a.fi][a.sc]=fd(f[a.fi][a.sc]);
}
void unio(pii a,pii b){
	f[a.fi][a.sc]=fd(b);
}
int main(){
	ios::sync_with_stdio(false),cin.tie(0);
	cin>>n>>m;
	init();
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++){
			cin>>a[i][j];
			if(a[i][j]=='.')	continue;
			if(a[i-1][j]=='B')	unio({i-1,j},{i,j});
			if(a[i+1][j]=='B')	unio({i+1,j},{i,j});
			if(a[i][j-1]=='B')	unio({i,j-1},{i,j});
			if(a[i][j+1]=='B')	unio({i,j+1},{i,j});
		}
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)
			if(a[i][j]=='B')	s.insert(fd({i,j}));
	cout<<s.size();
}
```

[完结！！](https://www.luogu.com.cn/record/98117184)