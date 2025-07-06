# P1331 题解

```
/*这道题的难点在于判断是否有船相邻。
 通过自己模拟的数据可以得出结论： 
 如果图是不和法的，一定存在如下结构：
# # 
. #
或
# #
# .
或
# .
# #
或
. #
# #
即在一个2*2的方格中有三个#。所以就能得出代码：*/
#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int r,c;
char map[1010][1010];
int fx[4]={0,-1,1,0};
int fy[4]={-1,0,0,1};
int dfs(int x,int y){
	map[x][y]='*';
	for(int i=0;i<4;i++){
		if(x+fx[i]>0&&x+fx[i]<=r&&y+fy[i]>0&&y+fy[i]<=c&&
		map[x+fx[i]][y+fy[i]]=='#')dfs(x+fx[i],y+fy[i]);
	}
}//把与#连通的所有点改成*因为它们是同一艘船 
bool d(int i,int j){
	int c=0;
	if(map[i][j]=='#')c++;
	if(map[i+1][j]=='#')c++;
	if(map[i][j+1]=='#')c++;
	if(map[i+1][j+1]=='#')c++;
	if(c==3)return 0;
	return 1;
}//判断是否合法 
int main(){
	scanf("%d%d",&r,&c);
	register int i,j;
	for(i=1;i<=r;i++){
		for(j=1;j<=c;j++){
		cin>>map[i][j];
		}
	}
	int s=0;
	for(i=1;i<=r;i++){
		for(j=1;j<=c;j++){
			if(i<r&&j<c&&d(i,j)==0){
				printf("Bad placement.");
				return 0;//不合法后面就没必要继续了 
			}
		}
	}
	for(i=1;i<=r;i++){
		for(j=1;j<=c;j++){
			if(map[i][j]=='#'){
			s++;
			dfs(i,j);	
			}//因为前面已经确保了是合法的，现在只需统计船的数量 
		}
	}
	printf("There are %d ships.",s);
	return 0;
}
```