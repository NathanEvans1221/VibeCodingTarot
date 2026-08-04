# Graph Report - VibeCodingTarot  (2026-08-04)

## Corpus Check
- 28 files · ~94,263 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 243 nodes · 294 edges · 20 communities (16 shown, 4 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 25 edges (avg confidence: 0.82)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `5800a0b8`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- CLAUDE.md
- app.py
- VibeCodingTarot Homepage Screenshot
- Base Template
- TestTarotApp
- main.js
- Architecture Decision Records
- divination.js
- Agent Task State
- Venv Setup Notes
- Tarot Card Sprite Redesign — 設計規格
- Tarot Card Sprite Redesign Implementation Plan
- TestCardFlipCss
- test_tarot_sprite.py
- TestTemplatesUseFlip
- TestDivinationPagePreload
- TestApiReturnsSpriteCoords
- TestBuildSpriteFailFast
- TestDownloadSourcesBackoff

## God Nodes (most connected - your core abstractions)
1. `Tarot Card Sprite Redesign Implementation Plan` - 15 edges
2. `TestTarotApp` - 11 edges
3. `Tarot Card Sprite Redesign — 設計規格` - 11 edges
4. `TestTemplatesUseFlip` - 8 edges
5. `TestDivinationPagePreload` - 8 edges
6. `Base Template` - 8 edges
7. `VibeCodingTarot Homepage Screenshot` - 8 edges
8. `TestCardFlipCss` - 7 edges
9. `Architecture Decision Records` - 7 edges
10. `API Endpoint /api/draw-single` - 7 edges

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

## Communities (20 total, 4 thin omitted)

### Community 0 - "CLAUDE.md"
Cohesion: 0.19
Nodes (18): AI Prompt Template, API Endpoint /api/card/<card_id>, API Endpoint /api/draw-single, API Endpoint /api/draw-three, API Endpoint /api/save-reading, Conventional Commits (Traditional Chinese), Execution Priority Order, Karpathy AI Principles (+10 more)

### Community 1 - "app.py"
Cohesion: 0.20
Nodes (15): celtic_cross(), draw_celtic_cross(), draw_single_card(), draw_three_cards(), generate_csrf_token(), get_card_info(), history(), index() (+7 more)

### Community 2 - "VibeCodingTarot Homepage Screenshot"
Cohesion: 0.17
Nodes (15): Celtic Cross Spread Option (凱爾特十字 - 尚未實作), Deep Interpretation Feature (深度解讀), Divination Method Selector (選擇占卜方式), About Tarot Features Section (關於塔羅牌), Hero Section '探索命運的指引', VibeCodingTarot Homepage Screenshot, Major Arcana Card Gallery (大阿爾克那 0-愚者 III-女皇), Top Navigation Menu (首頁/單張牌/三張牌/凱爾特十字/歷史紀錄) (+7 more)

### Community 3 - "Base Template"
Cohesion: 0.21
Nodes (14): Changelog, API Endpoint /api/draw-celtic-cross, Celtic Cross Spread (10 cards), CSRF Protection, Divination JS Module, LocalStorage Persistence (100 entries), Major Arcana (22 cards), Minor Arcana (56 cards) (+6 more)

### Community 4 - "TestTarotApp"
Cohesion: 0.12
Nodes (6): 測試單張牌頁面渲染（包含 csrf_token）, 每張牌都應包含 13 欄 6 列 sprite 座標。, 牌面順序應為 Major 後接四組 Minor。, 測試無 CSRF Token 的請求應被拒絕 (403), 測試合法 CSRF Token 的抽牌 API, TestTarotApp

### Community 6 - "Architecture Decision Records"
Cohesion: 0.32
Nodes (8): Architecture Document, Flask Framework Decision, Frontend Rendering Decision, JSON File Storage Decision, No Account System Decision, Single-Page Template Pattern, Architecture Decision Records, Python Requirements

### Community 11 - "Tarot Card Sprite Redesign — 設計規格"
Cohesion: 0.08
Nodes (24): D1 — 素材：公共領域 JPG sprite sheet, D2 — 載入策略：Lazy load + 預載提示, D3 — 渲染方式：CSS 變數驅動 background-position, D4 — 逆位：data 屬性 + CSS transform, D5 — 向後相容, DoD, Manual QA Checklist, Out of Scope (+16 more)

### Community 12 - "Tarot Card Sprite Redesign Implementation Plan"
Cohesion: 0.12
Nodes (15): File Structure, Self-Review Checklist, Tarot Card Sprite Redesign Implementation Plan, Task 10: 全部測試回歸, Task 11: 手動視覺驗證 78 張牌, Task 12: 建立 Pull Request, Task 1: 為 tarot_cards.json 加入 sprite 座標, Task 2: 建立 sprite sheet 組裝腳本 (+7 more)

### Community 13 - "TestCardFlipCss"
Cohesion: 0.08
Nodes (10): 塔羅牌翻牌動畫 + 自訂 SVG 牌背測試。, tarot-card-back.svg 必須存在。, 正面 .card-face-front 必須旋轉 180deg 以配合背面。, Divination.renderCardWithFlip 必須存在。, 方法應插入 .card-flip-container + .card-flip-inner + 兩個 .card-face。, 應在 front face 呼叫 renderCard 來放 sprite。, 應用 requestAnimationFrame 等一幀才觸發翻牌。, TestCardBackSvg (+2 more)

### Community 14 - "test_tarot_sprite.py"
Cohesion: 0.08
Nodes (6): TestBaseTemplateCss, TestCardSpriteCss, TestDivinationJsSprite, TestHistoryPageNoPreload, TestSpriteCoordinates, TestSpriteSheetAsset

### Community 15 - "TestTemplatesUseFlip"
Cohesion: 0.29
Nodes (4): 不再有「裸的 renderCard(...)」呼叫,確保翻牌動畫全站生效。, escapeHtml 已用於 card name(keyword/position),翻牌動畫不引入 XSS。, 3 個占卜模板都應呼叫 renderCardWithFlip 而非 renderCard。, TestTemplatesUseFlip

### Community 16 - "TestDivinationPagePreload"
Cohesion: 0.42
Nodes (3): 驗證占卜頁模板包含 sprite sheet preload link 與實際卡面容器。, 舊的 inline .card-face 渲染必須移除,否則 sprite CSS 不會生效。, TestDivinationPagePreload

### Community 17 - "TestApiReturnsSpriteCoords"
Cohesion: 0.32
Nodes (4): 驗證 draw API 同時回傳 sprite 座標,且既有欄位未消失。 說明: - app.py 使用自訂 CSRF middleware,token 透過…, 從 /single-card 頁面取得 csrf_token。, 確保新增 sprite 座標後,既有欄位仍完整保留。, TestApiReturnsSpriteCoords

### Community 18 - "TestBuildSpriteFailFast"
Cohesion: 0.29
Nodes (3): 以 patch 過的常數重新 import build_sprite。, 驗證 build_sprite.py 在缺圖時 fail-fast。 需求: - sys.exit(1) - 不產出 sprite(若已存在 stale…, TestBuildSpriteFailFast

### Community 19 - "TestDownloadSourcesBackoff"
Cohesion: 0.29
Nodes (3): 驗證 _http_get_bytes 在 HTTP 5xx 與 URLError 上會退避重試。, 驗證 User-Agent 符合 Wikimedia User-Agent 政策(識別型,不偽裝瀏覽器)。, TestDownloadSourcesBackoff

## Knowledge Gaps
- **49 isolated node(s):** `Divination`, `divinationStyle`, `File Structure`, `Task 1: 為 tarot_cards.json 加入 sprite 座標`, `Task 2: 建立 sprite sheet 組裝腳本` (+44 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `TestDivinationPagePreload` connect `TestDivinationPagePreload` to `test_tarot_sprite.py`?**
  _High betweenness centrality (0.023) - this node is a cross-community bridge._
- **Why does `TestApiReturnsSpriteCoords` connect `TestApiReturnsSpriteCoords` to `test_tarot_sprite.py`?**
  _High betweenness centrality (0.020) - this node is a cross-community bridge._
- **What connects `Divination`, `divinationStyle`, `File Structure` to the rest of the system?**
  _49 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `TestTarotApp` be split into smaller, more focused modules?**
  _Cohesion score 0.11764705882352941 - nodes in this community are weakly interconnected._
- **Should `Tarot Card Sprite Redesign — 設計規格` be split into smaller, more focused modules?**
  _Cohesion score 0.08 - nodes in this community are weakly interconnected._
- **Should `Tarot Card Sprite Redesign Implementation Plan` be split into smaller, more focused modules?**
  _Cohesion score 0.125 - nodes in this community are weakly interconnected._
- **Should `TestCardFlipCss` be split into smaller, more focused modules?**
  _Cohesion score 0.08 - nodes in this community are weakly interconnected._