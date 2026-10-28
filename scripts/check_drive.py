import subprocess
import json

gws_path = r"C:\Users\keiya\AntiGravity\kei-agentic-playground\node_modules\@googleworkspace\cli\bin\gws.exe"
params = json.dumps({"q": "'1b6-cEbbj0lB2JFad2p0OgSjms3Rv95hk' in parents and trashed = false"})

res = subprocess.run([gws_path, "drive", "files", "list", "--params", params], capture_output=True, text=True, encoding="utf-8")
print("STDOUT:", res.stdout)
print("STDERR:", res.stderr)
