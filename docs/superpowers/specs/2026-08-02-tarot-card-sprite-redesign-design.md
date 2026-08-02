# Tarot Card Sprite Redesign — 設計規格

**日期**：2026-08-02
**狀態**：Draft（待使用者審查）
**關聯**：brainstorming 流程產出、風格方向 = 古典神秘 (Style A)

---

## 目標

以單一公共領域 sprite sheet 取代目前純文字塔羅牌面，採用 Rider-Waite 古典圖像，涵蓋全部 78 張牌。對齊「古典神秘」星空美學（呼應 issue #24）。

---

## 背景

目前狀態：
- 卡面僅顯示 `name`、`name_en`、`suit` 純文字
- 卡片背面為 🃏 emoji + 深色框 + 金色描邊
- 無古典塔羅圖像，缺乏神秘學質感
- 78 張完整牌組資料已備齊（22 Major + 56 Minor），卡面卻無對應視覺

卡面是整個應用的視覺焦點，也是使用者「抽牌」時第一眼看到的元素。

---

## 設計決策

### D1 — 素材：公共領域 JPG sprite sheet

| 項目 | 規格 |
|---|---|
| 來源 | Wikimedia Commons Rider-Waite Tarot deck（1909，Pamela Colman Smith 原圖） |
| 授權 | Public Domain（1909 年出版，無著作權限制） |
| 格式 | 單一 JPG sprite sheet |
| 尺寸 | 2600 × 2040 px |
| 網格 | 13 欄 × 6 列 = 78 格（每格 200 × 340 px） |
| 品質 | JPEG quality 85，預估 ~5 MB |

**為何選 JPG 而非 SVG sprite**：搜尋結果顯示無「78 張完整 + 寬鬆授權 + SVG sprite」組合。Wikimedia 上的 Rider-Waite 原圖皆為 JPG。Game-icons.net 雖有 SVG 但僅覆蓋部分符號且為 CC-BY 3.0。

### D2 — 載入策略：Lazy load + 預載提示

- 首張牌渲染時才觸發 sprite 抓取（不在首頁預載）
- 占卜頁（`/single-card`、`/three-cards`、`/celtic-cross`）加入 `<link rel="preload" as="image" href="tarot_sprite.jpg">` 提示瀏覽器
- 首頁、歷史頁不預載
- 載入中佔位：背景色 `--color-cosmos` + 1.2s pulse 動畫（CSS `@keyframes`）

### D3 — 渲染方式：CSS 變數驅動 background-position

```css
.tarot-card-image {
  background-image: url('../img/tarot_sprite.jpg');
  background-size: 2600px 2040px;
  background-repeat: no-repeat;
  background-position: var(--sprite-pos, 0 0);
  width: 200px;
  height: 340px;
}
.tarot-card-image[data-reversed="true"] {
  transform: rotate(180deg);
}
```

```js
const posX = -card.sprite_x * 200;
const posY = -card.sprite_y * 340;
imgEl.style.setProperty('--sprite-pos', `${posX}px ${posY}px`);
imgEl.setAttribute('data-card', card.id);
imgEl.setAttribute('data-reversed', card.reversed ? 'true' : 'false');
```

- 避免 78 條硬編碼 CSS 規則
- 卡 id 透過 `data-card` 屬性保留，方便偵錯與測試
- 一張 sprite sheet 取代 78 個獨立 HTTP 請求

### D4 — 逆位：data 屬性 + CSS transform

- 逆位旗標儲存於 `.tarot-card-image` 的 `data-reversed="true"`
- CSS transform `rotate(180deg)` 套用於卡面元素
- 與既有 hover 翻牌動畫（父層 `rotateY`）不衝突：父子 transform 各管各軸

### D5 — 向後相容

- API 回應保留所有既有欄位，僅新增 `sprite_x`、`sprite_y`
- localStorage 內舊有讀記錄不丟失，下次重播時補上新欄位（從 JSON 反查）
- 缺 sprite 座標的牌 → 降級為純文字版卡面

---

## 元件

### 新增檔案

| 檔案 | 用途 |
|---|---|
| `static/img/tarot_sprite.jpg` | 2600×2040 sprite sheet，78 張 Rider-Waite 原圖 |
| `static/css/card-sprite.css` | `.tarot-card-image` 基底規則 + `data-reversed` 規則 + pulse 動畫 |

### 修改檔案

| 檔案 | 變更 |
|---|---|
| `data/tarot_cards.json` | 每張牌新增 `sprite_x` (0–12)、`sprite_y` (0–5) 兩個欄位 |
| `static/js/divination.js` | 擴充 `renderCard(card)`：計算 `--sprite-pos`、設定 `data-card` 與 `data-reversed`、座標 clamp |
| `templates/single_card.html` | 新增 preload link、卡面 DOM 改用 `.tarot-card-image` |
| `templates/three_cards.html` | 同上 |
| `templates/celtic_cross.html` | 同上 |
| `templates/history.html` | 不預載；渲染時依賴既有 localStorage 內 sprite 座標 |

### 保持不變

- `app.py` 所有路由
- API endpoint 簽章與回傳格式（僅擴充欄位）
- CSRF / localStorage 容量上限（100 筆）/ 版本顯示
- 占卜流程、誤差訊息、loading 狀態

---

## 資料流程

```
[使用者點擊抽牌]
   ↓
1. templates/*.html：submit 事件
   ↓
2. divination.js → POST /api/draw-{single|three|celtic-cross}
   body: { question, csrf_token }
   ↓
3. app.py draw_*()：
   - 讀 data/tarot_cards.json（已含 sprite_x/sprite_y）
   - 隨機抽牌 + 隨機正逆位
   - 回傳 { success, data: { card: { id, name, name_en, suit,
                                     number, sprite_x, sprite_y,
                                     upright_meaning, reversed_meaning,
                                     reversed } } }
   ↓
4. divination.js renderCard(card)：
   - clamp sprite_x ∈ [0,12]、sprite_y ∈ [0,5]
   - 計算 --sprite-pos 並 setProperty
   - 設定 data-card 與 data-reversed 屬性
   ↓
5. 瀏覽器渲染：
   - 首次需要圖 → lazy load tarot_sprite.jpg
   - 載入中顯示 pulse 動畫
   - CSS background-position 切到對應格
   - data-reversed="true" → rotate(180deg)
   ↓
6. localStorage.setItem('readings', ...) 含 sprite_x/sprite_y
   ↓
7. /history 重播：讀 localStorage → renderCard() → 視覺還原
```

---

## 錯誤處理

| 情境 | 策略 | 使用者體驗 |
|---|---|---|
| Sprite JPG 載入失敗（404 / 網路中斷 / 損壞） | `onerror` listener：移除 `background-image`，疊加 `.tarot-card-fallback` 文字層（顯示 `card.name` + suit 符號） | 卡框與牌名仍可見 |
| JSON 缺 sprite 座標（舊資料 / 新增牌漏欄位） | `renderCard()` 偵測 `sprite_x === undefined` → 直接走 fallback 路徑 | 同上 |
| Sprite 座標越界（手誤填 `sprite_x: 99`） | JS clamp：`Math.min(Math.max(v, 0), 12)` | 永遠顯示有效格 |
| Sprite 載入延遲（首次需要圖時還在下載） | 背景色 `--color-cosmos` + 1.2s pulse 動畫 | 視覺連貫，無白屏閃爍 |
| 翻牌 hover 與逆位衝突 | 子層（data-reversed）管 Z 軸旋轉、父層（:hover）管 Y 軸翻面 | 兩動畫可同時存在 |

### 觀測性

| 事件 | 記錄 |
|---|---|
| Sprite 404 / onerror | `console.warn('[tarot-sprite] 載入失敗,fallback 至文字版', card.id)` |
| 座標越界被 clamp | `console.warn('[tarot-sprite] 座標越界', card.id, rawX, rawY)` |

---

## 測試

### 單元測試（擴充 `tests/test_app.py`）

- `test_all_78_cards_have_sprite_coords`：78 張牌都有 `sprite_x ∈ [0,12]`、`sprite_y ∈ [0,5]`
- `test_sprite_coords_unique`：每格最多一張牌
- `test_sprite_coords_no_gaps`：78 個座標形成連續區塊
- `test_api_draw_single_includes_sprite`：API 回傳含 `sprite_x`、`sprite_y`
- `test_api_backward_compat`：既有 `id/name/meaning` 欄位未消失
- `test_sprite_jpg_exists`：`static/img/tarot_sprite.jpg` 存在
- `test_sprite_jpg_dimensions`：解析 JPG header，2600×2040 ±5px
- `test_render_card_js_contains_sprite_logic`：`divination.js` 含 `setProperty('--sprite-pos'` 與 `data-card`
- `test_card_sprite_css_present`：`card-sprite.css` 含 `.tarot-card-image` 規則

### 整合測試（Flask test client）

- `test_homepage_does_not_reference_sprite`：GET `/` HTML 不含 `tarot_sprite.jpg` 字串
- `test_single_card_preloads_sprite`：GET `/single-card` 含 preload link
- `test_three_cards_preloads_sprite`：同上
- `test_celtic_cross_preloads_sprite`：同上
- `test_history_does_not_preload_sprite`：GET `/history` 不預載

### 錯誤注入測試

- `test_missing_sprite_fallback`：暫時改名 sprite JPG → 重新 render → DOM 出現 `.tarot-card-fallback`、文字含 `card.name`
- `test_clamped_sprite_coords`：注入 `sprite_x=99, sprite_y=-5` → clamp 後合法
- `test_reversed_rotation_applied`：抽到逆位 → `data-reversed="true"` + computed transform 含 180°

### Manual QA Checklist

- [ ] 22 Major Arcana 各抽一次，目視確認位置正確
- [ ] 56 Minor Arcana 各抽一次（每 suit 14 張），目視確認
- [ ] 隨機逆位 5 次，確認 rotate 180° 無裁切溢出
- [ ] Hover 翻牌動畫在正/逆位皆流暢
- [ ] 行動裝置（375px / 768px）sprite 縮放清晰
- [ ] DevTools throttle 3G → pulse 動畫連貫
- [ ] Fallback 文字版在 sprite 缺失時仍堪用
- [ ] 螢幕閱讀器可讀到卡名（a11y）

---

## DoD

- [ ] 全部單元 + 整合 + 錯誤注入測試通過
- [ ] Manual QA 78 張全數通關（截圖存 `tests/visual_baseline/`）
- [ ] 既有測試無 regression
- [ ] `CHANGELOG.md` `[Unreleased]` 新增條目
- [ ] PR 描述附 sprite sheet 來源（Wikimedia Commons URL + 授權聲明）
- [ ] SPEC 文件 commit

---

## Out of Scope

- 進場動畫（粒子、光暈）— 後續優化項目
- 卡背重新設計 — 使用者指定只動卡面
- 卡面意義文字擴充 — 獨立議題
- 自動 sprite 生成腳本 — v1 手動產出，腳本作為後續
- a11y 鍵盤操作強化 — 基礎保留（卡名可讀），完整鍵盤支援後續

---

## 待釐清問題

無。設計決策於 brainstorming 階段全部解決。