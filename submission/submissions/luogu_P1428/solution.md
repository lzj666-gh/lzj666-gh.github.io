# P1428 题解

这题很简单，解题的关键在于遍历每只小鱼，统计其左侧所有可爱值小于它的鱼的数量。可以通过双重循环实现：外层用来遍历每只小鱼，内层遍历其左侧所有鱼并比较可爱值。具体步骤为先读取鱼的数量和每只鱼的可爱值，存储于数组中，再对每只小鱼，统计其左侧比它可爱值小的鱼的数量并记录；最后按顺序输出结果就好了。
### code：
```cpp
#include<bits/stdc++.h>
#include<vector>
using namespace std;
int main(){
    int n;
    cin>>n;
    vector<int> c(n);
    for (int i=0;i<n;i++) {
        cinc>>c[i];
    }
    vector<int> b(n,0);
    for(int i=1;i<n;i++){
        for(int j=0;j<i;j++){
            if (c[j]<c[i]){
                b[i]++;
            }
        }
    }
    for(int i=0;i<n;i++){
        cout<<b[i];
        if(i<n-1) cout<<" ";
    }
    return 0;
}
```
求赞求过。