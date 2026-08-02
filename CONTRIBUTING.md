# 貢獻指南

感謝你對 VibeCodingTarot 的興趣！本文件說明如何參與貢獻。

## 開發環境設定

### 前置需求
- Python 3.7+
- pip
- Git

### 安裝步驟

1. **Fork 專案**
   - 在 GitHub 上 Fork 此專案

2. **Clone 到本地**
   ```bash
   git clone https://github.com/<你的用戶名>/VibeCodingTarot.git
   cd VibeCodingTarot
   ```

3. **建立虛擬環境**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

4. **安裝依賴**
   ```bash
   pip install -r requirements.txt
   ```

5. **啟動開發伺服器**
   ```bash
   python app.py
   ```

## 開發流程

### 1. 選擇任務
- 查看 [GitHub Issues](https://github.com/chiisen/VibeCodingTarot/issues) 選擇任務
- 或建立新 Issue 提出你的想法

### 2. 建立分支
```bash
# 從 main 建立功能分支
git checkout -b feature/你的功能名稱

# 或從 issue 建立
git checkout -b fix/issue-123
```

### 3. 開發與測試
- 遵循 coding style（見下方規範）
- 確保功能正常運作
- 新增必要的測試

### 4. 提交變更
```bash
git add .
git commit -m "feat(scope): 簡短描述"
```

### 5. 建立 Pull Request
- 推送到你的 Fork
- 在 GitHub 建立 PR，連結相關 Issue

## Commit 規範

格式: `<type>(<scope>): <subject>`

### Type 類型
| Type | 說明 |
|------|------|
| feat | 新功能 |
| fix | Bug 修復 |
| docs | 文件更新 |
| style | 程式碼格式（不影響功能） |
| refactor | 重構（不新增功能/修復 Bug） |
| test | 測試相關 |
| chore | 建置/工具變更 |

### 範例
```
feat(tarot): 新增凱爾特十字牌陣
fix(security): 修復 XSS 漏洞
docs(api): 更新 API 文件
refactor(template): 提取共用 header/footer
```

## 程式碼規範

### Python
- 遵循 PEP 8
- 使用 4 個空格縮排
- 函數和類別需有 docstring

### HTML/CSS/JavaScript
- 使用 2 個空格縮排
- CSS 使用語意化類名
- JavaScript 使用 ES6+ 語法

## 文件更新

- 新功能需更新 `README.md`
- 變更需更新 `CHANGELOG.md`
- 重大架構變更需更新 `ARCHITECTURE.md`

## 問題回報

### Bug 報告
- 清晰的標題和描述
- 重現步驟
- 預期行為 vs 實際行為
- 環境資訊（OS、瀏覽器、Python 版本）

### 功能建議
- 使用案例說明
- 預期行為描述
- 相關 mockup 或範例

## Code Review

所有 PR 需經過 Code Review：
- 確認功能符合需求
- 確認代碼品質
- 確認無安全漏洞
- 確認文件已更新

## 行為準則

- 尊重所有參與者
- 建設性的回饋
- 專注於技術討論
- 適當的溝通語氣

## 問題？

如有任何問題，歡迎在 GitHub Issues 提問！
