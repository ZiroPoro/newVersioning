# Git Commands Cheat Sheet

This document contains useful Git commands for working with Git Flow and GitHub.

## Viewing Commit History

### View commit history with details

```bash
git log
```

### View commit history in one line per commit

```bash
git log --oneline
```

### View commit history with graph

```bash
git log --graph --oneline --all
```

### View commit history for specific file

```bash
git log -- filename
```

### View commit history with author and date

```bash
git log --pretty=format:"%h - %an, %ar : %s"
```

## Working with Branches

### List all branches

```bash
git branch
```

### List all branches (including remote)

```bash
git branch -a
```

### List only remote branches

```bash
git branch -r
```

### Create a new branch

```bash
git branch branch-name
```

### Switch to a branch

```bash
git checkout branch-name
```

### Create and switch to a new branch

```bash
git checkout -b branch-name
```

### Delete a local branch

```bash
git branch -d branch-name
```

### Force delete a local branch

```bash
git branch -D branch-name
```

### Delete a remote branch

```bash
git push origin --delete branch-name
```

## Working with Tags

### View tag history

```bash
git tag
```

### View tags with commit information

```bash
git tag -l -n
```

### View detailed tag information

```bash
git show tag-name
```

### Create a lightweight tag

```bash
git tag tag-name
```

### Create an annotated tag

```bash
git tag -a tag-name -m "Tag message"
```

### Push tags to remote

```bash
git push origin tag-name
```

### Push all tags to remote

```bash
git push origin --tags
```

### Delete a local tag

```bash
git tag -d tag-name
```

### Delete a remote tag

```bash
git push origin --delete tag-name
```

## Moving Files Between Branches

### Checkout a file from another branch

```bash
git checkout branch-name -- path/to/file
```

### Checkout multiple files from another branch

```bash
git checkout branch-name -- file1.txt file2.txt
```

### Cherry-pick a commit (moves changes from one branch to another)

```bash
git cherry-pick commit-hash
```

### Cherry-pick multiple commits

```bash
git cherry-pick commit-hash1 commit-hash2
```

### Cherry-pick a range of commits

```bash
git cherry-pick start-commit^..end-commit
```

## Git Flow Commands

### Initialize Git Flow

```bash
git flow init
```

### Start a feature branch

```bash
git flow feature start feature-name
```

### Finish a feature branch

```bash
git flow feature finish feature-name
```

### Start a hotfix branch

```bash
git flow hotfix start hotfix-name
```

### Finish a hotfix branch

```bash
git flow hotfix finish hotfix-name
```

## Merging and Pulling

### Merge a branch into current branch

```bash
git merge branch-name
```

### Merge with no fast-forward (creates merge commit)

```bash
git merge --no-ff branch-name
```

### Pull latest changes from remote

```bash
git pull origin branch-name
```

### Fetch changes without merging

```bash
git fetch origin
```

## Status and Information

### Check repository status

```bash
git status
```

### View differences

```bash
git diff
```

### View differences for staged files

```bash
git diff --staged
```

### View remote repositories

```bash
git remote -v
```

## Useful Tips

- Always check `git status` before committing
- Use `git log --oneline --graph --all` to visualize branch structure
- Use `git branch -a` to see all branches before switching
- Use `git tag` to see all tags before creating new ones
- When moving files between branches, make sure you're on the target branch first

