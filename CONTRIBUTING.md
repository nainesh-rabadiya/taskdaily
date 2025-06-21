# Contributing to Daily Work Notes Manager

Thank you for your interest in contributing to Daily Work Notes Manager! This document provides guidelines and instructions for contributing.

## 🌟 How to Contribute

1. **Fork the Repository**
   - Click the 'Fork' button on GitHub
   - Clone your fork locally
   ```bash
   git clone <your-fork-url>
   cd daily-work-notes
   ```

2. **Set Up Development Environment**
   - Install Python 3.6 or higher
   - Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
   - Install development dependencies
   ```bash
   pip install pytest black flake8
   ```

3. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes**
   - Follow the coding style guide
   - Add tests for new features
   - Update documentation as needed
   - Keep commits focused and atomic

5. **Test Your Changes**
   - Run the test suite
   ```bash
   pytest
   ```
   - Run the linter
   ```bash
   flake8 .
   black .
   ```

6. **Submit a Pull Request**
   - Push changes to your fork
   - Create a pull request from GitHub
   - Describe your changes in detail
   - Reference any related issues

## 📝 Code Style Guide

1. **Python Code**
   - Follow PEP 8 guidelines
   - Use type hints
   - Write docstrings for functions
   - Keep functions focused and small

2. **Documentation**
   - Keep README.md up to date
   - Document new features
   - Update QUICK_START.md if needed
   - Add comments for complex logic

3. **Commit Messages**
   - Use clear, descriptive messages
   - Start with a verb (Add, Fix, Update)
   - Reference issues when applicable
   - Keep commits focused

## 🧪 Testing

1. **Unit Tests**
   - Write tests for new features
   - Update existing tests as needed
   - Aim for high coverage
   - Test edge cases

2. **Manual Testing**
   - Test all new features
   - Verify backwards compatibility
   - Check error handling
   - Test different configurations

## 📋 Pull Request Checklist

- [ ] Code follows style guide
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] All tests passing
- [ ] No linter warnings
- [ ] Changelog updated
- [ ] Version bumped if needed

## 🐛 Reporting Issues

1. **Bug Reports**
   - Use the issue template
   - Provide clear steps to reproduce
   - Include relevant logs
   - Specify your environment

2. **Feature Requests**
   - Explain the use case
   - Describe expected behavior
   - Provide examples if possible
   - Consider alternatives

## 🚀 Development Workflow

1. **Local Development**
   ```bash
   # Create and activate virtual environment
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   .\venv\Scripts\activate  # Windows
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Run tests
   pytest
   
   # Check code style
   black .
   flake8 .
   ```

2. **Making Changes**
   - Create feature branch
   - Make changes
   - Run tests
   - Update documentation
   - Submit pull request

## 📚 Additional Resources

- [Python Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Git Commit Messages](https://chris.beams.io/posts/git-commit/)
- [Semantic Versioning](https://semver.org/)
- [Writing Good Documentation](https://www.writethedocs.org/guide/)

## ❓ Questions?

- Create an issue for questions
- Join our community discussions
- Check existing documentation
- Contact maintainers directly

Thank you for contributing to Daily Work Notes Manager! 🙏 