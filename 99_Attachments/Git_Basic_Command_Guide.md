# Git基本命令速查

_在仓库根目录运行命令。把示例中的文件名、分支名和提交编号替换成自己的内容；路径含空格时使用英文双引号。_

---

## 🚀 首次使用

设置提交者信息：

```powershell
git config --global user.name "你的名字"   # 设置以后写入提交记录的姓名
git config --global user.email "你的邮箱"  # 设置以后写入提交记录的邮箱
```

下载已有仓库：

```powershell
git clone <仓库地址>  # 把远程仓库下载到本地
cd "仓库目录"        # 进入刚下载的仓库目录
```

在当前目录建立新仓库：

```powershell
git init
```

## 🔍 查看当前情况

```powershell
git status            # 查看当前分支、已修改、已暂存和未跟踪文件
git status --short    # 用简短符号显示文件状态
git diff              # 查看尚未暂存的具体修改
git diff --staged     # 查看已经暂存、准备提交的具体修改
git log --oneline -10 # 查看最近10次提交的编号和说明
git show <提交编号>   # 查看某一次提交改了什么
```

只查看某个文件：

```powershell
git diff -- "路径/文件.md"        # 只查看这个文件尚未暂存的修改
git log --oneline -- "路径/文件.md" # 只查看与这个文件有关的提交历史
```

`git status --short`常见符号：

- `M`：文件已修改
- `A`：文件已加入版本记录
- `D`：文件已删除
- `??`：未跟踪的新文件

`git diff`表示查看差异。默认比较“工作区文件”和“已暂存内容”；加`--staged`后，比较“已暂存内容”和“最近一次提交”。输出中：

- `---`和`+++`：旧文件与新文件
- `@@`：下面差异所在的行号范围
- 行首`-`：原内容中被删除的行
- 行首`+`：新内容中增加的行
- 没有`+`或`-`：用于理解位置的上下文行

## ✅ 暂存与提交

暂存指定文件：

```powershell
git add -- "路径/文件1.md" "路径/文件2.md"
```

逐块选择要暂存的改动：

```powershell
git add -p
```

暂存当前目录全部改动：

```powershell
git add -A
```

提交前检查，然后提交：

```powershell
git status                    # 确认哪些文件已暂存、哪些尚未暂存
git diff --staged             # 逐行检查真正准备提交的内容
git commit -m "说明本次修改" # 把已暂存内容提交，并写入说明
```

修改最近一次提交说明：

```powershell
git commit --amend -m "新的提交说明"
```

最近一次提交已经推送时，不要直接使用`--amend`。

## ↩️ 撤销尚未提交的操作

取消暂存，但保留文件修改：

```powershell
git restore --staged -- "路径/文件.md"
```

丢弃某个文件尚未提交的修改：

```powershell
git restore -- "路径/文件.md"
```

恢复所有已跟踪文件的未提交修改：

```powershell
git restore --worktree -- .
```

以上两个丢弃修改的命令会覆盖未提交内容。运行前先执行`git diff`并确认目标。

恢复误删但尚未提交的已跟踪文件：

```powershell
git restore -- "路径/文件.md"
```

## ⏪ 回退已经提交的内容

撤销一个已提交或已推送的提交，并生成新的撤销提交：

```powershell
git log --oneline -10  # 找到需要撤销的提交编号
git revert <提交编号>  # 生成一个新提交，抵消指定提交的改动
```

把某个文件恢复为上一个提交中的版本，然后重新提交：

```powershell
git restore --source=HEAD~1 -- "路径/文件.md" # 取出上一次提交中的文件版本
git diff -- "路径/文件.md"                    # 检查恢复后将发生哪些变化
git add -- "路径/文件.md"                     # 暂存确认过的恢复结果
git commit -m "恢复文件的上一版本"            # 把恢复结果保存为新提交
```

把某个文件恢复为指定提交中的版本：

```powershell
git restore --source=<提交编号> -- "路径/文件.md"
```

撤销最近一次未推送的提交，但保留修改并保持暂存：

```powershell
git reset --soft HEAD~1
```

撤销最近一次未推送的提交，保留修改但取消暂存：

```powershell
git reset HEAD~1
```

彻底丢弃最近一次未推送的提交和对应修改：

```powershell
git reset --hard HEAD~1
```

`git reset --hard`会直接丢失工作区内容。仅在确认提交没有推送、目标正确且修改不需要保留时使用。

## 🛟 找回误操作前的提交

查看本地操作记录：

```powershell
git reflog
```

先创建恢复分支保留目标提交：

```powershell
git switch -c recovery/<名称> <提交编号>
```

只恢复目标提交中的某个文件：

```powershell
git restore --source=<提交编号> -- "路径/文件.md"
```

## 🌿 分支操作

```powershell
git branch                      # 列出本地分支，星号表示当前分支
git switch -c <新分支名>        # 创建新分支并立即切换过去
git switch <已有分支名>         # 切换到已经存在的分支
git merge <要合并的分支名>      # 把指定分支的改动合入当前分支
git branch -d <已合并的分支名>  # 删除已经合并完成的本地分支
```

切换分支前先执行：

```powershell
git status
```

## 📦 临时保存未提交修改

保存已跟踪文件和未跟踪文件：

```powershell
git stash push -u -m "临时保存说明"
```

查看、恢复或删除临时保存：

```powershell
git stash list               # 查看所有临时保存记录及编号
git stash apply "stash@{0}" # 恢复指定记录，但暂时保留该记录
git stash drop "stash@{0}"  # 确认恢复正确后删除该临时记录
```

确认恢复成功后再执行`drop`。

## ☁️ 远程同步

```powershell
git remote -v              # 查看远程仓库名称和地址
git fetch origin           # 下载远程最新记录，但不改当前工作文件
git pull --ff-only         # 只在能够直接快进时更新当前本地分支
git push origin <分支名>   # 把指定本地分支推送到origin
```

第一次推送新分支：

```powershell
git push -u origin <分支名>
```

推送前检查：

```powershell
git status                                  # 确认工作区状态和当前分支
git log --oneline origin/<分支名>..HEAD     # 查看本地有而远程还没有的提交
```

## 🧩 命令中常见写法

- `diff`：difference的缩写，用来查看修改前后的差异。
- `status`：查看仓库现在的状态，不修改文件。
- `log`：查看提交记录。
- `add`：把指定修改放入下一次提交范围。
- `commit`：保存已经暂存的修改。
- `staged`：已经执行过`git add`、准备提交的状态。
- `HEAD`：当前所在分支的最近一次提交。
- `HEAD~1`：当前提交的前一次提交；`HEAD~2`表示再往前两次。
- `origin`：远程仓库常用的默认名称。
- `restore`：恢复文件或取消暂存，主要处理文件内容。
- `revert`：用一个新提交抵消旧提交，适合已经推送的历史。
- `reset`：移动本地提交位置；不同参数决定是否保留文件修改。
- `--staged`：操作或查看已经暂存的内容。
- `--soft`：回退提交时保留修改，并保持暂存。
- `--hard`：回退提交并丢弃对应修改，使用前必须确认。
- `-m`：后面直接填写说明文字。
- `-u`：在对应命令中包含未跟踪文件；在`git push -u`中则记录默认远程分支。
- `--`：表示后面的内容是文件路径，避免路径被误认为命令参数。
- `<提交编号>`、`<分支名>`：占位符，运行时要连同尖括号一起替换掉。

## 🧭 本项目推荐操作顺序

```powershell
git status --short                         # 查看这次有哪些文件发生变化
git diff                                   # 检查尚未暂存的具体修改
git add -- "本次要提交的文件"              # 只暂存属于本次任务的文件
git diff --staged                          # 检查即将提交的最终内容
git commit -m "准确描述本次唯一任务"       # 保存暂存内容并写入提交说明
git status                                 # 确认提交后是否还留下其他改动
```

需要回退时，先按顺序执行：

```powershell
git status             # 确认未提交内容，避免回退时覆盖它们
git diff               # 查看这些未提交内容是否需要先保存
git log --oneline -10  # 找到准确的目标提交编号
```

然后根据情况选择`git restore`、`git revert`或仅限未推送提交的`git reset`。不要在没有确认文件和提交编号时直接运行清理、强制推送或`reset --hard`。
