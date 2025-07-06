# P11839 题解

# 题解：P11839 [USACO25FEB] The Best Lineup S

## Preface

提供一种 $O(n)$ 贪心解法，自认为比官解更好理解，代码也非常好写。

[视频题解。](https://www.bilibili.com/video/BV12mP3e5ECM/?spm_id_from=333.1387.homepage.video_card.click&vd_source=e30c5bf3cf935b96ec8bab557be3afbd)

9 场银组，~~我终于 Au 了~~。分数线才 700 分？~~这应该是 2020 年以来最简单的一场银组了~~。

## Problem Statement

[P11839](https://www.luogu.com.cn/problem/P11839)。
有一个序列，给你一次操作改变原序列顺序的机会，让你从前往后每个数可以选或不选，构造一个字典序最大的序列。

## Solution

首先，由于是要最大化字典序，显然是从最大的开始，能选就选。

因此对原数组按照元素大小为第一关键字降序排序，原位置为第二关键字升序排序（至于为什么等会解释）。然后就贪心的从前往后能选就选（因为字典序吗，前面更优就总体更优）。

如何判断能不能选呢？记录一个 $max1$ 和一个 $max2$， 分别代表已经选了的中，原位置最靠后的（$max1$），和已经选了的中原位置第二靠后的（$max2$）。

此时发现对于一个每一个元素 $i$，想选他则他必须要么在所有已经选了的元素之后出现，也就是 $pos_i > max1$，**或者已经选了的里面只有一个原位置比它靠后**，也就是 $max1 > pos_i > max2$。如果这样我们则可以通过用掉我们有的一次操作来把那个那个唯一一个比 $i$ 靠后的元素挪到 $i$ 前面。如果连 $max2$ 都比 $i$ 靠后，或者我们已经用了一次操作的机会了，则只能跳过 $i$ 不选了。

但是我们只有一次操作，怎么确保把它用到最优的 $i$ 上呢？其实第一次需要就用就行了。因为假设我们第一次需要的时候不用，而是跳过这个 $i$，那不管后面选的有多优，字典序都一定不可能更大了。因为我们是根据元素值的大小排的序。

但别忘了最后还有两个元素相同的情况，这种情况下我们之所以要以初始位置为第二关键字升序排序就是为了不会在两个相同的元素上因为位置反了而浪费掉操作的机会。

## Code
实现非常简单，记录 $max1$ 和 $max2$，以及是否用过操作机会就行了。


```cpp
#include<bits/stdc++.h>
#define int long long
using namespace std;
int T1, n, a[200005];
pair<int, int> val[200005];
int cmp(pair<int, int> &x, pair<int, int> &y){
	if(x.first != y.first)return x.first > y.first;
	else return x.second < y.second;
	//if they have different value, return bigger one, otherwise
	//return the one that appeared earlier
}
signed main(){
	cin>>T1;
	while(T1--){
		cin>>n;
		for(int i = 1; i <= n; i++){
			cin>>a[i];
			val[i].first = a[i];
			val[i].second = i;
		}
		int ma = 0, ma2 = 0, moved = 0, outp = 0;
		sort(val + 1, val + n + 1, cmp);
		for(int i = 1; i <= n; i++){
			if(val[i].second > ma){
				ma2 = ma;				
				ma = val[i].second;
				if(outp)cout<<" "<<val[i].first;
				else cout<<val[i].first;
				outp = 1;
			}else if(val[i].second > ma2 && !moved){
				ma = val[i].second;
				//we move ma
				if(outp)cout<<" "<<val[i].first;
				else cout<<val[i].first;
				outp = 1;
				moved = 1;
//				cout<<val[i].second<<endl;
			}
		}
		cout<<endl;
	}
	return 0;
}

```

赛时代码，略丑。

## After thought

这场真的有点简单了，~~我都怀疑 USACO 是不是故意放水，打算再加一个组呀？就像 2015 年加白金之前放水那样。~~

求赞。