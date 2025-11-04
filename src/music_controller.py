"""
Gesture Music Controller
Control your music playback with hand gestures!
"""

import cv2
import numpy as np
import time
import sys
import os
import pyautogui
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Add parent directory to path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.hand_detector import HandDetector
from utils.gesture_recognizer import GestureRecognizer


class MusicController:
    """
    Music controller application that uses hand gestures to control playback.
    """
    
    # Class variable to track window close
    window_closed = False
    
    def __init__(self, camera_index=0, screen_width=1280, screen_height=720):
        """
        Initialize the Music Controller.
        
        Args:
            camera_index: Webcam index
            screen_width: Width of the display
            screen_height: Height of the display
        """
        self.camera_index = camera_index
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Initialize webcam
        self.cap = cv2.VideoCapture(self.camera_index)
        self.cap.set(3, self.screen_width)
        self.cap.set(4, self.screen_height)
        
        # Initialize hand detector
        self.detector = HandDetector(max_hands=1, detection_confidence=0.8)
        
        # Initialize gesture recognizer
        self.recognizer = GestureRecognizer(cooldown_time=1.5)
        
        # Initialize Windows volume control
        try:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            self.volume = cast(interface, POINTER(IAudioEndpointVolume))
            self.volume_available = True
        except:
            print("Warning: Could not access system volume control")
            self.volume_available = False
        
        # FPS calculation
        self.prev_time = 0
        
        # Current gesture display
        self.current_gesture = None
        self.gesture_display_time = 0
        self.gesture_display_duration = 2.0  # seconds
        
        # PyAutoGUI settings
        pyautogui.PAUSE = 0.1
        
    def control_playback(self, action):
        """
        Control music playback using keyboard shortcuts.
        
        Args:
            action: 'play_pause', 'next', 'previous'
        """
        if action == 'play_pause':
            pyautogui.press('playpause')
            print("🎵 Play/Pause")
        elif action == 'next':
            pyautogui.press('nexttrack')
            print("⏭️ Next Track")
        elif action == 'previous':
            pyautogui.press('prevtrack')
            print("⏮️ Previous Track")
    
    def adjust_volume(self, action):
        """
        Adjust system volume.
        
        Args:
            action: 'up', 'down', 'mute', 'fine_up', 'fine_down'
        """
        if not self.volume_available:
            # Fallback to keyboard controls
            if action == 'up' or action == 'fine_up':
                pyautogui.press('volumeup')
                print("🔊 Volume Up")
            elif action == 'down' or action == 'fine_down':
                pyautogui.press('volumedown')
                print("🔉 Volume Down")
            elif action == 'mute':
                pyautogui.press('volumemute')
                print("🔇 Mute/Unmute")
            return
        
        try:
            current_volume = self.volume.GetMasterVolumeLevelScalar()
            
            if action == 'up':
                new_volume = min(1.0, current_volume + 0.1)
                self.volume.SetMasterVolumeLevelScalar(new_volume, None)
                print(f"🔊 Volume: {int(new_volume * 100)}%")
            elif action == 'down':
                new_volume = max(0.0, current_volume - 0.1)
                self.volume.SetMasterVolumeLevelScalar(new_volume, None)
                print(f"🔉 Volume: {int(new_volume * 100)}%")
            elif action == 'fine_up':
                new_volume = min(1.0, current_volume + 0.05)
                self.volume.SetMasterVolumeLevelScalar(new_volume, None)
                print(f"🔊 Volume: {int(new_volume * 100)}%")
            elif action == 'fine_down':
                new_volume = max(0.0, current_volume - 0.05)
                self.volume.SetMasterVolumeLevelScalar(new_volume, None)
                print(f"🔉 Volume: {int(new_volume * 100)}%")
            elif action == 'mute':
                is_muted = self.volume.GetMute()
                self.volume.SetMute(not is_muted, None)
                print(f"🔇 {'Unmuted' if is_muted else 'Muted'}")
        except Exception as e:
            print(f"Volume control error: {e}")
    
    def process_gesture(self, gesture):
        """
        Process recognized gesture and execute corresponding action.
        
        Args:
            gesture: Gesture name string
        """
        if gesture is None:
            return
        
        self.current_gesture = gesture
        self.gesture_display_time = time.time()
        
        # Map gestures to actions
        if gesture == 'palm_open':
            self.control_playback('play_pause')
        elif gesture == 'swipe_right':
            self.control_playback('next')
        elif gesture == 'swipe_left':
            self.control_playback('previous')
        elif gesture == 'volume_up':
            self.adjust_volume('up')
        elif gesture == 'volume_down':
            self.adjust_volume('down')
        elif gesture == 'pinch_volume_up':
            self.adjust_volume('fine_up')
        elif gesture == 'pinch_volume_down':
            self.adjust_volume('fine_down')
        elif gesture == 'peace_sign':
            self.adjust_volume('mute')
    
    def draw_ui(self, img):
        """
        Draw modern, professional user interface on the image.
        
        Args:
            img: Input image
            
        Returns:
            Image with UI elements
        """
        overlay = img.copy()
        h, w = img.shape[:2]
        
        # Modern gradient header
        header_height = 140
        for i in range(header_height):
            alpha = 0.85 - (i / header_height) * 0.3
            color_intensity = int(30 + (i / header_height) * 20)
            cv2.line(overlay, (0, i), (w, i), (color_intensity, color_intensity, color_intensity + 10), 1)
        cv2.addWeighted(overlay, 0.9, img, 0.1, 0, img)
        
        # Modern title with shadow
        title = "GESTURE MUSIC CONTROLLER"
        title_font = cv2.FONT_HERSHEY_DUPLEX
        title_size = 1.3
        title_thickness = 3
        
        # Shadow
        cv2.putText(img, title, (22, 47), title_font, title_size, (0, 0, 0), title_thickness + 1)
        # Main text with gradient effect
        cv2.putText(img, title, (20, 45), title_font, title_size, (0, 220, 255), title_thickness)
        
        # Subtitle/Instructions
        instructions = "Control your music with hand gestures"
        cv2.putText(img, instructions, (20, 85), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (200, 200, 200), 2)
        
        # Status bar
        status_text = "READY | Press Q/ESC to quit"
        cv2.putText(img, status_text, (20, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (180, 180, 180), 1)
        
        # Modern gesture control panel (right side)
        panel_x = w - 420
        panel_y = 160
        panel_width = 400
        panel_height = 240
        
        # Glass-morphism effect for control panel
        cv2.rectangle(overlay, (panel_x, panel_y - 10), 
                     (panel_x + panel_width, panel_y + panel_height), 
                     (30, 30, 40), -1)
        cv2.addWeighted(overlay, 0.75, img, 0.25, 0, img)
        
        # Panel border
        cv2.rectangle(img, (panel_x, panel_y - 10), 
                     (panel_x + panel_width, panel_y + panel_height), 
                     (0, 220, 255), 2)
        
        # Panel title
        cv2.putText(img, "GESTURE CONTROLS", (panel_x + 20, panel_y + 20), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 220, 255), 2)
        
        # Simplified gesture list - just gesture names and actions
        gestures = [
            ("Palm Open", "Play/Pause"),
            ("Swipe Right", "Next Track"),
            ("Swipe Left", "Previous"),
            ("Index Up", "Vol +"),
            ("3 Fingers", "Vol -"),
            ("Peace Sign", "Mute"),
        ]
        
        y_offset = panel_y + 55
        for gesture, action in gestures:
            # Gesture name
            cv2.putText(img, gesture, (panel_x + 20, y_offset), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.55, (220, 220, 220), 1)
            # Arrow
            cv2.putText(img, "->", (panel_x + 200, y_offset), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 220, 255), 1)
            # Action
            cv2.putText(img, action, (panel_x + 235, y_offset), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.55, (100, 255, 100), 2)
            y_offset += 35
        
        # Modern gesture feedback display
        if self.current_gesture and (time.time() - self.gesture_display_time < self.gesture_display_duration):
            gesture_text = self.current_gesture.replace('_', ' ').upper()
            text_size = cv2.getTextSize(gesture_text, cv2.FONT_HERSHEY_DUPLEX, 1.8, 4)[0]
            text_x = (w - text_size[0]) // 2
            text_y = h - 120
            
            # Animated background with glow effect
            padding = 30
            cv2.rectangle(overlay, (text_x - padding, text_y - 70), 
                         (text_x + text_size[0] + padding, text_y + 25), 
                         (0, 200, 0), -1)
            cv2.addWeighted(overlay, 0.8, img, 0.2, 0, img)
            
            # Border glow
            cv2.rectangle(img, (text_x - padding, text_y - 70), 
                         (text_x + text_size[0] + padding, text_y + 25), 
                         (100, 255, 100), 3)
            
            # Shadow text
            cv2.putText(img, gesture_text, (text_x + 3, text_y + 3), 
                       cv2.FONT_HERSHEY_DUPLEX, 1.8, (0, 0, 0), 6)
            # Main text
            cv2.putText(img, gesture_text, (text_x, text_y), 
                       cv2.FONT_HERSHEY_DUPLEX, 1.8, (255, 255, 255), 4)
        
        return img
    
    @staticmethod
    def on_window_close():
        """Callback when window is closed."""
        MusicController.window_closed = True
    
    def run(self):
        """
        Main application loop.
        """
        print("=" * 70)
        print("🎵 GESTURE MUSIC CONTROLLER")
        print("=" * 70)
        print("\n🎮 Gesture Controls:")
        print("  ✋ Palm Open          → Play/Pause")
        print("  👉 Swipe Right       → Next Track")
        print("  👈 Swipe Left        → Previous Track")
        print("  ☝️  Index Finger Up   → Volume Up")
        print("  🖖 3 Fingers Up      → Volume Down")
        print("  ✌️  Peace Sign        → Mute/Unmute")
        print("\n⌨️  Press 'q' or 'ESC' to quit | Click X to close")
        print("=" * 70)
        print("\n🎬 Starting camera...\n")
        
        # Create window and set close callback
        cv2.namedWindow("Gesture Music Controller", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Gesture Music Controller", self.screen_width, self.screen_height)
        
        while True:
            # Check if window was closed
            if MusicController.window_closed:
                print("\n🛑 Window closed. Exiting...")
                break
            
            # Read frame from webcam
            success, img = self.cap.read()
            if not success:
                print("Failed to read from camera")
                break
            
            # Flip image for mirror effect
            img = cv2.flip(img, 1)
            
            # Resize to screen size
            img = cv2.resize(img, (self.screen_width, self.screen_height))
            
            # Find hands
            img = self.detector.find_hands(img, draw=True)
            landmark_list = self.detector.find_position(img, draw=False)
            
            if len(landmark_list) != 0:
                # Get finger states
                fingers = self.detector.fingers_up()
                
                # Recognize gesture
                gesture = self.recognizer.recognize_gesture(
                    fingers, landmark_list, self.screen_height
                )
                
                # Process gesture
                if gesture:
                    self.process_gesture(gesture)
            
            # Draw UI
            img = self.draw_ui(img)
            
            # Calculate and display FPS
            curr_time = time.time()
            fps = 1 / (curr_time - self.prev_time) if self.prev_time > 0 else 0
            self.prev_time = curr_time
            cv2.putText(img, f'FPS: {int(fps)}', (20, self.screen_height - 20), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            # Show the final image
            cv2.imshow("Gesture Music Controller", img)
            
            # Check if window was closed
            try:
                visible = cv2.getWindowProperty("Gesture Music Controller", cv2.WND_PROP_VISIBLE)
                if visible < 1:
                    print("\n🛑 Window closed. Exiting...")
                    break
            except:
                print("\n🛑 Window closed. Exiting...")
                break
            
            # Handle key presses
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                print("\n🛑 Exiting Gesture Music Controller...")
                break
            elif key == 27:  # ESC key
                print("\n🛑 Exiting Gesture Music Controller...")
                break
        
        # Cleanup
        self.cap.release()
        cv2.destroyAllWindows()


def main():
    """
    Entry point for the application.
    """
    controller = MusicController(camera_index=0, screen_width=1280, screen_height=720)
    controller.run()


if __name__ == "__main__":
    main()
