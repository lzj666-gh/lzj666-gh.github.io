# P11840 题解

# 题解：P11840 [USACO25FEB] Vocabulary Quiz S

~~不是，现在银组都简单成这样了？看看去年二月银组，难度可是直逼铂金呀。~~

[视频题解](https://www.bilibili.com/video/BV1n1P5eVEJo/?spm_id_from=333.1387.homepage.video_card.click&vd_source=e30c5bf3cf935b96ec8bab557be3afbd)。

介绍一种时间复杂度 $O(n)$，非常简单直白，码量小，且不需要 st 表，lca 的方法。

## Problem Statement

[P11840](https://www.luogu.com.cn/problem/P11840)。

## Solution

虽然题目感觉有些绕，但是很快就能发现其实这 $n - 1$ 个点构成的就是一颗以节点 0 为根的树，每个节点的父节点就是 $p_i$，而那 $m$ 个 "不作为另一个单词前缀的单词" 就是所有的叶子节点。

现在我们先不考虑读的顺序，就是假设目前还没有任何单词因为被读过而删除掉了。

我们发现对于一个叶节点 $i$，想要知道它的具体身份至少需要读到的字符数就是 $i$ 深度最深的，有超过一个儿子的祖先节点的深度。为什么呢？设这个节点是 $j$, 发现如果我们不把 $j$ 读完，我们并不知道这个单词到底是 $i$，还是 $j$ 的另一个儿子下的某一个叶子，因此至少需要把 $j$ 读完，且还要再多读一个字符。同时读 $dep_j + 1$ 也一定足够确定 $i$ 了（$dep_j$ 为 $j$ 节点的深度），因为我们知道从 $j$ 到 $i$ 没有任何其他节点有超过一个儿子了，因此 $j$ 下面唯一的叶节点就是 $i$。

现在发现删除节点也很简单了，直接将此节点的父亲出度减一就行了。如果发现一个节点的出度已经为零了（儿子被删完了）说明他下面没有叶节点了，就把它也删除就行了。

代码十分简洁好写。

## Code

赛时代码。


```cpp
#include<bits/stdc++.h>
#define int long long
using namespace std;
int n, m, p[1000005], dep[1000005];
int cnt[1000005];
vector<int> e[1000005];
void pdfs(int x){
	dep[x] = dep[p[x]] + 1;
	if(!cnt[x])m++;
	for(auto i: e[x]){
		pdfs(i);
	}
}
int rdfs(int x){
	if(cnt[x]){
		//this point has other sons
		return dep[x] + 1;
	}
	if(x == 0){
		//last one
		return 0;
	}
	cnt[p[x]]--;//erase this node
	return rdfs(p[x]);
}
signed main(){
	cin>>n;
	for(int i = 1; i <= n; i++){
		cin>>p[i];
		cnt[p[i]]++;
		e[p[i]].push_back(i);
	}
	p[0] = 0;
	dep[0] = -1;
	//so when we do dep[i] = dep[p[i]] + 1 we have dep[0] = 0
	pdfs(0);
	//pre process depth and m
	for(int i = 1; i <= m; i++){
		int now;
		cin>>now;
		cout<<rdfs(now)<<endl;
		//reverse dfs
	}
	return 0;
}
```

## After thoughts

对于银组来说真的太简单了，顺着想一步一步非常直白就出来了，考场上花了大概 10 分钟。