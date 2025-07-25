# 「Wdoi-4」使用三个系统程度的能力

## 题目描述

在 $\text{Windows}$、$\text{Linux}$ 和 $\text{Mac}$ 系统下，分别采用了三种不同的换行符方式。表示为显式转义符，分别是 $\verb!\r\n!$、$\verb!\n!$ 和 $\verb!\r!$ 。现在有一份已经写好了的非空文本文件（里面仅由大小写英文字母、下划线、阿拉伯数字、空格，以及换行符组成）。这个文本文件是在单一系统中写成的，因此保证换行符只会出现上述三种情况**之一**。

比如，这是一个合法的文本文件：

```plain
SCP2021 J rp plus plus
chen zhe AK IOI

Welcome to Hell
```

现在将其中的换行变为对应的转义符。那么在上述三个系统中，分别会变为以下三种模样：

- $\text{Windows}$ 系统：  

$$\colorbox{f5f5f5}{\verb!SCP2021 J rp plus plus\r\nchen zhe AK IOI\r\n\r\nWelcome to Hell!}$$

- $\text{Linux}$ 系统：

$$\colorbox{f5f5f5}{\verb!SCP2021 J rp plus plus\nchen zhe AK IOI\n\nWelcome to Hell!\kern{31.5pt}}$$

- $\text{Mac}$ 系统：

$$\colorbox{f5f5f5}{\verb!SCP2021 J rp plus plus\rchen zhe AK IOI\r\rWelcome to Hell!\kern{31.5pt}}$$ 

---

现在你被给定的任务是，根据转换后的文本文件，判断这是哪个系统下编写的文本文件。对于上述三种情况，分别输出 `windows`、`linux` 或 `mac`。

## 输入格式

输入共一行，为转换后的文本文件。保证文本文件非空，且转换前至少有一个换行符。**输入可能包含空格。**

## 输出格式

输出一行一个小写单词，输出此文本文件在哪个系统下编写。

## 提示

样例 $4$ 见下发的附件 $\textbf{\textit{system4.in}/\textit{system4.out}}$。

#### 数据范围

- 对于 $40\%$ 的数据，保证不存在空格。
- 对于 $100\%$ 的数据，保证输入字符串的长度 $\le 10^5$。输入中仅包含大写英文字母、小写英文字母、下划线、数字、空格和转义字符（`\r`、`\n`）。

#### 注意

本题中的 `\n` 及 `\r` 表示直接写在输入里的一个反斜杠符号跟着一个小写字母 `n` 或 `r`，而不是一个**真正的**转义字符。

## 时空限制

时间限制: 1000 ms
内存限制: 125 MB
