# Changelog

All notable changes to TaskDaily will be documented in this file.

## [2.0.0] - 2024-03-20

### Changed
- Removed task completion command line interface
- Simplified task status management to use file-based editing only
- Updated formatters to handle task status through emoji indicators
- Improved documentation for task status management
- Added comprehensive testing guide

### Added
- New TESTING.md with detailed testing instructions
- Enhanced status behavior documentation
- More examples in README.md for task status management
- Configuration examples for status behaviors

### Removed
- `daily complete` command
- Task completion via CLI
- Direct task status manipulation methods

### Fixed
- Improved emoji handling in task parsing
- Better status tracking in formatters
- Enhanced carry-forward logic for tasks

## [1.0.0] - 2024-03-XX

### Added
- Initial release
- Basic task management functionality
- Multiple output formats (Slack, Teams, WhatsApp, Email)
- Project management with emoji prefixes
- Task status workflow
- Configuration management
- File-based storage system
