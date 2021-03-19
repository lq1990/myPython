# OpenSSL SSL_connect: Connection was reset in connection to github.com:443

## 方案一

在git bash命令行中依次输入以下命令：

> git config --global http.sslBackend "openssl"
git config --global http.sslCAInfo "C:\Program Files\Git\mingw64\ssl\cert.pem"

注意上面第二个命令，路径要换成git安装的路径。


## 方案二

如果你开启了VPN，很可能是因为代理的问题，这时候设置一下http.proxy就可以了。
先查看当前VPN代理使用的端口号，如下图所示，我的端口号是7890

所以，在git bash命令行中输入以下命令即可：

> git config --global http.proxy 127.0.0.1:7890
>
> git config --global https.proxy 127.0.0.1:7890



如果你之前git中已经设置过上述配置，则使用如下命令取消再进行配置即可：

> git config --global --unset http.proxy
>
> git config --global --unset https.proxy



下面是几个常用的git配置查看命令：
```
git config --global http.proxy #查看git的http代理配置
git config --global https.proxy #查看git的https代理配置
git config --global -l #查看git的所有配置
```

## 方案三

还有一个情况，是你的VNP代理服务器节点有问题，有时候更换一个结点就好了。


## 方案四

打开一个新的git bash终端，就没问题了。这个可能是当前git的会话有关。


# refer
https://blog.csdn.net/qq_37555071/article/details/114260533?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-0&spm=1001.2101.3001.4242

