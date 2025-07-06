# P11021 题解

求答案并不难，将 $t_i$ 排序，容易发现只需要求 $\max\limits_{i=1}^{n-1}\left\lfloor\frac{|x_i-x_{i+1}|}{|t_i-t_{i+1}|}\right\rfloor$ 的值即可，因为如果 $i,j$ 不相邻，且其中小区间的值都比大区间的小，大区间才有可能是最优解，但显然这不可能，大区间的值一定在所有小区间的最小值和最大值这个范围内。

因此，现在我们要解决如何快速求出修改后的答案这个问题：

注意到每次修改能影响答案的值只有三个：由于原来那个时间点的记录信息没了，所以需要将其左右两边的小区间（这里的小区间指的是相邻两点之间的区间，下同）合并为一个区间，答案可能会变小，同理，由于有新的时间点产生了记录信息，所以就要把原来包含这个时间点的小区间切割成两个区间，答案就可能会变大。最方便实现的是用 set 维护时间点，当然，用普及组的方法配合一些记录数组也是能做的，只不过稍微麻烦了一点。

下面给出由 [jason_sun](https://www.luogu.com.cn/user/399762) 大佬提供的 std：


```cpp
#include<bits/stdc++.h>
using namespace std;
#define ll long long
const int N=2e5+5;
int a[N], b[N];
vector<pair<ll,ll>> vc1;
vector<ll> vc2, vc3, vc4;
int get(pair<ll,ll> x, pair<ll,ll> y){
	return abs(x.second-y.second)/abs(x.first-y.first);
}
void insert(int x, int y, int p, int q){
	auto it=lower_bound(vc1.begin(), vc1.end(), make_pair((ll)x, (ll)y));
	auto it1=it, it2=it;
	it1--;
	if(*it1==make_pair((ll)p, (ll)q)) it1--;
	if(*it2==make_pair((ll)p, (ll)q)) it2++; 
	vc4.push_back(get(*it1, {x, y}));
	vc4.push_back(get({x, y}, *it2));
}
void erase(int x, int y){
	auto it=lower_bound(vc1.begin(), vc1.end(), make_pair((ll)x, (ll)y));
	auto it1=it, it2=it;
	it1--, it2++;
	vc4.push_back(get(*it1, *it2));
	vc3.push_back(get(*it1, *it));
	vc3.push_back(get(*it, *it2));
}
bool cmp(int x, int y){
	return x>y;
}
int main(){
	vector<pair<ll,ll>>().swap(vc1);
	vector<ll>().swap(vc2);
	vc1.push_back({-1e18, -1});
	vc1.push_back({1e18, 1e9+1});
	vc2.push_back(0);
	int n, m;
	scanf("%d%d", &n, &m);
	for(int i=1; i<=n; ++i){
		scanf("%d%d", &a[i], &b[i]);
		vc1.push_back({b[i], a[i]});
	}
	sort(vc1.begin(), vc1.end());
	for(int i=0; i<n-1; ++i){
		vc2.push_back(get(vc1[i], vc1[i+1]));
	}
	sort(vc2.begin(), vc2.end(), cmp);
	for(int i=1; i<=m; ++i){
		vector<ll>().swap(vc3);
		vector<ll>().swap(vc4);
		int x, y;
		scanf("%d%d", &x, &y);
		erase(b[x], a[x]);
		insert(y, a[x], b[x], a[x]);
		sort(vc3.begin(), vc3.end(), cmp);
		sort(vc4.begin(), vc4.end(), cmp);
		ll ans=vc4[0]; int p=0;
		while(p<(int)vc3.size()&&vc2[p]==vc3[p]) p++;
		ans=max(ans, vc2[p]);
		printf("%lld\n", ans);
	}
	return 0;
}
```