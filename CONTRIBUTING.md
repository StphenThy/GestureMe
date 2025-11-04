# 🤝 Contributing to Hand Gesture Applications

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

---

## 🌟 How Can I Contribute?

### 🐛 Reporting Bugs

If you find a bug, please create an issue with:

**Bug Report Template:**
```
**Description:**
A clear description of the bug

**Steps to Reproduce:**
1. Go to '...'
2. Click on '...'
3. See error

**Expected Behavior:**
What should happen

**Actual Behavior:**
What actually happens

**Environment:**
- OS: [e.g., Windows 11]
- Python Version: [e.g., 3.12.10]
- Webcam: [e.g., Logitech C920]

**Screenshots:**
If applicable, add screenshots
```

### 💡 Suggesting Features

We love new ideas! Create an issue with:

**Feature Request Template:**
```
**Feature Description:**
A clear description of the feature

**Use Case:**
Why would this be useful?

**Proposed Implementation:**
(Optional) How might this work?

**Alternatives:**
Other solutions you've considered
```

### 🔧 Code Contributions

1. **Fork the repository**
2. **Create a branch** (`git checkout -b feature/amazing-feature`)
3. **Make your changes**
4. **Test thoroughly**
5. **Commit** (`git commit -m 'Add amazing feature'`)
6. **Push** (`git push origin feature/amazing-feature`)
7. **Open a Pull Request**

---

## 📝 Coding Standards

### Python Style Guide

We follow **PEP 8** with some modifications:

```python
# Good ✅
class HandDetector:
    """Detects hands using Mediapipe."""
    
    def __init__(self, max_hands=2):
        self.max_hands = max_hands
        self.hands = mp.solutions.hands.Hands()
    
    def find_hands(self, image):
        """Find hands in the image."""
        return self.hands.process(image)

# Bad ❌
class handdetector:
    def __init__(self,maxHands=2):
        self.maxHands=maxHands
```

### Key Guidelines

1. **Use descriptive variable names**
   ```python
   # Good ✅
   hand_landmarks = detector.find_hands(frame)
   
   # Bad ❌
   hl = d.fh(f)
   ```

2. **Add docstrings to functions**
   ```python
   def calculate_distance(point1, point2):
       """
       Calculate Euclidean distance between two points.
       
       Args:
           point1 (tuple): (x, y) coordinates
           point2 (tuple): (x, y) coordinates
           
       Returns:
           float: Distance between points
       """
       return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
   ```

3. **Keep functions focused**
   - One function = One responsibility
   - Max ~50 lines per function
   - Extract complex logic into helper functions

4. **Use type hints (optional but encouraged)**
   ```python
   def get_finger_position(self, finger_id: int) -> tuple[int, int]:
       """Get the (x, y) position of a finger tip."""
       return (x, y)
   ```

---

## 🧪 Testing

Before submitting, test your changes:

### Manual Testing Checklist

- [ ] Code runs without errors
- [ ] All gestures work correctly
- [ ] UI displays properly
- [ ] No memory leaks (run for 5+ minutes)
- [ ] Works with different lighting conditions
- [ ] Camera releases properly on exit
- [ ] Tested on Windows (and Mac/Linux if possible)

### Test Both Applications

```powershell
# Test launcher
python launcher.py

# Test Air Canvas directly
python src/air_canvas.py

# Test Music Controller directly
python src/music_controller.py
```

---

## 📁 Project Structure

When adding new features, follow this structure:

```
hand-gesture-apps/
├── src/                    # Main applications
│   ├── air_canvas.py
│   └── music_controller.py
├── utils/                  # Reusable modules
│   ├── hand_detector.py
│   ├── gesture_recognizer.py
│   └── your_new_module.py  # Add new utilities here
├── tests/                  # Unit tests (future)
├── screenshots/            # Project screenshots
└── docs/                   # Additional documentation
```

---

## 🎯 Good First Issues

New to contributing? Try these:

### 🟢 Beginner-Friendly

- [ ] Add more colors to Air Canvas palette
- [ ] Improve gesture detection accuracy
- [ ] Add keyboard shortcuts documentation
- [ ] Create demo GIFs for README
- [ ] Add more configuration options
- [ ] Improve error messages

### 🟡 Intermediate

- [ ] Implement undo/redo in Air Canvas
- [ ] Add shape drawing (circles, rectangles)
- [ ] Create unit tests for utilities
- [ ] Support multiple hands
- [ ] Add gesture customization UI
- [ ] Improve performance optimization

### 🔴 Advanced

- [ ] Cross-platform audio control (macOS/Linux)
- [ ] Real-time hand tracking smoothing
- [ ] Machine learning gesture customization
- [ ] Mobile app version
- [ ] 3D hand tracking visualization
- [ ] Gesture macro recording

---

## 💬 Communication

### Where to Ask Questions

- **General Questions:** Open a GitHub Discussion
- **Bug Reports:** Create an Issue
- **Feature Requests:** Create an Issue
- **Code Questions:** Comment on relevant Pull Request

### Response Time

We aim to respond within:
- **Issues:** 2-3 days
- **Pull Requests:** 3-5 days
- **Discussions:** 1 week

---

## 🔍 Code Review Process

When you submit a PR, we'll review:

1. **Code Quality**
   - Follows style guide
   - Well-documented
   - No unnecessary complexity

2. **Functionality**
   - Works as intended
   - Doesn't break existing features
   - Handles edge cases

3. **Performance**
   - No significant slowdowns
   - Efficient algorithms
   - Memory-conscious

4. **Testing**
   - Manually tested
   - No obvious bugs
   - Works on multiple systems

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## 🎓 Learning Resources

New to computer vision? Check these out:

### OpenCV
- [OpenCV Python Tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
- [OpenCV Course - freeCodeCamp](https://www.youtube.com/watch?v=oXlwWbU8l2o)

### Mediapipe
- [Mediapipe Hand Tracking](https://google.github.io/mediapipe/solutions/hands.html)
- [Mediapipe Python Examples](https://github.com/google/mediapipe/tree/master/mediapipe/python)

### Git & GitHub
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)

---

## 🙏 Thank You!

Every contribution helps make this project better. Whether it's:
- Reporting a bug 🐛
- Suggesting a feature 💡
- Improving documentation 📝
- Writing code 💻
- Sharing the project ⭐

**Your contribution matters!**

---

## ✨ Contributors

Thank you to all our contributors! 🎉

<!-- Add contributor badges here -->

---

## 📞 Contact

For major contributions or collaborations, feel free to reach out:

- GitHub Issues: [Create an Issue](https://github.com/StphenThy/GestureMe/issues)
- GitHub Discussions: [Start a Discussion](https://github.com/StphenThy/GestureMe/discussions)

---

**Happy Contributing! 🚀**
