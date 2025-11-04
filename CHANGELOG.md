# 📝 Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2025-01-XX

### 🎉 Initial Release

This is the first public release of Hand Gesture Applications!

### ✨ Added

#### Air Canvas
- Hand tracking using Mediapipe (21 landmarks)
- Drawing mode with index finger
- Selection mode with two fingers
- 6-color palette (Red, Green, Blue, Yellow, Magenta, Cyan)
- Clear canvas functionality
- Save drawings as PNG images
- Modern gradient UI with glass-morphism design
- Real-time FPS display
- Status indicators for mode and color

#### Gesture Music Controller
- Palm open gesture for Play/Pause
- Swipe right/left for Next/Previous track
- Index finger up for Volume Up
- Three fingers up for Volume Down
- Peace sign for Mute/Unmute
- Works with any music application (Spotify, YouTube, etc.)
- Modern UI with gradient header
- Real-time gesture feedback panel
- Gesture cooldown system to prevent accidental triggers

#### Modern Launcher
- Professional dark theme UI
- Card-based layout for app selection
- Hover effects and animations
- Window icon and branding
- Launches applications as separate processes

#### Utilities
- **HandDetector** - Mediapipe hand tracking wrapper
  - Multi-hand support
  - Finger up/down detection
  - Landmark position retrieval
  - Configurable confidence thresholds

- **GestureRecognizer** - Complex gesture recognition
  - Swipe detection (left/right)
  - Pinch detection
  - Palm open detection
  - Peace sign detection
  - Cooldown system for gesture stability

### 🔧 Configuration
- `config.ini` file for customization
  - Camera settings (index, resolution)
  - Hand detection parameters
  - Drawing settings (brush thickness)

### 📚 Documentation
- Comprehensive README with installation guide
- GitHub setup guide
- Contributing guidelines
- MIT License
- Code of Conduct (implicit in Contributing.md)
- Quick start scripts (`.bat` and `.ps1`)

### 🛠️ Technical Stack
- Python 3.12+ support
- OpenCV 4.12.0.88
- Mediapipe 0.10.14
- NumPy 2.2.6
- PyAutoGUI 0.9.54
- Pycaw (Windows audio control)
- Tkinter (built-in GUI)

### 🐛 Known Issues
- Music controller requires Windows OS for volume control
- Emoji rendering not supported (uses text labels instead)
- Camera must be closed properly to release resources

---

## [Unreleased]

### 🔮 Planned Features

#### Air Canvas Enhancements
- [ ] Undo/Redo functionality
- [ ] Shape drawing tools (circle, rectangle, line)
- [ ] Eraser mode
- [ ] Brush size adjustment
- [ ] Fill bucket tool
- [ ] Layer support
- [ ] More colors and color picker

#### Music Controller Enhancements
- [ ] Volume slider visualization
- [ ] Current song display
- [ ] Playlist navigation
- [ ] Cross-platform audio support (macOS, Linux)
- [ ] Spotify API integration
- [ ] Custom gesture mapping

#### General Improvements
- [ ] Multi-hand support (two hands simultaneously)
- [ ] Gesture customization UI
- [ ] Performance optimizations
- [ ] Better error handling
- [ ] Automated tests
- [ ] CI/CD pipeline
- [ ] Pre-built executables (.exe files)

#### Platform Support
- [ ] macOS compatibility testing
- [ ] Linux compatibility testing
- [ ] Mobile app version (Android/iOS)
- [ ] Web-based version using WebRTC

#### User Experience
- [ ] Tutorial mode for first-time users
- [ ] Gesture training module
- [ ] Settings panel in applications
- [ ] Keyboard shortcuts reference
- [ ] Dark/light theme toggle

---

## Version History

### How to Read Versions

Given a version number MAJOR.MINOR.PATCH:
- **MAJOR** version for incompatible API changes
- **MINOR** version for new functionality (backwards-compatible)
- **PATCH** version for bug fixes (backwards-compatible)

### Example Future Versions

**[1.0.1]** - Bug fixes and minor improvements
**[1.1.0]** - New features added (undo/redo, shapes)
**[2.0.0]** - Major changes (multi-hand support, API changes)

---

## 📅 Release Schedule

We aim for:
- **Patch releases** (bug fixes): As needed
- **Minor releases** (new features): Every 2-3 months
- **Major releases** (breaking changes): Yearly

---

## 🎯 Contribution to Changelog

When contributing, please update this file:

1. Add your changes under **[Unreleased]**
2. Use these categories:
   - **Added** - New features
   - **Changed** - Changes to existing functionality
   - **Deprecated** - Features marked for removal
   - **Removed** - Removed features
   - **Fixed** - Bug fixes
   - **Security** - Security fixes

3. Format:
   ```markdown
   ### Added
   - Feature description (#issue-number if applicable)
   ```

---

## 📜 License

All versions are released under the MIT License.

---

**Thank you for using Hand Gesture Applications!** 🎉

For detailed changes in each version, see the [GitHub Releases](https://github.com/StphenThy/GestureMe/releases) page.
