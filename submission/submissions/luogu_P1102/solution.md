# P1102 题解

这一题将A-B=C转换成A-C=B，首先将A数组每个元素出现的次数统计起来，用map映射，最后将A数组每次减一个C，再将A数组扫一遍，将所有映射的次数和加起来就是答案

    
    
    
```cpp
    #include <iostream>
    #include <map>
    using namespace std;
    typedef long long LL;
    LL a[200001];
    map<LL,LL> m;//建立一个数字到出现次数的映射 map<num,times>
    //A-B=C --> A-C=B
    int main() {
        int n;
        LL c;
        LL ans=0;
        cin >> n >> c;
        for(int i=1;i<=n;i++) {
            cin >> a[i];
            m[a[i]]++;
            a[i]-=c;    
        } 
        for(int i=1;i<=n;i++) ans+=m[a[i]];
        cout << ans << endl;
        return 0;
}
```