# Python


## whl for windows
    - https://www.lfd.uci.edu/~gohlke/pythonlibs/


## VS中每次更新代码都会要输入账号密码
```git
git config --global credential.helper store   //在Git Bash输入这个命令就可以了
```

## 只拉取最新的一次(拉取默认分支)
```git
git clone --depth=1 github.com/xxxxx
```

## 拉取指定分支
```git
$ git remote set-branches origin 'remote_branch_name'
$ git fetch --depth 1 origin remote_branch_name
$ git checkout remote_branch_name
```
