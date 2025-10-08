# 🚀 Setting Up GitHub Actions for PyPI Publishing

This guide will help you set up automated publishing to PyPI using GitHub Actions.

## 📋 Prerequisites

1. **PyPI Account**: Create accounts on both [PyPI](https://pypi.org) and [Test PyPI](https://test.pypi.org)
2. **GitHub Repository**: Your Israeli Queue repository on GitHub
3. **Admin Access**: You need admin access to the repository to set up secrets

## 🔑 Step 1: Create API Tokens

### PyPI Production Token
1. Go to [PyPI Account Settings](https://pypi.org/manage/account/)
2. Scroll to "API tokens" section
3. Click "Add API token"
4. Token name: `IsraeliQueue-GitHub-Actions`
5. Scope: "Entire account" (or specific to your project if it exists)
6. Copy the token (starts with `pypi-`)

### Test PyPI Token  
1. Go to [Test PyPI Account Settings](https://test.pypi.org/manage/account/)
2. Repeat the same process as above
3. Copy the token (starts with `pypi-`)

## 🔒 Step 2: Add Secrets to GitHub

1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add these secrets:

| Secret Name | Value | Description |
|-------------|-------|-------------|
| `PYPI_API_TOKEN` | `pypi-...` | Your PyPI production token |
| `TEST_PYPI_API_TOKEN` | `pypi-...` | Your Test PyPI token |

## 🌍 Step 3: Create GitHub Environments (Optional)

For additional security, create environments:

1. Go to **Settings** → **Environments**
2. Create two environments:
   - `pypi` (for production releases)
   - `test-pypi` (for test releases)
3. Add protection rules if desired (e.g., require reviews)

## 🚀 Step 4: How the Workflow Works

### Automatic Test Publishing
- **Trigger**: Push to `main` branch
- **Action**: Publishes to Test PyPI automatically
- **Purpose**: Test that packaging works correctly

### Production Publishing
- **Trigger**: Create a GitHub release
- **Action**: Publishes to production PyPI
- **Purpose**: Official releases for users

## 📦 Step 5: Creating a Release

### Using GitHub UI
1. Go to your repository
2. Click **Releases** → **Create a new release**
3. Choose a tag (e.g., `v2.0.0`)
4. Fill in release notes
5. Click **Publish release**

### Using GitHub CLI
```bash
# Install GitHub CLI first
gh release create v2.0.0 --title "Release v2.0.0" --notes "Major update with improved API"
```

### Using the Release Workflow
1. Go to **Actions** → **Create Release**
2. Click **Run workflow**
3. Enter version (e.g., `v2.0.0`)
4. Choose if it's a pre-release
5. Click **Run workflow**

## 🔍 Step 6: Monitoring

### Check Workflow Status
- Go to **Actions** tab to see workflow runs
- Check for any failures and review logs
- Verify packages appear on PyPI/Test PyPI

### Verify Installation
```bash
# Test PyPI
pip install -i https://test.pypi.org/simple/ IsraeliQueue

# Production PyPI (after release)
pip install IsraeliQueue
```

## 🐛 Troubleshooting

### Common Issues

**Token Authentication Failed**
- Verify token is correct and hasn't expired
- Check token scope includes your project
- Ensure secret name matches exactly

**Package Already Exists**
- PyPI doesn't allow overwriting versions
- Increment version number in your release
- Use `skip-existing: true` for test uploads

**Build Failures**
- Check that all tests pass locally
- Verify `pyproject.toml` is valid
- Ensure all dependencies are specified

**Permission Denied**
- Verify you have maintainer access to the PyPI project
- Check that API token has correct permissions

### Getting Help

1. **Check Action Logs**: Detailed error messages in GitHub Actions
2. **PyPI Help**: [PyPI Help Documentation](https://pypi.org/help/)
3. **GitHub Issues**: Open an issue if you suspect a bug

## 🎉 Success!

Once set up, your workflow will:

- ✅ Run tests on every push
- ✅ Publish to Test PyPI on main branch
- ✅ Publish to production PyPI on releases
- ✅ Generate build artifacts
- ✅ Provide security scanning

Your Israeli Queue package will now be automatically maintained and distributed! 🚀