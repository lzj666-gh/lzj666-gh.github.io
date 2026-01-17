# P7284 题解

不得不说，这是一道**极为经典**的**广搜变形**题目，做完之后无论是 BFS 还是 pair 的使用都更加娴熟，收获颇丰。李煜东·《算法竞赛进阶指南》中在广搜变形这一章内有一道非常相似的题目。当时我以为自己会了，就没有多想。没想到今天遇到原题竟然还写错了好几次，作文以记之：

对于这道题目，第一眼看出来是 BFS 应该不难，但是这里有一个问题：由于各个状态被加入队列的时候所需要改变的次数是不同的（对于每个点），而 BFS 的要求是对于序列中的每一个元素，其第一关键字都应该是不递减的。

那么这个时候该怎么办呢？

- Solution1

使用 SPFA,Dijkstra 等最短路算法，通过多次更新/序列内排序等方法保证正确性。但这么做效率显然不高（至少增加一个   log，如果题目要求更严格那么显然是过不去的。

- Solution2

使用**双端队列**BFS，即每次加入新状态的时候判断代价是否需要增加，如果需要，就压进队头，不需要则压进队尾。可以证明，这样对于每一个点每次得到的最优状态一定比较劣状态更先取出。

至于输出修改后的地图，这个点也难了我一会儿。最后想到的办法是每次一个节点能够被更新就说明它的前驱被修改一定更优，所以我们用 pre 数组来记录每个点的前驱，最后从终点往起点扫一遍即可。

不得不说思维难度比较大，而且需要抽象思维。

题外话：我真的很佩服发明这种算法的人，我只能用优美这个词形容双端队列和 BFS 的结合，真的太优美了。

复杂度 $O(r*s)$

Code:

```
#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> pr;
#define mp make_pair
int n,m;
deque <pr> dq;
char sea[2005][2005];
int sx,sy,ex,ey,dis[2005][2005];
pr pre[2005][2005];
int dx[4]={1,-1,0,0},dy[4]={0,0,1,-1};
char dir[4]={'v','^','>','<'};
int main(){
	cin>>n>>m;
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++){
			cin>>sea[i][j];
			if(sea[i][j]=='x')
				ex=i,ey=j;
			else if(sea[i][j]=='o')
				sx=i,sy=j;
		}
	memset(dis,0x3f,sizeof(dis));
	dq.push_back(mp(sx,sy));
	dis[sx][sy]=0;
	while(!dq.empty()){
		pr temp=dq.front();
		dq.pop_front();
		if(temp==mp(ex,ey)||dis[temp.first][temp.second]>=dis[ex][ey])
			continue;
		//cout<<temp.first<<" "<<temp.second<<endl;
		for(int i=0;i<4;i++){
			int tx=temp.first+dx[i],ty=temp.second+dy[i];
			if(tx<1||tx>n||ty<1||ty>m)
				continue; 
			int w=(sea[temp.first][temp.second]==dir[i]||sea[temp.first][temp.second]=='o')?0:1;
			if(dis[tx][ty]>dis[temp.first][temp.second]+w){
				dis[tx][ty]=dis[temp.first][temp.second]+w;
				pre[tx][ty]=temp;
				if(w==0)
					dq.push_front(mp(tx,ty));
				else
					dq.push_back(mp(tx,ty));
			}
		}
	}
	pr before=pre[ex][ey],now=mp(ex,ey);
	//cout<<before.first<<" "<<before.second<<" 114514"<<endl;
	while(before!=mp(sx,sy)){
		if(before.first==now.first+1)
			sea[before.first][before.second]='^';
		if(before.first==now.first-1)
			sea[before.first][before.second]='v';
		if(before.second==now.second+1)
			sea[before.first][before.second]='<';
		if(before.second==now.second-1)
			sea[before.first][before.second]='>';
		now=before;
		before=mp(pre[before.first][before.second].first,pre[before.first][before.second].second);
	}
	cout<<dis[ex][ey]<<endl;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=m;j++)
			cout<<sea[i][j];
		cout<<endl;
	}
	return 0;
}
```
