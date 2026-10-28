import json
import subprocess
import sys

GWS_PATH = r"C:\Users\keiya\AntiGravity\kei-agentic-playground\node_modules\@googleworkspace\cli\bin\gws.exe"
DOC_ID = "15_BJinz3LYk7pWUemLYkIE88OdVS0NPePG4aJLQpq6g"

NEW_CONTENT = """【基本方針＆抽出手順】支社長代理AIプロジェクト
〜 秘書ではなく「業務・判断の作業代替」×「最小限のHuman-in-the-Loop」〜

■ 1. 本プロジェクトの基本ポリシー
本プロジェクトで目指すのは、「予定管理や気配りをする秘書」ではありません。
現場の従業員が迷ったときに知識と判断を提供し、作業を前に進める【業務・判断の作業代替エンジン】の構築です。

【設計ポリシー：最小限の Human-in-the-Loop】
・AIの役割：社内ナレッジや過去の判断履歴をもとに、従業員からの相談・確認に対して自律的に一次回答・作業代行を完結させる。
・人間の役割：例外的な未定義案件の判断と、AIが間違えたときの回答修正（フィードバック）のみに限定する。
・ゴール：社長や責任者の拘束時間を最小化しつつ、現場が「回答待ち」で止まる時間をゼロにする。

--------------------------------------------------

■ 2. 短期立ち上げの育成ステップ（最短で戦力化する順序）
ゼロから完璧なマニュアルを作るのではなく、以下の3ステップで短期間に実戦投入可能なAIを育てます。

【ステップ①：初期ナレッジの投入（過去ログの移植）】
・社内マニュアルや規程に加え、過去1年分のメール（社長の生きた判断・指示ログ）をAIに読み込ませる。

【ステップ②：社長の下働きフェーズ（シャドー運用）】
・現場から相談・質問が来たら、まずAIに回答案を作らせる。
・社長はそれを確認し、ズレている部分があればサッと修正してAIに戻す。
・この修正ログ（差分）をルールとして蓄積することで、短期間で社長の判断基準を芯まで学習させる。

【ステップ③：現場投入（自律稼働・例外のみエスカレ）】
・従業員向けにAIを公開し、日常の相談の8割以上をAIが即時回答・作業代行。
・AIが判断できない特殊案件のみ社長にエスカレーションし、最小限の人間介入で会社を回す。

--------------------------------------------------

■ 3. 佳久社長の作業（所要時間：約5分）
ステップ①の元ネタとなる「直近1年間の判断ログ」を、Geminiを使ってGmailから抽出します。
プロンプトを2回コピペするだけで完了します。

【手順1】Gemini（無料版）を開く
1. PCまたはスマホで Gemini（ https://gemini.google.com ）を開きます。
2. 拡張機能で「Google Workspace（Gmail等）」がオンになっていることを確認します（通常は初期設定でオン）。

【手順2】直近1年の「頻出判断・指示TOP10」を抽出
Geminiのチャット欄に、以下の枠内の文章をそのままコピペして送信してください。

▼ コピペ用プロンプト①（頻出判断の抽出）：
==================================================
@Gmail 
直近1年間のメールを検索して、以下の内容を分析してください。

1. 社員や部下から「判断や指示を求められた業務上の相談」
2. トラブル対応や例外処理で私が指示を出した内容
3. 業務の進め方やルール・仕様についてよく聞かれる質問

これらをパターン化して、「私がよく判断・指示している頻出テーマ TOP10」を箇条書きで教えてください。
==================================================

【手順3】重要テーマの判断ロジックをDocsに書き出す
TOP10が出たら、特に属人化しているテーマや現場から頻繁に聞かれる番号（例：1番と3番）を選び、続けてGeminiにこう指示してください。

▼ コピペ用プロンプト②（判断ロジックの詳細化）：
==================================================
@Gmail 
上記の「○番」と「○番」について、私が社員や相手に送った具体的な指示・判断内容・メール文面を時系列で詳しく要約して書き出してください。
（どういう条件・基準で私が判断・回答しているかが分かるようにまとめてください）
==================================================
※「○番」は実際の番号に置き換えてください。

【手順4】Docsをエクスポートして共有フォルダに配置
1. Geminiの回答の右下にある「共有アイコン（上矢印マーク等）」をクリックし、「Google ドキュメントにエクスポート」を選択します。
2. 作成されたGoogle Docsを、この作業用フォルダ（「侍AI化プロジェクト」）に保存・移動してください。

--------------------------------------------------

■ 4. 今後の進行（山本側での実装）
共有いただいたDocsをもとに、山本側で以下の実装を進めます：
1. 抽出された判断ロジックをAIの実行ルールに落とし込み、支社長代理エージェントのプロトタイプを構築
2. 社長の「下働き」として従業員からの相談に回答案を返すテスト環境を準備
"""

def update_document():
    # 1. Get current document end index
    cmd_get = [GWS_PATH, "docs", "documents", "get", "--params", json.dumps({"documentId": DOC_ID})]
    res = subprocess.run(cmd_get, capture_output=True, text=True, encoding="utf-8")
    data = json.loads(res.stdout)
    end_index = data["body"]["content"][-1]["endIndex"]
    
    requests = []
    # Delete existing text if any (leaving 1 char at the end as required by Docs API)
    if end_index > 2:
        requests.append({
            "deleteContentRange": {
                "range": {
                    "startIndex": 1,
                    "endIndex": end_index - 1
                }
            }
        })
    
    # Insert new text
    requests.append({
        "insertText": {
            "location": {
                "index": 1
            },
            "text": NEW_CONTENT
        }
    })
    
    payload = json.dumps({"requests": requests}, ensure_ascii=True)
    params = json.dumps({"documentId": DOC_ID}, ensure_ascii=True)
    
    cmd_update = [GWS_PATH, "docs", "documents", "batchUpdate", "--params", params, "--json", payload]
    res_up = subprocess.run(cmd_update, capture_output=True, text=True, encoding="utf-8")
    print("Update status:", res_up.returncode)
    if res_up.returncode != 0:
        print("Update error:", res_up.stderr)
    else:
        print("Updated successfully!")

if __name__ == "__main__":
    update_document()
