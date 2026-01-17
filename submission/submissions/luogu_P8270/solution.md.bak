# P8270 题解

## 题意
首先，给我们两个字符串，分别为 $S,T$ ( $S$ 和 $T$ 的长度均小于 $10^5$  )， 这两个字符串只包含 `a-r` 这些字符。然后给我们 $Q (Q \leq 10^5)$ 个查询，每个查询输入一个字符串，比如输入了 `abc` 这个查询，我们应该判断 $S$ 和 $T$ 中的 `a,b,c` 都提取出来，看是否相同。
__________
## 思路
我们第一眼看到字符只能是 `a-r` 时，会想到为什么不是 `a-z` 呢？我们可以想到用 $O(18^2 \cdot \max(|S|,|T|))$ 的时间复杂度来求解，刚好可以卡过这一题，而 `a-z` 时的 $O(26^2 \cdot \max(|S|,|T|))$ 刚好会被卡。**Tip**：$|S|$ 表示字符串 $S$ 的长度。

### step-1：预处理
我们设 $f_{i,j} = true$ 表示将 `a-r` 中第 $i,j$ 个字符 (如 `a` 和 `c` ) 从 $S,T$ 中提取出来时，提取出来的这些字符并不相等，等于 $false$ 则反之。
#### 举个例子:
- $S:$ `abcd`

- $T:$ `abccd`

那么 $f_{0,2}$ 显然是等于 $true$， 因为将第 $0,2$ 个字符(分别是 `a` 和 `c` )从 $S$ 和 $T$ 提取出来,发现他们不同，所以等于 $true$。
__________________
### step-2：处理询问。
现在我们对于每一个询问就很好处理了。设一个询问为 $C$， 长度为: $|C|$ 那么我们枚举 $C$ 的第 $i$ 和 $j (1 \le {i,j} \le |C|)$， 个字符如果 $f_{C_i,C_j} = true$ 的话，就代表它不合法，反之代表它合法。
______________
### 最后贴上代码

```cpp
#include<bits/stdc++.h>
#define ull unsigned long long
using namespace std;
const int maxlen=200010;
char s[maxlen],t[maxlen],tmp[maxlen];
int q;
bool b[25][25];
int main(){
    cin>>s>>t;
    int lens=strlen(s),lent=strlen(t);
    for(char i='a';i<='r';i++){
        for(char j='a';j<='r';j++){
            char strs[maxlen],strt[maxlen];
            int cnts=0,cntt=0;
            for(int k=0;k<lens;k++){
                if(s[k]==i||s[k]==j)strs[cnts++]=s[k];
            }
            for(int k=0;k<lent;k++){
                if(t[k]==i||t[k]==j)strt[cntt++]=t[k];
            }
            if(cnts!=cntt){b[(int)i-'a'][(int)j-'a']=1;continue;}
            bool flag=0;
            for(int k=0;k<cnts;k++){
                if(strs[k]!=strt[k]){flag=1;}
            }
            b[(int)i-'a'][(int)j-'a']=flag;
        }
    }
    scanf("%d",&q);
    while(q--){
        scanf("%s",tmp);
        int len=strlen(tmp);
        bool flag=0;
        for(int i=0;i<len;i++){
            for(int j=0;j<len;j++){
                if(b[tmp[i]-'a'][tmp[j]-'a']){flag=1;break;}
            }
            if(flag)break;
        }
        if(flag)printf("N");
        else printf("Y");
    }
    return 0;
}```








