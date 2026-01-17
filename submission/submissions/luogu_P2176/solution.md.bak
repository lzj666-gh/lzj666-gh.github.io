# P2176 题解


 - 作为一个提交了无数遍此题的蒟蒻，我决定来为此题献上我的第一篇题解。
 

------------

   暴力做法：
   
    毕竟我们比赛的时候不可能所有题都去想正解，所以当我们遇到一些没有必要打正解的题目时，我们应该尝试去暴力拿分（当暴力也能ac或拿大部分分时）
   
   该怎么打暴力呢？
   
   这是一项“玄学”，首先我们有个思路，这道题是在不停地找最短路，那我们就拿出我们的最短路模板 dijkstra+堆优化 ，要修边的话，因为我们~~并不想~~并不知道要修改哪些边，那我们干脆就把每条边都修改一次，然后走（m+1）次最短路
   
   然而，用dijkstra+堆优化 打暴力的同学可能会发现无论如何暴力拿分都有1个点t掉，这里是一处此题很奇妙的地方。让我们来算一算这个暴力算法的时间复杂度 首先是dijkstra+堆优化的最短路复杂度 （n+m）logn【按最大数据大约是35000次】 然后因为我们走了（m+1次）所以是 （m+1）（n+m）logn 我们会发现，这个算法在题目的范围内破亿了，这也就是dijkstra+堆优化t掉的原因。
  
  但是由于这道题n的范围极其之小，我们会发现最原始的dijkstra的时间复杂度（n^2） 我们扫一遍查找离起点最近的未遍历的点，再扫一遍，用此点来进行松弛操作【更新最短路】 那么大致的时间复杂度就是（2*n^2）我们再进行（m+1）次 【按最大数据来计算则大概刚好到1亿，算是勉强挨边】 次数要小于堆优化过的 （所以这道题用原始版dijkstra是可以过的）
  
  dijkstra暴力代码如下（由于我不会用邻接表做原始dijkstra所以就用邻接矩阵来存图，若有哪位巨佬会，望能多多指教） （1050ms）
  ```cpp
#include <iostream>
#include <queue>
#include <iomanip>
#include <cstdio>
#define ll long long
using namespace std;
int uv[105][105]={0};//用邻接矩阵
int q=0,n,m;
int x[6005],y[6005],o=0;//用于记录“要修改”的每条边

bool flag[110]={0};
int road[110]={0};//这两个是dijkstra用的数组保存状态和最短路
void dijkstra(){

for( int i=1;i<=n;i++){
 flag[i]=0;
 road[i]=uv[1][i];
}
road[1]=0;
flag[1]=1;
    for( int i=1;i<n;i++){
        int minn=0x7fffff;
        int t;
        for( int j=1;j<=n;j++)
            if(flag[j]==0&&road[j]<minn){
                t=j;
                minn=road[j];
            }
    flag[t]=1;
    for( int k=1;k<=n;k++) 
     road[k]=min(road[k],road[t]+uv[t][k]); 
}
}

int main (){
   int l;
 scanf("%d%d",&n,&m);

 for(int i=1;i<=n;i++)
  for( int j=1;j<=n;j++)
    uv[i][j]=0x7fffff; //初始化每条边

    for( int i=1;i<=m;i++){
        int j,k,l;
        scanf("%d%d%d",&j,&k,&l);

          uv[j][k]=l;
          uv[k][j]=l;
        x[++o]=j;
        y[o]=k;
    } //输入，存储图

    dijkstra();
  int ans=road[n];//求出修边前的最短路长度
    l=0;

    for(int i=1;i<=o;i++){
        uv[x[i]][y[i]]*=2;
        uv[y[i]][x[i]]*=2;
    dijkstra();
         l=max(l,road[n]);
        uv[y[i]][x[i]]/=2;
         uv[x[i]][y[i]]/=2;
    } //暴力修边，疯狂求最短路
printf("%d",l-ans);    

}

```

除外，spfa玄学的时间复杂度（kE）用来暴力这道题也能过

spfa暴力代码如下 （1134ms）

```cpp
#include <iostream>
#include <cstdio>
#include <queue>
using namespace std;
int m,n;
queue <int> q;
bool flag[110];
int uv[110][110]={0};
int road[110];
int x[6000],y[6000],o=0;
void spfa(int v){
    for(int i=1;i<=n;i++) {
        flag[i]=0;
        road[i]=0x7fffff;
    }
    road[v]=0;
    flag[v]=1;
    q.push(v);
    while(!q.empty()){
        int t=q.front();
        for(int i=1;i<=n;i++)
        if(uv[t][i]!=0x7fffff) 
        if(road[i]>road[t]+uv[t][i]){
            road[i]=road[t]+uv[t][i];
            if(flag[i]==0){
                q.push(i);
                flag[i]=1;
            }
        }
        
        flag[t]=0;
        q.pop();
    }
}

int main (){
    int i,j,k,l;
    
    scanf("%d%d",&n,&m);
    for(i=1;i<=n;i++)
    for(j=1;j<=n;j++) 
    uv[i][j]=0x7fffff;
    
    for(i=1;i<=m;i++){
        cin>>j>>k>>l;
        uv[j][k]=l;
        uv[k][j]=l;
        x[++o]=j;
        y[o]=k;
    }

    spfa(1);
   
    
    l=0;
    int ans=road[n];
    for(i=1;i<=o;i++){
        uv[x[i]][y[i]]*=2;
        uv[y[i]][x[i]]*=2;
        spfa(1);
        l=max(l,road[n]);
        uv[x[i]][y[i]]/=2;
        uv[y[i]][x[i]]/=2;
    }
    printf("%d",l-ans);
    }


```


------------


 对比来看，spfa的代码显得很简洁呢（或许这就是spfa常年被noip针对的缘故吧）
 
 ~~愉快~~“艰难的”暴力过后，我们也该想想正解了，毕竟oier做题不能仅靠暴力，况且这道题是因为其数据范围小才能被暴力ac，那么这道题的正确方法到底该怎么做呢？
 
 其实原理很简单，看过其他题解的，也应该懂了，但为了题解的完整性，蒟蒻我还是提及一番吧
 
 原理：如果我们修改的路不在原来的最短路上，那么它（这条修改后的边）的修改对于这一次最短路的值没有意义。那么我们也该想到了，在做完第一次dijkstra后，找到位于最短路上的边，对这些边来进行修改求解就好了

那么我们用邻接矩阵的优势也就来了，
可以直接用dfs往回搜索

```cpp
void dfs(int v,int len){
    if(v==1) return ;
    for(int i=1;i<=n;i++)
    if(uv[i][v]!=0x7fffff)
    if(road[v]-uv[i][v]==road[i]){
        x[++o]=v;y[o]=i;
        dfs(i,road[i]);
        return ;
    }
}


```
这样加一个子程序，再对源代码进行一些操作
dijkstra+dfs ac正解（33ms）

```cpp
#include <iostream>
#include <queue>
#include <iomanip>
#include <cstdio>
#define ll long long
using namespace std;
int uv[105][105]={0};
int q=0,n,m;
int x[5005],y[5005],o=0;
bool flag[110]={0};
int road[110]={0};
void dijkstra(){
  
for( int i=1;i<=n;i++){
 flag[i]=0;
 road[i]=uv[1][i];
}
road[1]=0;
flag[1]=1;
    for( int i=1;i<n;i++){
    	int minn=0x7fffff;
    	int t;
    	for( int j=1;j<=n;j++)
    		if(flag[j]==0&&road[j]<minn){
    			t=j;
    			minn=road[j];
            }
    flag[t]=1;
    for( int k=1;k<=n;k++) 
     road[k]=min(road[k],road[t]+uv[t][k]); 
}
}

void dfs(int v,int len){
    if(v==1) return ;
    for(int i=1;i<=n;i++)
    if(uv[i][v]!=0x7fffff)
    if(road[v]-uv[i][v]==road[i]){
        x[++o]=v;y[o]=i;
        dfs(i,road[i]);
        return ;
    }
}

int main (){
   
    int l;
  // freopen("t.txt","r",stdin); 
 scanf("%d%d",&n,&m);
 
 for(int i=1;i<=n;i++)
  for( int j=1;j<=n;j++)
    uv[i][j]=0x7fffff;
 
    for( int i=1;i<=m;i++){
    	int j,k,l;
        scanf("%d%d%d",&j,&k,&l);
 
      	uv[j][k]=l;
      	uv[k][j]=l;
    }

    dijkstra();
    dfs(n,road[n]);
   
  int ans=road[n];
    l=0;
    for(int i=1;i<=o;i++){
       uv[x[i]][y[i]]*=2;
        uv[y[i]][x[i]]*=2;
    dijkstra();
     	l=max(l,road[n]);

     	  uv[x[i]][y[i]]/=2;
     	  uv[y[i]][x[i]]/=2;
    
 }
printf("%d",l-ans);	
    
} 
```
spfa也是类似（避免过长，我在此就不贴出代码了）
【要真想要代码，可以在评测记录中搜我的名字】
【但是不要直接抄哦，小心被抓到】


最后总结： 其实这是一道不算难的题，主要考察的是最短路的模板，以及最短路dfs，或者暴力时对暴力算法时间复杂度的估量，计算；

  引文：此处n较小，我们可用邻接矩阵和原始dijkstra来处理，那么如果n、m数据都增强，这样做会不会出问题呢？
  
  还真那么有这样一道题，与此题极为相似
  P1186 玛丽卡 
  
  建议大家都可以去试试
  
  那么我们就在那道题的题解上，再见吧，拜拜。
  
  


~~【可能看不到我了，因为懒】~~
  
 【如果觉得我打的题解有那么一点点作用的话，欢迎给我留言和点赞】
 
 【各位巨佬对本蒟蒻有什么建议和指教，指正的也欢迎提出】
 
 【最后谢谢各位巨佬，能看完这篇啰嗦鬼码的题解】
   

 
 
 
  
  
  
  
   
   
  
   

 
 