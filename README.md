# SMB-CEO-PoC（Samurai）

株式会社サムライTシャツ（東京都青梅市）向けの「支社長代理 / CEO業務代替AIエージェント」プロトタイプ開発環境です。
SMB（中小企業）向け経営者・現場判断代替エージェントのPoCモデルとして、実戦導入可能なアーキテクチャを構築しています。

---

## 体系化フレームワーク（完全移植パッケージ）

本リポジトリは、山本圭氏が実際に構築・運用して成果を出している**「山本圭代理」の実証実績**を元に、4層アーキテクチャ（頭脳・表現・安全装置・手足）をコア基盤として採用しています。

* **[framework_ceo_proxy_architecture.md](file:///c:/Users/keiya/AntiGravity/SMB-CEO-PoC-Samurai/knowledge/framework_ceo_proxy_architecture.md)**: 4層構造、脱AI臭ルール、2段階承認、仮想役員会、導入4ステップの全体仕様。
* **[template_ceo_profile.md](file:///c:/Users/keiya/AntiGravity/SMB-CEO-PoC-Samurai/knowledge/template_ceo_profile.md)**: 社長のログやインタビューから人格・判断基準・安全設定を定義するテンプレートシート。

---

## ディレクトリ構成

```
SMB-CEO-PoC-Samurai/
├── .gemini/
│   └── GEMINI.md              # プロジェクト専用のローカルルール（コンテキスト隔離・守秘規定）
├── prompts/                   # エージェント用システムプロンプト
│   └── ceo_proxy_system_prompt.md  # 支社長代理のコアシステムプロンプト（実戦版）
├── knowledge/                 # 支社長代理の知識ベース（Markdown）
│   ├── framework_ceo_proxy_architecture.md      # 【中核】SMB社長代理構築フレームワーク
│   ├── template_ceo_profile.md                  # 社長プロファイル設定テンプレート
│   ├── knowledge_base_technical.md              # 技術側面（DTF機材・トラブル復旧）
│   ├── knowledge_base_business.md               # 経営側面（PL・戦略・歴史・組織）
│   ├── architecture_subagents_and_tools.md      # サブエージェント群（KOT-MCP等）
│   ├── industry_landscape_screen_vs_dtf.md      # 業界動向・市場構造分析
│   ├── samurai_tshirts_company_profile_and_keywords.md # 会社概要・表記揺れ
│   ├── samurai_tshirts_financial_analysis_11th.md      # 第11期決算分析
│   ├── samurai_tshirts_management_review_11th_12th.md  # 経営所感・戦略チャット
│   └── smb_proxy_agent_roadmap.md               # 全体開発ロードマップ
└── scripts/                   # Google Workspace連携・操作スクリプト
    ├── build_sawada_guide.py
    ├── update_sawada_guide.py
    └── fix_drive_file.py
```

---

## 外部連携リソース
* 作業用Google Drive: `1b6-cEbbj0lB2JFad2p0OgSjms3Rv95hk`（侍AI化プロジェクト）
* Google Chatスペース: `spaces/AAQAIDiKCHY`
