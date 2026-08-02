# Graph Report - D:/github/chiisen/VibeCodingTarot  (2026-08-02)

## Corpus Check
- Corpus is ~11,200 words - fits in a single context window. You may not need a graph.

## Summary
- 107 nodes · 148 edges · 11 communities (7 shown, 4 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 25 edges (avg confidence: 0.82)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- AI Agent 設定與 API 概念
- Flask 後端路由
- 首頁 UI 螢幕截圖
- 歷史實作與設計系統
- 測試套件
- 前端主程式 (main.js)
- 架構決策記錄
- 占卜模組 (divination.js)
- 代理任務狀態
- 虛擬環境文件

## God Nodes (most connected - your core abstractions)
1. `TestTarotApp` - 9 edges
2. `Base Template` - 8 edges
3. `VibeCodingTarot Homepage Screenshot` - 8 edges
4. `Architecture Decision Records` - 7 edges
5. `API Endpoint /api/draw-single` - 7 edges
6. `API Endpoint /api/draw-three` - 7 edges
7. `validate_csrf_token()` - 6 edges
8. `API Documentation` - 5 edges
9. `PR Workflow` - 5 edges
10. `Changelog` - 4 edges

## Surprising Connections (you probably didn't know these)
- `Base Template` --conceptually_related_to--> `Purple Gradient Theme Decision`  [INFERRED]
  templates/base.html → docs/DECISIONS.md
- `Single Card Template` --references--> `API Endpoint /api/draw-single`  [INFERRED]
  templates/single_card.html → docs/API.md
- `Contributing Guide` --references--> `PR Workflow`  [EXTRACTED]
  CONTRIBUTING.md → CLAUDE.md
- `Celtic Cross Template` --references--> `API Endpoint /api/draw-celtic-cross`  [INFERRED]
  templates/celtic_cross.html → CHANGELOG.md
- `History Template` --implements--> `LocalStorage Persistence (100 entries)`  [INFERRED]
  templates/history.html → CHANGELOG.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **AI Collaboration Configuration Files** — claude_md, agents_md, gemini_md, ai_prompt_template_md, _agent_task_state_md [EXTRACTED 0.95]
- **Divination Page Templates** — templates_index_html, templates_single_card_html, templates_three_cards_html, templates_celtic_cross_html, templates_history_html, templates_base_html [EXTRACTED 1.00]
- **Architecture Decision Records** — concept_json_storage, concept_frontend_rendering, concept_flask_framework, concept_single_page_template, concept_no_account_system, concept_purple_gradient, concept_restful_api [EXTRACTED 1.00]
- **Homepage Visual Layout Sections** — images_tarot01_navigation_menu, images_tarot01_hero_section, images_tarot01_divination_method_selector, images_tarot01_major_arcana_gallery, images_tarot01_feature_highlights, images_tarot01_version_footer [EXTRACTED 1.00]
- **Three Divination Spread Options** — images_tarot01_single_card_spread, images_tarot01_three_card_spread, images_tarot01_celtic_cross_spread [EXTRACTED 1.00]

## Communities (11 total, 4 thin omitted)

### Community 0 - "AI Agent 設定與 API 概念"
Cohesion: 0.19
Nodes (18): AI Prompt Template, API Endpoint /api/card/<card_id>, API Endpoint /api/draw-single, API Endpoint /api/draw-three, API Endpoint /api/save-reading, Conventional Commits (Traditional Chinese), Execution Priority Order, Karpathy AI Principles (+10 more)

### Community 1 - "Flask 後端路由"
Cohesion: 0.20
Nodes (15): celtic_cross(), draw_celtic_cross(), draw_single_card(), draw_three_cards(), generate_csrf_token(), get_card_info(), history(), index() (+7 more)

### Community 2 - "首頁 UI 螢幕截圖"
Cohesion: 0.17
Nodes (15): Celtic Cross Spread Option (凱爾特十字 - 尚未實作), Deep Interpretation Feature (深度解讀), Divination Method Selector (選擇占卜方式), About Tarot Features Section (關於塔羅牌), Hero Section '探索命運的指引', VibeCodingTarot Homepage Screenshot, Major Arcana Card Gallery (大阿爾克那 0-愚者 III-女皇), Top Navigation Menu (首頁/單張牌/三張牌/凱爾特十字/歷史紀錄) (+7 more)

### Community 3 - "歷史實作與設計系統"
Cohesion: 0.21
Nodes (14): Changelog, API Endpoint /api/draw-celtic-cross, Celtic Cross Spread (10 cards), CSRF Protection, Divination JS Module, LocalStorage Persistence (100 entries), Major Arcana (22 cards), Minor Arcana (56 cards) (+6 more)

### Community 4 - "測試套件"
Cohesion: 0.15
Nodes (4): 測試單張牌頁面渲染（包含 csrf_token）, 測試無 CSRF Token 的請求應被拒絕 (403), 測試合法 CSRF Token 的抽牌 API, TestTarotApp

### Community 6 - "架構決策記錄"
Cohesion: 0.32
Nodes (8): Architecture Document, Flask Framework Decision, Frontend Rendering Decision, JSON File Storage Decision, No Account System Decision, Single-Page Template Pattern, Architecture Decision Records, Python Requirements

## Knowledge Gaps
- **16 isolated node(s):** `Divination`, `divinationStyle`, `CONSTANTS`, `style`, `Agent Task State` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Architecture Decision Records` connect `架構決策記錄` to `AI Agent 設定與 API 概念`, `歷史實作與設計系統`?**
  _High betweenness centrality (0.049) - this node is a cross-community bridge._
- **Why does `Base Template` connect `歷史實作與設計系統` to `AI Agent 設定與 API 概念`?**
  _High betweenness centrality (0.038) - this node is a cross-community bridge._
- **What connects `Divination`, `divinationStyle`, `CONSTANTS` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._