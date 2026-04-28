

> **⚠️ CRITICAL ETHICAL DISCLAIMER**
> 
> This tool is for **EDUCATIONAL PURPOSES ONLY**. It is designed to demonstrate how keyloggers work so that cybersecurity professionals can better understand, detect, and defend against them.
> 
> **You may only run this software on:**
> - Your own personal computer
> - Systems you have explicit written permission to test
> - Virtual machines or lab environments you control
> 
> **Unauthorized use constitutes:**
> - A violation of privacy laws
> - Computer fraud and abuse (CFAA in the US, similar laws globally)
> - Potential criminal offense
> - Civil liability
> 
> **THE AUTHOR ASSUMES NO RESPONSIBILITY FOR MISUSE OF THIS SOFTWARE.**

---

## 📋 Overview

This project is a simple, educational keylogger written in Python. It captures keyboard events and logs them to a file with timestamps. The purpose is to demonstrate:

- **Event handling and hooks** - How programs can intercept system events
- **Input capture mechanisms** - Understanding how keystrokes can be recorded
- **File I/O operations** - Writing captured data to persistent storage
- **Security awareness** - Understanding malicious techniques to better defend against them

This knowledge is essential for:
- Security analysts investigating potential malware infections
- System administrators implementing defense-in-depth strategies
- Developers building secure applications
- Anyone interested in cybersecurity fundamentals

---

## 🚀 Live Demo

### Sample Session Output

When you run the program, you will see:
╔══════════════════════════════════════════════════════════════╗
║ ║
║ EDUCATIONAL KEYLOGGER DEMO v1.0 ║
║ ║
║ ⚠️ FOR EDUCATIONAL AND RESEARCH PURPOSES ONLY ⚠️ ║
║ ║
╚══════════════════════════════════════════════════════════════╝

By continuing, you confirm that:

You are running this on a system you own

You understand this is for educational purposes

You will not use this tool illegally

Do you understand and agree? (yes/no): yes

Enter log file path (default: keylog.txt): test_log.txt

[+] Log file initialized: test_log.txt

====================================================================
EDUCATIONAL KEYLOGGER DEMO
====================================================================

⚠️ IMPORTANT DISCLAIMER:
This tool is for EDUCATIONAL PURPOSES ONLY.
Use only on systems you own or have explicit permission to test.

📋 Instructions:

Press any key to test the logger

Press ESC to stop the logger

Logs are saved to: test_log.txt

Starting keylogger capture... (Press ESC to stop)

Hello World![ENTER]
This is a test[ENTER]
[ESC]

[!] ESC pressed. Stopping keylogger...

[+] Keylogger stopped. Log saved to test_log.txt

text

### Sample Log File Output

After running the demo, the log file (`keylog.txt`) will contain:

```text
============================================================
EDUCATIONAL KEYLOGGER DEMO - LOG FILE
Session started: 2024-01-15 14:30:22
============================================================

Hello World!
[ENTER]
This is a test
[ENTER]

[SESSION ENDED] 2024-01-15 14:30:45
Demonstration Video (Conceptual)
text
┌─────────────────────────────────────────────────────────────┐
│  User types: "password123"                                  │
│                                                             │
│  Keylogger captures: p a s s w o r d 1 2 3                  │
│                                                             │
│  Log file records: password123                              │
│                                                             │
│  [Security Lesson] A real attacker would use this          │
│  captured password for unauthorized access.                 │
└─────────────────────────────────────────────────────────────┘
🔧 Installation
Prerequisites
Python 3.6 or higher

pip package manager

Step 1: Clone the Repository
bash
git clone https://github.com/nyam0si/keylogger-demo.git
cd keylogger-demo
Step 2: Install Dependencies
bash
pip install -r requirements.txt
Or manually:

bash
pip install pynput
Step 3: Run the Keylogger
bash
python keylogger.py
💻 Usage
Basic Usage
Run python keylogger.py

Confirm the ethical disclaimer by typing yes

Optionally specify a custom log file path

Type normally - all keystrokes will be captured

Press ESC to stop the logger

Check the log file for captured input

Command Line Options (Extensible)
Future versions could support:

bash
python keylogger.py --log-file custom.log --silent --no-banner
Stopping the Keylogger
Press the ESC key at any time to stop the logger

Or use Ctrl+C for keyboard interrupt

