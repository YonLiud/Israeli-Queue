# Contributing to Israeli Queue

Thank you for your interest in contributing to Israeli Queue! This document provides guidelines and instructions for contributors.

## 🚀 Quick Start for Contributors

### 1. Fork and Clone
```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/Israeli-Queue.git
cd Israeli-Queue
```

### 2. Set Up Development Environment
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Install the package in development mode
pip install -e .

# Set up pre-commit hooks (optional but recommended)
pre-commit install
```

### 3. Run Tests
```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=IsraeliQueue --cov-report=term-missing

# Run specific test file
pytest tests/test_israeli_queue.py -v
```

## 🔧 Development Workflow

### Making Changes

1. **Create a branch** for your feature or bugfix:
   ```bash
   git checkout -b feature/amazing-feature
   # or
   git checkout -b fix/bug-description
   ```

2. **Make your changes** following our coding standards

3. **Write tests** for new functionality

4. **Run the test suite** to ensure everything works:
   ```bash
   pytest
   ```

5. **Check code quality**:
   ```bash
   # Format code
   black .
   
   # Lint code
   flake8 .
   
   # Type checking
   mypy IsraeliQueue/
   ```

6. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: add amazing new feature"
   ```

7. **Push and create a Pull Request**:
   ```bash
   git push origin feature/amazing-feature
   ```

### Commit Message Format

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat:` new features
- `fix:` bug fixes  
- `docs:` documentation changes
- `test:` adding or modifying tests
- `refactor:` code refactoring
- `chore:` maintenance tasks

Examples:
```
feat: add new queue method for batch operations
fix: resolve item equality comparison bug
docs: update README with new examples
test: add edge case tests for empty queues
```

## 🧪 Testing Guidelines

### Writing Tests

- Place tests in the `tests/` directory
- Use descriptive test names that explain what is being tested
- Follow the `test_*.py` naming convention
- Use fixtures for common test data
- Test both success and failure cases

### Test Structure
```python
def test_feature_description(self):
    """Test that feature works correctly in specific scenario."""
    # Arrange
    queue = IsraeliQueue()
    item = Item("test", 1)
    
    # Act
    queue.enqueue(item)
    
    # Assert
    assert queue.size() == 1
    assert queue.peek() == item
```

### Coverage Requirements

- Maintain **95%+ test coverage**
- All new code must include tests
- Tests should cover edge cases and error conditions

## 📋 Code Quality Standards

### Python Style
- Follow [PEP 8](https://pep8.org/) style guidelines
- Use [Black](https://black.readthedocs.io/) for code formatting
- Maximum line length: 88 characters
- Use type hints for all public APIs

### Documentation
- Write docstrings for all public classes and methods
- Use Google-style docstrings
- Include examples in docstrings when helpful
- Update README.md for user-facing changes

### Type Safety
- Use type hints throughout the codebase
- Run `mypy` to check type consistency
- Prefer explicit types over `Any` when possible

## 🚀 Release Process

Releases are handled automatically through GitHub Actions:

1. **Create a release** using GitHub's release interface or the manual workflow
2. **Tag format**: Use semantic versioning (`v2.1.0`)
3. **Automatic publishing**: The CI/CD pipeline will automatically:
   - Run full test suite
   - Build the package
   - Publish to PyPI
   - Update documentation

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Python version** and operating system
2. **Israeli Queue version**
3. **Minimal code example** that reproduces the issue
4. **Expected behavior** vs **actual behavior**
5. **Full error traceback** if applicable

## 💡 Feature Requests

For new features:

1. **Check existing issues** to avoid duplicates
2. **Describe the use case** and problem being solved
3. **Provide implementation ideas** if you have them
4. **Consider offering to implement** the feature yourself

## 🔒 Security

If you discover a security vulnerability:

1. **DO NOT** open a public issue
2. **Email** the maintainers directly
3. **Provide** detailed information about the vulnerability
4. **Allow time** for the issue to be addressed before disclosure

## 📝 Documentation

### API Documentation
- All public APIs must have comprehensive docstrings
- Include parameter types, return types, and exceptions
- Provide usage examples for complex features

### README Updates
- Update examples when adding new features
- Keep the feature list current
- Update performance characteristics if applicable

## 🏆 Recognition

Contributors will be:
- Added to the project's contributors list
- Mentioned in release notes for significant contributions
- Given credit in documentation where appropriate

## ❓ Questions?

If you have questions about contributing:

1. Check existing [issues](https://github.com/YonLiud/Israeli-Queue/issues)
2. Open a new issue with the `question` label
3. Join discussions in existing issues

Thank you for contributing to Israeli Queue! 🎉