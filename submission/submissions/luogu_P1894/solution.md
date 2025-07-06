# P1894 题解

两个月前过的二分图模板，没想到两个月后又能在这里邂逅几乎一模一样的题（反正我没看出区别），那就发篇题解纪念吧

二分图压压行真的很短（~~至少比SPFA、BSGS短多了~~）
### 就像这样：
```cpp
#include<bits/stdc++.h>
const int N=201;
int n,m,lk[N],g[N][N],v[N],ans;
bool dfs(int now){
	for(int i=1;i<=n;i++)
		if(!v[i]&&g[now][i]&&(v[i]=1))//其实在&&中修改变量还是挺方便的
			if((!lk[i]||dfs(lk[i]))&&(lk[i]=now))return 1;//与或非优先级懒得算了，于是搞了一堆括号
	return false;
}
int main(){
	scanf("%d%d",&n,&m);
	for(int i=1,s,x;i<=n;i++){
		scanf("%d",&s);
		while(s--)scanf("%d",&x),g[i][x]=1;
	}
	for(int i=1;i<=n;i++)
		memset(v,0,sizeof(v)),ans+=dfs(i);
	return 0*printf("%d",ans);
}
```
开学后发的第一篇题解（~~看我多懒~~）