# P11020 题解

当 $k \leq \min(m,n)$ 时，只需把 $k$ 个石头放在不同的行和列（例如放在对角线的前 $k$ 个位置），这样至少需要 $k$ 次宇宙射线才可以全部销毁，显然是最优的。

当 $k > \min(m,n)$ 时，由于不管怎么样都可以通过至多 $\min(m,n)$ 步全部销毁（直接对每行或每列依次销毁即可），所以可以先按照对角线放，多余石头随意摆放即可达到 $\min(m,n)$ 步。

有兴趣的读者可以思考一下 checker 的实现。

特别注意：不要每组数据都把整个数组 `memset`，否则会 TLE！

```cpp
#include<bits/stdc++.h>
using namespace std;

char mp[2000][2001];

int main(){
    int T; scanf("%d",&T);
    while(T--){
        int n,m,k;
        scanf("%d%d%d",&n,&m,&k);
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++)mp[i][j]='.';
            mp[i][m]='\0';
        }
        for(int i=0;i<min({n,m,k});i++)mp[i][i]='S';
        int i=0,j=0; k-=min({n,m,k});
        while(k){
            if(mp[i][j]=='.')mp[i][j]='S',k--;
            j++;
            if(j==m)i++,j=0;
        }
        for(int i=0;i<n;i++)
            printf("%s\n",mp[i]);
    }
    return 0;
}
```