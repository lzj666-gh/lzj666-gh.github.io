# P1506 题解

## 最详细的dfs解释(附图附解析)
#### 遇到好多次这样的dfs思路了，所以就详解一下
### 思路
```
5 7
0 0 * * * 0 0
0 0 * 0 * 0 0
* * * 0 * * 0
* 0 * * * 0 0
* * * 0 * * 0
```
以这个样例详解一下做法
1. 首先输入
2. 然后搜索最外层，如果有空洪水就可以沿着空一直往里走，所以要dfs搜索一下(画叉号的是搜索有空的)
![](https://cdn.luogu.com.cn/upload/pic/53432.png)
3. 将所有外面能进来的格子填上数(深色的是后来填上的)
![](https://cdn.luogu.com.cn/upload/pic/53433.png)
4. 搜索所有白色格子就是最终答案
答案是 3
### AC代码
[AC详情](https://www.luogu.org/recordnew/show/17013744)
```cpp
#include<bits/stdc++.h>
using namespace std;
int n,m,s=0;
int kx[5]={0,1,-1,0,0}; 
int ky[5]={0,0,0,1,-1};
int a[501][501];
void search(int x,int y){
    a[x][y]=1;//先标记被淹没了 
    for(int i=1;i<=4;i++){//向四个方向搜索 
        int x0=x+kx[i];
        int y0=y+ky[i];
        if(x0>0&&x0<=n&&y0>0&&y0<=m&&a[x0][y0]==0)search(x0,y0);
    }//如果新的数在整个数组范围内并且不是障碍(能走),那么就搜索从这个格子能走到其他哪些格子 
}
int main(){
    cin>>n>>m;
    char e;
    for(int i=1;i<=n;i++){//输入 
        for(int j=1;j<=m;j++){
            cin>>e;
            if(e=='*')a[i][j]=1;//如果是障碍就输入1 
            else a[i][j]=0;//可以过就是0 
        }
    }
    for(int i=1;i<=n;i++){//搜索第一列和最后一列的格子 
        if(a[i][1]==0)search(i,1);//如果有能过的就搜索 
        if(a[i][m]==0)search(i,m);
    }
    for(int i=1;i<=m;i++){//搜索第一行和最后一行的格子 
        if(a[1][i]==0)search(1,i);
        if(a[n][i]==0)search(n,i);
    }
    for(int i=1;i<=n;i++){//最后搜索没有被淹的格子 
        for(int j=1;j<=m;j++){
            if(a[i][j]==0)s++;
        }
    }
    cout<<s;//输出 
    return 0;
}
```
感谢大家能看我的题解!~