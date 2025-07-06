# P7692 题解

题意不多赘述。

求超车次数，可以发现能将问题转换为一个逆序对问题。

由于速度的范围只有 $1\sim 99$ 所以我们可以直接开个桶储存 $1\sim i-1$ 的速度，然后直接暴力统计前面的速度大于当前的速度的个数累加就行。

然后就是超车问题。

我们首先将车按位置排序，可以发现所有车都无法越位超车，即第 $i$ 辆车不可能在：

第 $i$ 辆车不超过第 $i+1$ 辆车且第 $i+1$ 辆车不超过第 $i+2$ 辆车的情况下超过第 $i+2$ 辆车。

所以我们可以发现当前时间后的第二次超车一定是相邻两辆车之间发生的。

所以我们直接开个结构体堆维护相邻两辆车之间的超车所用相对时间。

优先比较时间就行。

剩下的似乎就是模拟了。

因为担心出现精度问题，所以这里直接用 `double` 类型储存时间。

```cpp
#include<bits/stdc++.h>
#define int long long
using namespace std;
const int N = 250010;
int n, x[N],v[N];
int f[N],id[N];
//排名，编号
struct fyn1 {
	int x, y;
	double t;
	inline bool operator <(const fyn1 &fyn)const {
		return t!=fyn.t? t > fyn.t: f[x] > f[fyn.x];
	}
};

priority_queue<fyn1> q;
int fyn[110];

signed main() {

	cin>>n;
	int ans = 0;
	for (int i = 1; i <= n; ++i) {
		cin>>x[i]>>v[i];
		f[i] = id[i] = i;
		for(int j=v[i]+1; j<=99; ++j) {
			ans+=fyn[j];
			ans%=1000000;
		}
		++fyn[v[i]];
		if(i^1 && v[i - 1] > v[i])
			q.push((fyn1) {
			i-1,i,1.0*(x[i] - x[i - 1]) / (v[i - 1] - v[i])
		});//将相邻超车时间全部记录下来

	}

	cout<<ans<<endl;//超车次数

	int cnt = 1;
	while (cnt <= 10000 && q.size()) {//控制次数
		int nx=q.top().x,ny=q.top().y;
		q.pop();
		if(f[nx]+1!=f[ny])continue;
		else
			++cnt;
		cout<<nx<<' '<<ny<<endl;

		swap(id[f[nx]], id[f[ny]]);
		swap(v[f[nx]], v[f[ny]]);
		swap(x[f[nx]], x[f[ny]]);
		swap(f[nx], f[ny]);//交换位置

		if (f[nx]<n && v[f[nx]]>v[f[nx]+1]&&f[id[f[nx]]] + 1 == f[id[f[nx] + 1]])//若能超车且相邻
			q.push((fyn1) {
			id[f[nx]],id[f[nx]+1],1.0*(x[f[nx] + 1] - x[f[nx]]) / (v[f[nx]] - v[f[nx] + 1])
		});

		if (f[ny] > 1 && v[f[ny] - 1] > v[f[ny]] && f[id[f[ny] - 1]] + 1 == f[id[f[ny]]])//若能超车且相邻
			q.push((fyn1) {
			id[f[ny] - 1], id[f[ny]], 1.0*(x[f[ny]] - x[f[ny] - 1]) / (v[f[ny] - 1] - v[f[ny]])
		});
	}
	return(0-0);
}
```
