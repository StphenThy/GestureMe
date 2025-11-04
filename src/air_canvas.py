"""
Air Canvas - Draw in the air using hand gestures
Main application file
"""

import cv2
import numpy as np
import time
import os
from datetime import datetime
import sys

# Add parent directory to path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.hand_detector import HandDetector


class AirCanvas:
    """
    Air Canvas application that allows drawing using hand gestures.
    """
    
    def __init__(self, camera_index=0, canvas_width=1280, canvas_height=720):
        """
        Initialize the Air Canvas application.
        
        Args:
            camera_index: Webcam index (usually 0 for default camera)
            canvas_width: Width of the canvas
            canvas_height: Height of the canvas
        """
        self.camera_index = camera_index
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        
        # Initialize webcam
        self.cap = cv2.VideoCapture(self.camera_index)
        self.cap.set(3, self.canvas_width)
        self.cap.set(4, self.canvas_height)
        
        # Initialize hand detector
        self.detector = HandDetector(max_hands=1, detection_confidence=0.8)
        
        # Drawing settings
        self.draw_color = (255, 0, 255)  # Default color (Magenta)
        self.brush_thickness = 15
        self.eraser_thickness = 50
        
        # Canvas for drawing
        self.img_canvas = np.zeros((self.canvas_height, self.canvas_width, 3), np.uint8)
        
        # Previous position for smooth drawing
        self.xp, self.yp = 0, 0
        
        # Color palette
        self.colors = {
            'red': (0, 0, 255),
            'green': (0, 255, 0),
            'blue': (255, 0, 0),
            'yellow': (0, 255, 255),
            'magenta': (255, 0, 255),
            'cyan': (255, 255, 0),
            'white': (255, 255, 255)
        }
        
        # Header section height
        self.header_height = 120
        
        # Create header with color options
        self.header = self.create_header()
        
        # FPS calculation
        self.prev_time = 0
        
        # Drawing mode
        self.mode = 'drawing'  # 'drawing' or 'selection'
        
    def create_header(self):
        """
        Create a modern header with color selection buttons and clear button.
        
        Returns:
            Header image
        """
        header = np.zeros((self.header_height, self.canvas_width, 3), np.uint8)
        
        # Modern gradient background
        for i in range(self.header_height):
            alpha = i / self.header_height
            color_val = int(25 + alpha * 35)
            header[i, :] = (color_val, color_val, color_val + 10)
        
        # Title section
        cv2.putText(header, "AIR CANVAS", (20, 35), 
                    cv2.FONT_HERSHEY_DUPLEX, 1.2, (0, 220, 255), 3)
        cv2.putText(header, "Draw in the air with your hand", (20, 65), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (180, 180, 180), 1)
        
        # Modern color palette
        button_width = 130
        button_height = 50
        margin = 15
        y_offset = 70
        start_x = 250
        
        color_names = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan']
        
        for i, color_name in enumerate(color_names):
            x1 = start_x + i * (button_width + margin)
            x2 = x1 + button_width
            y1 = y_offset
            y2 = y1 + button_height
            
            # Glass-morphism effect for color buttons
            overlay = header.copy()
            cv2.rectangle(overlay, (x1, y1), (x2, y2), self.colors[color_name], -1)
            cv2.addWeighted(overlay, 0.85, header, 0.15, 0, header)
            
            # Modern border with glow
            border_color = tuple([min(255, c + 80) for c in self.colors[color_name]])
            cv2.rectangle(header, (x1, y1), (x2, y2), border_color, 3)
            
            # Add color name
            text_color = (255, 255, 255) if color_name not in ['yellow', 'cyan'] else (50, 50, 50)
            cv2.putText(header, color_name.upper()[:3], (x1 + 40, y1 + 33), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, text_color, 2)
        
        # Modern Clear button with gradient
        clear_x1 = self.canvas_width - button_width - 30
        clear_x2 = self.canvas_width - 30
        clear_y1 = y_offset
        clear_y2 = y_offset + button_height
        
        # Gradient background for clear button
        for i in range(clear_y2 - clear_y1):
            alpha = i / (clear_y2 - clear_y1)
            color_val = int(40 + alpha * 20)
            cv2.line(header, (clear_x1, clear_y1 + i), (clear_x2, clear_y1 + i), 
                    (color_val, color_val, color_val), 1)
        
        cv2.rectangle(header, (clear_x1, clear_y1), (clear_x2, clear_y2), (200, 200, 200), 3)
        cv2.putText(header, "CLEAR", (clear_x1 + 25, clear_y1 + 33), 
                    cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255), 2)
        
        return header
    
    def check_header_click(self, x, y):
        """
        Check if a header button was clicked and update settings accordingly.
        
        Args:
            x, y: Click coordinates
        """
        if y > self.header_height:
            return
        
        button_width = 130
        button_height = 50
        margin = 15
        y_offset = 70
        start_x = 250
        
        # Check color buttons
        color_names = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan']
        for i, color_name in enumerate(color_names):
            x1 = start_x + i * (button_width + margin)
            x2 = x1 + button_width
            y1 = y_offset
            y2 = y1 + button_height
            
            if x1 <= x <= x2 and y1 <= y <= y2:
                self.draw_color = self.colors[color_name]
                print(f"Color changed to: {color_name}")
                return
        
        # Check clear button
        clear_x1 = self.canvas_width - button_width - 30
        clear_x2 = self.canvas_width - 30
        if clear_x1 <= x <= clear_x2 and y_offset <= y <= y_offset + button_height:
            self.img_canvas = np.zeros((self.canvas_height, self.canvas_width, 3), np.uint8)
            self.xp, self.yp = 0, 0
            print("Canvas cleared")
    
    def save_drawing(self):
        """
        Save the current drawing to a file.
        """
        # Create saved_drawings folder if it doesn't exist
        save_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'saved_drawings')
        os.makedirs(save_dir, exist_ok=True)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"air_canvas_{timestamp}.png"
        filepath = os.path.join(save_dir, filename)
        
        # Save the canvas
        cv2.imwrite(filepath, self.img_canvas)
        print(f"Drawing saved as: {filename}")
        return filepath
    
    def run(self):
        """
        Main application loop.
        """
        print("=" * 60)
        print("AIR CANVAS - Hand Gesture Drawing")
        print("=" * 60)
        print("\nInstructions:")
        print("  • Index finger UP only → Drawing mode")
        print("  • Index + Middle fingers UP → Selection mode (move cursor)")
        print("  • Click header buttons to change colors or clear canvas")
        print("  • Press 's' to save your drawing")
        print("  • Press 'q' to quit")
        print("\nStarting application...\n")
        
        while True:
            # Read frame from webcam
            success, img = self.cap.read()
            if not success:
                print("Failed to read from camera")
                break
            
            # Flip image for mirror effect
            img = cv2.flip(img, 1)
            
            # Resize to canvas size
            img = cv2.resize(img, (self.canvas_width, self.canvas_height))
            
            # Find hands
            img = self.detector.find_hands(img, draw=True)
            landmark_list = self.detector.find_position(img, draw=False)
            
            if len(landmark_list) != 0:
                # Get index finger tip position (landmark 8)
                x1, y1 = landmark_list[8][1], landmark_list[8][2]
                
                # Get middle finger tip position (landmark 12)
                x2, y2 = landmark_list[12][1], landmark_list[12][2]
                
                # Check which fingers are up
                fingers = self.detector.fingers_up()
                
                # Selection Mode - Index and Middle fingers up
                if fingers[1] and fingers[2]:
                    self.mode = 'selection'
                    self.xp, self.yp = 0, 0
                    
                    # Draw selection cursor
                    cv2.circle(img, (x1, y1), 15, (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, "Selection Mode", (x1 + 20, y1 - 10), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                    
                    # Check if clicking on header
                    self.check_header_click(x1, y1)
                
                # Drawing Mode - Only index finger up
                elif fingers[1] and not fingers[2]:
                    self.mode = 'drawing'
                    
                    # Draw drawing cursor
                    cv2.circle(img, (x1, y1), 15, self.draw_color, cv2.FILLED)
                    
                    # Don't draw on header area
                    if y1 > self.header_height:
                        if self.xp == 0 and self.yp == 0:
                            self.xp, self.yp = x1, y1
                        
                        # Draw line on canvas
                        cv2.line(img, (self.xp, self.yp), (x1, y1), self.draw_color, self.brush_thickness)
                        cv2.line(self.img_canvas, (self.xp, self.yp), (x1, y1), self.draw_color, self.brush_thickness)
                        
                        self.xp, self.yp = x1, y1
                    else:
                        self.xp, self.yp = 0, 0
                else:
                    self.xp, self.yp = 0, 0
            
            # Merge canvas with camera image
            img_gray = cv2.cvtColor(self.img_canvas, cv2.COLOR_BGR2GRAY)
            _, img_inv = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)
            img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)
            img = cv2.bitwise_and(img, img_inv)
            img = cv2.bitwise_or(img, self.img_canvas)
            
            # Add header to the image
            img[0:self.header_height, 0:self.canvas_width] = self.header
            
            # Modern status bar at bottom
            overlay = img.copy()
            status_bar_height = 50
            cv2.rectangle(overlay, (0, self.canvas_height - status_bar_height), 
                         (self.canvas_width, self.canvas_height), (30, 30, 35), -1)
            cv2.addWeighted(overlay, 0.85, img, 0.15, 0, img)
            
            # Calculate and display FPS with modern styling
            curr_time = time.time()
            fps = 1 / (curr_time - self.prev_time)
            self.prev_time = curr_time
            
            # FPS indicator
            cv2.putText(img, f'FPS: {int(fps)}', (15, self.canvas_height - 18), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 255, 100), 2)
            
            # Current color indicator
            color_indicator_x = 150
            cv2.circle(img, (color_indicator_x, self.canvas_height - 25), 15, self.draw_color, -1)
            cv2.circle(img, (color_indicator_x, self.canvas_height - 25), 15, (255, 255, 255), 2)
            cv2.putText(img, "Current Color", (color_indicator_x + 25, self.canvas_height - 18), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
            
            # Display mode with modern badge
            mode_x = self.canvas_width - 250
            mode_color = (100, 255, 100) if self.mode == 'drawing' else (255, 200, 100)
            mode_icon = "[DRAW]" if self.mode == 'drawing' else "[SELECT]"
            mode_text = f"{mode_icon} {self.mode.upper()}"
            cv2.putText(img, mode_text, (mode_x, self.canvas_height - 18), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, mode_color, 2)
            
            # Show the final image
            try:
                cv2.imshow("Air Canvas", img)
                
                # Check if window was closed
                if cv2.getWindowProperty("Air Canvas", cv2.WND_PROP_VISIBLE) < 1:
                    print("\nWindow closed. Exiting Air Canvas...")
                    break
            except:
                print("\nWindow closed. Exiting Air Canvas...")
                break
            
            # Handle key presses
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                print("\nExiting Air Canvas...")
                break
            elif key == ord('s'):
                filepath = self.save_drawing()
                print(f"Saved to: {filepath}")
            elif key == 27:  # ESC key
                print("\nExiting Air Canvas...")
                break
        
        # Cleanup
        self.cap.release()
        cv2.destroyAllWindows()


def main():
    """
    Entry point for the application.
    """
    # Create and run the Air Canvas application
    app = AirCanvas(camera_index=0, canvas_width=1280, canvas_height=720)
    app.run()


if __name__ == "__main__":
    main()
