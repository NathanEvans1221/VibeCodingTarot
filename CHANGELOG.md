# 變更日誌

本文件記錄 VibeCodingTarot 專案的所有重要變更。

格式基於 [Keep a Changelog](https://keepachangelog.com/zh-TW/1.1.0/)，
版本號遵循 [語意化版本](https://semver.org/lang/zh-TW/)。

## [1.0.2] - 2026-08-02

### 修復
- 於 `static/js/divination.js` 補回 `escapeHtml` 轉義防護函數，修復解牌結果畫面拋出 `Divination.escapeHtml is not a function` 錯誤。

## [1.0.1] - 2026-08-02


### 修復
- 註冊 Jinja2 `csrf_token` 全域函數，修復 `single_card` 等頁面 render_template 時拋出 `jinja2.exceptions.UndefinedError: 'csrf_token' is undefined` 錯誤
- 新增 `tests/test_app.py` 單元與迴歸測試，確保所有頁面與 CSRF API 端點運作正常

## [1.0.0] - 2026-08-02

### 新增
- 建立 `static/js/divination.js` 共用占卜模組
- 實作 localStorage 持久化占卜記錄（最多 100 筆）
- 建立 `AGENTS.md` - OpenCode Agent 協調規則
- 建立 `GEMINI.md` - Google Gemini 指令
- 建立 `ARCHITECTURE.md` - 架構文檔
- 建立 `CONTRIBUTING.md` - 貢獻指南
- 建立 `docs/API.md` - API 詳細文檔
- 建立 `docs/DECISIONS.md` - 架構決策紀錄
- 新增 Flask logging 記錄請求與錯誤
- 新增 Flask gzip 壓縮（flask-compress）
- 新增 HTML 頁面快取控制（1 小時）
- 新增字體 preconnect 優化載入速度
- 新增占卜歷史記錄頁面 `/history`
- 導航列新增「歷史記錄」連結
- 新增凱爾特十字占卜功能 `/celtic-cross`
- 新增 `/api/draw-celtic-cross` API 端點
- 新增 56 張 Minor Arcana 牌組資料
- 新增版本號顯示（頁面標題與頁腳）

### 重構
- 抽取共同 JS 邏輯到 `divination.js` 模組
- 簡化 `single_card.html` 和 `three_cards.html` 的腳本
- 使用 `Divination` 模組統一處理 API 呼叫、載入狀態、錯誤處理
- 清理 `main.js` 未使用代碼（escapeHtml, handleError, showSuccessMessage）
- 提取魔法數字為命名常數（CONSTANTS, APP_CONSTANTS）
- 移除假延遲動畫（setTimeout 2000/3000ms）

### 完整功能
- 單張牌占卜功能
- 三張牌（過去-現在-未來）占卜功能
- 凱爾特十字（10 張牌深度占卜）
- 完整 78 張塔羅牌（22 Major Arcana + 56 Minor Arcana）
- RESTful API 端點
- 紫色漸層主題 UI

### 修復
- 修復 SECRET_KEY 硬編碼安全問題
- 修復 XSS 風險
- 新增 CSRF 保護

### 新增
- 建立 `static/js/divination.js` 共用占卜模組
- 實作 localStorage 持久化占卜記錄（最多 100 筆）
- 建立 `AGENTS.md` - OpenCode Agent 協調規則
- 建立 `GEMINI.md` - Google Gemini 指令
- 建立 `ARCHITECTURE.md` - 架構文檔
- 建立 `CONTRIBUTING.md` - 貢獻指南
- 建立 `docs/API.md` - API 詳細文檔
- 建立 `docs/DECISIONS.md` - 架構決策紀錄
- 新增 Flask logging 記錄請求與錯誤
- 新增 Flask gzip 壓縮（flask-compress）
- 新增 HTML 頁面快取控制（1 小時）
- 新增字體 preconnect 優化載入速度
- 新增占卜歷史記錄頁面 `/history`
- 導航列新增「歷史記錄」連結
- 新增凱爾特十字占卜功能 `/celtic-cross`
- 新增 `/api/draw-celtic-cross` API 端點

### 重構
- 抽取共同 JS 邏輯到 `divination.js` 模組
- 簡化 `single_card.html` 和 `three_cards.html` 的腳本
- 使用 `Divination` 模組統一處理 API 呼叫、載入狀態、錯誤處理
- 清理 `main.js` 未使用代碼（escapeHtml, handleError, showSuccessMessage）
- 提取魔法數字為命名常數（CONSTANTS, APP_CONSTANTS）
- 移除假延遲動畫（setTimeout 2000/3000ms）

### 塔羅牌占卜網站初始版本
- 單張牌占卜功能
- 三張牌（過去-現在-未來）占卜功能
- 完整 78 張塔羅牌（22 Major Arcana + 56 Minor Arcana）
- RESTful API 端點
- 紫色漸層主題 UI

### 修復
- 修復 SECRET_KEY 硬編碼安全問題
- 修復 XSS 風險
- 新增 CSRF 保護

### 重構
- 模板繼承架構優化
- JavaScript 共用函數提取

## [0.1.0] - 2026-08-02

### 新增
- 初始版本發佈
- 基本占卜功能實作

---

本專案由 [chiisen] 維護。
