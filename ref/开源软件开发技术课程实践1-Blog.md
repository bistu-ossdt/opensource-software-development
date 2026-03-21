```markdown
# 北京信息科技大学课程报告

报告题目：使用开源软件建立博客

课程名称：开源软件开发

任课教师：李宁

姓名：

学号：

学院专业：

本报告考察通过阅读文档使用开源软件的能力，通过社区讨论解决问题的能力，以及对Github的初步使用。请完成以下步骤，填写表格并提交本文档作为作业。本作业需要在指定时间完成并提交。在现场实验课中完成将有加分，不能按时提交将会有扣分。

## 报告内容（需要填写3项）

**Github Blog**

Blog网站地址(例如 https://<username>.github.io )

第一篇文章的地址

安装过程记录

请粘贴所有的命令行和窗口输出

---

## 安装中遇到的问题及解决方法

请描述问题及解决方法

---

## 作业要求：

1. 安装Git
2. 安装Hugo
3. 用Hugo创建和配置Blog
4. 写一篇Blog，内容是自己在配置中遇到的问题以及如何解决
5. 将Hugo Blog通过Github Pages发布

---

## 如何解决问题

- 查看安装指南
- 查看官方文档
- 询问本组的同学和导师
- 在课程微信群提问

---

## 步骤

安装Git  
（提示：如果遇到SSL certificate problem，是因为FastGithub引起，需要关闭git的证书验证，运行：`git config --global http.sslverify false`）  
以下操作请在Git Bash中运行。

安装Hugo  
（提示：将hugo.exe拷贝到系统路径）

创建一个新的站点  
（提示：选择一个你存放站点的本地路径），然后cd进入这个目录。以下操作均在你建立的站点目录下运行。

```

hugo new site hugo-blog
cd hugo-blog

```
（注意：“hugo-blog”可以更换为你喜欢的其他名字）

安装一个主题  
（提示：[Complete List | Hugo Themes (gohugo.io)](https://themes.gohugo.io/)有全部的主题，可以选择一个自己喜欢的主题。使用主题的稳定版本，以及阅读主题的安装配置文档，一般在主题目录下的README。如果一个主题不好用，可以更换其他主题）

```

git init
git submodule add [https://github.com/theNewDynamic/gohugo-theme-ananke.git](https://github.com/theNewDynamic/gohugo-theme-ananke.git) themes/ananke

```

（注意：根据ananke的安装说明，要从exampleSite文件夹里复制config.toml文件并做编辑）

添加一篇文章，描述自己在完成本作业中遇到的问题(可以完成全部步骤后再来更新这个文档，MarkDown格式请见文末链接)

```

hugo new posts/my-first-post.md

```

启动 Hugo 预览服务器预览站点效果，预览网址 //localhost:1313/

```

hugo server -D

```

构建静态页面

```

hugo -D

```

通过个人主页发布：登录Github，创建一个 `<USERNAME>.github.io` 仓库来托管生成的静态内容，发布后的域名为 `https://<USERNAME>.github.io`。（提示：<USERNAME>替换为你在Github的用户名）

将hugo站点中的配置文件的 `baseUrl` 设置为 `<USERNAME>.github.io`（提示：可能是config.toml，或者主题指定的配置文件）

配置Github的SSH证书

在 Hugo站点的public目录中创建一个 git 子模块，之后这个目录将以 `https://github.com/<USERNAME>/<USERNAME>.github.io.git` 作为远程仓库（提示：<USERNAME>替换为你在Github的用户名）

```

git submodule add -b main [https://github.com/](https://github.com/)<USERNAME>/<USERNAME>.github.io.git public

```

将Hugo站点的静态内容推送到Github Pages

```

git add .
git commit -m "<你想写的提交说明>"
git push origin main

````

如果你很快完成了以上步骤，可以试试其他Hugo模板，或者美化修改一下当前模板。（提示：实践3-开源项目建设，可以选择开发一个简单的Hugo模板作为题目）

---

## 参考教程

### 本作业中用到的软件

#### Hugo

- [Hugo](https://gohugo.io/)  最受欢迎的开源静态站点生成器之一。
- [快速开始](https://gohugo.io/getting-started/quick-start/)
- [Github部署](https://gohugo.io/hosting-and-deployment/hosting-on-github/)

#### Git

- [Git](https://git-scm.com/)
- [Git教程 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/896043488029600)

#### Github Pages

- [Github Pages](https://pages.github.com/)  Github为用户提供的免费站点空间。

#### MarkDown

- [Markdown](https://daringfireball.net/projects/markdown/) 一种轻量级标记语言，它允许人们使用易读易写的纯文本格式编写文档。
- [Markdown基本语法 | Markdown官方教程](https://markdown.com.cn/basic-syntax/)

---

## 命令示例

```bash
$ hugo new site jane

Congratulations! Your new Hugo site is created in C:\Users\Zen\Documents\jane.

Just a few more steps and you're ready to go:

1. Download a theme into the same-named folder.
   Choose a theme from https://themes.gohugo.io/ or
   create your own with the "hugo new theme <THEMENAME>" command.
2. Perhaps you want to add some content. You can add single files
   with "hugo new <SECTIONNAME>\<FILENAME>.<FORMAT>".
3. Start the built-in live server via "hugo server".

Visit https://gohugo.io/ for quickstart guide and full documentation.

$ cd jane

$ git clone https://github.com/xianmin/hugo-theme-jane.git --depth=1 themes/jane
Cloning into 'themes/jane'...
remote: Enumerating objects: 221, done.
remote: Counting objects: 100% (221/221), done.
remote: Compressing objects: 100% (202/202), done.
remote: Total 221 (delta 13), reused 107 (delta 1), pack-reused 0
Receiving objects: 100% (221/221), 630.70 KiB | 1.85 MiB/s, done.
Resolving deltas: 100% (13/13), done.

$ cp -r themes/jane/exampleSite/content ./
$ cp themes/jane/exampleSite/config.toml ./

$ hugo new post/firstblog.md
Content "C:\\Users\\Zen\\Documents\\jane\\content\\post\\firstblog.md" created

$ vi content/post/firstblog.md

$ hugo server -D
Start building sites …
hugo v0.101.0-466fa43c16709b4483689930a4f9ac8add5c9f66 windows/amd64 BuildDate=2022-06-16T07:09:16Z VendorInfo=gohugoio

                   | EN
-------------------+-----
  Pages            | 85
  Paginator pages  |  7
  Non-page files   |  0
  Static files     | 19
  Processed images |  0
  Aliases          | 31
  Sitemaps         |  1
  Cleaned          |  0

Built in 113 ms
Watching for changes in C:\Users\Zen\Documents\jane\{archetypes,content,data,layouts,static,themes}
Watching for config changes in C:\Users\Zen\Documents\jane\config.toml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop

$ hugo -D
Start building sites …
hugo v0.101.0-466fa43c16709b4483689930a4f9ac8add5c9f66 windows/amd64 BuildDate=2022-06-16T07:09:16Z VendorInfo=gohugoio

                   | EN
-------------------+-----
  Pages            | 85
  Paginator pages  |  7
  Non-page files   |  0
  Static files     | 19
  Processed images |  0
  Aliases          | 31
  Sitemaps         |  1
  Cleaned          |  0

Total in 219 ms

$ cd public/
$ git init
Initialized empty Git repository in C:/Users/Zen/Documents/jane/public/.git/

$ git add .

$ git config --global user.name "xxx"
$ git config --global user.email "xxx@gmail.com"

$ ssh-keygen -t rsa -C "xxx@gmail.com"
Generating public/private rsa key pair.
Enter file in which to save the key (/c/Users/Zen/.ssh/id_rsa):
Created directory '/c/Users/Zen/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /c/Users/Zen/.ssh/id_rsa
Your public key has been saved in /c/Users/Zen/.ssh/id_rsa.pub

$ vi ~/.ssh/id_rsa.pub

$ ssh -T git@github.com
The authenticity of host 'github.com (::1)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? y
Please type 'yes', 'no' or the fingerprint: yes
Warning: Permanently added 'github.com' (ED25519) to the list of known hosts.
Hi xxx! You've successfully authenticated, but GitHub does not provide shell access.

$ git remote add origin https://github.com/Bistu-OSSDT-2022/Bistu-OSSDT-2022.github.io.git

$ git branch -M main

$ git commit -m 'first commit'

$ git push -u origin main

warning: ----------------- SECURITY WARNING ----------------
warning: | TLS certificate verification has been disabled! |
warning: ---------------------------------------------------
warning: HTTPS connections may not be secure. See https://aka.ms/gcm/tlsverify for more information.
warning: ----------------- SECURITY WARNING ----------------
warning: | TLS certificate verification has been disabled! |
warning: ---------------------------------------------------
warning: HTTPS connections may not be secure. See https://aka.ms/gcm/tlsverify for more information.
Enumerating objects: 275, done.
Counting objects: 100% (275/275), done.
Delta compression using up to 8 threads
Compressing objects: 100% (189/189), done.
Writing objects: 100% (275/275), 371.04 KiB | 4.88 MiB/s, done.
Total 275 (delta 107), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (107/107), done.
To https://github.com/Bistu-OSSDT-2022/ossdt2022.github.io.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
````

```
```
