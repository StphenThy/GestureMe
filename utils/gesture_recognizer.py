"""
Gesture Recognizer Module
Detects and recognizes hand gestures for controlling applications.
"""

import math
import time


class GestureRecognizer:
    """
    Recognizes various hand gestures for application control.
    """
    
    def __init__(self, cooldown_time=1.0):
        """
        Initialize the GestureRecognizer.
        
        Args:
            cooldown_time: Time in seconds between gesture detections to avoid spam
        """
        self.cooldown_time = cooldown_time
        self.last_gesture_time = {}
        self.previous_hand_position = None
        self.swipe_threshold = 150  # Pixels needed for a swipe
        
    def can_trigger_gesture(self, gesture_name):
        """
        Check if enough time has passed since last gesture trigger.
        
        Args:
            gesture_name: Name of the gesture to check
            
        Returns:
            Boolean indicating if gesture can be triggered
        """
        current_time = time.time()
        if gesture_name not in self.last_gesture_time:
            self.last_gesture_time[gesture_name] = 0
        
        if current_time - self.last_gesture_time[gesture_name] >= self.cooldown_time:
            self.last_gesture_time[gesture_name] = current_time
            return True
        return False
    
    def get_hand_center(self, landmark_list):
        """
        Calculate the center point of the hand.
        
        Args:
            landmark_list: List of hand landmarks
            
        Returns:
            Tuple (x, y) of hand center or None
        """
        if len(landmark_list) == 0:
            return None
        
        # Use wrist (landmark 0) as reference point
        return (landmark_list[0][1], landmark_list[0][2])
    
    def detect_swipe(self, landmark_list):
        """
        Detect left or right swipe gestures.
        
        Args:
            landmark_list: List of hand landmarks
            
        Returns:
            'swipe_left', 'swipe_right', or None
        """
        current_position = self.get_hand_center(landmark_list)
        
        if current_position is None:
            self.previous_hand_position = None
            return None
        
        if self.previous_hand_position is not None:
            dx = current_position[0] - self.previous_hand_position[0]
            
            # Swipe right
            if dx > self.swipe_threshold:
                self.previous_hand_position = current_position
                if self.can_trigger_gesture('swipe_right'):
                    return 'swipe_right'
            
            # Swipe left
            elif dx < -self.swipe_threshold:
                self.previous_hand_position = current_position
                if self.can_trigger_gesture('swipe_left'):
                    return 'swipe_left'
        
        self.previous_hand_position = current_position
        return None
    
    def detect_palm_open(self, fingers):
        """
        Detect if palm is fully open (all fingers extended).
        
        Args:
            fingers: List of finger states [thumb, index, middle, ring, pinky]
            
        Returns:
            Boolean
        """
        return all(fingers) and len(fingers) == 5
    
    def detect_peace_sign(self, fingers):
        """
        Detect peace sign (index and middle fingers up, others down).
        
        Args:
            fingers: List of finger states
            
        Returns:
            Boolean
        """
        return (fingers[1] == 1 and fingers[2] == 1 and 
                fingers[0] == 0 and fingers[3] == 0 and fingers[4] == 0)
    
    def detect_fist(self, fingers):
        """
        Detect closed fist (all fingers down).
        
        Args:
            fingers: List of finger states
            
        Returns:
            Boolean
        """
        return not any(fingers)
    
    def detect_thumbs_up(self, fingers):
        """
        Detect thumbs up gesture.
        
        Args:
            fingers: List of finger states
            
        Returns:
            Boolean
        """
        return (fingers[0] == 1 and fingers[1] == 0 and 
                fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0)
    
    def detect_index_up(self, fingers):
        """
        Detect only index finger up (for volume up).
        
        Args:
            fingers: List of finger states
            
        Returns:
            Boolean
        """
        return (fingers[1] == 1 and fingers[0] == 0 and 
                fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0)
    
    def detect_three_fingers_up(self, fingers):
        """
        Detect three fingers up: index, middle, ring (for volume down).
        
        Args:
            fingers: List of finger states
            
        Returns:
            Boolean
        """
        return (fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and 
                fingers[0] == 0 and fingers[4] == 0)
    
    def detect_pinch(self, landmark_list):
        """
        Detect pinch gesture (thumb and index finger close together).
        
        Args:
            landmark_list: List of hand landmarks
            
        Returns:
            Boolean
        """
        if len(landmark_list) == 0:
            return False
        
        # Get thumb tip (4) and index finger tip (8)
        thumb_tip = None
        index_tip = None
        
        for landmark in landmark_list:
            if landmark[0] == 4:
                thumb_tip = (landmark[1], landmark[2])
            elif landmark[0] == 8:
                index_tip = (landmark[1], landmark[2])
        
        if thumb_tip and index_tip:
            # Calculate distance
            distance = math.sqrt(
                (thumb_tip[0] - index_tip[0])**2 + 
                (thumb_tip[1] - index_tip[1])**2
            )
            # Pinch detected if distance is small
            return distance < 40
        
        return False
    
    def get_vertical_hand_position(self, landmark_list, img_height):
        """
        Get the vertical position of the hand (for volume control).
        
        Args:
            landmark_list: List of hand landmarks
            img_height: Height of the image
            
        Returns:
            'top', 'middle', or 'bottom'
        """
        if len(landmark_list) == 0:
            return 'middle'
        
        # Use wrist position
        wrist_y = landmark_list[0][2]
        
        # Divide screen into 3 zones
        if wrist_y < img_height / 3:
            return 'top'
        elif wrist_y > 2 * img_height / 3:
            return 'bottom'
        else:
            return 'middle'
    
    def recognize_gesture(self, fingers, landmark_list, img_height):
        """
        Recognize the current gesture from finger states and landmarks.
        
        Args:
            fingers: List of finger states
            landmark_list: List of hand landmarks
            img_height: Height of the image
            
        Returns:
            Gesture name string or None
        """
        if len(fingers) == 0:
            return None
        
        # Check for swipe first
        swipe = self.detect_swipe(landmark_list)
        if swipe:
            return swipe
        
        # Palm open - Play/Pause
        if self.detect_palm_open(fingers):
            if self.can_trigger_gesture('palm_open'):
                return 'palm_open'
        
        # Peace sign - Mute/Unmute
        elif self.detect_peace_sign(fingers):
            if self.can_trigger_gesture('peace_sign'):
                return 'peace_sign'
        
        # Index finger up - Volume up
        elif self.detect_index_up(fingers):
            if self.can_trigger_gesture('volume_up'):
                return 'volume_up'
        
        # Three fingers up - Volume down
        elif self.detect_three_fingers_up(fingers):
            if self.can_trigger_gesture('volume_down'):
                return 'volume_down'
        
        # Fist - (removed, now using 3 fingers for volume down)
        # elif self.detect_fist(fingers):
        #     position = self.get_vertical_hand_position(landmark_list, img_height)
        #     if position == 'bottom':
        #         if self.can_trigger_gesture('volume_down'):
        #             return 'volume_down'
        
        # Pinch - Fine volume control
        elif self.detect_pinch(landmark_list):
            position = self.get_vertical_hand_position(landmark_list, img_height)
            if position == 'top' and self.can_trigger_gesture('pinch_up'):
                return 'pinch_volume_up'
            elif position == 'bottom' and self.can_trigger_gesture('pinch_down'):
                return 'pinch_volume_down'
        
        return None
