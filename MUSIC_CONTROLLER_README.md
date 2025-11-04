# 🎵 Gesture Music Controller

Control your music with hand gestures! No need to touch your keyboard - just wave your hand in front of the camera.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.12-green)
![Mediapipe](https://img.shields.io/badge/Mediapipe-0.10-orange)

## ✨ Features

- 🎵 **Play/Pause** - Open palm gesture
- ⏭️ **Next Track** - Swipe right
- ⏮️ **Previous Track** - Swipe left
- 🔊 **Volume Up** - Thumbs up at top of screen
- 🔉 **Volume Down** - Fist at bottom of screen
- 🔇 **Mute/Unmute** - Peace sign
- 🎚️ **Fine Volume Control** - Pinch gesture (top/bottom)
- 📊 **Real-time feedback** - See your gestures on screen
- 🎮 **Works with any music app** - Spotify, YouTube Music, Windows Media Player, etc.

## 🎮 Gesture Guide

| Gesture | Hand Position | Action |
|---------|--------------|--------|
| ✋ **Palm Open** | All 5 fingers extended | ⏯️ Play/Pause |
| 👉 **Swipe Right** | Move hand quickly to the right | ⏭️ Next Track |
| 👈 **Swipe Left** | Move hand quickly to the left | ⏮️ Previous Track |
| 👍 **Thumbs Up** | Thumb up, hand at TOP of screen | 🔊 Volume Up (+10%) |
| ✊ **Fist** | All fingers closed, hand at BOTTOM | 🔉 Volume Down (-10%) |
| ✌️ **Peace Sign** | Index + Middle fingers up | 🔇 Mute/Unmute |
| 🤏 **Pinch** | Thumb + Index close, TOP of screen | 🔊 Small Volume Up (+5%) |
| 🤏 **Pinch** | Thumb + Index close, BOTTOM of screen | 🔉 Small Volume Down (-5%) |

## 🚀 Quick Start

### Run the Music Controller

```powershell
py -3.12 src/music_controller.py
```

### How to Use

1. **Start your music** (Spotify, YouTube, any music player)
2. **Run the script** (command above)
3. **Position yourself** so your hand is visible in the camera
4. **Make gestures** and watch your music respond!

## 📋 Prerequisites

All packages are already installed if you set up the Air Canvas project:

- Python 3.12
- opencv-python
- mediapipe
- numpy
- pyautogui
- pycaw
- comtypes

If you need to install them:

```powershell
py -3.12 -m pip install opencv-python mediapipe numpy pyautogui pycaw comtypes
```

## 🎯 Tips for Best Results

### Camera Position
- Make sure your hand is well-lit
- Keep hand within camera frame
- Maintain 1-2 feet distance from camera

### Gesture Recognition
- **Hold gestures briefly** - the system has a cooldown to prevent spam
- **Make clear gestures** - fully extend or close fingers
- **Swipe quickly** - fast movements are detected better
- **For volume control** - move hand to TOP third (up) or BOTTOM third (down) of screen

### Troubleshooting

**Gestures not detected?**
- Ensure good lighting
- Make gestures more distinct
- Check if hand is fully visible
- Try a plain background

**Volume control not working?**
- System falls back to keyboard shortcuts automatically
- Make sure hand is at TOP or BOTTOM of screen
- Windows volume must be unlocked

**Music controls not responding?**
- Make sure a music app is running
- Some apps may need to be in focus
- Try with Windows Media Player, Spotify, or browser-based players

## 🎨 Customization

Edit `src/music_controller.py` to customize:

```python
# Gesture cooldown (seconds between same gesture)
cooldown_time = 1.5

# Swipe sensitivity
swipe_threshold = 150  # pixels

# Volume change amount
volume_step = 0.1  # 10%
fine_volume_step = 0.05  # 5%

# Camera settings
camera_index = 0
screen_width = 1280
screen_height = 720
```

## 🎵 Compatible Music Players

Works with any application that responds to media keys:

✅ Spotify  
✅ YouTube Music (browser)  
✅ Apple Music  
✅ Windows Media Player  
✅ VLC Media Player  
✅ iTunes  
✅ SoundCloud  
✅ And many more!

## 🔧 How It Works

### Architecture

1. **Hand Detection** (`utils/hand_detector.py`)
   - Uses Mediapipe to detect hand landmarks
   - Tracks 21 points on your hand
   - Identifies which fingers are up/down

2. **Gesture Recognition** (`utils/gesture_recognizer.py`)
   - Analyzes hand landmarks to identify gestures
   - Detects swipes, pinches, and finger patterns
   - Includes cooldown to prevent gesture spam

3. **Music Control** (`src/music_controller.py`)
   - Translates gestures into actions
   - Uses PyAutoGUI for media key simulation
   - Uses pycaw for Windows volume control

### Gesture Detection Logic

**Palm Open**: All 5 fingers extended  
**Peace Sign**: Only index and middle fingers up  
**Fist**: All fingers down  
**Thumbs Up**: Only thumb extended  
**Pinch**: Distance between thumb and index < 40 pixels  
**Swipe**: Hand moves > 150 pixels horizontally  

## 📝 Code Examples

### Add a Custom Gesture

```python
# In gesture_recognizer.py
def detect_ok_sign(self, fingers, landmark_list):
    # Implement your gesture logic
    return fingers[0] == 1 and fingers[1] == 1  # Example

# In music_controller.py
def process_gesture(self, gesture):
    if gesture == 'ok_sign':
        self.control_playback('shuffle')  # Custom action
```

## 🐛 Debugging

Enable verbose output:

```python
# In music_controller.py, add to recognize_gesture:
print(f"Fingers: {fingers}")
print(f"Hand position: {self.get_vertical_hand_position(landmark_list, img_height)}")
```

## 🎓 Learning Resources

- [Mediapipe Hand Tracking](https://google.github.io/mediapipe/solutions/hands.html)
- [PyAutoGUI Documentation](https://pyautogui.readthedocs.io/)
- [Pycaw Audio Control](https://github.com/AndreMiras/pycaw)

## 🔮 Future Enhancements

- [ ] Custom gesture mapping
- [ ] Gesture recording and playback
- [ ] Multi-hand support
- [ ] Spotify API integration for track info
- [ ] Gesture macros
- [ ] Playlist control
- [ ] Hand distance for volume control

## 🤝 Projects in This Repository

### 1. Air Canvas (`src/air_canvas.py`)
Draw in the air using your index finger

### 2. Gesture Music Controller (`src/music_controller.py`)
Control your music with hand gestures (this project!)

Both projects share the same hand detection utilities in the `utils/` folder.

## 🎉 Enjoy!

Have fun controlling your music with gestures! This is perfect for:
- 🎵 Hands-free music control while cooking
- 💻 Controlling music during presentations
- 🎮 Gaming with background music
- 🏃 Workout playlists
- ♿ Accessibility - no keyboard needed!

---

**Press 'q' to quit the application**

Made with ❤️ using Python, OpenCV, and Mediapipe
