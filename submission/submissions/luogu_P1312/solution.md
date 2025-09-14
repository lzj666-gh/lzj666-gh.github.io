# P1312 题解

## 萌新~~年~~日常打卡
### 思路~~很简单~~，就模拟
##### ~~题目要你干什么那就干什么(废话)~~
###### 大部分的题解已经讲了怎么模拟了
###### 不过我还是我还是讲一遍吧
- 模拟思路   
- 枚举所有可能的移动，用搜索的方法即可，建议使用dfs   
- 重要的部分在时间优化上(虽然我不知道不优化能不能过)

关于剪枝   
首先搜索移动的时候，并不用全部往下搜，   
如果左边有块,不向左移动(这个各位大佬都讲了)   
因为左边的块会向右移动且字典序更小   
我想说的是，另一个剪枝!   
现在如果我说不可以剪交换相同各位可以理解吧   
但是交换相同颜色其实是可以优化的   
可以发现无论交换哪个地方的相同颜色结果相同   
所以只要保留字典序最小的交换相同颜色即可   
就是每层dfs搜到第一次相同的就允许,再搜到就剪掉   
这样既可以优化又不会被故意浪费步数的数据卡   
#### 上代码
```cpp
#include<bits/stdc++.h>
using namespace std;
int read()//快速读入
{
    int sum=0,flag=1;
    char ch=getchar();
    while(ch>'9'||ch<'0'){if(ch=='-')ch=getchar();ch=getchar();}
    while(ch<='9'&&ch>='0'){sum=sum*10+ch-'0';ch=getchar();}
    return sum*flag;
}
struct node{int x,y,z;}c[7];//储存答案
int  n,a[7][9],    b[7][7][9];
//   读入数据   存放dfs前的备份数据
queue<node>q;
//消除块的队列(也可以用bool数组,但我觉得这样消除时快将近一半的时间)
void fz(int k)//从a备份内容到b
{
    for(int i=1;i<=5;i++)
    for(int j=1;j<=7;j++)
    b[k][i][j]=a[i][j];
}
void zf(int k)//从b还原内容到a
{
    for(int i=1;i<=5;i++)
    for(int j=1;j<=7;j++)
    a[i][j]=b[k][i][j];
}
bool jc()//检测是不是没有块了
{
    for(int i=1;i<=5;i++)//只要检测最下排即可
    if(a[i][1])return 0;
    return 1;
}
bool xc()//消除判定
{
    for(int i=1;i<=5;i++)for(int j=1;j<=7;j++)
    {//判定可消除,一定不要直接赋值0
        if(a[i][j]&&a[i-1][j]==a[i][j]&&a[i+1][j]==a[i][j])q.push({i,j,0});
        if(a[i][j]&&a[i][j-1]==a[i][j]&&a[i][j+1]==a[i][j])q.push({i,j,1});
    }
    if(q.empty())return 0;//没有动
    while(!q.empty())//处理删除的块
    {
        node k=q.front();q.pop();
        if(k.z)a[k.x][k.y]=a[k.x][k.y-1]=a[k.x][k.y+1]=0;
        else a[k.x][k.y]=a[k.x-1][k.y]=a[k.x+1][k.y]=0;
    }
    return 1;//动了
}
void dl()//掉落判定
{
    for(int i=1;i<=5;i++)
    for(int j=2;j<=7;j++)
    if(a[i][j]&&!a[i][j-1])//如果一个块踩空
    for(int k=j-1;k>=0;k--)//一直往下找到一个非空块
    if(a[i][k])//找到了
    {
        swap(a[i][j],a[i][k+1]);//交换
        break;
    }
}
void yd(int x,int y,int k)//移动函数
{
    swap(a[x][y],a[x+k][y]);
    if(!a[x][y])dl();//这个应该很好理解,只有和空气交换才会掉落
    while(xc())dl();//需要循环判定!!!
}
void dfs(int k)//搜索
{
    if(!k)//移动完检测
    {
        if(jc())//检测
        {//输出
            for(int i=n;i>0;i--)printf("%d %d %d\n",c[i].x-1,c[i].y-1,c[i].z);
            exit(0);//直接退出程序
        }
        return;//否则返回继续搜
    }
    fz(k);//先备份a
    bool flag=0;//标记,用来做相同色优化
    for(int i=1;i<=5;i++)
    for(int j=1;j<=7;j++)
    if(a[i][j])//枚举每个点,如果有色就继续
    {
        if(i>1&&!a[i-1][j])//如果不在最左边且左边是空的就左移
        {
            yd(i,j,-1);//移动
            c[k]={i,j,-1};//记录答案
            dfs(k-1);//继续搜
            zf(k);//恢复a
        }
        if(i<5)//如果不在最右边都右移
        {
            if(a[i][j]==a[i+1][j]&&flag)continue;//已经有一个了,其余剪掉
            if(a[i][j]==a[i+1][j])flag=1;//第一个放走,然后标记
            yd(i,j,1);//移动
            c[k]={i,j,1};//记录答案
            dfs(k-1);//继续搜
            zf(k);//恢复a
        }
    }
}
int main()//主函数
{
    n=read();//读n
    for(int i=1;i<=5;i++)a[i][0]=2147483647;//这个在掉落判定中有用(10以上的数都可以)
    for(int i=1;i<=5;i++)
    for(int j=1;j<=8;j++)
    {//读入
        a[i][j]=read();
        if(!a[i][j])break;
    }
    dfs(n);//搜索,n是层数(可能大部分人会写1)
    cout<<-1;//无解输出-1,因为如果有解在dfs里就退出了
    return 0;
}
```
### 欢迎 ~~挑刺与找茬~~ 指出错误