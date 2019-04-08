# Python

在vs中每次更新代码都会要输入账号密码
git config --global credential.helper store   //在Git Bash输入这个命令就可以了


只拉取最新的一次(拉取默认分支)
git clone --depth=1 github.com/xxxxx

拉取指定分支
$ git remote set-branches origin 'remote_branch_name'
$ git fetch --depth 1 origin remote_branch_name
$ git checkout remote_branch_name