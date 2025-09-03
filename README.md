# deepqore-ai-research-log
This repository contains my personal notes, daily learnings, and hands-on experiments during my AI/ML Research Internship at DeepQore. It serves as a journal to track progress, document research insights, and practice implementations throughout the internship journey.”



Day 1:

# 📘 Understanding Git, Version Control, and GitHub  

## 🔹 What is Version Control?  
Imagine you are writing a school project with your friends. Everyone keeps editing the same file. Without any system, it becomes messy — someone overwrites your work, someone deletes a section, and nobody remembers who did what.  

That’s where **Version Control** comes in.  
- It keeps track of **who changed what and when**.  
- You can **go back** to older versions if something breaks.  
- It lets multiple people work on the same project without clashing.  

👉 Think of it like Google Docs for coding — but more powerful.  

---

## 🔹 What is Git?  
**Git** is a tool that makes version control possible.  

With Git:  
- You save your code in **snapshots (commits)**.  
- You can create **branches** to test new ideas without affecting the main project.  
- You can always **go back in time** if your code stops working.  

👉 Simply put: Git is like a **time machine for your code**.  

---

## 🔹 What is GitHub?  
Now, Git works on your computer. But what if you want to **share your code with others** or **store it safely online**?  

That’s where **GitHub** comes in.  
- It’s a website where you can **upload your Git projects**.  
- Lets you **collaborate with people** (through pull requests, issues, comments).  
- Used for both **open-source projects** (anyone can see) and **private projects** (only your team can see).  
- Makes your work visible to the world, like an **online portfolio** for developers.  

👉 Git = Tool  
👉 GitHub = Place to share and collaborate with Git  

---

## 🔹 Quick Comparison  

| Term | Simple Meaning |
|------|----------------|
| **Version Control** | Keeping track of changes in files |
| **Git** | The tool that does version control |
| **GitHub** | A website/platform to share Git projects and work with others |

---
# Git vs GitHub


| Feature               | Git                                         | GitHub                                      |
|-----------------------|--------------------------------------------|--------------------------------------------|
| **Type**              | Version Control System (VCS)               | Cloud-based platform for hosting Git repos |
| **Usage**             | Track changes in code, manage versions     | Share repositories, collaborate online    |
| **Installation**      | Installed locally on your computer         | No installation; web-based service        |
| **Internet Required** | Not required                               | Required for online collaboration          |
| **Collaboration**     | Branching, merging, pull, push (locally)  | Pull requests, issues, code reviews        |
| **Command Examples**  | `git init`, `git commit`, `git branch`     | `git push`, `git pull`, `fork`, `clone`   |
| **Ownership**         | Free and open-source                        | Owned by Microsoft                        |
| **Analogy**           | Personal notebook for tracking work        | Online library to share your notebook     |

## Quick Summary
- **Git** is your local tool for version control.  
- **GitHub** is an online platform to host and collaborate on Git repositories.  
- Together, they make managing and sharing code easy.  

![Git vs GitHub Diagram](https://github.com/user-attachments/assets/7c6f3c67-a792-4c08-9244-799f3d2e6bac)

# GitLab vs Bitbucket

This document explains GitLab and Bitbucket in a simple, easy-to-understand way and highlights their key differences.

---

## **1. GitLab**

- **What it is:** A platform to store Git repositories, collaborate with your team, and automate testing and deployment.  
- **Analogy:** GitLab is like a **smart workshop**. You store your tools (code), and the workshop can **check your work automatically, fix errors, and even assemble the final product**.  
- **Why use it:** Ideal for teams that want a **complete development workflow in one place** – code storage, collaboration, testing, and deployment.  
- **How it works:** You push your code → GitLab can automatically run tests → You can deploy the project directly from GitLab.

---

## **2. Bitbucket**

- **What it is:** A platform to store Git repositories and collaborate with your team, with simple automation features.  
- **Analogy:** Bitbucket is like an **organized locker room**. You store your tools (code) in lockers, and your team can check them out, make changes, and put them back.  
- **Why use it:** Best for teams using **Atlassian tools** like Jira or Trello.  
- **How it works:** You push your code → teammates review and merge changes → optional pipelines can automate small tasks.

---

## **Key Differences Between GitLab and Bitbucket**

| Feature                 | GitLab                                 | Bitbucket                               |
|-------------------------|----------------------------------------|----------------------------------------|
| **CI/CD (Automation)**  | Full built-in pipelines for testing & deployment | Basic pipelines for automation tasks  |
| **Hosting Options**     | Cloud-hosted or self-hosted             | Cloud-hosted or self-hosted             |
| **Best Use Case**       | Complete DevOps workflow in one place  | Teams using Atlassian tools like Jira/Trello |
| **Complexity**          | More advanced features for DevOps      | Simpler and easier to use               |
| **Analogy**             | Smart workshop (code + tests + deployment) | Organized locker room (store & share tools) |


 Version Control Tools: Git, GitHub, GitLab, Bitbucket

> **Note:** Git, GitHub, GitLab, and Bitbucket are all tools related to **Version Control Systems (VCS)**. They help developers track changes, collaborate on code, and manage projects efficiently.
# 🛠️ Git Undo & Restore Operations Interactive Guide

This interactive guide helps you quickly decide **which Git undo operation to use** in different scenarios.  


---




```
flowchart TD
    A[Have you made changes?] --> B{Are changes staged?}
    B -->|No| C[Use `git restore <file>` or `git restore .` to discard changes]
    B -->|Yes| D{Have you committed changes?}
    D -->|No| E[Use `git restore --staged <file>` to unstage changes]
    D -->|Yes| F{Have you pushed to remote?}
    F -->|No| G{Do you want to keep changes?}
    G -->|Yes| H[Undo last commit but keep staged: `git reset --soft HEAD~1`]
    G -->|No| I[Undo last commit and unstage: `git reset --mixed HEAD~1`]
    I --> J[Discard last commit completely: `git reset --hard HEAD~1`]
    F -->|Yes| K[Use `git revert <commit-hash>` to undo safely on remote]
    H --> L[Optional: Edit changes and recommit]

