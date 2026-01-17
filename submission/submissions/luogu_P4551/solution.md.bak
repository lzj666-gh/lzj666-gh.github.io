# P4551 题解

蒟蒻第一次学习01trie，发篇题解加深一下印象。

首先说一下题意。这题就是给你一棵树，求树上所有路径中异或和最大的。

两个前置芝士：

# 1、01trie 

把数拆成二进制的形式，然后每一位都只有两个字符：0或1，然后按照trie的方式存下来，以达到节省空间的效果。

如下图：

![](https://cdn.luogu.com.cn/upload/pic/53407.png)

这样就不用一个数一个数组的浪费空间来存了QAQ

# 2、异或

把两个数写成二进制的形式，对照每一位，如果相同则这一位为0，否则为1。

如下：

3:  011

4:  100

3^4=111=7

理解了我们就接下来进入正题。

# 题解

我们对于每一个数到根节点的异或和进行建01trie树。

以样例为例子：

![](https://cdn.luogu.com.cn/upload/pic/53408.png)

然后有一个定论：一个数，如果它两次异或同一个数，那么它是不会有改变的。

那么i~j的路径上的异或和，就可以表示成根到i的异或和异或上根到j的异或和。

那思路就很明确了：对于每一位进行贪心，如果这一位有一个与它不同的，即异或
后是1，那我们就顺着这条路往下走；否则就顺着原路往下走。

这样贪心为什么是对的呢？因为当前这一位的权值比后面所有位数加起来还要高。

就比如有一个数它的二进制表示是10...0（n个0）

那么它比01...1(n-1个1）还要大。

所以最高位决定一切qwq~

然后代码闪亮登场~

    #include<bits/stdc++.h>
    using namespace std;
    struct qwq{
        int v;
        int w;
        int nxt;
    }edge[2000001];
    int head[2000001];
    int cnt=-1;
    void add(int u,int v,int w){
        edge[++cnt].nxt=head[u];
        edge[cnt].v=v;
        edge[cnt].w=w;
        head[u]=cnt;
    }
    int sum[2000001];
    void dfs(int x,int fa){//预处理
        for(int i=head[x];~i;i=edge[i].nxt){
            int v=edge[i].v;
            int w=edge[i].w;
            if(v!=fa){
                sum[v]=sum[x]^w;
                dfs(v,x);
            }
        }
    }
    struct trie{
        int ch[2];
    }t[2000001];
    int tot;
    void build(int val,int x){
        for(int i=(1<<30);i;i>>=1){
            bool c=val&i;//取出二进制下这个数的当前位置
            if(!t[x].ch[c]){
                t[x].ch[c]=++tot;
            }
            x=t[x].ch[c];
        }
    }
    int query(int val,int x){
        int ans=0;
        for(int i=(1<<30);i;i>>=1){
            bool c=val&i;
            if(t[x].ch[!c]){//如果这一位可以进行异或就沿着这一条往下走
                ans+=i;
                x=t[x].ch[!c];
            }
            else x=t[x].ch[c];//否则就沿着另一条路往下走
        }
        return ans;
    }
    int main(){
        memset(head,-1,sizeof(head));
        int n;
        scanf("%d",&n);
        for(int i=1;i<n;++i){
            int u,v,w;
            scanf("%d%d%d",&u,&v,&w);
            add(u,v,w);
            add(v,u,w);
        }
        dfs(1,-1);//预处理出每一个节点到根的异或和
        for(int i=1;i<=n;++i)build(sum[i],0);//建立trie数
        int ans=0;
        for(int i=1;i<=n;++i){
            ans=max(ans,query(sum[i],0));//查询，取最大值
        }
        printf("%d\n",ans);
    } 

复杂度O(n)  ~~自带30的常数~~