# SP703 题解

### 这么好的一道DP题竟然在洛谷本地没有！！！（或许是我没找到）
### 分析题目，显然用到DP，状态为已经完成的方案数与三个员工的位置
### But……
### 时间复杂度为NL^3完全搞不过去啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
### 所以我们需要压缩状态
### 分析题目可知，在第N个方案完成时，必定有一个人在第N个方案要求的地方，而只要知道其他两个员工的位置与当前方案就可以推出第三个员工的位置了！
### 所以将状态压缩一维，设状态为已经完成的方案数与不在当前方案要求位置的其他两个员工的位置，状态转移方程应该一抹就出来了，我就不赘述，没思路的可以看代码啊XD
```
#include<bits/stdc++.h>
using namespace std;
inline int read(){
//快读
	int a = 0;
	char c = getchar();
	while(!isdigit(c))	c = getchar();
	while(isdigit(c))	a = (a << 3) + (a << 1) + (c ^ '0') , c = getchar();
	return a;
}
inline int min(int a , int b){
	return a < b ? a : b;
}
int pri[201][201] , minN[2][201][201] , To[1001];
//minN滚动数组避免爆空间！
int main(){
	for(int T = read() ; T ; T--){
		memset(minN[0] , 0x3f , sizeof(minN[0]));
		int L = read() , N = read() , now = 0;
		for(int i = 1 ; i <= L ; i++)
			for(int j = 1 ; j <= L ; j++)
				pri[i][j] = read();
		for(int i = 1 ; i <= N ; i++)	To[i] = read();
		To[0] = 3;
		minN[0][1][2] = 0;
		now = 0;
		for(int i = 1 ; i <= N ; i++){
			now ^= 1;
            //数组滚动
			memset(minN[now] , 0x3f , sizeof(minN[now]));
			for(int x = 1 ; x <= L ; x++)
				if(x - To[i - 1])
					for(int y = 1 ; y <= L ; y++)
						if(x - y && y - To[i - 1]){
                        //想一想为什么上面那一句的判断条件里面没有x!=To[i]与y!=To[i]
							if(x - To[i] && y - To[i])	minN[now][x][y] = min(minN[now][x][y] , minN[now ^ 1][x][y] + pri[To[i - 1]][To[i]]);
							if(y - To[i])	minN[now][To[i - 1]][y] = min(minN[now][To[i - 1]][y] , minN[now ^ 1][x][y] + pri[x][To[i]]);
							if(x - To[i])	minN[now][x][To[i - 1]] = min(minN[now][x][To[i - 1]] , minN[now ^ 1][x][y] + pri[y][To[i]]);
                            //三个状态转移方程，对应三个员工去到新的要求的地点
						}
		}
		int allMin = 0x3f3f3f3f;
		for(int x = 1 ; x <= L ; x++)
			for(int y = 1 ; y <= L ; y++)
				if(x - y && x - To[N] && y - To[N])
					allMin = min(allMin , minN[now][x][y]);
		cout << allMin << endl;
	}
	return 0;
}
```