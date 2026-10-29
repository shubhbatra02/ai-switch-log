# Git Commands Cheat Sheet

Commands used so far in the ai-switch-log project, with what each one does.

## 1. Setup (one time)

| Command | What it does |
|---|---|
| `git --version` | Checks that Git is installed and shows its version. |
| `git config --global user.name "Your Name"` | Sets the name attached to your commits. |
| `git config --global user.email "you@example.com"` | Sets the email attached to your commits. Use the same email as your GitHub account. |
| `git config --list` | Shows all your Git settings, to confirm name and email saved. |
| `git clone <url>` | Copies a GitHub repo to your computer, history included. |

## 2. Daily workflow

| Command | What it does |
|---|---|
| `git status` | Shows which files are changed, staged, or untracked. Run it often. |
| `git add <file>` | Stages a file, meaning it is selected for the next commit. |
| `git add .` | Stages all changed files in the current folder. Check `git status` first so you don't stage secrets like `.env`. |
| `git commit -m "message"` | Saves a snapshot of the staged files with a short message. |
| `git push` | Uploads your commits to GitHub. |
| `git pull` | Downloads new commits from GitHub and merges them into your branch. |

(VS Code's "Sync Changes" button does a pull and a push together.)

## 3. Looking at history and changes

| Command | What it does |
|---|---|
| `git log --oneline` | Lists commits, one line each (short ID plus message). |
| `git log --oneline --graph --all` | Draws all branches as a tree. |
| `git diff` | Shows changes you have made but not yet staged, line by line. |
| `git diff main experiment` | Shows what differs between two branches. |
| `git show <commit>` | Shows what one commit changed. |
| `git ls-files` | Lists files Git is tracking. Useful to check a secret file is not tracked. |

## 4. Branches

| Command | What it does |
|---|---|
| `git branch` | Lists branches. The current one is marked with `*`. |
| `git switch -c <name>` | Creates a new branch and moves onto it. |
| `git switch <name>` | Moves to an existing branch. |
| `git merge <name>` | Brings the changes from branch `<name>` into the branch you are on. |
| `git branch -d <name>` | Deletes a branch label after it is merged. The commits stay in the history. |

## 5. Undoing things

| Situation | Command | What it does |
|---|---|---|
| Edited a file, not committed, want to discard | `git restore <file>` | Throws away your uncommitted edits to that file. Cannot be undone. |
| Staged a file by mistake | `git restore --staged <file>` | Unstages it but keeps your edits. |
| Committed (even pushed) something wrong | `git revert <commit>` | Creates a new commit that cancels the old one. Safe, history stays intact. |
| Want an old version of one file | `git restore --source=<commit> <file>` | Puts that file back as it was in the given commit. Then commit it. |
| Want to look at an old version without changing anything | `git show <commit>:<file>` | Prints the file as it was in that commit. |
| Local commit not pushed yet, want it gone | `git reset --hard <commit>` | Moves the branch back and **deletes** later work. Dangerous. Avoid on pushed commits. |

## 6. Keeping secrets out of Git

- Create a file named `.gitignore` in the repo root and list files to ignore, for example `.env`.
- Add the ignore rule **before** the first commit of that file. Ignoring a file that is already committed does not remove it from history.
- Check with `git status` that the file does not appear.

## 7. Handy habits

1. Run `git status` before every commit.
2. Write commit messages that say what changed, like `add employees CRUD functions`.
3. Commit small and often.
4. Never commit passwords, keys, or `.env` files.
5. Try risky changes on a branch.
