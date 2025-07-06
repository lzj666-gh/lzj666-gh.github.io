# P3966 题解

首先，我们都知道fail树就是在跑ac机中把失配指针所指向的值与失配指针所表示的边重新建出来的树。有这个思想，那么这道题就很简单了。

跑一遍AC自动机，每一个节点保存一下属于多少字符串，为它的权值。然后一个节点表示的字符串在整个字典中出现的次数相当于其在Fail树中的子树的权值的和。

# code

```
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#define N 1100005
using namespace std;
int n,a[N],h[N],cnt,last,ch[N][26],sz[N],fail[N];
char s[N];
struct ac{
	void ins(int x){
		scanf("%s",s+1);int now=0,len=strlen(s+1);
		for(int i=1;i<=len;i++){
			int u=s[i]-'a';
			if(!ch[now][u]) ch[now][u]=++cnt;
			now=ch[now][u];
			sz[now]++;
		}
		a[x]=now;
	}
	void build(){
		int i,head=0,tail=0;
		for(i=0;i<26;i++) if(ch[0][i]) h[++tail]=ch[0][i];
		while(head<tail){
			int x=h[++head],y;
				for(i=0;i<26;i++) if(y=ch[x][i]){
				h[++tail]=y;
				fail[y]=ch[fail[x]][i];
			}
			else ch[x][i]=ch[fail[x]][i];
		}
	}
	void solve(){
		for(int i=cnt;i>=0;i--) sz[fail[h[i]]]+=sz[h[i]];
		for(int i=1;i<=n;i++) printf("%d\n",sz[a[i]]);
	}
}ac;
int main(){
	//freopen("word.in","r",stdin);
	//freopen("word.out","w",stdout);
	scanf("%d",&n);
	for(int i=1;i<=n;i++) ac.ins(i);
	ac.build();ac.solve();
	return 0;
}
```
