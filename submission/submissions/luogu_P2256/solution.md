# P2256 题解

## 裸的并查集+map
## （STL大法好！）


------------
题目背景和题目描述~~非常直接地~~告诉我们：

这就是个并查集模板，只不过改成了字符串


------------
因此我们的问题就成了如何处理字符串

当然，可以用结构体，结构体的成员包含编号和名字

但是，还有一个更好用的东西:STL中的**map**

直接**建立一个由字符串到字符串的映射**代替数组

然后把并查集的模板粘上去改一改就成了

（没错，就是这么水）

------------
代码来了~
```cpp
#include<iostream>
#include<cstdio>
#include<map>//map库
using namespace std;
map<string,string> a;//建立映射
string fin(string x){//查找字符串x的祖先
	if(a[x]==x) return x;
	else return a[x]=fin(a[x]);//路径压缩
}
int main(){
	int n,m,k;
	string s1,s2;//s1,s2可重复使用
	cin>>n>>m;
	for(int i=1;i<=n;++i){
		cin>>s1;//选手名字
		a[s1]=s1;//每个人的祖先初始化为自己
	}
	for(int i=1;i<=m;++i){
		cin>>s1>>s2;//两位选手
		string x1=fin(s1),x2=fin(s2);//合并
		if(x1!=x2) a[x1]=x2;
	}
	cin>>k;
	for(int i=1;i<=k;++i){
		cin>>s1>>s2;
		string x1=fin(s1),x2=fin(s2);//查询
		if(x1!=x2) printf("No.\n");
		else printf("Yes.\n");
	}
	return 0;//后话：STL大法好！
}
```


------------
你AC了吗？AC了就点个赞呗