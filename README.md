# Python Threat Scanner: A Lightweight Static Analyzer for Suspicious Python Scripts

## 1. Introduction

As a Python enthusiast exploring cybersecurity, I realized how dangerous even a few lines of malicious code can be.  
That curiosity led me to build **Python Threat Scanner** — a lightweight tool that simulates basic antivirus behavior by **scanning Python scripts** for **suspicious patterns**.

Instead of executing unknown code, this tool **analyzes the script statically** — just like a human would — and raises alerts if it finds risky operations like system command executions, network activities, or dynamic code evaluation.

Think of it as a code buddy who quietly taps you on the shoulder when something looks "off."

---

## 2. Objective

The goal behind Python Threat Scanner is to:

- Explore static analysis concepts in cybersecurity.
- Detect dangerous function calls without running the code.
- Build a simple, beginner-friendly, fully offline tool using only pure Python.
- Make learning cybersecurity fun, practical, and hands-on.

---

## 3. Why Static Analysis?

Normally, antivirus systems use **dynamic analysis** (watching how code behaves at runtime).  
However, **static analysis** — inspecting code before running it — is safer for early threat detection and beginner projects.

With static analysis, we can:

- Avoid running dangerous code accidentally.
- Detect suspicious patterns just by reading the script.
- Practice secure coding and basic cybersecurity habits.

---

## 4. How Python Threat Scanner Works

The scanner works by:

- Reading a given Python script (either hardcoded or passed dynamically).
- Searching each line for **known dangerous patterns**.
- Reporting any matches with line number and context.

---

## 5. Suspicious Patterns Detected

Currently, the scanner flags usage of:

- `os.system()` → Executes system commands
- `subprocess.Popen()` → Spawns new processes
- `eval()`, `exec()` → Dynamically evaluates strings as code
- `socket` → Network connections (possible backdoors)
- `open()` → File operations (data leaks, modifications)
- `input()` → Capturing user input (phishing risk)
- `shutil.rmtree()` → Deletes directories (destructive)
- `wget`, `curl` → Downloads from external sources
- `rm -rf` → Unix force delete (extremely destructive)

---

## 6. Sample Code Example

Example of a script that would be flagged:

```python
import os
os.system("rm -rf /")         # deleting all files - super dangerous
subprocess.Popen("ls", shell=True)  # spawning shell
eval("2+2")                   # executing code dynamically
```

The scanner would flag:

```
Suspicious: Line 2 → os.system
Suspicious: Line 3 → subprocess.Popen
Suspicious: Line 4 → eval
```

---

## 7. How to Use

**Step 1:**  
Paste or load any Python script into the `sample_script` variable inside `code_guard.py`.

**Step 2:**  
Run the script:

```bash
python code_guard.py
```

**Step 3:**  
View the flagged suspicious lines printed in the terminal.

That’s it. No external installation or setup needed.

---

## 8. Limitations

- It doesn't deeply understand code logic (only matches patterns).
- It might show false positives (not all `open()` or `input()` are bad).
- It doesn't scan multiple files automatically.
- It cannot detect obfuscated or hidden threats yet.

---

## 9. Future Enhancements

- Allow dynamic file uploads for scanning
- Assign a "risk score" to each file
- Build a GUI version with Tkinter or Streamlit
- Add support for regex-based matching
- Handle scanning nested folders recursively

---

## 10. Final Thoughts

**Python Threat Scanner** is my first step into blending cybersecurity and coding into real-world tools.  
It’s lightweight, simple, and designed with learning in mind — to help beginners like me **read code critically** instead of trusting everything blindly.

Security awareness begins from curiosity, and curiosity begins with projects like these.

---

## 11. Author

**Sukanya Ghosh**  
Cybersecurity Enthusiast | Python Developer | Tech Journal Writer  
GitHub: https://github.com/SukanyaGhosh6


