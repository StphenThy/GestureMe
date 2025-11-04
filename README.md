# 🎨 Hand Gesture Applications

**A collection of interactive hand gesture-controlled applications using Computer Vision**

Control your computer and create art using just your hands and webcam! This project includes two powerful applications:
1. **Air Canvas** - Draw in the air with your fingers
2. **Gesture Music Controller** - Control your music playback with hand gestures

![Python](https://img.shields.io/badge/Python-3.12-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.12-green)
![Mediapipe](https://img.shields.io/badge/Mediapipe-0.10-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🚀 Quick Start

**Run the Modern Launcher:**
```bash
python launcher.py
```

Choose which application to launch from the beautiful UI!

**Or run applications directly:**
```bash
# Air Canvas
python src/air_canvas.py

# Music Controller
python src/music_controller.py
```

---

## ✨ Features

### 🎨 Air Canvas
- ✏️ **Drawing Mode** - Draw using your index finger
- 🖱️ **Selection Mode** - Select colors with two fingers
- 🎨 **6 Colors** - Red, Green, Blue, Yellow, Magenta, Cyan
- 🧹 **Clear Canvas** - One-click to clear
- 💾 **Save Drawing** - Save as PNG image
- 📊 **Modern UI** - Professional gradient interface

### 🎵 Gesture Music Controller
- ⏯️ **Play/Pause** - Open palm gesture
- ⏭️ **Next Track** - Swipe right
- ⏮️ **Previous Track** - Swipe left
- 🔊 **Volume Up** - Index finger up
- 🔉 **Volume Down** - Three fingers up
- 🔇 **Mute/Unmute** - Peace sign
- 🎮 **Universal** - Works with Spotify, YouTube, any music app
- 🎨 **Modern UI** - Glass-morphism design with real-time feedback

---

## 📋 Requirements

- **Python 3.12** (or 3.11, 3.10)
- **Webcam**
- **Windows** (tested on Windows, but should work on macOS/Linux)

---

## 🔧 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/StphenThy/GestureMe.git
cd GestureMe
```

### 2. Install Python 3.12
Download from [python.org](https://www.python.org/downloads/)
- ✅ **Important:** Check "Add Python to PATH" during installation

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

**Required packages:**
- opencv-python
- mediapipe
- numpy
- pyautogui
- pycaw
- comtypes
- psutil

---

## 🎮 How to Use

### Air Canvas

**Controls:**
| Gesture | Action |
|---------|--------|
| ☝️ Index finger only | Draw on canvas |
| ✌️ Index + Middle fingers | Selection mode (choose colors) |
| Press **'s'** | Save drawing |
| Press **'q'** or **ESC** | Quit |
| Click **X** button | Close window |

**Tips:**
- Keep your hand visible in the camera
- Use good lighting
- Point directly with your index finger to draw
- Raise two fingers to select colors from the top bar

### Gesture Music Controller

**Controls:**
| Gesture | Action |
|---------|--------|
| ✋ Palm Open | Play/Pause |
| 👉 Swipe Right | Next Track |
| 👈 Swipe Left | Previous Track |
| ☝️ Index Finger Up | Volume Up |
| 🖖 3 Fingers Up | Volume Down |
| ✌️ Peace Sign | Mute/Unmute |

**Tips:**
- Start playing music first
- Make clear, distinct gestures
- Wait a moment between gestures (cooldown prevention)
- Gestures are displayed on screen when detected

---

## 📁 Project Structure

```
hand-gesture-apps/
├── launcher.py              # Modern GUI launcher
├── src/
│   ├── air_canvas.py       # Air Canvas application
│   └── music_controller.py # Music Controller application
├── utils/
│   ├── __init__.py
│   ├── hand_detector.py    # Hand tracking module
│   └── gesture_recognizer.py # Gesture recognition
├── saved_drawings/         # Your saved artwork
├── requirements.txt        # Python dependencies
├── config.ini             # Configuration file
├── README.md              # This file
└── .gitignore
```

---

## 🛠️ Configuration

Edit `config.ini` to customize:

```ini
[Camera Settings]
camera_index = 0
canvas_width = 1280
canvas_height = 720

[Hand Detection]
max_hands = 1
detection_confidence = 0.8
tracking_confidence = 0.7

[Drawing Settings]
brush_thickness = 15
```

---

## 🎯 How It Works

### Technology Stack
- **OpenCV** - Image processing and display
- **Mediapipe** - Hand tracking (21 landmark points)
- **NumPy** - Efficient array operations
- **PyAutoGUI** - Keyboard simulation for media controls
- **Pycaw** - Windows audio control

### Hand Detection
1. Mediapipe detects 21 hand landmarks in real-time
2. Identifies which fingers are up/down
3. Tracks finger positions and movements

### Gesture Recognition
- **Palm Open**: All 5 fingers extended
- **Peace Sign**: Only index and middle fingers up
- **Swipe**: Hand movement > 150 pixels horizontally
- **3 Fingers**: Index, middle, and ring fingers up

---

## 🐛 Troubleshooting

### Camera not opening
- Close other apps using the webcam
- Try changing `camera_index` to 1 or 2 in code
- Restart your computer

### Hand not detected
- Ensure good lighting
- Keep hand within camera frame
- Use a plain background
- Check hand is fully visible

### Gestures not working
- Make gestures more distinct
- Wait for cooldown between gestures
- Ensure webcam can clearly see your hand

### Installation errors
```bash
# Update pip first
python -m pip install --upgrade pip

# Reinstall packages
pip install -r requirements.txt --force-reinstall
```

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.
```

---

## 🎓 Learning Resources

- [OpenCV Documentation](https://docs.opencv.org/)
- [Mediapipe Hand Tracking](https://google.github.io/mediapipe/solutions/hands.html)
- [Python Official Docs](https://docs.python.org/3/)

---

## 🔮 Future Enhancements

- [ ] Support for multiple hands
- [ ] Custom gesture recording
- [ ] More drawing tools (shapes, brushes)
- [ ] Gesture macros and shortcuts
- [ ] Cross-platform volume control
- [ ] Mobile app version
- [ ] Voice command integration

---

## 👨‍💻 Author

Created as an educational computer vision project demonstrating hand tracking and gesture recognition.

---

## 🌟 Acknowledgments

- **Mediapipe** by Google for amazing hand tracking
- **OpenCV** community for computer vision tools
- **Python** community for excellent libraries

---

## 📞 Support

If you encounter issues:
1. Check the [Troubleshooting](#-troubleshooting) section
2. Review existing Issues on [GitHub](https://github.com/StphenThy/GestureMe/issues)
3. Create a new issue with details

---

**⭐ If you found this project helpful, please give it a star!**

**Made with ❤️ using Python, OpenCV, and Mediapipe**
