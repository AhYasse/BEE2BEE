# Tauri App Update Instructions

This guide explains how to release a new version of the ConnectIT Tauri application.

## Workflow Triggers

The GitHub Actions workflow (`.github/workflows/actions.yaml`) automatically builds and publishes the Tauri app when:

1. **Any file changes in `tauri-app/` folder** are pushed to `main` branch
2. **A version tag** (e.g., `v1.0.0`) is pushed to the repository
3. **A GitHub release** is published
4. **Manually triggered** via the Actions tab

## Release Process

### Option 1: Automatic Build on Push (Recommended)

1. **Update the version** in `tauri-app/src-tauri/tauri.conf.json`:

   ```json
   {
     "version": "1.0.1"
   }
   ```

2. **Commit and push** your changes:

   ```bash
   git add tauri-app/
   git commit -m "Release v1.0.1"
   git push origin main
   ```

3. **Monitor the build** in the [Actions tab](https://github.com/Chatit-cloud/BEE2BEE/actions)

4. **Find your release draft** in the [Releases section](https://github.com/Chatit-cloud/BEE2BEE/releases) and publish it

### Option 2: Manual Tag-Based Release

1. **Update version** in `tauri-app/src-tauri/tauri.conf.json`

2. **Commit changes**:

   ```bash
   git add tauri-app/src-tauri/tauri.conf.json
   git commit -m "Bump version to 1.0.1"
   ```

3. **Create and push a version tag**:

   ```bash
   git tag v1.0.1
   git push origin v1.0.1
   ```

4. The workflow will automatically trigger and build for all platforms

### Option 3: Manual Trigger

1. Go to the [Actions tab](https://github.com/Chatit-cloud/BEE2BEE/actions)
2. Select the "publish" workflow
3. Click "Run workflow"
4. Choose the branch (usually `main`)
5. Click "Run workflow"

## Build Platforms

The workflow builds for:

- **Windows** (x64)
- **macOS** (Intel x64)
- **macOS** (Apple Silicon ARM64)
- **Linux** (x64, Ubuntu 22.04)
- **Linux** (ARM64, Ubuntu 22.04) - Only for public repos

## Release Artifacts

After a successful build, the following files will be attached to the draft release:

- **Windows**: `.msi` installer and `.exe` portable
- **macOS**: `.dmg` disk image and `.app.tar.gz`
- **Linux**: `.deb`, `.AppImage`, and `.tar.gz`

## Important Notes

- All releases are created as **drafts** by default - you must manually publish them
- The version number in `tauri.conf.json` is automatically used in the release name
- Builds require the `GITHUB_TOKEN` (automatically provided) and optionally `TAURI_SIGNING_PRIVATE_KEY` for code signing
- Changes to `.github/workflows/actions.yaml` will also trigger the workflow

## Version Naming Convention

Follow semantic versioning (semver):

- **Major** (1.0.0): Breaking changes
- **Minor** (1.1.0): New features, backwards compatible
- **Patch** (1.0.1): Bug fixes, backwards compatible

Git tags should always start with `v` (e.g., `v1.0.0`)

## Troubleshooting

**Build fails on a specific platform?**

- Check the platform-specific logs in the Actions tab
- For macOS builds, ensure you have the correct targets configured
- For Linux builds, ensure all dependencies are listed in the Ubuntu setup step

**Release not appearing?**

- Verify the workflow completed successfully
- Check that the release was created as a draft in the Releases section
- Ensure you have `contents: write` permissions

**Version not updating?**

- Double-check `tauri.conf.json` has the correct version
- The `__VERSION__` placeholder is automatically replaced by Tauri

## Testing Before Release

To test locally before pushing:

```bash
cd tauri-app
npm install
npm run tauri build
```

The built application will be in `tauri-app/src-tauri/target/release/bundle/`
