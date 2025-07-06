# P10488 题解

# 题解：P10488 Booksort

[题目传送门](https://www.luogu.com.cn/problem/P10488)

## Part 1 思路讲解

1. 考虑每个状态的转移（分支）数量，在每个状态下，可以抽取连续的一段数，移动到另一个位置。

- 对于任意的长度 $len$，当抽取长度为 $len$ 时，有 $n - len + 1$ 种选择，有 $n - len$ 个可插入的位置。

- 另外，把一段数移动到更靠前的位置，等价于把“跳过”的那段书移动到靠后的某个位置，所以上面的计算方法把每种移动情况算了两遍，每个状态的分支数量约为：

- $\sum_{k = 1}^{n-1} \ (n-k) \times (n-k+1) \div 2 \le \sum_{k = 1}^{14} \ (n-k) \times (n-k+1) \div 2 = 560$

2. 根据题目要求，只需要考虑在 $4$ 次操作内是否能实现目标，也就是我们只需要考虑搜索树的前 $4$ 层。

- 四层的搜索树的规模能够达到 $560^4$，超时！

3. 算法 1：采用双向 BFS，从初始状态，目标状态开始各搜 $2$ 步，看能否在相同的状态相遇，复杂度降为 $560^2$（请自行尝试）。

4. 算法 2：IDA Star

- 在目标状态下，第 $i$ 本书的后面应该是 $i+1$ 本书，称 $i+1$ 时 $i$ 的正确后继。

- 对于任意状态下，考虑整个排列中书的错误后继的总个数（记为 $cnt$），可以发现，每次操作最多更改 $3$ 本书的后继。即使在最理想的情况下，每次操作都能把某 $3$ 个错误后继全部改对，清除所有错误后继的操作次数也至少需要 $\lceil \frac{cnt}{3} \rceil$ 次。

- 因此，可以将状态 $stat$ 的估价函数设计为 $f(stat) = \lceil \frac{cnt}{3} \rceil$，其中 $cnt$ 表示状态 $stat$ 中有多少本书的后继是错误的。

- 采用迭代加深的方法，从 $1 \to 4$ 一次限制搜索深度，然后从起始状态出发 DFS。DFS 时，在每个状态下直接枚举抽取那一段，移动到更靠后的某个位置，沿着该分支深入即可。注意在进入任何状态 $stat$ 后，先进行判断，如果当前操作次数 + $f(s)$ 已经大于深度限制，直接从当前分支回溯。

## Part 2 代码

```cpp
#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
#include <algorithm>
#include <cstring>
using namespace std;
int n;
int a[20],tmp[20];
void move(int x,int y,int z){
	memset(tmp,0,sizeof tmp);
	int t=0;
	for(int i=y+1;i<=z;i++) tmp[++t]=a[i];
	for(int i=x;i<=y;i++) tmp[++t]=a[i];
	t=0;
	for(int i=x;i<=z;i++) a[i]=tmp[++t]; 
}
bool dfs(int maxd,int dep){
	if(dep>maxd) return false;
	int q[20];
	memcpy(q,a,sizeof(q));
	for(int i=1;i<=n;i++){
		for(int j=i;j<=n;j++){
			for(int k=j+1;k<=n;k++){
				move(i,j,k);
				int F=0;
				for(int p=1;p<n;p++) if(a[p+1]!=a[p]+1) F++;
				if(a[n]!=n) F++;
				if(F==0) return true;
				if(F==0||3*dep+F<=3*maxd&&dfs(maxd,dep+1)) return true; 
				memcpy(a,q,sizeof(a));
			}
		}
	}
	return false;
}
int main() {
	int t;
	cin>>t;
	while(t--){
        cin>>n;
    	int t[20];
    	for(int i=1;i<=n;i++) cin>>a[i];
        memcpy(t,a,sizeof(t));
    	bool flag=0;
    	for(int i=1;i<n;i++) 
            if(a[i+1]!=a[i]+1) flag=1;
    	if(a[n]!=n) flag=1;
    	if(!flag){
    		cout<<"0\n";
    		continue;
    	}
    	int f=1;
    	for(int i=1;i<=4;i++){
    		if(dfs(i,1)){
    			cout<<i<<"\n";
    			f=0;
    			break;
    		}
    		memcpy(a,t,sizeof(a));
    	}
    	if(f==1)cout<<"5 or more\n";
    }
	return 0;
} 
```