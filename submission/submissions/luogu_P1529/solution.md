# P1529 题解

这一题看见大家用dijkstra,spfa，不禁感慨，这年头都不看数据范围吗？最多52个点

flyod稳过呀，见丑陋代码

```cpp
#include<bits/stdc++.h>
using namespace std;
const int inf=1<<30;
int dist[60][60];
int getnum(char c){
	if(c>='a'&&c<='z')return c-'a'+26;
	else return c-'A';
}
int main(){
	for(int i=0;i<60;i++)for(int j=0;j<60;j++)dist[i][j]=inf-1;
	int m;
	cin>>m;
	while(m--){
		string s1,s2;int d;
		cin>>s1>>s2>>d;
		//cout<<getnum(s1[0])<<" "<<getnum(s2[0])<<" "<<d<<endl;
		dist[getnum(s1[0])][getnum(s2[0])]=min(dist[getnum(s1[0])][getnum(s2[0])],d);
		dist[getnum(s2[0])][getnum(s1[0])]=min(dist[getnum(s2[0])][getnum(s1[0])],d);
		//cout<<getnum(s1[0])<<" "<<getnum(s2[0])<<" "<<d<<" "<<dist[getnum(s1[0])][getnum(s2[0])]<<endl;
	}
	for(int k=0;k<60;k++)for(int i=0;i<60;i++)for(int j=0;j<60;j++)if(dist[i][k]+dist[k][j]<dist[i][j])dist[i][j]=dist[i][k]+dist[k][j];
	char ansc;int ans=inf;
	for(int i=0;i<25;i++)if(dist[i][25]<=ans){
		ans=dist[i][25];ansc=i+'A';
	}
	cout<<ansc<<" "<<ans<<endl;
	return 0;
}

```