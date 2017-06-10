# 老王Python学习笔记
## 一、基础篇

### 基础篇第3、4节主要内容
1. 用虚拟机vbox安装xubuntu开发环境(Linux)
2. 基于win7的Win系统 Python开发环境配置：[ANACONDA](https://www.continuum.io/downloads/)

#### 一. 用虚拟机vbox安装xubuntu开发环境；
1. 下载安装[virtualbox](https://www.virtualbox.org/wiki/Downloads)
，按照提示一路next即可完成安装

2. 下载安装[xubuntu](https://xubuntu.org/getxubuntu/)
- 文件较大，最好提前下载好，注意下载的版本，amd64.iso是64位，i386.iso是32位文件。
- 新建->几步常规设置
- 安装iso：设置->存储->没有盘片->属性中点击最右侧光盘形状的图标加载ISO文件
- 然后基本上就是按照提示一路next即可
- 系统安装完成之后，还需要安装一个增强功能，更加丰富的功能
- 安装过程并不太顺利，又是安装了一半突然报错，然后重新安装，暂时没有好的解决办法
> 可能需要安装两三次才能安装成功，耗时较长，遇见问题可以百度一下相关教程。
- 安装增强功能：设备->安装增强功能->需要打开命令行安装
```
cd /media/zsx/VBOXADDITIONS_5.1.22_115126/  #设置当前工作目录
sudo sh VBoxLinuxAdditions.run  # 安装增强功能
```
- 最后一步设置软件下来来源，检测最合适服务器，速度会快一些。

#### 二. linux基本命令
1. ctrl + alt + f6 开启真正的终端
2. ctrl + alt + f7 关闭真正的终端
3. pwd 返回当前工作目录
3. sudo super do 超级管理员
4. nano ubuntu默认的编辑器
```
cd /tmp/ 
nano hello.py  # 在tmp/ 目录下创建文件hello.py
print('hello world')   #线文件内写入一行代码
ctrl + x               # 退出文件
y                      # 回复y保存所做的改变

python hello.py        # 运行py文件，并输出结果'hello world'
```

5. 文件权限：r w x
```

cd /tmp/  
ls -l   # 查看文件详细信息
-rw------- 1 zsx  zsx     0 6月   9 20:34 config-err-pVx0cf
-rw-rw-r-- 1 zsx  zsx    20 6月   9 20:37 hello.py
drwx------ 3 root root 4096 6月   9 20:33 systemd-private
```
- r read 读的权限
- w write 写的权限
- x 执行的权限
- r w x的值分别为4 2 1
- rwx=7 r-w=6 r-x=5 w-x=3 
以上述的hello.py文件为例说明文件权限及更改方法：
- 最前边的-代表文件，如果是d则代表是文件夹
- 最前边的rw 表示该文件或文件所属的用户对该文件的操作权限
- 中间的rw 表示该文件或文件所属的用户组对该文件的操作权限
- 最后边的r 表示其他用户或用户组对该文件的操作权限
- 以值的形式表示上述文件操作权限则是664
-更改文件操作权限的命令是chmod
```
chmod 764 hello.py # 增加该文件所述用户对文件的执行权限
ls -l
-rwxrw-r-- 1 zsx  zsx    20 6月   9 20:37 hello.py
```
6. rm renmove删除文件

7. tail -n filename 查看文件内容
```
tail -10 test.py
```

8. man 查看帮助
```
man tail     # 查看tail命令的帮助文章
tail --help  # 查看tail命令的帮助文档
```
9. 在linux的终端退出python命令行: 使用 quit(), exit(), 或者Ctrl+D退出命令行。
10. 三种常见的文件安装命令
> 主要参考: [ubuntu一些基本软件安装方法](http://blog.csdn.net/yandawcheng/article/details/51331467)
```
"1. deb类型安装包的安装方式"
# deb 是 debian 系 Linux 的包管理方式, ubuntu 是属于 debian 系的 Linux 发行版,
# 默认支持这种软件安装方式,当下载到一个 deb 格式的软件后,在终端输入如下一行命令就能安装:
'''
sudo dpkg -i （deb安装包名称加后缀）

"2. 下载安装包后编译安装方式（以python3.5安装为例）"
# 下载完成后把安装包复制到指定安装目录下（本人安装在/usr/local/下）
tar -xzvf Python-3.5.3.tgz  # 解压安装包，并出现Python-3.5.3.tgz目录
cd Python-3.5.3.tgz
./configure
make   # 如果报错请求被拒绝 ，则使用sudo重新运行，遇到这种情况暂时这样处理。
make install

"3. apt-get安装方式"
wget url      # 根据链接url下载文件target
unzip target       # 解压文件
sudo apt-get update     # 更新软件信息库
sudo apt-get install target    #以编译方式安装target文件
```

11. LINUX中常用操作命令
>- [LINUX中常用操作命令](http://www.daniubiji.cn/archives/25)
>- [10 Basic Linux Commands That Every Linux](http://www.linuxandubuntu.com/home/10-basic-linux-commands-that-every-linux-newbies-should-remember)

---

#### 三. 开发环境sublime text3 的安装配置(Linux系统)
1. 安装sublime text3
打开命令行，依次执行以下命令（安装命令来自sublim官网）
```
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-get update
sudo apt-get install sublime-text
```
2. 安装package
- 安装package contral：preferences-> install package contral
- 使用package contral安装其他package：preferences-> package contral -> install package ->输入安装包名称既即可在线安装
- 推荐安装anaconda和Python pep8 autoformat
- ctrl + B即可运行已完成的代码，sublime默认调用系统中已安装的Python版本
> 还可以参考一个比较全面的教程[Ubuntu16.04下使用sublime text3搭建Python IDE](http://www.cnblogs.com/unflynaomi/p/5704293.html)
---

### 四. Win系统 Python开发环境配置：[ANACONDA](https://www.continuum.io/downloads/)
> 如果操作系统为Win7，还可以采用以下进行开发环境配置。

**ANACONDA**主要包含一下几部分：
- 1. **jupyter notebook**：网页版交互计算环境（无需联网）
- 2. **spyder**：专门的Python开发环境
- 3. **IPython**：可理解为升级版Python
- etc.

其中，

- **jupyter notebook**用的最多，运行视频中的案列代码，以及每一节的练习题，都可以通过他完成。
- **spyder**将Python和IPython统一在该平台，可以安装并调用已经模块（package），也可以自己撰写独立模块，然后加载运行。
- **ANACONDA**安装配置比较简单，按照提示完成即可。安装完成，可查看帮助文档，探索一下。

#### 3. Windows基本命令

```
pwd  #输出当前工作目录

ls   #显示当前文件夹下的文件

cd   # 显示或更改当前目录

```