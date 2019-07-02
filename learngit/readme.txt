cd D:/MyGit   定位到git库地址
git config --global user.name "Your Name" 设置用户名
git config --global user.email "email@example.com"  设置email

pwd  查询当前路径
mkdir projectname  新建文件夹，即版本库
cd projectname 定位到项目文件夹
git init    在当前路径下创建并初始化Git 仓库，存放该项目的所有数据
必须先将git add到暂存区，才能git commit到版本库中去
git add filename  提交新增/修改的文件到暂存区
git commit -m "explanation about what you add"  将刚添加/修改的文件从暂存区提交到分支库，并且清空暂存区
git status   查看仓库当前状态，如文件被修改等
git diff  显示文件修改的具体内容
git log  查看修改记录
cat filename  查看文件内容
git reflog 查看每次执行的命令
git checkout -- filename    让文件回到最近一次git commit或git add时的状态,丢弃工作去的修改
git reset HEAD filename    把暂存区的修改回退到工作区
回退版本：
HEAD代表当前版本  
git reset --hard HEAD^   回退到上一个版本
git reset --hard HEAD~100 会退到上100个版本
git reset --hard commit_id       回退/返回到对应版本(be68为commit id)
rm filename  删除工作区的文件
git rm filename 删除版本库中的文件
git checkout -- filename 使用版本库中的版本替换工作区的版本，即将版本库中的文件恢复到工作区中

***********************MyGit 工作区
***********************.git为版本库
一次修改的流程:Git add->将文件添加到版本库的暂存区--->Git commit提交到版本库的master分支

ssh-keygen -t rsa -C "email"   创建SSH可以
git remote add origin git@github.com:username/filename.git   将本地库关联到github的库相关联，需要在本地库路径下运行
git push -u origin master             将本地库的所有内容推送到远程库上去，首次指定默认服务器，需要添加-u
ssh -T git@github.com                                          git链接github
git clone git@github.com:username/projectname克隆远程库到本地库中
ls 查看当前路径下的文件夹



新建分支，并切换到分支
将工作区修改的内容更新到分支中区，此时master分支内容保持不变
在dev库更新完成，并确认无误后，切换到master分支，并合并dev分支，此时两者库会变成同步的状态
分支管理
git checkout -b dev    创建名为dev的分支(-b表示创建并切换)
= git branch dev  +  git checkout dev   创建分支dev + 切换分支

git branch 查看当前分支
git checkout master  切换为master分支，切换分支前确保已将工作区内容更新到git库中去
git log 显示 End时，输入CTRL+C or “：q”
git merge  --no-ff -m “explanation”  dev  
将指定的dev分支合并到当前分支(即master分支)中去，内容完成同步
git branch -d dev 删除dev分支
git branch -D dev 强行删除dev分支
git log --graph   可查看分支合并图
<<<<<<< HEAD
=======
git log --graph --pretty=oneline --abbrev-commit   查看分支合并图
>>>>>>> dev
branch test1 and test2
git stash 将当前工作现场“储藏起来”，后续恢复再继续，一般用在临时新建分支去解bug
git stash list 查看储存的工作现场
git stash pop = git stash apply + git stash drop 恢复并删除stash
<<<<<<< HEAD
git stash apply stash@{0} 选择指定的stash恢复
=======
git stash apply stash@{0} 选择指定的stash恢复

git remote 查看远程库
git remote -v 查看抓取和推送的origin的地址，如果没有推送权限，就看不到push的地址

多人协作的工作模式通常是这样：

    1.首先，可以试图用git push origin <branch-name>推送自己的修改；

    2.如果推送失败，则因为远程分支比你的本地更新，需要先用git pull试图合并；

    3.如果合并有冲突，则解决冲突，并在本地提交；

    4.没有冲突或者解决掉冲突后，再用git push origin <branch-name>推送就能成功！

如果git pull提示no tracking information，则说明本地分支和远程分支的链接关系没有创建，用命令git branch --set-upstream-to <branch-name> origin/<branch-name>。
>>>>>>> dev

git tag v1.0 在当前分支添加新标签
git tag 查看所有标签
git tag -d v1.0删除标签
git push origin v1.0推送标签到远程库
git push origin --tags  推送所有标签到远程库
git push origin :refs/tags/v1.0删除远程的标签
git show v1.0 查看标签的具体信息
git tag v1.1  commit_id 针对此次的commit添加tag
git tag -a v1.2 -m "version 1.2 released" commit_id添加带有说明的标签，-a指定标签名，-m指定说明文字

将本地推送到远程库中去
git push master  #推送到远程库的master主分支
git push dev     #推送到远程库的对应分支上


Gitee #码云
git remote add origin_gitee git@gitee.com:Arlen/python.git #git连接到码云的远程库
git push origin_gitee master