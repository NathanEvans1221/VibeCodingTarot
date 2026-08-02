# 變更日誌

本文件記錄 VibeCodingTarot 專案的所有重要變更。

格式基於 [Keep a Changelog](https://keepachangelog.com/zh-TW/1.1.0/)，
版本號遵循 [語意化版本](https://semver.org/lang/zh-TW/)。

## [未發佈]

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

### 重構
- 抽取共同 JS 邏輯到 `divination.js` 模組
- 簡化 `single_card.html` 和 `three_cards.html` 的腳本
- 使用 `Divination` 模組統一處理 API 呼叫、載入狀態、錯誤處理
- 清理 `main.js` 未使用代碼（escapeHtml, handleError, showSuccessMessage）
- 提取魔法數字為命名常數（CONSTANTS, APP_CONSTANTS）

### 塔羅牌占卜網站初始版本
- 單張牌占卜功能
- 三張牌（過去-現在-未來）占卜功能
- 22 張 Major Arcana 牌組
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
