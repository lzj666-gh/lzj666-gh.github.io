# P6033 题解

这道题很有意思，也很清真。贪心思路想必大家都已经了解了，就是每一次选取最小的两堆果子进行合并，但是我们怎么选取呢？优先队列确实是一种比较优秀的解法，但是他还不够优秀，这里要求是$O(n)$的算法。

我们回归问题的本质，我们还是要选取最小的两堆果子，最清真、最自然的方式显然是排序了吧。先排序，选取最小的两堆果子，然后合并，插入。但是插入的效率太低了，我们想要优化。

我们可以把这些需要插入的点用一个队列存储起来，首先这些需要插入的点肯定会越来越大 ~~显然~~ ， 这相当于延迟插入。当我们目标插入点就是我们当前最小的那一堆的时候，我们就把他插入进来。

以上是精神，代码写出来大概就是，桶排，建立两个队列，排序结果放进第一个当中，合并结果放在第二个当中，每次选从两个队列队头选取比较小的合并。

代码如下：

```cpp

#include <cstdio>
#include <queue>
#define int long long
using namespace std;
queue <int> q1;
queue <int> q2;
int to[100005];
void read(int &x){ 
	int f=1;x=0;char s=getchar();
	while(s<'0'||s>'9'){if(s=='-')f=-1;s=getchar();}
	while(s>='0'&&s<='9'){x=x*10+s-'0';s=getchar();}
	x*=f;
}
signed main() {
	int n;
	read(n);
	for (int i = 1; i <= n; ++i) {
		int a;
		read(a);
		to[a] ++;
	}
	for (int i = 1; i <= 100000; ++i) {
		while(to[i]) {
			to[i] --;
			q1.push(i);
		}
	}
	int ans = 0;
	for (int i = 1; i < n; ++i) {
		int x , y;
		if((q1.front() < q2.front() && !q1.empty()) || q2.empty()) {
			x = q1.front();
			q1.pop();
		}
		else {
			x = q2.front();
			q2.pop();
		}
		if((q1.front() < q2.front() && !q1.empty()) || q2.empty()) {
			y = q1.front();
			q1.pop();
		}
		else {
			y = q2.front();
			q2.pop();
		}
		ans += x + y;
		q2.push(x + y);
	} 
	printf("%lld" , ans);
	return 0;
} 

```