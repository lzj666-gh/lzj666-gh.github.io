# P1074 题解

本人蒟蒻，发个蒟蒻看得懂的题解~~


dfs代码最终效率不高——**2000ms——3000多ms**，（~~但是AC了，或许是数据水吧~~）


大家玩过数独（没玩过的先了解规则去吧）


我的思路是dfs（不打表），用一个序列s[ ]保存要填的点，dfs携带的参数就是要填写的点的坐标：

s[ i ][0]与s[ i ][1]存点的坐标，s[ i ][2]存点的分值，s[ i ][3]存点的所在宫（我用函数现生成，避免了打表）。


需要注意的有如下几点：


一、dfs过程中就判断数能不能放，别放到最后判断（这一条可能是废话）实现方法用三个数组分别存各行、列、宫每个数字的状态（0表示没填过，1表示填过）


（重要）二、dfs层数与0的个数有关，层数太多就TLE了，我们知道，一行中填过的数字越多，需要填的数越少，就意味着dfs层数越少！所以，我们先填0的数量少的行。（详细实现见代码）


不懂的看这：）











```cpp
0 0 0 0 0 0 0 0 0    //这一行有9个0
1 0 0 0 0 5 9 0 0  //这一行有6个0
0 0 0 2 0 0 0 8 0 //这一行有7个0
0 0 5 0 2 0 0 0 3 //这一行有6个0
0 0 0 0 0 0 6 4 8 //这一行有6个0
4 1 3 0 0 0 0 0 0 //这一行有6个0
0 0 7 0 0 2 0 9 0 //这一行有6个0
2 0 1 0 6 0 8 0 4 //这一行有4个0
0 8 0 5 0 4 0 1 2//这一行有4个0
```
在这个例子中，从第一行到第九行dfs的话，那么dfs第一层就有9种情况！！！根据dfs的原理，从第一层9种情况开始拓展，那么时间就要花很多。而若从第8层开始只有4种情况，搜索需要的时间就大大减少。~~TLE再见！！~~

**Code：**

```cpp
#include<iostream>
#include<algorithm>
using namespace std;
struct f
{
    int rank,sum;//定义结构体，将行号与0的个数对应 
}cou[10];
int a[10][10],hang[10][10],lie[10][10],gong[10][10],s[100][4],u,ok,most=-1,have;
int which(int,int);//给出两个整型变量代表坐标，返回此坐标的所在宫                                     
int point(int,int);//给出两个整型变量代表坐标，返回此坐标的分值                                                                  
void dfs(int,int); 
bool cmp(f a,f b)
{
    return a.sum<b.sum; 
}
int main()
{
    for(int i=1;i<=9;i++)  cou[i].rank=i;//rank存其初始行号，排序后就不会丢失 
    for(int i=1;i<=9;i++)
    for(int j=1;j<=9;j++)
    {
        cin>>a[i][j];
        if(a[i][j]>0)
        hang[i][a[i][j]]=lie[j][a[i][j]]=gong[which(i,j)][a[i][j]]=1,have+=a[i][j]*point(i,j);//非零就不存储到搜索数组s中，但将这个点的值在其所在行、列、宫中标记 ，计算加分 
        else  cou[i].sum++;//是0就计数 
    }
    sort(cou+1,cou+10,cmp);//排序，0少的在前 
    for(int i=1;i<=9;i++)//整理s数组，准备搜索 
    {
        for(int j=1;j<=9;j++)//先搜0少的行 
        if(a[cou[i].rank][j]==0)
        s[u][0]=cou[i].rank,s[u][1]=j,s[u][2]=point(cou[i].rank,j),s[u++][3]=which(cou[i].rank,j);//保存不解释 
    }
    dfs(0,have);//搜索 
    cout<<most<<endl;//most保存答案，初始值为-1 
    return 0;
} 

void dfs(int p,int score)// 表示正在搜s[p],score为目前分数 
{
    if(p==u)//合法填完了所有的数 
    {
        if(score>most)  most=score;//更大就更新 
        return;
    }
    for(int i=1;i<=9;i++) 
    {
        if(!hang[s[p][0]][i]&&!lie[s[p][1]][i]&&!gong[s[p][3]][i])//判断可不可以将i填入 
        {
            hang[s[p][0]][i]=lie[s[p][1]][i]=gong[s[p][3]][i]=1;//填了后就将这个点的值在其所在行、列、宫中标记
            dfs(p+1,score+(s[p][2]*i));//下一层递归 
            hang[s[p][0]][i]=lie[s[p][1]][i]=gong[s[p][3]][i]=0;//回溯 
        }
    }
    return;
}

int which(int i,int j)
{
    if(i<=3)
    {
        if(j<=3)        return 1;
        else if(j<=6)   return 2;
        else            return 3;
    }
    else if(i<=6)
    {
        if(j<=3)        return 4;
        else if(j<=6)    return 5;
        else            return 6;
    }
    else
    {
        if(j<=3)        return 7;
        else if(j<=6)   return 8;
        else            return 9;
    }
}

int point(int i,int j)
{
    if(i==1||j==1||i==9||j==9)   return 6;
    if(i==2||j==2||i==8||j==8)     return 7;
    if(i==3||j==3||i==7||j==7)   return 8;
    if(i==4||j==4||i==6||j==6)   return 9;
    return 10;
}
```
我认为已经很详细了，还不懂私我。
