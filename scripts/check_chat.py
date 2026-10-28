import subprocess
import json

gws_path = r"C:\Users\keiya\AntiGravity\kei-agentic-playground\node_modules\@googleworkspace\cli\bin\gws.exe"
params = json.dumps({"parent": "spaces/AAQAIDiKCHY", "pageSize": 5})

res = subprocess.run([gws_path, "chat", "spaces", "messages", "list", "--params", params], capture_output=True, text=True, encoding="utf-8")
print("STDOUT:", res.stdout)
print("STDERR:", res.stderr)
