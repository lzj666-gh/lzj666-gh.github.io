# Cinema (翻译版)

## 题目描述

莫斯科在举办一场重要的有$n$ 个不同国家的珂学家参与的国际会议，每个珂学家都只会一种语言。为了方便起见，我们规定一种语言用$1$ 到$10^9$ 的数来描述。 
在会议之后的晚上，珂学家们决定去看电影。他们去的电影院有$m$ 场电影，每场有两个不同的数字，分别代表配音的语言和字幕的语言。如果一个珂学家能听懂配音，他会非常愉悦；如果能看懂字幕，他会比较满意。如果既看不懂也听不懂，他会很生气。 
珂学家们决定去看同一场电影，你必须帮助他们选择一场电影，让愉悦的人最多的前提下，比较满意的人最多。 
输入格式： 第一行一个整数$n(1 \leq n \leq 200000)$ 表示珂学家个数。
第二行$n$ 个整数$a_1, a_2, ..., a_n(1 \leq a_i \leq 10^9)$ 表示珂学家们会的语言。 
第三行一个整数$1 \leq m \leq 200000$ 表示电影的场数。 
第四行$m$ 个整数$b_1, b_2, ..., b_n(1 \leq b_j \leq 10^9)$ 表示电影的配音用的语言。
第五行$m$ 个整数$c_1, c_2, ..., c_n(1 \leq c_j \leq 10^9)$ 表示电影的字幕用的语言。 
输出格式： 一个整数表示安排哪一场电影。 如果有多种情况，选择比较满意的方案输出。

## 输入格式

The first line of the input contains a positive integer $ n $ ( $ 1<=n<=200000 $ ) — the number of scientists.

The second line contains $ n $ positive integers $ a_{1},a_{2},...,a_{n} $ ( $ 1<=a_{i}<=10^{9} $ ), where $ a_{i} $ is the index of a language, which the $ i $ -th scientist knows.

The third line contains a positive integer $ m $ ( $ 1<=m<=200000 $ ) — the number of movies in the cinema.

The fourth line contains $ m $ positive integers $ b_{1},b_{2},...,b_{m} $ ( $ 1<=b_{j}<=10^{9} $ ), where $ b_{j} $ is the index of the audio language of the $ j $ -th movie.

The fifth line contains $ m $ positive integers $ c_{1},c_{2},...,c_{m} $ ( $ 1<=c_{j}<=10^{9} $ ), where $ c_{j} $ is the index of subtitles language of the $ j $ -th movie.

It is guaranteed that audio languages and subtitles language are different for each movie, that is $ b_{j}≠c_{j} $ .

## 输出格式

Print the single integer — the index of a movie to which scientists should go. After viewing this movie the number of very pleased scientists should be maximum possible. If in the cinema there are several such movies, you need to choose among them one, after viewing which there will be the maximum possible number of almost satisfied scientists.

If there are several possible answers print any of them.

## 提示

In the first sample, scientists must go to the movie with the index $ 2 $ , as in such case the $ 1 $ -th and the $ 3 $ -rd scientists will be very pleased and the $ 2 $ -nd scientist will be almost satisfied.

In the second test case scientists can go either to the movie with the index $ 1 $ or the index $ 3 $ . After viewing any of these movies exactly two scientists will be very pleased and all the others will be not satisfied.

## 时空限制

时间限制: 2000 ms
内存限制: 250 MB
