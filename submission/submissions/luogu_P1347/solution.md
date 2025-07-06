# P1347 题解

这一道题一看就知道是拓扑排序。

1.首先观察数据范围和输出，数据范围26，是真的小，就说明多搞一搞肯定也T不了。输出要求输出到第几次就行了，或者不行了，就说明我们每建一条边就需要一次拓扑排序。

2.再看这道题的三种情况。第一个是有稳定顺序，第二个是有环，第三个是无环但是也没有稳定拓扑顺序。然后我们对这三个问题进行依次解决。

第一个问题：有稳定拓扑排序说明拓扑排序的层数是n。也就是下面代码的val。一层一层下去如果是n层的话，那么这个图里面肯定包含一个n长度的链，我们只要看最大的层数是不是n就可以了，也就是代码的ans==n。

第二个问题就是成环，拓扑排序判断有没有环其实很简单，如果拓扑排序没能遍历所有的点，就说明存在一个环。也就是下面的sum==s1.size()。s1是用来存储目前元素（点）个数的。

最后一种情况最简单，如果前两种都不是，那肯定就是最后一种了！

下面上代码：
```cpp
#include <bits/stdc++.h>
#define MAXN 50
using namespace std;
int n,m;
struct Node{
    int u;
    int val;
    Node(int u=0,int val=0):u(u),val(val){}
};
vector<int> vec[MAXN];
int ru[MAXN];
int sum;
int ans;
int k;
set<int> s1;
void make(){
    queue<int> q;
    int ru1[MAXN];
    memset(ru1,0,sizeof(ru1));
    for(int i=0; i<26; i++){
        for(int j=0; j<vec[i].size(); j++){
            ru1[vec[i][j]]++;
        }
    }
    for(int i=0; i<26; i++){
        if(ru1[i]==0&&s1.count(i)){
            q.push(i);
            cout<<char(i+'A');
        }
    }
    while(!q.empty()){
        int u=q.front();
        q.pop();
        for(int i=0; i<vec[u].size(); i++){
            int v=vec[u][i];
            ru1[v]--;
            if(ru1[v]==0){
                q.push(v);
                cout<<char(v+'A');
            }
        }
    }
}
int have;
void topo(){
    queue<Node> q;
    for(int i=0; i<26; i++){
        if(ru[i]==0&&s1.count(i)){
            q.push(Node(i,1));
            sum++;
        }
    }
    while(!q.empty()){
        int u=q.front().u;
        int val=q.front().val;
        q.pop();
        for(int i=0; i<vec[u].size(); i++){
            int v=vec[u][i];
            ru[v]--;
            if(ru[v]==0){
                sum++;
                q.push(Node(v,val+1));
                ans=max(ans,val+1);
            }
        }
    }
    if(ans==n){
        printf("Sorted sequence determined after %d relations: ",k);
        make();
        cout<<".";
        exit(0);
    }
    if(sum!=have){
        printf("Inconsistency found after %d relations.",k);
        exit(0);
    }
}
int ru2[MAXN];
int main(){
    cin>>n>>m;
    for(int i=1; i<=m; i++){
        string s;
        cin>>s;
        k=i;
        vec[s[0]-'A'].push_back(s[2]-'A');
        s1.insert(s[0]-'A');
        s1.insert(s[2]-'A');
        have=s1.size();
        ru2[s[2]-'A']++;
        sum=0;
        ans=0;
        memcpy(ru,ru2,sizeof(ru2));
        topo();
    }
    printf("Sorted sequence cannot be determined.");
    return 0;
}

```