# P7911 题解

UPD：修复了正则表达式的错误。

提供两种极其好写的做法，代码长度均 <1k。  
这题主要难点在于判断一个地址是否合法，剩下部分可以直接使用 `std::map/unordered_map` 来解决，因此主要判断地址是否合法。

方法一：  
注意到字符串长度 $\le25$，因此一个数字最长为 17 位，可以使用 `long long` 存储。  
`std::sscanf(s, "%lld.%lld.%lld.%lld:%lld", &a, &b, &c, &d, &port)` 表示从 `s` 中读入 `a`，忽略下一个 `.`，读入 `b`，忽略下一个 `.`。以此类推。其返回值是成功读取的元素个数。因此如果返回值不是 $5$ 一定不合法。如果几个值不满足题目要求也不合法。  
然后考虑处理前导 0 和后面是否多出来一些内容。但是我们可以反过来，用得到的的数拼出合法的地址，然后和原串比较一下是否完全相同。如果没有前导 0 且后面没有多余内容，两者应该完全相同。拼出地址可以使用 `std::stringstream` 或者 `std::to_string` 来处理。代码使用了 `std::stringstream`。  
```cpp
#include <bits/stdc++.h>
using namespace std;
int n;
bool Check(string s) {
  long long a, b, c, d, port;
  if (sscanf(s.c_str(), "%lld.%lld.%lld.%lld:%lld", &a, &b, &c, &d, &port) != 5)  return false;
  if (a < 0 || a > 255 || b < 0 || b > 255 || c < 0 || c > 255 || d < 0 || d > 255 || port < 0 || port > 65535)  return false;
  stringstream ss;
  ss << a << '.' << b << '.' << c << '.' << d << ':' << port;
  return ss.str() == s;
}
map<string, int> mp;
string op, ad;
int main(int argc, char const *argv[]) {
  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> op >> ad;
    if (!Check(ad)) { cout << "ERR\n"; continue; }
    if (op[0] == 'S') {
      if (mp[ad]) cout << "FAIL\n";
      else mp[ad] = i, cout << "OK\n";
    } else {
      if (!mp.count(ad)) cout << "FAIL\n";
      else cout << mp[ad] << '\n';
    }
  }
  return 0;
}
```
方法二：  
今年使用 C++14 标准，因此可以使用 C++11 的 `regex` 库。直接写一个正则表达式判断是否合法即可。正则表达式可以参考洛谷日报或者百度。正则库的使用方法可以参考 [C++ Reference](https://zh.cppreference.com/w/cpp/regex)。
```cpp
#include <bits/stdc++.h>
using namespace std;
int n;
regex r("(\\d|[1-9]\\d|1\\d{2}|2[0-4]\\d|25[0-5])\\.(\\d|[1-9]\\d|1\\d{2}|2[0-4]\\d|25[0-5])\\.(\\d|[1-9]\\d|1\\d{2}|2[0-4]\\d|25[0-5])\\.(\\d|[1-9]\\d|1\\d{2}|2[0-4]\\d|25[0-5]):(\\d|[1-9]\\d{1,3}|[1-5]\\d{4}|6[0-4]\\d{3}|65[0-4]\\d{2}|655[0-2]\\d|6553[0-5])");
map<string, int> m;
string o, a;
int main(int argc, char const *argv[]) {
  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> o >> a;
    if (!regex_match(a, r)) { cout << "ERR\n"; continue; }
    if (o[0] == 'S') {
      if (m[a]) cout << "FAIL\n";
      else m[a] = i, cout << "OK\n";
    } else {
      if (!m.count(a)) cout << "FAIL\n";
      else cout << m[a] << '\n';
    }
  }
  return 0;
}
```