# P1605 题解

#C++题解

##基本思路：搜索 标记 打表 AC

###代码呈上：

```cpp
#include<iostream>//个人建议不使用万能头文件，如果要使用万能头文件，就不能定义数组map；
#include<cstdlib>
#include<cstdio>
#include<cmath>
using namespace std;
int map[6][6];//地图；
bool temp[6][6];//走过的标记；
int dx[4]={0,0,1,-1};//打表；
int dy[4]={-1,1,0,0};//打表；
int total,fx,fy,sx,sy,T,n,m,l,r;//total计数器，fx，fy是终点坐标，sx，sy是起点坐标，T是障碍总数，n，m是地图的长和宽，l，r是障碍的横坐标和纵坐标；
void walk(int x,int y)//定义walk；
{
    if(x==fx&&y==fy)//fx表示结束x坐标，fy表示结束y坐标；
    {
        total++;//总数增加；
        return;//返回，继续搜索；
    }
    else
    {
        for(int i=0;i<=3;i++)//0——3是左，右，下，上四个方向；
        {
            if(temp[x+dx[i]][y+dy[i]]==0&&map[x+dx[i]][y+dy[i]]==1)//判断没有走过和没有障碍；
            {
                temp[x][y]=1;//走过的地方打上标记；
                walk(x+dx[i],y+dy[i]);
                temp[x][y]=0;//还原状态；
            }    
        } 
    }
}
int main()
{
    cin>>n>>m>>T;//n，m长度宽度，T障碍个数 
    for(int ix=1;ix<=n;ix++)
        for(int iy=1;iy<=m;iy++)
            map[ix][iy]=1;//把地图刷成1；
    cin>>sx>>sy;//起始x，y 
    cin>>fx>>fy;//结束x，y 
    for(int u=1;u<=T;u++)
    {
        cin>>l>>r;//l，r是障碍坐标；
        map[l][r]=0;
    }
    walk(sx,sy);
    cout<<total;//输出总数；
    return 0;
} 
```
题整体来说比较简单，使用深搜一个个查，使用一个数组map记录障碍的地方，再使用一个temp来标记自己所走过的路；


int dx[4]={0,0,1,-1};

int dy[4]={-1,1,0,0};

使用自动选择方向来代替4个if判断（~~使代码更加简洁~~长度变短）；


如果没有障碍并且不是自己走过的，就进一步搜索，把自己走过的路打上标记，返回时，再将标记还原；


###注意：有些同学可能觉得就在地图map数组上打标记（自己走过的路）比较简单，走过的路和障碍可能引起混淆，如果只用map数组的话，可能只的得到80分；~~（贴主的惨痛经历）~~


###这里再给大家一个基本的深搜模板：

```cpp
int search(int t)
{
    if(满足输出条件)
    {
        输出解;
    }
    else
    {
        for(int i=1;i<=尝试方法数;i++)
            if(满足进一步搜索条件)
            {
                为进一步搜索所需要的状态打上标记;
                search(t+1);
                恢复到打标记前的状态;//也就是说的{回溯一步}
            }
    }
}
```
###整个模板有几个地方需要注意：

1.第一个if是符合输出解的条件，第二个if是符合进一步搜索的条件；

2.下一步搜索时，不是使用return search(t+1)，直接search(t+1);（~~新手可能会注意不到这个关键的地方，以至于每次写完不知道为什么只得到一个答案就返回主程序了~~）

3.for循环之后的if可以是多个;

4.for循环边界，例如：

1>方向是四个，那么边界肯定就是4；（帖主用3，是因为从0开始的）

2>素数环需要尝试1至20，那么边界就是20；



如果想要得到更多知识，请关注我博客：https://www.luogu.org/blog/AHacker/


此博客不定期更新内容！！！感谢大家！！！
