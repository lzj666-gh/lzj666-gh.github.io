# P3916 题解

### 反向建边 + dfs

按题目来每次考虑每个点可以到达点编号最大的点，不如考虑较大的点可以反向到达哪些点

循环从N到1，则每个点i能访问到的结点的A值都是i

每个点访问一次，这个A值就是最优的，因为之后如果再访问到这个结点那么答案肯定没当前大了

---

思路已经很明晰了，代码实现不难

```cpp
#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

#define MAXL 100010

int N, M, A[MAXL];
vector<int> G[MAXL]; //vector存图 

void dfs(int x, int d) {
	if(A[x]) return; //访问过 
	A[x] = d;
	for(int i=0; i<G[x].size(); i++)
		dfs(G[x][i], d);
}

int main() {
	int u, v;
	scanf("%d%d", &N, &M);
	for(int i=1; i<=M; i++) {
		scanf("%d%d", &u, &v);
		G[v].push_back(u); //反向建边 
	}
	for(int i=N; i; i--) dfs(i, i); 
	for(int i=1; i<=N; i++) printf("%d ", A[i]);
	printf("\n");
	return 0;
}
```