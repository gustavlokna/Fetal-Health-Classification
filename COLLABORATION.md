# 🤝 Collaboration Guide

Welcome to the Sensor Anomaly Detection project! This document outlines the conventions we follow for commits and issues to ensure a smooth and efficient workflow.

## 📜 Conventional Commits

We follow the Conventional Commits specification for our commit messages. This convention helps us maintain a clean and readable commit history. Here's how you should format your commit messages:

### Commit Message Format

Each commit message should include a type, a scope, and a subject:

```
<type>(<scope>): <subject>
```

### Types

- **feat**: A new feature for the user.
- **fix**: A bug fix.
- **docs**: Changes to the documentation.
- **style**: Code style changes (white-space, formatting, missing semi-colons, etc).
- **refactor**: A code change that neither fixes a bug nor adds a feature.
- **perf**: A code change that improves performance.
- **test**: Adding missing or correcting existing tests.
- **build**: Changes that affect the build system or external dependencies.
- **ci**: Changes to our CI configuration files and scripts.
- **chore**: Other changes that don't modify src or test files.
- **revert**: Reverts a previous commit.

### Scopes

The scope provides additional context about the commit. Use it to identify the part of the codebase the commit affects, such as:

- **data**
- **features**
- **models**
- **visualization**
- **docs**
- **tests**

### Examples

Here are a few examples of properly formatted commit messages:

```
feat(data): add new data loading functionality
fix(models): correct the model training process
docs(readme): update installation instructions
style(visualization): reformat the visualization script
refactor(features): simplify feature extraction logic
```

## 📝 Issue Management

We use GitHub Issues to track bugs, enhancements, and other requests. Here's how to work with issues:

### Creating Issues

When creating an issue, please provide the following information:

1. **Title**: A clear and concise title describing the issue.
2. **Description**: A detailed description of the issue, including steps to reproduce if it's a bug, or the desired outcome if it's a feature request.
3. **Labels**: Apply appropriate labels such as `bug`, `enhancement`, `documentation`, etc.
4. **Assignees**: Assign the issue to yourself or someone else if appropriate.

### Issue Types

- **Bug**: Report a bug or an issue.
- **Enhancement**: Suggest a new feature or enhancement.
- **Documentation**: Improvements or additions to documentation.
- **Question**: Questions or requests for help.
- **Task**: General tasks that need to be completed.

### Working on Issues

1. **Assign Yourself**: Assign the issue to yourself before starting work.
2. **Create a Branch**: Create a new branch for your work. Use the issue number in the branch name for easy reference.
   ```sh
   git checkout -b feat/123-new-feature
   ```
3. **Link Commits to Issues**: Reference the issue number in your commit messages.
   ```sh
   git commit -m "feat(data): add new data loading functionality #123"
   ```
4. **Submit a Pull Request**: When your work is ready, submit a pull request. Reference the issue number in the pull request description.

## 🔄 Pull Request Process

1. **Open a PR**: Open a pull request to the `main` branch.
2. **Review**: Request a review from one or more team members.
3. **Address Feedback**: Make changes based on feedback and update the PR.
4. **Merge**: Once approved, merge the PR into the `main` branch.
