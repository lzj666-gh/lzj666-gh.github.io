# P5121 题解

# P5121 [USACO18DEC]Mooyo Mooyo
## [题目传送门](https://www.luogu.com.cn/problem/P5121)
这题其实就是支持二个操作：

1.找联通块，然后删掉。

2.把有颜色的方格下落。

**显然，dfs可以完成第一个操作，而第二个操作可以直接暴力。**

**注意每次dfs前都要把数组清空。**

还有一些细节，代码中会提到。

### 接下来是美妙的代码时间：
```cpp
#include<bits/stdc++.h>
using namespace std;
bool biaoji[101][11],f;
int sum,n,k;
char ch[101][11];
int q[4]= {0,1,0,-1};
int w[4]= {1,0,-1,0};
void dfs(int x,int y,int s) {
	biaoji[x][y]=1;//当前点是联通块中的。
	for(int i=0; i<=3; i++) {
		int xx=x+q[i];
		int yy=y+w[i];
		if(biaoji[xx][yy]==0&&ch[xx][yy]==s) {
			sum++;//联通块数目加1。
			dfs(xx,yy,s);
		}
	}
}
void xialuo() {
	for(int i=n; i>=1; i--) {//注意要倒着，下面的掉下去了上面的才能掉。
		for(int j=1; j<=10; j++) {
			if(ch[i][j]!='0') {
				int k=i;
				while(ch[k+1][j]=='0'&&k<=n) {//k是掉到的位置。
					k++;
				}
				if(k!=i) {
					ch[k][j]=ch[i][j];
					ch[i][j]='0';
				}
			}
		}
	}
}
int main() {
	cin>>n>>k;
	for(int i=1; i<=n; i++) {//不用解释的字符输入。
		for(int j=1; j<=10; j++) {
			cin>>ch[i][j];
		}
	}
	f=1;//f表示当前是否有联通块，如果没有联通块就退出。
	while(f) {
		f=0;
		for(int i=1; i<=n; i++) {
			for(int j=1; j<=10; j++) {
				if(ch[i][j]!='0') {
					sum=1;
					memset(biaoji,false,sizeof(biaoji));//数组清空。
					dfs(i,j,ch[i][j]);
					if(sum>=k) {
						for(int xxx=1; xxx<=n; xxx++) {
							for(int xxxx=1; xxxx<=10; xxxx++) {
								if(biaoji[xxx][xxxx]) {//把联通块里的元素赋为0。
									ch[xxx][xxxx]='0';
								}
							}
						}
						f=1;
					}
				}
			}
		}
		if(f==1) {
			xialuo();
		}
	}
	for(int i=1; i<=n; i++) {
		for(int j=1; j<=10; j++) {
			cout<<ch[i][j];
		}
		cout<<endl;
	}
	return 0;
}

```
