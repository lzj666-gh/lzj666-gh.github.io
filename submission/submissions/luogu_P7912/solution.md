# P7912 题解

在[博客](https://yjh965.github.io/post/csp-j-2021-xiao-xiong-de-guo-lan-ti-jie/)食用更佳。

# 思路

容易想到，可以把每一个块看成一个整体。

由于队列先进先出的特性，可以使用队列维护块。

需要注意的是，当两个块在队列里相邻且元素相同，就可以直接合并。

然后这道题就变成了一道模拟啦！

# 代码

```cpp
#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <queue>

using namespace std;

struct kuai{ // 块
	int st, ed, th;
}f, x, ad;
int n, cnt, t[200002];
queue<kuai> q, q2;
bool used[200001]; // 记录是否被取出
int main(){
	scanf("%d", &n);
	for (int i = 1;i <= n;i ++) scanf("%d", &t[i]);
	t[n + 1] = !t[n];
	for (int i = 2, si = 1;i <= n + 1;i ++){
		if (t[i] != t[i - 1]) q.push((kuai){si, i - 1, t[i - 1]}), si = i; // 把连续一段相同的元素合成一个块
	}
	cnt = n;
	while (cnt){
		while (q.size()){
			f = q.front();
			q.pop();
			while (used[f.st] && f.st <= f.ed) f.st ++; // 如果已经被取了
			if (f.st > f.ed) continue;
			printf("%d ", f.st), cnt --;
			used[f.st] = 1; // 将块的开头元素去掉并输出
			if (f.ed == f.st) continue; // 如果这个块被取完了
			f.st ++;
			q2.push(f); // 先临时存到 q2 里进行合并
		}
		putchar('\n');
		while (q2.size()){
			ad = q2.front();
			q2.pop();
			while (q2.size()){
				x = q2.front();
				if (x.th == ad.th){ // 能合并就合并
					ad.ed = x.ed;
					q2.pop();
				}
				else break;
			}
			q.push(ad); // 丢回 q 里
		}
	}
}
```

# 关于时间复杂度

原本，在这种做法里，每一个水果只会被删除一次，最多会删除 $n$ 次。但是，我的代码实现的可能不太好，最坏时间复杂度是 $O(n \sqrt n)$ 的，为了保留每个元素原本的位置，我使用了一个 `bool` 数组，对每块里的数进行类似于懒惰删除法的操作（见代码中“如果已经被取了”一行），构造 `00000000111111000011011000011111100000000` 这样的数据可以将这部分卡到移动 $O(n \sqrt n)$ 次。像这样的做法实现应该是可以做到 $O(n)$ 的，如果做到了，欢迎与作者讨论实现方式。