************
Git常用命令
************

.. metadata::
   Chen Longhao
   2020,07,23

1.常用单个命令
---------------

============================= ===================================================================
    命令                        用途
============================= ===================================================================
 git add 文件名                 添加文件到暂存区
 git branch                     显示本地仓库中存在的分支
 git checkout -b 分支名         创建并切换分支（不加 ``-b`` ，则切换到已存在的分支）
 git clone 仓库url              从服务器上clone一个仓库
 git diff                       查看工作树与暂存区的差别
 git diff HEAD                  查看工作树与最新提交的差别
 git commit                     提交暂存区的文件至仓库
 git merge 分支名               合并分支到当前分支
 git init                       初始化一个仓库
 git log                        查看提交历史
 git log --graph                以图表形式查看分支
 git push                       推送本地仓库到远程仓库
 git pull                       从远程仓库拉取
 git rebase -i 哈希值           交互式变基
 git reset --hard 哈希值        将工作树，暂存区，版本库恢复到指定时间点
 git reset --soft 哈希值        将版本库恢复到指定时间点
 git reset --mixed 哈希值       将暂存区，版本库恢复到指定时间点
 git status                     查看仓库状态
============================= ===================================================================

2.常用组合命令
----------------

.. warning::
    命令需要根据实际情况修改，否则可能会造成严重后果！

合并服务器上无关的历史：

.. code-block::

    git fetch --all     #下载版本库到本地
    git reset --hard origin/master  #把HEAD指向下载的版本库

删除历史，只留下最新的干净的代码：

.. code-block::

    git checkout --orphan latest_branch
    git add -A
    git commit  #最新的提交
    git branch -D master
    git branch -m master
    git push -f origin master

统计版本库中当前代码量：

.. code-block::

    git log --pretty=tformat: --numstat | awk '{ adds += $1; subs += $2; loc += $1 - $2 } END {printf "added lines: %s, removed lines: %s, total lines: %s\n", adds, subs, loc }' -

