# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project setup
- Core network scanning functionality
- Device discovery module
- Port scanning module
- JSON output support
- Verbose logging
- Comprehensive test suite

### Planned
- IPv6 support
- Custom scan profiles
- GUI interface
- Performance metrics and statistics
- Rate limiting options

## [0.1.0] - 2026-06-04

### Added
- Initial release of ShibaCuddles
- ICMP-based device discovery
- TCP port scanning (ports 1-1024 by default)
- Configurable port ranges
- JSON output support
- Verbose mode for detailed output
- Unit test suite
- Documentation (README, CONTRIBUTING)
- MIT License

### Features
- Device discovery on network subnets
- Multi-threaded port scanning
- Flexible command-line interface
- JSON result export
- Comprehensive error handling

---

## [Planned Releases]

### Version 0.2.0
- **Target**: Q3 2026
- Async scanning support
- Performance optimizations
- Extended configuration options
- API interface

### Version 0.3.0
- **Target**: Q4 2026
- IPv6 support
- Vulnerability scanning
- Web dashboard
- Advanced filtering options

### Version 1.0.0
- **Target**: 2027
- Stable API
- Production-ready features
- Comprehensive documentation
- Native binaries for major platforms

---

## Guidelines for Updating This File

- New features should be added under `[Unreleased]`
- Released versions use semantic versioning: MAJOR.MINOR.PATCH
- Include date in YYYY-MM-DD format
- Categories: Added, Changed, Deprecated, Removed, Fixed, Security
- Keep it human-readable

## How to Release

1. Update version in `setup.py` and `__version__.py`
2. Move changes from `[Unreleased]` to new version
3. Create Git tag: `git tag v0.x.x`
4. Build and publish: `python -m build && python -m twine upload dist/*`
5. Update release notes on GitHub
