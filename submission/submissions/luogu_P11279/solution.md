# P11279 题解

## 思路

很明显本题是求一个字符出现次数的最小值的加强版，具体来说是每一次删除某个字符然后再求。

### Subtask 1

直接暴力枚举即可，$26^4=456976$，稳稳地 $O(26^n)$ 通过。

### Subtask 2

直接输出 $n$ 个 `z` 即可。因为字符串中没有 `z`，所以此时的**不相似度**可以达到最大值。

### Subtask 3

直接暴力统计即可。时间复杂度 $O(n^2)$ 没有任何问题。

### Subtask 4

考虑如何快速计算。

首先算出每一种字符出现的次数，以及所有字符出现次数的最小值和出现次数的最小的字符。

令当前所在位置的字符出现的次数为 $x$，所有字符出现次数的最小值为 $y$。

因为当前出现的不纳入统计，所以当 $x-1\le y$ 时，可以填当前所在位置的字符，不然填全局出现次数的最小的字符。

## 代码


```cpp
#include<bits/stdc++.h>
using namespace std;

int n;
string s;
int ans[140];
int main(){
	cin>>n;
	cin>>s;
	s=' '+s;
	for(int i=1;i<=n;i++){
		ans[s[i]]++;
	}
	char min1='9';
	int min2=1e9;
	for(int i='a';i<='z';i++){
		if(ans[i]<min2){
			min2=ans[i];
			min1=i;
		}
	} 
	for(int i=1;i<=n;i++){
		int now1=ans[s[i]]-1;
		if(now1<min2){
			cout<<(char)s[i];
		}
		else{
			cout<<min1;
		}
	}
	cout<<endl;
	return 0;
}//有谁能比我知道 你的温柔像羽毛
```

笑点：笔者为了防止有人和自己代码完全相同导致自己被判为作弊，在代码末尾写了一句周杰伦《你听得到》的歌词，居然还写错了，现已纠正。