# P9122 题解

一道大**暴力**。

~~话说 USACO 是不是和 CCF 学的赛时放那么恶心的题。~~

回归正题：

由于格子只会由白变黑，不会由黑变白。

所以直接枚举 4 个方向判断有没有不应该黑的格子黑了（注意不是错了因为后面还可以印）。

代码实现：

```cpp
#include<bits/stdc++.h>
using namespace std;
#define neverTLE ios::sync_with_stdio(false);cin.tie(0);cout.tie(0)
#define reg register
#define endl '\n'
int t,n,k;
int main(){
	neverTLE;
	cin>>t;
	while(t--){
		cin>>n;
		char mp[30][30]={0},st[30][30]={0},bd[30][30]={0};
		for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				cin>>mp[i][j];
			}
		}
		cin>>k;
		for(int i=1;i<=k;i++){
			for(int j=1;j<=k;j++){
				cin>>st[i][j];
			}
		}
		
		for(int i=1;i+k-1<=n;i++){
			for(int j=1;j+k-1<=n;j++){
				bool flag=1;
				for(int ii=i,iii=1;ii<=i+k-1;ii++,iii++){
					for(int jj=j,jjj=1;jj<=j+k-1;jj++,jjj++){
						if(mp[ii][jj]!=st[iii][jjj]&&mp[ii][jj]=='.'){
							flag=0;
						}
					}
				}
				if(flag){
				for(int ii=i,iii=1;ii<=i+k-1;ii++,iii++){
					for(int jj=j,jjj=1;jj<=j+k-1;jj++,jjj++){
						if(bd[ii][jj]!='*')	bd[ii][jj]=st[iii][jjj];
					}
				}
				}
				flag=1;
				for(int ii=i,jjj=k;ii<=i+k-1;ii++,jjj--){
					for(int jj=j,iii=1;jj<=j+k-1;jj++,iii++){
						if(mp[ii][jj]!=st[iii][jjj]&&mp[ii][jj]=='.'){
							flag=0;
						}
					}
				}
				if(flag){
				for(int ii=i,jjj=k;ii<=i+k-1;ii++,jjj--){
					for(int jj=j,iii=1;jj<=j+k-1;jj++,iii++){
							if(bd[ii][jj]!='*')bd[ii][jj]=st[iii][jjj];
					}
				}
				}
				flag=1;
				for(int ii=i,iii=k;ii<=i+k-1;ii++,iii--){
					for(int jj=j,jjj=k;jj<=j+k-1;jj++,jjj--){
						if(mp[ii][jj]!=st[iii][jjj]&&mp[ii][jj]=='.'){
							flag=0;
						}
					}
				}
				if(flag){
				for(int ii=i,iii=k;ii<=i+k-1;ii++,iii--){
					for(int jj=j,jjj=k;jj<=j+k-1;jj++,jjj--){
						if(bd[ii][jj]!='*')	bd[ii][jj]=st[iii][jjj];
					}
				}
				}
				flag=1;
				for(int ii=i,jjj=1;ii<=i+k-1;ii++,jjj++){
					for(int jj=j,iii=k;jj<=j+k-1;jj++,iii--){
						if(mp[ii][jj]!=st[iii][jjj]&&mp[ii][jj]=='.'){
							flag=0;
						}
					}
				}
				if(flag){
				for(int ii=i,jjj=1;ii<=i+k-1;ii++,jjj++){
					for(int jj=j,iii=k;jj<=j+k-1;jj++,iii--){
						if(bd[ii][jj]!='*')	bd[ii][jj]=st[iii][jjj];
					}
				}
				}
			}
		}
		int flagg=0;
		for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				if(bd[i][j]!=mp[i][j]&&mp[i][j]=='*'){
					flagg=1;
					goto jump;
				}
			}
		}
		jump:
		/*for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				cout<<bd[i][j]<<' ';
			}
			cout<<endl;
		}
		*/
		if(flagg){
			cout<<"NO"<<endl;
		}
		else{
			cout<<"YES"<<endl;
		}
	}
	return 0;
}
```