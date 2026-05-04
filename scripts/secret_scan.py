import re
import sys
 
print("Scanning for secrets...")

patterns = [
    r'AKIA[0-9A-Z]{16}', 
    r'(?i)password\s*=\s*["\'].*["\']',
    r'(?i)api_key\s*=\s*["\'].*["\']'
]

with open("app/app.py", "r") as f:   # adjust if needed
    content = f.read() 

for pattern in patterns:
    if re.search(pattern, content):
        print("[FAIL] Secret detected!")
        sys.exit(1)

print("[PASS] No secrets found")
