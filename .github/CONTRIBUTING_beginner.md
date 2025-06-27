# 👋 Welcome! Contributing to BeLux Engineering Experience Repositories

Thank you for your interest in contributing! This guide is designed for **beginners** – even if you’ve never used Git or GitHub before. We’ll walk you through every step to help you succeed.

---

## 🧰 What You Need Before You Start

1. **A GitHub account** → [Sign up](https://github.com/join)
2. **Git** → [Install Git](https://git-scm.com/downloads)
3. **VS Code (Visual Studio Code)** → [Download here](https://code.visualstudio.com/)
4. (Optional) **Enable GitHub Copilot** → [https://aka.ms/copilot](https://aka.ms/copilot)

---

## 💻 First Time Setup on Your Laptop

1. Open VS Code
2. Open the Terminal (menu: View → Terminal)
3. Type the following to check if Git is installed:
   ```bash
   git --version
   ```

---

## 🚀 Step-by-Step: How to Contribute

### 1. Fork a Repository under the Belux Engineering Experience

- Go to: [https://github.com/BeLux-Engineering-Experience](https://github.com/BeLux-Engineering-Experience)
- Find a repository that you would like to contribute to.
- The link you click should bring you to the repository itself.
- Click the **“Fork”** button (top right) → this creates a copy under your account.

### 2. Clone It to Your Laptop

Open the terminal in VS Code and run:

```bash
git clone https://github.com/YOUR-USERNAME/BeLux-Engineering-Experience.git
cd BeLux-Engineering-Experience
```

### 3. Create a New Branch

```bash
git checkout -b my-first-contribution
```

### 4. Make Your Changes

Use VS Code to make edits (e.g. documentation, code, etc.).

### 5. Save and Commit Changes

```bash
git add .
git commit -m "My first contribution: updated docs"
```

### 6. Push Your Branch to GitHub

```bash
git push origin my-first-contribution
```

### 7. Open a Pull Request

- Go to your GitHub repo
- Click **“Compare & Pull Request”**
- Describe what you changed and click **“Create Pull Request”**

---

## ✅ Good Practices

- ✅ Keep your repo **public** (not private)
- ✅ Enable **[Secret Scanning](https://docs.github.com/en/code-security/secret-scanning)**
- ✅ Prefer using the **MIT License**
- ✅ Test your code if possible

---

## 🧠 Resources to Learn

- [Git and GitHub for Beginners](https://www.youtube.com/watch?v=RGOj5yH7evk) 📺 By freeCodeCamp – best 1-hour walkthrough for visual learners. 😉
- [GitHub Glossary](https://docs.github.com/en/get-started/quickstart/github-glossary)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [GitHub Copilot](https://aka.ms/copilot)

---

## 🌟 Example GitHub Repositories

These projects are known for their clean structure, CONTRIBUTING guidelines, and community onboarding:

- [First Contributions GitHub Repository](https://github.com/firstcontributions/first-contributions)
  🎓 Best repo for teaching how to make your first PR!
  Includes a full tutorial and simulated workflow.

## ❓ Need Help?

Open an issue in the repo or tag a maintainer. We're here to support you.

---

### 🤖 Using GitHub Copilot

GitHub Copilot is an AI pair programmer that helps you write code faster and with fewer errors.

#### 🔗 Enable Copilot at Microsoft
1. Go to: [https://aka.ms/copilot](https://aka.ms/copilot)
2. Sign in with your Microsoft account.
3. It should be enabled for your Enterprise Managed User (EMU) account.
4. Enable Copilot for your personal account by linking it.
5. Join the MicrosoftCopilot GitHub organization that grants your personal GitHub account GitHub Copilot access.
6. Accept the invitation
   
![image](https://github.com/user-attachments/assets/a4061071-b612-4aed-a114-3ef2a08705fb)
![image](https://github.com/user-attachments/assets/bffba021-ccd2-494e-a32d-afa1b48a4d8b)
8. 🥳 Welcome to Copilot

![image](https://github.com/user-attachments/assets/9a9325f1-0826-4c5f-97fa-fca8bfa6ff94)


#### 💻 Set Up in VS Code
1. Open **Visual Studio Code**
2. Go to **Extensions** (left menu)
3. Search for **GitHub Copilot**
4. Click **Install**
5. Sign in with GitHub when prompted

#### ✨ How to Use
- Start typing a comment or function, and Copilot will suggest code
- Press `Tab` to accept a suggestion
- Use `Ctrl + Enter` (Windows/Linux) or `Cmd + Enter` (Mac) to open Copilot panel for more options

#### 🧠 Examples
```python
# Suggest a function to reverse a string
def
```
Copilot will auto-suggest:
```python
def reverse_string(s):
    return s[::-1]
```

#### 🛠 Resources
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [Copilot Labs for advanced features](https://githubnext.com/projects/copilot-labs/)

🎉 **You're ready to contribute!**
