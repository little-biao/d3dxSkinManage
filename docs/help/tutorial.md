# 快速上手

## 免责声明

该项目的所有者及其他贡献者不对项目本身及其任何衍生作品提供任何形式的保证，包括但不限于其准确性、完整性、功能性或适用性。
在任何情况下，所有者和贡献者均不对因使用该项目或其衍生作品而产生的任何损害、损失或问题承担责任。

## 不适宜的使用场景

::: danger 首先
在开始之前，你需要了解一些事情，以确保这个项目适合你，而不是在浪费你的时间；<br/>
如果你不能接受或不能理解以下内容，请不要使用本程序。
:::

该项目具有以下特点：
1. 模组文件会压缩后以 **SHA-1** 命名存储，所以他在本地看上去会像一串 **“乱码”** ；
2. 通过索引文件来记录每个模组所要表达的信息，并自行计算其分组而非用文件夹组织；
3. 不允许手动管理模组工作目录，你需要通过一些特殊的方式加入否则它们会被程序删除。

::: info 有关 **SHA-1** 的更多信息
[维基百科](https://zh.wikipedia.org/wiki/SHA-1)　[百度百科](https://baike.baidu.com/item/SHA-1)
:::

::: info 关于压缩存储的更多信息
程序会将模组文件压缩后存储，在需要使用时释放到工作目录，这样可以减少磁盘空间占用，
但缺点是会增加程序加载模组的时间。
:::

::: warning 关于磁盘空间占用
之前有人提出这种方式会占用双倍的磁盘空间，但经过测试，压缩后的文件远比之前要小得多，
即使你将文件全部释放到工作目录，也远远达不到两倍的磁盘空间占用，
且在大多数情况下（在定期清理缓存之后），总的磁盘占用（算上所有已释放的文件和所有压缩后的文件）
也比压缩前要小。
:::


## 运行环境要求

1. **Windows 10** x64 及以上的非精简版系统；
2. 会看文档的眼睛；
3. 灵活操作的双手；
4. 善于沟通的嘴巴；
5. 聪明伶俐的脑瓜。

::: tip 提醒
程序在发布之前会在一台纯净的 **Windows 10 (19045.2006)** 虚拟机上进行测试，
如果你无法正常使用，多数情况下是你的系统问题，请尝试更换或更新系统版本，
以及**不要使用任何精简版系统**。
:::


## 让我们开始吧

此次教程将使用一个不带任何预置内容的程序作为示例，如果你当前的程序包已经包含某些预置内容，
可以选择性的跳过某些步骤，否则请严格按照左侧导航栏的步骤顺序进行，
当然你也可以选择点击文档底部的**下一页**按钮进行跳转。
