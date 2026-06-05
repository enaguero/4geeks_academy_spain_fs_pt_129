[🇪🇸 Español](index.md) | 🇬🇧 **English**

# Day 05: Git - Version Control

## Why Git Is Essential

Git is the most popular version control system in the world. Imagine you're writing an important document and:

- You want to save different versions without creating copies like `final_project.doc`, `final_project_v2.doc`, `final_project_REAL.doc`
- You need to work with other people without overwriting their work
- You want to be able to go back if something goes wrong
- You want to keep a complete history of every change

**Git does all of this automatically**. It's like having a time machine for your code.

### Key Benefits

1. **Complete history**: Every change is recorded with who, when, and why
2. **Teamwork**: Multiple people can work simultaneously
3. **Safe experimentation**: Try ideas without fear of breaking the project
4. **Automatic backup**: Your code is safe in the cloud (GitHub)
5. **Industry standard**: Every tech company uses Git

---

## Repository Architecture

A **repository** (or "repo") is like a special folder that Git watches over. Inside this folder, Git keeps a complete history of every change.

### Basic Structure

```
my-project/
├── .git/               ← Hidden folder where Git stores everything
├── index.html
├── style.css
└── script.js
```

The `.git/` folder contains:
- All commits (saved versions)
- The branches
- The repository configuration
- References to remote repositories

**Important**: Never manually modify the contents of `.git/`

---

## Commit Objects

A **commit** is a snapshot of your project at a specific moment. Each commit contains:

```
Commit #abc123
├── Message: "Add contact form"
├── Author: Erwin Aguero <erwin@example.com>
├── Date: 2025-12-15 16:30:00
├── Modified files:
│   ├── index.html (+ 25 lines)
│   └── style.css (+ 10 lines)
└── Parent: Commit #def456
```

### Commit Characteristics

- **Immutable**: Once created, it cannot be changed
- **Unique**: It has a unique identifier (SHA hash)
- **Connected**: It points to the previous commit (its "parent")
- **Descriptive**: It has an explanatory message

---

## Head: The Tip of the List

**HEAD** is a pointer that indicates where you are right now in the history. It usually points to the latest commit on the current branch.

```
[Commit 1] → [Commit 2] → [Commit 3] ← HEAD
```

When you make a new commit, HEAD moves automatically:

```
[Commit 1] → [Commit 2] → [Commit 3] → [Commit 4] ← HEAD
```

---

## Branches: Multiple Lines of Development

A **branch** is simply a line of commits. You can have several branches to work on different features simultaneously.

### Branch Visualization

```
                    main
                     ↓
[A] → [B] → [C] → [D] ← HEAD
             ↓
             [E] → [F]
                    ↓
                  feature-login
```

- `main`: The main branch (previously called `master`)
- `feature-login`: A branch for developing the login
- Both share history up to commit [B]

---

## Starting a Repository: git init

To create a new repository:

```bash
# Create a folder for your project
mkdir my-first-project
cd my-first-project

# Initialize Git
git init
```

This creates the `.git/` folder and turns your folder into a repository.

### Check the Status

```bash
git status
```

This command shows you:
- Which branch you're on
- Which files have changed
- What's ready to be saved (commit)

---

## Saving Changes: The Commit Process

Git uses an intermediate area called the **staging area** (or index). It's like packing boxes before shipping them.

### The Three States of a File

1. **Working Directory**: Where you edit files
2. **Staging Area**: Changes marked for the next commit
3. **Repository**: Commits saved permanently

### Complete Flow

```bash
# 1. Create a file
echo "# My Project" > README.md

# 2. Check the status (untracked file)
git status

# 3. Add to staging area
git add README.md

# 4. Verify it's ready
git status

# 5. Create the commit
git commit -m "Add initial README"

# 6. View the history
git log
```

### Important Commands

```bash
# Add a specific file
git add index.html

# Add all modified files
git add .

# See what changed in the files
git diff

# See what's in staging
git diff --staged

# Make commit with message
git commit -m "Your descriptive message here"
```

**Tips for Commit Messages**:
- Use present tense: "Add" not "Added"
- Be descriptive but concise: "Add validation to contact form"
- Don't use periods at the end
- Good examples: "Fix bug in price calculation", "Improve responsive design of header"

---

## Referencing a Commit

There are several ways to refer to a commit:

### By Hash (SHA)

```bash
# Full hash
git show abc123def456789...

# Short hash (first 7 characters)
git show abc123d
```

### By Relative Reference

```bash
# The latest commit
HEAD

# One commit before HEAD
HEAD~1

# Two commits before
HEAD~2

# The direct parent commit
HEAD^
```

### By Branch

```bash
# The latest commit on main
main

# The latest commit on feature-login
feature-login
```

---

## Creating a Branch

Branches let you experiment without affecting the main code.

```bash
# Create a new branch
git branch feature-menu

# View all branches
git branch

# Create and switch to a branch in one command
git checkout -b feature-footer
```

### When to Create Branches

- For every new feature
- To fix bugs
- To experiment with ideas
- To work on something without affecting `main`

---

## Switching Between Branches

```bash
# Switch to an existing branch
git checkout main
git checkout feature-menu

# Modern form (Git 2.23+)
git switch main
git switch feature-menu
```

**Important**: Before switching branches, make sure to:
1. Commit your changes, or
2. Save them temporarily with `git stash`

---

## Merging Branches: Merge

When you finish work on a branch, you can **merge** it with another.

### Practical Example

```bash
# You're on feature-login and finished the work
git checkout main          # Switch to main
git merge feature-login    # Merge feature-login into main
```

### Types of Merge

**1. Fast-Forward**:
```
Before:
main:    [A] → [B]
                ↓
feature:        [C] → [D]

After:
main:    [A] → [B] → [C] → [D]
```

**2. Merge Commit**:
```
Before:
main:    [A] → [B] → [C]
                ↓
feature:        [D] → [E]

After:
main:    [A] → [B] → [C] → [F (merge)]
                ↓           ↗
feature:        [D] → [E] ─┘
```

---

## Resolving Conflicts

A **conflict** happens when two branches modify the same line of code.

### Conflict Example

You have this file on `main`:
```html
<h1>Welcome to my site</h1>
```

And on `feature-header`:
```html
<h1>Welcome to my web page</h1>
```

When merging, Git doesn't know which version to use:

```html
<<<<<<< HEAD
<h1>Welcome to my site</h1>
=======
<h1>Welcome to my web page</h1>
>>>>>>> feature-header
```

### Resolving the Conflict

```bash
# 1. Git warns you about the conflict
git merge feature-header
# Auto-merging index.html
# CONFLICT (content): Merge conflict in index.html

# 2. Open the file and choose what to keep
# Edit manually to leave:
<h1>Welcome to my web page</h1>

# 3. Mark as resolved
git add index.html

# 4. Complete the merge
git commit -m "Resolve conflict in header title"
```

### Tips to Avoid Conflicts

- Make frequent, small commits
- Communicate with the team about which files you're modifying
- Update your branch regularly with `git pull`
- Don't have everyone work on the same files at the same time

---

## Collaboration with Git

Git shines when you work as a team. The **distributed version control** model lets each person have a complete copy of the repository.

### Centralized vs Distributed Version Control

**Centralized** (old):
```
        Central Server
              ↓
    ┌─────────┼─────────┐
  User 1    User 2    User 3
```
- Single point of failure
- Requires constant connection

**Distributed** (Git):
```
    Local Repo 1 ←→ GitHub ←→ Local Repo 2
                      ↕
                 Local Repo 3
```
- Each person has the full history
- Works offline
- Multiple natural backups

---

## Specifying Remotes

A **remote** is a version of your repository hosted on the internet (typically on GitHub, GitLab, or Bitbucket).

### View Remotes

```bash
# List remotes
git remote -v

# Typical result:
# origin  https://github.com/user/project.git (fetch)
# origin  https://github.com/user/project.git (push)
```

**origin**: It's the default name for the main remote.

---

## GitHub.com: Your Repository in the Cloud

**GitHub** is a platform that hosts Git repositories and adds:

- **Collaboration**: Pull requests, issues, projects
- **Visualization**: Web interface to explore code
- **CI/CD**: Automation with GitHub Actions
- **Community**: Millions of open source projects
- **Portfolio**: Your profile showcases your work

### Create a Repository on GitHub

1. Go to https://github.com
2. Click the "+" button in the top right
3. Select "New repository"
4. Give it a name: `my-first-project`
5. Choose public or private
6. **DO NOT** check "Initialize with README" (you already have one locally)
7. Click "Create repository"

---

## Adding a Remote

After creating the repo on GitHub:

```bash
# Add the remote
git remote add origin https://github.com/your-user/my-first-project.git

# Verify
git remote -v
```

---

## Uploading Changes: git push

**Push** = "push" your local commits to the remote repository.

```bash
# First time (establishes connection)
git push -u origin main

# After that, simply:
git push
```

### What Push Does

```
YOUR COMPUTER                     GITHUB
     main                          main
      ↓                             ↓
[A] → [B] → [C] → [D]  ────push───→ [A] → [B] → [C] → [D]
```

---

## Downloading Changes: git pull

**Pull** = "pull" changes from the remote into your local repository.

```bash
# Download and merge changes
git pull

# Equivalent to:
# git fetch (download)
# git merge (merge)
```

### What Pull Does

```
YOUR COMPUTER                     GITHUB
     main                          main
      ↓                             ↓
[A] → [B] → [C]  ←────pull──── [A] → [B] → [C] → [D] → [E]
```

After the pull, your local will have [D] and [E] too.

---

## Cloning a Repository: git clone

**Clone** creates a complete copy of a remote repository onto your computer.

```bash
# Clone a repository
git clone https://github.com/user/project.git

# Clone with a different name
git clone https://github.com/user/project.git my-local-copy
```

### When to Use Clone

- Joining an existing project
- Copying open source projects
- Working on a new computer
- Collaborating with a teammate

---

## Teamwork Timeline: Practical Example

### Scenario: Building a Landing Page

**Team**: Ana (front-end designer) and Carlos (developer)

**Project**: Build a landing page for a coffee shop

**Goal**: Ana works on design/styles, Carlos on the contact form functionality

### Initial Setup (Day 1 - Monday)

**Carlos** (project lead):

```bash
# 1. Create the project locally
mkdir cafeteria-landing
cd cafeteria-landing
git init

# 2. Create basic structure
echo "# La Esquina Coffee Shop Landing" > README.md
mkdir css js
touch index.html css/style.css js/app.js

# 3. Make initial commit
git add .
git commit -m "Initialize project with basic structure"

# 4. Create repo on GitHub and push it
git remote add origin https://github.com/carlos/cafeteria-landing.git
git push -u origin main
```

**Ana** (joins the project):

```bash
# 1. Clone the repository
git clone https://github.com/carlos/cafeteria-landing.git
cd cafeteria-landing

# 2. Verify everything is fine
git log
git branch
```

---

### Parallel Development (Day 2 - Tuesday)

**Ana** works on the design:

```bash
# 1. Create branch for her work
git checkout -b feature-diseno-header

# 2. Work on index.html and style.css
# (Add header HTML with logo and navigation)
# (Add styles for the header)

# 3. Make frequent commits
git add index.html css/style.css
git commit -m "Add header HTML structure"

# 4. Keep working
# (Add more styles)
git add css/style.css
git commit -m "Style header with brand colors"

# 5. Push her branch to GitHub
git push -u origin feature-diseno-header
```

**Carlos** works on the form (at the same time):

```bash
# 1. Create his own branch
git checkout -b feature-formulario-contacto

# 2. Work on the form
# (Add form HTML in index.html)
# (Add validation in js/app.js)

# 3. Make commits
git add index.html js/app.js
git commit -m "Add contact form with validation"

# 4. Push his branch
git push -u origin feature-formulario-contacto
```

**State on GitHub**:
```
main:                     [A: initial commit]
                               ↓
feature-diseno-header:         [B] → [C]
                               ↓
feature-formulario-contacto:   [D]
```

---

### Integration (Day 3 - Wednesday Morning)

**Ana** finishes first and opens a **Pull Request** on GitHub:

1. Goes to GitHub.com
2. Clicks "Pull requests" → "New pull request"
3. Base: `main` ← Compare: `feature-diseno-header`
4. Title: "Add header design"
5. Description: "Header with logo, navigation, and brand styles"
6. Clicks "Create pull request"

**Carlos** reviews Ana's code:

1. Sees the Pull Request on GitHub
2. Reviews the changes line by line
3. Leaves a comment: "Looks great! Just one detail: could you increase the header padding on mobile?"
4. Ana makes the adjustment:

```bash
# Ana is still on her branch
git checkout feature-diseno-header

# Makes the requested change
# (Edits style.css)

git add css/style.css
git commit -m "Increase header padding on mobile"
git push
```

**Carlos** approves and merges:

1. On GitHub, clicks "Approve"
2. Clicks "Merge pull request"
3. Clicks "Confirm merge"
4. Ana's work is now on `main`

---

### Local Update (Wednesday Afternoon)

**Carlos** needs to update his local copy:

```bash
# 1. Return to main
git checkout main

# 2. Download changes Ana pushed
git pull

# Now Carlos has Ana's header on his local main
```

**Ana** can delete her branch:

```bash
# Return to main
git checkout main

# Download changes (already includes her merged work)
git pull

# Delete local branch (no longer needed)
git branch -d feature-diseno-header

# Delete remote branch
git push origin --delete feature-diseno-header
```

---

### Continuing the Work (Thursday)

**Carlos** continues with his form:

```bash
# 1. Return to his branch
git checkout feature-formulario-contacto

# 2. IMPORTANT: Update his branch with main's changes
git merge main

# This brings Ana's header into his branch
```

If there are conflicts (both edited the same line of `index.html`):

```bash
# Git marks the conflict
# CONFLICT (content): Merge conflict in index.html

# Carlos opens index.html and sees:
<<<<<<< HEAD
    <div class="formulario">
=======
    <header class="header">
>>>>>>> main

# Carlos resolves manually, keeping both sections:
    <header class="header">
        <!-- Ana's header code -->
    </header>
    <div class="formulario">
        <!-- Carlos's form code -->
    </div>

# Mark as resolved
git add index.html
git commit -m "Merge main into feature-formulario-contacto"

# Push changes
git push
```

---

### Finalization (Friday)

**Carlos** opens a Pull Request for his form:

1. On GitHub: Pull Request from `feature-formulario-contacto` to `main`
2. Ana reviews and approves
3. Carlos merges

**Both update main**:

```bash
git checkout main
git pull
```

**Final state**:
```
main: [A] → [B] → [C] → [merge Ana] → [D] → [merge Carlos]
```

---

### Full Timeline Summary

| Day | Time | Who | Action | Command |
|-----|------|-----|--------|---------|
| Mon | 10:00 | Carlos | Creates repo and pushes to GitHub | `git init`, `git push` |
| Mon | 11:00 | Ana | Clones the project | `git clone` |
| Tue | 09:00 | Ana | Creates design branch | `git checkout -b feature-diseno-header` |
| Tue | 09:00 | Carlos | Creates form branch | `git checkout -b feature-formulario-contacto` |
| Tue | 12:00 | Ana | Pushes changes | `git push` |
| Tue | 15:00 | Carlos | Pushes changes | `git push` |
| Wed | 09:00 | Ana | Opens Pull Request | (On GitHub) |
| Wed | 10:00 | Carlos | Reviews and requests changes | (On GitHub) |
| Wed | 11:00 | Ana | Fixes and pushes | `git commit`, `git push` |
| Wed | 12:00 | Carlos | Approves and merges | (On GitHub) |
| Wed | 14:00 | Carlos | Updates his local main | `git pull` |
| Thu | 09:00 | Carlos | Updates his branch with main | `git merge main` |
| Thu | 09:30 | Carlos | Resolves conflicts | `git add`, `git commit` |
| Fri | 10:00 | Carlos | Final Pull Request | (On GitHub) |
| Fri | 11:00 | Ana | Reviews and approves | (On GitHub) |
| Fri | 12:00 | Both | Update main | `git pull` |

---

## Most Important Git Commands (Cheat Sheet)

### Initial Configuration

```bash
git config --global user.name "Your Name"
git config --global user.email "you@email.com"
```

### Basics

```bash
git init                          # Initialize repository
git status                        # View status
git add file.html                 # Add file
git add .                         # Add all files
git commit -m "Message"           # Create commit
git log                           # View history
git log --oneline                 # Compact history
```

### Branches

```bash
git branch                        # List branches
git branch branch-name            # Create branch
git checkout branch-name          # Switch to branch
git checkout -b branch-name       # Create and switch
git merge branch-name             # Merge branch
git branch -d branch-name         # Delete local branch
```

### Remotes

```bash
git remote add origin URL         # Add remote
git remote -v                     # View remotes
git push -u origin main           # Push for the first time
git push                          # Push changes
git pull                          # Pull changes
git clone URL                     # Clone repository
```

### Useful

```bash
git diff                          # See unstaged changes
git diff --staged                 # See staged changes
git restore file.html             # Discard changes
git restore --staged file.html    # Unstage file
git stash                         # Save changes temporarily
git stash pop                     # Restore saved changes
```

---

## Practical Exercises

### Exercise 1: Your First Repository

1. Create a folder called `portfolio`
2. Initialize Git
3. Create `index.html` with your name
4. Commit the changes
5. Create a GitHub account
6. Create a repository on GitHub called `portfolio`
7. Connect your local repo with GitHub
8. Push your changes

### Exercise 2: Working with Branches

1. In your `portfolio` project, create a branch `feature-about`
2. Add an "About me" section in the HTML
3. Make a commit
4. Switch back to `main`
5. Merge `feature-about` into `main`
6. Push the changes to GitHub

### Exercise 3: Collaboration (with a partner)

1. One of you creates a new repo on GitHub with a basic `index.html`
2. Add your partner as a collaborator (Settings → Collaborators)
3. The other one clones the repository
4. Each one creates their own branch and adds different content
5. Push your branches to GitHub
6. Open Pull Requests
7. Review each other's code
8. Merge the changes
9. Both update their local `main`

---

## Additional Resources

- **Official documentation**: https://git-scm.com/doc
- **GitHub Guides**: https://guides.github.com/
- **Git Visualizer**: https://git-school.github.io/visualizing-git/
- **Practice Git**: https://learngitbranching.js.org/

---

## Conclusion

Git is a powerful tool that:
- Protects you from losing work
- Makes team collaboration easier
- Is essential in the software industry
- Improves with practice

**Next steps**:
1. Practice the basic commands daily
2. Use Git in all your projects
3. Collaborate with others to learn the full workflow
4. Explore advanced features (rebase, cherry-pick, etc.)

Remember: Git seems complicated at first, but with practice it becomes natural!
