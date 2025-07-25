# 【FUN】打字练习

## 题目描述

本题需要 Windows 或有视窗的 Linux 系统。

请在附件中下载打字练习器压缩包并解压，然后运行对应平台版本的可执行文件。

玩法：当细线下落到底部红色提示线上时，按下对应键位即可。

系统会综合评判您在关卡当中的表现，给出通关 / 失败的评价。通关后您将获得一个形如 `"xxxx"` 的字符串，此为通关凭证。

游玩提示：

- 请切换为英文输入法。当系统当前为中文输入法时，游戏有可能无法检测字母按键；
- 选择关卡请使用**方向键**。按照**隐藏歌曲**输入**隐藏指令**可以进入**隐藏**关（没有通关凭证）；
- 不管您是否有基础，都请**慢慢来**，慢慢来才能看得清楚。


## 输入格式

无

## 输出格式

通关凭证（不带引号）。

## 提示

程序运行时会读取 `config.txt` 作为配置文件（如果没有，则创建会一个默认的）。内含三项配置：

- `"keys"`：长度为 4 的小写字母字符串，惯用键位。
- `"speed"`：实数，速率。
- `"offset"`：实数，单位为秒，用于调节来自各种因素的延迟（键盘性能等）。

我们提供五种难度的关卡以及一个游戏内隐藏的密码（11 位数字组成）。根据您提交的内容，得分如下表：

| 提交内容 | 得分 | | 提交内容 | 得分 |
| :----------: | :----------: | :----------: | :----------: | :----------: |
| Easy 通关凭证 | $70$ |  | Normal 通关凭证 | $80$ |
| Hard 通关凭证 | $90$ | | Master 通关凭证 | $95$ |
| Legend 通关凭证 | $100$ | | 游戏内隐藏密码 | $100$ |

不要作弊或者开挂哦！

---

如果无法正常游玩，请优先按照以下步骤检查：

- 整个压缩包解压。单独解压一个 exe 文件是不够的。另外，在解压软件里双击 exe 大概率不行的——不要问为什么！不行就是不行！

- 杀毒软件告警。别管！没那么无聊给你塞个病毒！另外，解压后 exe 消失了的话，大概率是杀毒软件误判然后自动清除了。自己动手把程序加入白名单吧。

- 按按键没反应，请检查输入法是否切换为英文模式。多检查几次，有时候，按 Enter 开启了游戏，输入法会自己跳回中文的。

如果您不是海洋馆“关爱唐氏儿童童话故事化装剧场”里演虾的那些人，请勿在讨论区 / 洛谷交流群等地重复提问。

## 时空限制

时间限制: 1000 ms
内存限制: 512 MB
