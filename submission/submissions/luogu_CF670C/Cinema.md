# Cinema

## 题目描述

Moscow is hosting a major international conference, which is attended by $ n $ scientists from different countries. Each of the scientists knows exactly one language. For convenience, we enumerate all languages of the world with integers from $ 1 $ to $ 10^{9} $ .

In the evening after the conference, all $ n $ scientists decided to go to the cinema. There are $ m $ movies in the cinema they came to. Each of the movies is characterized by two distinct numbers — the index of audio language and the index of subtitles language. The scientist, who came to the movie, will be very pleased if he knows the audio language of the movie, will be almost satisfied if he knows the language of subtitles and will be not satisfied if he does not know neither one nor the other (note that the audio language and the subtitles language for each movie are always different).

Scientists decided to go together to the same movie. You have to help them choose the movie, such that the number of very pleased scientists is maximum possible. If there are several such movies, select among them one that will maximize the number of almost satisfied scientists.

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
