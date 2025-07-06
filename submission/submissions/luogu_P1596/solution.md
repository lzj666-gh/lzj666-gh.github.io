# P1596 题解

# 这篇题解是这道题的DFS和BFS解法的介绍

### 这道题主要有两种解法，深搜和广搜。很多人只会拿DFS写，那我来写写这两种解题方法，再分析一下深搜和广搜的优缺点

## 首先，看看DFS
#### 其实DFS就是一口气往一个方向搜索，然后遇到障碍之后再改一个方向搜索
#### 优点：好写，不易出错，浅显易懂
#### 缺点：往一个方向查找耗时，当寻找最优解时没有剪枝会卡时间

核心代码：
```cpp
void dfs(int x,int y){
    a[x][y]='.';//标记为已走
    int dx,dy;
    for(int i=-1;i<=1;i++){//搜索周围的地方
        for(int j=-1;j<=1;j++){
            dx=x+i;
            dy=y+j;
            if(dx>=0&&dx<=n&&dy>=0&&dy<m&&a[dx][dy]=='W'){//如果没有超过边界且为'W'的话就往那个点继续深入搜索
                dfs(dx,dy);
            }
        }
    }
    return;//在void中return为返回上一值，表示如果不能继续深搜就返回上面的点继续搜索
} 
```

所以，有了这组代码整个代码就写出来了

```cpp
#include<cstdio>
using namespace std;
char a[101][101];
int ans;
int n,m;
void dfs(int x,int y){
    a[x][y]='.';
    int dx,dy;
    for(int i=-1;i<=1;i++){
        for(int j=-1;j<=1;j++){
            dx=x+i;
            dy=y+j;
            if(dx>=0&&dx<=n&&dy>=0&&dy<m&&a[dx][dy]=='W'){
                dfs(dx,dy);
            }
        }
    }
    return;
} 
int main(){
    scanf("%d%d",&n,&m);
    for(int i=0;i<=n;i++){
    	scanf("%s",a[i]);//避免换行带来问题这里直接读入字符串
    }
    for(int i=0;i<=n;i++){
        for(int j=0;j<m;j++){
            if(a[i][j]=='W'){//如果是W的话就直接开始遍历
                dfs(i,j);
                ans++;//水潭加一处
            }
        }
    }
    printf("%d",ans);
    return 0;
}
```

##### 显然 ，dfs的好处就是好打、方便

## 那么，再过来看看BFS
#### BFS就是维护一个队列，以一个点往四周搜索，如果符合条件的话就把它放进队列里
#### 优点：同级优先搜索，在求最优解的时候可以避免许多无用的搜索，提高效率、可以避免递归
#### 缺点：不好写，易出问题，用stl写队列很慢

### 当我们用stl写队列时的BFS核心代码
```cpp
void bfs(int x,int y){
    s[x][y]='.';
    int dx,dy;
    for(int i=-1;i<=1;i++){
        for(int j=-1;j<=1;j++){
            dx=x+i;
            dy=y+j;
            if(dx>=0&&dx<n&&dy>=0&&dy<m&&s[dx][dy]=='W'){
                hori.push(dx);//把行放入队列
                para.push(dy);//把列放入队列
            }//注意，其实可以用一个队列维护，但是用两个队列更好写，更直观
        }
    }
}
```

那么，整体代码就稍微有点差别

```cpp
#include<cstdio>
#include<queue>
using namespace std;
queue<int>hori;//行的队列
queue<int>para;//列的队列
int n,m;
int ans;
char s[101][101];
inline int read(){//读入优化，可以加快数字的输入
    char p=0;int r=0,o=0;
    for(;p<'0'||p>'9';o|=p=='-',p=getchar());
    for(;p>='0'&&p<='9';r=(r<<1)+(r<<3)+(p^48),p=getchar());
    return o?(~r)+1:r;
}
inline void bfs(int x,int y){//不用递归时可以加inline，提高1ms的运行速度
    s[x][y]='.';
    int dx,dy;
    for(int i=-1;i<=1;i++){
        for(int j=-1;j<=1;j++){
            dx=x+i;
            dy=y+j;
            if(dx>=0&&dx<n&&dy>=0&&dy<m&&s[dx][dy]=='W'){
                hori.push(dx);
                para.push(dy);
            }
        }
    }
}
int main(){
    n=read();m=read();//看不懂的话可以把这一行改成cin或scanf
    for(int i=0;i<n;i++){
        scanf("%s",s[i]);
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(s[i][j]=='W'){
                hori.push(i);
                para.push(j);
                while(!hori.empty()){//如果队列不为空
                    bfs(hori.front(),para.front());//广搜队列前面的元素
                    hori.pop();para.pop();//弹出元素
                }
                ans++;
            }
        }
    }
    printf("%d",ans);
    return 0;
}
```
#### 值得一提的是，加上快读等优化以后已经做到stl队列能运行时间的极致了，然而提交就算开O2优化还是会有两个测试点被T
#### 这就需要我们手写队列了以及各种优化了，但是这个代码适合bfs的初学者理解