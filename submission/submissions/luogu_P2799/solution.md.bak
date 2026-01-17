# P2799 题解

这是一道很不（e）错（xin）的题目，让我们来看看。


------------
很明显，此处应要判断项链是否是回文串。我用了一个递归函数来判断回文串：
```cpp
int jc(int n){                  //n为搜索右界
	if((n+1)%2)return n+1;  //如果是奇数直接输出长度
	if(n==0)return 1;       //如果只剩1个字母直接输出1
	int l=0,r=n;            //设置左右界
	while(l<r){
		if(s[l]!=s[r])
			return n+1;//输出当前长度
		++l; --r;       //左界右移，右界左移
	}
	return jc(r);           //返回下一段最短长度
}
```
这下，main函数里就干净多了：
```cpp
string s;
int main(){
	cin>>s;
	printf("%d",jc(s.size()-1));//直接调用
	return 0;
}
```
总代码如下：
```cpp
#include <bits/stdc++.h>
using namespace std;
string s;
int jc(int n){
	if((n+1)%2)return n+1;
	if(n==0)return 1;
	int l=0,r=n;
	while(l<r){
		if(s[l]!=s[r])
			return n+1;
		++l; --r;
	}
	return jc(r);
}
int main(){
	cin>>s;
	printf("%d",jc(s.size()-1));
	return 0;
}
```
唠叨几句：

1、回文串标程请务必记住！！！

2、审题请务必仔细！！！

~~3、看完题解一定要点赞+评论！！！~~