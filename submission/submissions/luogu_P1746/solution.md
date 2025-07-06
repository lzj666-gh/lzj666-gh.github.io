# P1746 题解

### 这道题是一道水题，可以直接用BFS的方法做
### BFS的时间复杂度是n*n，可以直接过掉
## 可能有些人还不知道怎么用BFS
###  _那就来看下面的解释_ 
#### 首先，先要用到一个叫队列的东西
#### 它可以从尾巴进去，头上出来
#### 把一个数丢到队列的末尾，可以用到函数push（）
#### 把队列里的东西拿出来的，可以用到函数front（）
#### 把队列里的东西扔了，可以用到函数pop（）
#### 测量队列长度，可以用到函数size（）


------------

### 讲完队列后，你可能会想，队列和BFS有什么关系
#### 那么，就再讲一讲队列的作用


------------

#### 关于BFS，我们可以用结构体来表示一个横坐标，一个纵坐标
#### 我们先把起点的横、竖坐标放进队列q里
#### 当然，我们还要把步数存进vis二维数组里
### 然后如果队列q里还有数，就执行以下操作
#### 1.把队列里的第一个数取出来
#### 2.判断移动上下左右四个方向可不可以走
#### 3.如果可以走，就把它的横坐标合纵坐标存进队列q里
#### 4.把步数定为前一步加一
## 最后，把参数设为起点就行了
```
#include<bits/stdc++.h>
using namespace std;
int n;
int vis[1005][1005];
int h[4]={0,0,1,-1},s[4]={1,-1,0,0};
//h、s数组代表可以走的上下左右四个方向
char a[1005][1005];
//a数组表示地图
struct node{
	int x,y;
};
//结构体
queue<node>q;
//如上，队列q
bool check(int x,int y){	
	if(a[x][y]=='1')
	    return false;
    	//如果是障碍物，就返回false
	if(vis[x][y]>0)
	    return false;
   	//如果以前走过了，就返回false
	if(x>n||x<1)
	    return false;
	if(y>n||y<1)
	    return false;
        //如果超出地图边界，就返回false
	return true;
    	//如果它通过了重重考验，就给它过吧
}
void bfs(int x,int y){
	vis[x][y]=1;
    	//标记起点
	q.push((node){x,y});
    	//把起点和终点放进队列q里 
	while(q.size()!=0){
    	    //如果队列里还有数，就继续
	    int xx=q.front().x;
	    int yy=q.front().y;
            //把队列里的数取出来
	    q.pop();
            //用过了就把它扔了
	    for(int i=0;i<4;i++){
            //代表四个方向
		int xxx=xx+h[i];
		int yyy=yy+s[i];
                //向某一个方向前进
		if(check(xxx,yyy)){
		    vis[xxx][yyy]=vis[xx][yy]+1;
            	    //记录步数
		    q.push((node){xxx,yyy});
            	    //把通过的答案扔进队列里
	        }
	    }
        }
}
int main(){
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
	    for(int j=1;j<=n;j++){
		cin>>a[i][j];
	    }
	}
    	//地图
	int x1,x2,y1,y2;
    	//x1表示起点的横坐标，x2表示起点的纵坐标
	scanf("%d%d%d%d",&x1,&x2,&y1,&y2);
	bfs(x1,x2);
	printf("%d",vis[y1][y2]-1);
	//输出答案减一，它把起点也算了一步
	return 0;
} 
```
#### 在这里插一句，为什么vis数组要等于一呢？
#### 等于0不就不用减一了吗
## 不不不，如果它初始值是0,
## 也会在check里面被算为false


------------
### ~~求过求赞~~
