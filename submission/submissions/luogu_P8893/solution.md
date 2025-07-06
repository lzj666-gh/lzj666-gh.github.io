# P8893 题解

# solution:  
我们可以发现，模拟的时间复杂度是 $O(n^2)$ ，可以通过该题。  
那么怎么模拟呢？将一开始的推荐题目放到明天推荐题目中，不停地做以下操作：
1. 将明天推荐题目复制到今天推荐题目中并清空。如果明天推荐题目数为零，输出 `-1` ，结束。
2. 否则处理今天推荐题目，记录当前题目已被做过，并遍历题目集合包含此题的所有题目。
3. 将当前题目的需做题数减一，如果需做题数为零，那将此题加入明天推荐题目中。
4. 如果第 `k` 道题已被做过，退出循环，输出当前天数；否则将天数加一。
# code：
```
#include<bits/stdc++.h>
using namespace std;
const int N=5005;
int n,k,r,day,vis[N],t[N];
//vis 记录某题是否已做，t 记录做某题所需要做的题数
int w,nw,ok[N],nok[N];
//分别记录今天推荐题目，明天推荐题目
vector <int> relat[N];
//relat 记录某题在哪些题的题目集合里
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);cout.tie(0);
	cin>>n>>k>>nw;
	for(int i=1;i<=nw;i++) cin>>nok[i];
	cin>>r;
	for(int i=1,x,y;i<=r;i++){
		cin>>x>>t[x];
		for(int j=1;j<=t[x];j++){
			cin>>y;
			relat[y].push_back(x);
		}
	}
	while(1){
		//明天推荐题目复制到今天推荐题目里
		w=nw;nw=0;
		for(int i=1;i<=w;i++)
			ok[i]=nok[i];
		//如果当天没有任何推荐题目，无解
		if(!w){
			cout<<"-1\n";
			return 0;
		}
		for(int i=1;i<=w;i++){
			//记录已做
			vis[ok[i]]=1;
			//遍历包含本题的题目集合
			for(int j=0,l=relat[ok[i]].size();j<l;j++){
				t[relat[ok[i]][j]]--;
				//如果需做题数为零，则明天能做这道题
				if(!t[relat[ok[i]][j]]){
					nok[++nw]=relat[ok[i]][j];
				}
			}
		}
		//做完了第k道题，退出循环
		if(vis[k]) break;
		day++;
 	}
	cout<<day<<'\n';
	return 0;
}
```
第一次发题解，若有错误之处还敬请各位神犇斧正。