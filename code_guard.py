# --------------------------------------------
# CodeGuard - A Lightweight Python Script Scanner
# Author: Sukanya Ghosh
# Description:
# This script is built to scan Python code for potentially
# suspicious or dangerous patterns — like use of eval, os.system, etc.
# It's a small static analyzer for security beginners.
# --------------------------------------------

# We're using basic built-in modules only
# So that it's portable and can run anywhere
import re

# These are some common patterns that are often used in malware
# They’re not *always* dangerous, but in most cases they’re worth flagging
dangerous_keywords = [
    "os.system",           # can execute system commands
    "subprocess.Popen",    # can spawn new processes (often used in malware)
    "eval(",               # executes string as code (very risky)
    "exec(",               # executes string as code too
    "socket",              # used for making network connections (e.g., for backdoors)
    "open(",               # used for file access, could be used to read/write sensitive data
    "input(",              # capturing user input, possibly for phishing
    "shutil.rmtree",       # deletes directories - often used in destructive scripts
    "rm -rf",              # *nix command to force delete - might be embedded in shell commands
    "wget", "curl",        # often used to download malicious payloads
]

# Here's a fake script for testing
# You can later replace this with real code from user input or a file
sample_script = '''
import os
os.system("rm -rf /")   # deleting everything? definitely not good
import subprocess
subprocess.Popen("ls -l", shell=True)
print("hello world")
eval("2+2")             # another red flag
'''

# This function scans the code line by line
# If it finds any dangerous keyword, it reports the line number and content
def scan_script(code):
    print("Starting scan...\n")
    flagged_lines = []
    lines = code.split('\n')

    for line_num, line in enumerate(lines, start=1):
        for keyword in dangerous_keywords:
            if keyword in line:
                flagged_lines.append((line_num, keyword, line.strip()))

    if flagged_lines:
        print("Suspicious patterns found:\n")
        for line_num, keyword, content in flagged_lines:
            print(f" - Line {line_num}: `{keyword}` found in → {content}")
    else:
        print("No suspicious patterns detected. All clear!")

# If this script is run directly, run the scan on the sample code
if __name__ == "__main__":
    # You can replace 'sample_script' with any string containing Python code
    scan_script(sample_script)
