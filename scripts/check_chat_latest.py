import subprocess
import json

gws_path = r"C:\Users\keiya\AntiGravity\kei-agentic-playground\node_modules\@googleworkspace\cli\bin\gws.exe"
params = json.dumps({"parent": "spaces/AAQAIDiKCHY", "pageSize": 5, "orderBy": "createTime desc"})

res = subprocess.run([gws_path, "chat", "spaces", "messages", "list", "--params", params], capture_output=True, text=True, encoding="utf-8")
data = json.loads(res.stdout)
for msg in data.get("messages", []):
    sender = msg.get("sender", {}).get("displayName", "")
    time = msg.get("createTime", "")
    text = msg.get("text", "")
    print(f"[{time}] {sender}: {text}")
