"""
Modern Launcher for Hand Gesture Applications
Professional UI to select between Air Canvas and Music Controller
"""

import tkinter as tk
from tkinter import ttk
import subprocess
import sys
import os


class ModernLauncher:
    """
    Modern launcher application with professional UI.
    """
    
    def __init__(self):
        """Initialize the launcher."""
        self.root = tk.Tk()
        self.root.title("Hand Gesture Applications Launcher")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Set colors - Modern dark theme
        self.bg_color = "#1e1e2e"
        self.card_color = "#2a2a3e"
        self.accent_color = "#00d4ff"
        self.text_color = "#ffffff"
        self.subtitle_color = "#a0a0b0"
        
        self.root.configure(bg=self.bg_color)
        
        # Get project root directory
        self.project_root = os.path.dirname(os.path.abspath(__file__))
        
        self.create_ui()
        
    def create_ui(self):
        """Create the modern UI."""
        # Title Section
        title_frame = tk.Frame(self.root, bg=self.bg_color)
        title_frame.pack(pady=30)
        
        title_label = tk.Label(
            title_frame,
            text="🎨 Hand Gesture Applications",
            font=("Segoe UI", 32, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="Choose your application to start",
            font=("Segoe UI", 12),
            bg=self.bg_color,
            fg=self.subtitle_color
        )
        subtitle_label.pack(pady=5)
        
        # Cards Container
        cards_frame = tk.Frame(self.root, bg=self.bg_color)
        cards_frame.pack(pady=20, padx=50)
        
        # Air Canvas Card
        self.create_app_card(
            cards_frame,
            "🎨 Air Canvas",
            "Draw in the air using your hand",
            [
                "✓ Drawing mode with index finger",
                "✓ Color selection with gestures",
                "✓ Save your artwork",
                "✓ Multiple colors available"
            ],
            self.launch_air_canvas,
            column=0
        )
        
        # Music Controller Card
        self.create_app_card(
            cards_frame,
            "🎵 Music Controller",
            "Control your music with gestures",
            [
                "✓ Play/Pause with palm open",
                "✓ Volume control with gestures",
                "✓ Skip tracks by swiping",
                "✓ Works with any music app"
            ],
            self.launch_music_controller,
            column=1
        )
        
        # Footer
        footer_frame = tk.Frame(self.root, bg=self.bg_color)
        footer_frame.pack(side=tk.BOTTOM, pady=20)
        
        footer_label = tk.Label(
            footer_frame,
            text="Powered by OpenCV & Mediapipe | Press ESC or close window to exit apps",
            font=("Segoe UI", 9),
            bg=self.bg_color,
            fg=self.subtitle_color
        )
        footer_label.pack()
        
    def create_app_card(self, parent, title, subtitle, features, command, column):
        """
        Create a modern card for each application.
        
        Args:
            parent: Parent frame
            title: Card title
            subtitle: Card subtitle
            features: List of features
            command: Function to call on launch
            column: Grid column position
        """
        # Card Frame
        card = tk.Frame(
            parent,
            bg=self.card_color,
            highlightbackground=self.accent_color,
            highlightthickness=2,
            relief=tk.FLAT
        )
        card.grid(row=0, column=column, padx=20, pady=10, sticky="nsew")
        
        # Card content padding
        content_frame = tk.Frame(card, bg=self.card_color)
        content_frame.pack(padx=25, pady=25)
        
        # Title
        title_label = tk.Label(
            content_frame,
            text=title,
            font=("Segoe UI", 20, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )
        title_label.pack(anchor="w", pady=(0, 5))
        
        # Subtitle
        subtitle_label = tk.Label(
            content_frame,
            text=subtitle,
            font=("Segoe UI", 11),
            bg=self.card_color,
            fg=self.subtitle_color
        )
        subtitle_label.pack(anchor="w", pady=(0, 20))
        
        # Features
        for feature in features:
            feature_label = tk.Label(
                content_frame,
                text=feature,
                font=("Segoe UI", 10),
                bg=self.card_color,
                fg=self.text_color,
                anchor="w",
                justify=tk.LEFT
            )
            feature_label.pack(anchor="w", pady=3)
        
        # Launch Button
        launch_btn = tk.Button(
            content_frame,
            text="LAUNCH",
            font=("Segoe UI", 12, "bold"),
            bg=self.accent_color,
            fg="#000000",
            activebackground="#00b8e6",
            activeforeground="#000000",
            relief=tk.FLAT,
            cursor="hand2",
            command=command,
            width=20,
            height=2
        )
        launch_btn.pack(pady=(20, 0))
        
        # Hover effects
        def on_enter(e):
            launch_btn.config(bg="#00b8e6")
        
        def on_leave(e):
            launch_btn.config(bg=self.accent_color)
        
        launch_btn.bind("<Enter>", on_enter)
        launch_btn.bind("<Leave>", on_leave)
        
    def launch_air_canvas(self):
        """Launch the Air Canvas application."""
        print("🎨 Launching Air Canvas...")
        canvas_path = os.path.join(self.project_root, "src", "air_canvas.py")
        
        try:
            # Launch in a new process
            subprocess.Popen([sys.executable, canvas_path])
            print("✅ Air Canvas launched successfully!")
        except Exception as e:
            print(f"❌ Error launching Air Canvas: {e}")
    
    def launch_music_controller(self):
        """Launch the Music Controller application."""
        print("🎵 Launching Music Controller...")
        controller_path = os.path.join(self.project_root, "src", "music_controller.py")
        
        try:
            # Launch in a new process
            subprocess.Popen([sys.executable, controller_path])
            print("✅ Music Controller launched successfully!")
        except Exception as e:
            print(f"❌ Error launching Music Controller: {e}")
    
    def run(self):
        """Run the launcher."""
        print("=" * 60)
        print("🚀 Hand Gesture Applications Launcher")
        print("=" * 60)
        print("\nLauncher window opened. Choose an application to start.\n")
        
        # Center window on screen
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
        self.root.mainloop()


def main():
    """Entry point for the launcher."""
    launcher = ModernLauncher()
    launcher.run()


if __name__ == "__main__":
    main()
