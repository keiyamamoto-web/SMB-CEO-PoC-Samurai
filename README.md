# SMB-CEO-PoC（Samurai）

株式会社サムライTシャツ（東京都青梅市）向けの「支社長代理 / CEO業務代替AIエージェント」プロトタイプ開発環境です。
SMB（中小企業）向け経営者・現場判断代替エージェントのPoCモデルとして構築しています。

## ディレクトリ構成

```
SMB-CEO-PoC（Samurai）/
├── .gemini/
│   └── GEMINI.md              # プロジェクト専用のローカルルール（コンテキスト隔離・守秘規定）
├── knowledge/                 # 支社長代理の知識ベース（Markdown）
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

## 外部連携リソース
* 作業用Google Drive: `1b6-cEbbj0lB2JFad2p0OgSjms3Rv95hk`（侍AI化プロジェクト）
* Google Chatスペース: `spaces/AAQAIDiKCHY`
