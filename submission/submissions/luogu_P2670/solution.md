# P2670 题解

蒟蒻第一篇题解跪求过~~~~~~

这个题目有一些注意的地方：

1.方向是八联通，可以用这种双重循环实现

for(int dy=-1;dy<=1;dy++){

        for(int dx=-1;dx<=1;dx++){

                int nx=dx+x,ny=dy+y;

2.必须注意不越界，这在双重循环中进行判断

3.只搜索是空的地方


这道题用循环遍历所有的点，并在这些所有的点上进行深搜，搜索附近八个方向上有没有雷，如果有自身+1；


#######-----分割线-----#######

下面附上代码：

```cpp
#include<iostream>
using namespace std;
int n,m;
char juzhen[101][101];//需要用字符类型 
void dfs(int y,int x){//需要返回空类型，定义void函数 
    if(juzhen[y][x]=='0'){
        for(int dy=-1;dy<=1;dy++){
            for(int dx=-1;dx<=1;dx++){
                int nx=dx+x,ny=dy+y;
                if(0<=ny&&ny<n&&0<=nx&&nx<m&&juzhen[ny][nx]=='*')//八连通循环 ，且必须不越界
                juzhen[y][x]+=1;//如果是雷的话将那一个点加1 
            }
        }
    }
    return;//将那个点加完之后就返回继续找下一个点 
} 
int main(){
    cin>>n>>m;//不必多说 
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++){
            cin>>juzhen[i][j];//循环输入 
            if(juzhen[i][j]=='?')
            juzhen[i][j]='0';//将？转成0，方便之后+1 
        }
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            dfs(i,j);//遍历每一个点进行深搜 
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++)
            cout<<juzhen[i][j];//按序输出每一个点 
            cout<<endl;
    }
    return 0;//OK 
}
```