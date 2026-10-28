import json
import subprocess
import urllib.request
import urllib.parse

GWS_PATH = r"C:\Users\keiya\AntiGravity\kei-agentic-playground\node_modules\@googleworkspace\cli\bin\gws.exe"
TARGET_FOLDER_ID = "1b6-cEbbj0lB2JFad2p0OgSjms3Rv95hk"
DOC_ID = "15_BJinz3LYk7pWUemLYkIE88OdVS0NPePG4aJLQpq6g"

def get_access_token():
    res = subprocess.run([GWS_PATH, "auth", "export"], capture_output=True, text=True, encoding="utf-8")
    lines = res.stdout.strip().split("\n")
    # find json start
    json_str = ""
    for i, line in enumerate(lines):
        if line.strip().startswith("{"):
            json_str = "\n".join(lines[i:])
            break
    creds = json.loads(json_str)
    
    # Refresh token to get access token
    token_url = "https://oauth2.googleapis.com/token"
    data = urllib.parse.urlencode({
        "client_id": creds["client_id"],
        "client_secret": creds["client_secret"],
        "refresh_token": creds["refresh_token"],
        "grant_type": "refresh_token"
    }).encode("utf-8")
    
    req = urllib.request.Request(token_url, data=data, method="POST")
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        return result["access_token"]

def update_file_meta():
    token = get_access_token()
    
    # 1. Get current file parents
    get_url = f"https://www.googleapis.com/drive/v3/files/{DOC_ID}?fields=id,name,parents"
    req = urllib.request.Request(get_url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req) as resp:
        meta = json.loads(resp.read().decode("utf-8"))
        print("Current meta:", meta)
    
    current_parents = meta.get("parents", [])
    remove_parents = ",".join([p for p in current_parents if p != TARGET_FOLDER_ID])
    add_parents = TARGET_FOLDER_ID if TARGET_FOLDER_ID not in current_parents else ""
    
    patch_url = f"https://www.googleapis.com/drive/v3/files/{DOC_ID}"
    params = {}
    if add_parents:
        params["addParents"] = add_parents
    if remove_parents:
        params["removeParents"] = remove_parents
    if params:
        patch_url += "?" + urllib.parse.urlencode(params)
        
    body = {
        "name": "【手順書】社長の判断ログをGeminiで5分で抽出するガイド"
    }
    body_bytes = json.dumps(body, ensure_ascii=False).encode("utf-8")
    
    req = urllib.request.Request(
        patch_url,
        data=body_bytes,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8"
        },
        method="PATCH"
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        print("Updated meta:", json.dumps(res, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    update_file_meta()
