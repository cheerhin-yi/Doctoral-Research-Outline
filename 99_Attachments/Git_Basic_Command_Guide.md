# Git基本命令速查

_在仓库根目录运行命令。把示例中的文件名、分支名和提交编号替换成自己的内容；路径含空格时使用英文双引号。_

---

## 🚀 首次使用

设置提交者信息：

```powershell
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

下载已有仓库：

```powershell
git clone <仓库地址>
cd "仓库目录"
```

在当前目录建立新仓库：

```powershell
git init
```

## 🔍 查看当前情况

```powershell
git status
git status --short
git diff
git diff --staged
git log --oneline -10
git show <提交编号>
```

只查看某个文件：

```powershell
git diff -- "路径/文件.md"
git log --oneline -- "路径/文件.md"
```

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
git status
git diff --staged
git commit -m "说明本次修改"
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
git log --oneline -10
git revert <提交编号>
```

把某个文件恢复为上一个提交中的版本，然后重新提交：

```powershell
git restore --source=HEAD~1 -- "路径/文件.md"
git diff -- "路径/文件.md"
git add -- "路径/文件.md"
git commit -m "恢复文件的上一版本"
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
git branch
git switch -c <新分支名>
git switch <已有分支名>
git merge <要合并的分支名>
git branch -d <已合并的分支名>
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
git stash list
git stash apply "stash@{0}"
git stash drop "stash@{0}"
```

确认恢复成功后再执行`drop`。

## ☁️ 远程同步

```powershell
git remote -v
git fetch origin
git pull --ff-only
git push origin <分支名>
```

第一次推送新分支：

```powershell
git push -u origin <分支名>
```

推送前检查：

```powershell
git status
git log --oneline origin/<分支名>..HEAD
```

## 🧭 本项目推荐操作顺序

```powershell
git status --short
git diff
git add -- "本次要提交的文件"
git diff --staged
git commit -m "准确描述本次唯一任务"
git status
```

需要回退时，先按顺序执行：

```powershell
git status
git diff
git log --oneline -10
```

然后根据情况选择`git restore`、`git revert`或仅限未推送提交的`git reset`。不要在没有确认文件和提交编号时直接运行清理、强制推送或`reset --hard`。
