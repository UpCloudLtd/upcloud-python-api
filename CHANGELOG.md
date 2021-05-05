# Changelog
All notable changes to this project will be documented in this file.

Changelog was added with version 2.0.0.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.0.0] - 2021-05-05

Python 2 is no longer supported. This is a maintenance release without
that many added features. It was mostly done to make future development easier.

### Added
- Storage upload accepts filenames in strings and PathLike or BinaryIO variables.
- Code style is now guarded by Black, flake8, isort etc.
- Improved documentation and its examples, especially regarding server creation and storage uploads.

### Changed
- Huge amount of fixups in project tests, style and imports by [akx](https://github.com/akx). Thank you! :heart:
- Zone default from storage creation has been removed, making zone a required variable with `create_storage()`.
- Passwords for server user are not created by default if SSH keys are provided.
- Tests and deployments moved fully from CircleCI to GitHub Actions.
- Fixed storage upload not reading the file into memory before uploading.
- Moved to fully using setup.cfg instead of requirements.txt.

### Removed
- Python 2 support.
