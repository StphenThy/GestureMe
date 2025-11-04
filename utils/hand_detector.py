"""
Hand Detector Module
Uses Mediapipe to detect and track hand landmarks in real-time.
"""

import cv2
import mediapipe as mp
import numpy as np


class HandDetector:
    """
    Hand detection class that uses Mediapipe to detect hands and their landmarks.
    """
    
    def __init__(self, mode=False, max_hands=1, detection_confidence=0.7, tracking_confidence=0.7):
        """
        Initialize the HandDetector with Mediapipe settings.
        
        Args:
            mode: Static image mode (False for video stream)
            max_hands: Maximum number of hands to detect
            detection_confidence: Minimum confidence for hand detection
            tracking_confidence: Minimum confidence for hand tracking
        """
        self.mode = mode
        self.max_hands = max_hands
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence
        
        # Initialize Mediapipe hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_hands,
            min_detection_confidence=self.detection_confidence,
            min_tracking_confidence=self.tracking_confidence
        )
        self.mp_draw = mp.solutions.drawing_utils
        
        # Finger tip IDs for landmark detection
        self.tip_ids = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
        
    def find_hands(self, img, draw=True):
        """
        Find hands in the image and optionally draw landmarks.
        
        Args:
            img: Input image (BGR format)
            draw: Whether to draw hand landmarks on the image
            
        Returns:
            Image with or without drawn landmarks
        """
        # Convert BGR to RGB for Mediapipe
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)
        
        # Draw hand landmarks if detected
        if self.results.multi_hand_landmarks and draw:
            for hand_landmarks in self.results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(
                    img, 
                    hand_landmarks, 
                    self.mp_hands.HAND_CONNECTIONS
                )
        
        return img
    
    def find_position(self, img, hand_no=0, draw=True):
        """
        Find the position of hand landmarks.
        
        Args:
            img: Input image
            hand_no: Which hand to track (0 for first hand)
            draw: Whether to draw circles on landmarks
            
        Returns:
            List of landmark positions [id, x, y]
        """
        self.landmark_list = []
        
        if self.results.multi_hand_landmarks:
            if hand_no < len(self.results.multi_hand_landmarks):
                hand = self.results.multi_hand_landmarks[hand_no]
                
                for id, landmark in enumerate(hand.landmark):
                    # Get image dimensions
                    h, w, c = img.shape
                    # Convert normalized coordinates to pixel coordinates
                    cx, cy = int(landmark.x * w), int(landmark.y * h)
                    self.landmark_list.append([id, cx, cy])
                    
                    if draw:
                        cv2.circle(img, (cx, cy), 7, (255, 0, 255), cv2.FILLED)
        
        return self.landmark_list
    
    def fingers_up(self):
        """
        Determine which fingers are up.
        
        Returns:
            List of 5 values (0 or 1) for each finger [Thumb, Index, Middle, Ring, Pinky]
        """
        fingers = []
        
        if len(self.landmark_list) != 0:
            # Thumb (special case - check horizontal position)
            if self.landmark_list[self.tip_ids[0]][1] > self.landmark_list[self.tip_ids[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            
            # Four fingers (check vertical position)
            for id in range(1, 5):
                if self.landmark_list[self.tip_ids[id]][2] < self.landmark_list[self.tip_ids[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
        
        return fingers
    
    def get_finger_position(self, finger_id=8):
        """
        Get the position of a specific finger tip.
        
        Args:
            finger_id: Landmark ID of the finger tip (default 8 for index finger)
            
        Returns:
            Tuple (x, y) or None if not found
        """
        if len(self.landmark_list) != 0:
            for landmark in self.landmark_list:
                if landmark[0] == finger_id:
                    return (landmark[1], landmark[2])
        return None
