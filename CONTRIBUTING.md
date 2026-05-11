# 🤝 Contributing to AI Learning Hub

We welcome contributions from everyone! Whether you're fixing a typo, adding content, or improving code - your help makes this resource better for everyone.

## Getting Started

### 1. Fork the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Learning-Hub.git
cd AI-Learning-Hub
git remote add upstream https://github.com/AnushkaMunde074/AI-Learning-Hub.git
```

### 2. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 3. Make Your Changes

- Add content, code, or fixes
- Follow the style guide
- Keep commits focused and clean

### 4. Commit and Push

```bash
git add .
git commit -m "Add: Description of your contribution"
git push origin feature/your-feature-name
```

### 5. Create a Pull Request

- Go to GitHub and create PR
- Link to related issues
- Describe your changes
- Wait for review

## Contribution Types

### 🐛 Bug Reports

Create an issue with:
- Clear title and description
- Steps to reproduce
- Expected vs. actual behavior
- Environment details
- Screenshots if applicable

### ✨ Feature Requests

Include:
- Clear description of feature
- Why it's needed
- Implementation approach (if you have one)
- Links to relevant resources

### 📚 Content Additions

Contribute:
- New modules or sections
- Code examples
- Exercises and solutions
- Projects and templates
- Resources and links

### 🔧 Code Improvements

Fix:
- Bugs in examples
- Performance issues
- Code style
- Documentation
- Dependencies

### 📝 Documentation

Improve:
- README files
- Code comments
- Examples
- Getting started guides
- FAQs

## Style Guide

### Markdown

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold** and *italic*

- Bullet points
- With clear structure

1. Numbered lists
2. For steps

[Links](url)
![Images](path)

```code blocks```
```

### Python Code

```python
# Clear comments
def function_name(parameter):
    """Docstring explaining function."""
    # Implementation
    return result

# PEP 8 style
# 4-space indentation
# Descriptive variable names
# Type hints when possible
```

### File Structure

```
Module-Name/
├── README.md           (Overview and outline)
├── concepts.md         (Theory and concepts)
├── examples.py         (Code examples)
├── code/               (Additional code files)
│   ├── algorithm1.py
│   └── algorithm2.py
├── notebooks/          (Jupyter notebooks)
│   └── tutorial.ipynb
├── exercises/          (Practice problems)
│   ├── exercise1.py
│   └── solutions/
│       └── exercise1_solution.py
└── resources.md        (Links and references)
```

## Commit Messages

Use clear, descriptive commit messages:

```
Add: New feature description
Fix: Bug fix description
Update: Updated existing content
Refactor: Code reorganization
Docs: Documentation updates
Test: Added tests

Example:
Add: Implement A* pathfinding algorithm with examples
```

## Pull Request Process

1. **Sync with main branch**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Check your changes**
   - Run code examples
   - Check formatting
   - Verify links

3. **Create PR with**
   - Clear title
   - Description of changes
   - Related issues
   - Screenshots/demos if applicable

4. **Respond to reviews**
   - Address feedback
   - Make requested changes
   - Push updates

## Code Review

We'll review your PR for:
- ✅ Correctness
- ✅ Code quality
- ✅ Documentation
- ✅ Style consistency
- ✅ Contribution guidelines

## Project Structure

When adding content:

1. **Create module directory** if new
2. **Add README.md** with overview
3. **Add concepts/theory** in markdown
4. **Add code examples** with comments
5. **Add exercises** with solutions
6. **Add resources** links

## Reporting Issues

Include:
- [ ] Title and description
- [ ] Steps to reproduce
- [ ] Expected behavior
- [ ] Actual behavior
- [ ] Environment (OS, Python version, etc.)
- [ ] Error messages/logs
- [ ] Screenshots if visual

## Questions?

- Check existing issues/discussions
- Read GETTING_STARTED.md
- Open a discussion
- Email maintainers

## Recognition

Contributors are recognized in:
- README.md contributors section
- GitHub contributors page
- Commit history

## Code of Conduct

Please follow our Code of Conduct in all interactions. Respectful, inclusive community for all!

## License

By contributing, you agree your content will be under the MIT License.

---

Thank you for contributing! 🙏✨
