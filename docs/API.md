# VibeCodingTarot API 文檔

## 基礎資訊

- **Base URL**: `http://localhost:5000`
- **資料格式**: JSON
- **字符編碼**: UTF-8

## 端點列表

| 方法 | 端點 | 說明 |
|------|------|------|
| GET | `/` | 首頁 |
| GET | `/single-card` | 單張牌占卜頁面 |
| GET | `/three-cards` | 三張牌占卜頁面 |
| POST | `/api/draw-single` | 抽取單張牌 |
| POST | `/api/draw-three` | 抽取三張牌 |
| GET | `/api/card/<card_id>` | 取得特定牌資訊 |
| POST | `/api/save-reading` | 儲存占卜結果 |

---

## 詳細端點說明

### 1. 首頁

**GET** `/`

回傳首頁 HTML 頁面。

**回應**: HTML 頁面

---

### 2. 單張牌占卜頁面

**GET** `/single-card`

回傳單張牌占卜的 HTML 頁面。

**回應**: HTML 頁面

---

### 3. 三張牌占卜頁面

**GET** `/three-cards`

回傳三張牌占卜的 HTML 頁面。

**回應**: HTML 頁面

---

### 4. 抽取單張牌

**POST** `/api/draw-single`

抽取一張隨機塔羅牌。

**請求 body**:
```json
{
  "question": "使用者的問題（選填）"
}
```

**成功回應** (200):
```json
{
  "success": true,
  "data": {
    "card": {
      "id": "the_fool",
      "name": "愚者",
      "name_en": "The Fool",
      "number": 0,
      "arcana": "major",
      "upright_meaning": "新的開始、冒險、自由",
      "reversed_meaning": "魯莽、猶豫、恐懼",
      "description": "愚者代表新的開始和冒險精神...",
      "keywords": ["開始", "冒險", "自由"]
    },
    "is_reversed": false,
    "interpretation": "這張牌暗示著新的開始..."
  },
  "message": "抽取成功"
}
```

**錯誤回應** (400):
```json
{
  "success": false,
  "data": null,
  "message": "請求格式錯誤"
}
```

---

### 5. 抽取三張牌

**POST** `/api/draw-three`

抽取三張隨機塔羅牌，分別代表過去、現在、未來。

**請求 body**:
```json
{
  "question": "使用者的問題（選填）"
}
```

**成功回應** (200):
```json
{
  "success": true,
  "data": {
    "cards": [
      {
        "position": "past",
        "card": {
          "id": "the_magician",
          "name": "魔法師",
          "name_en": "The Magician",
          "number": 1,
          "arcana": "major",
          "upright_meaning": "創造力、意志力、技能",
          "reversed_meaning": "欺騙、操縱、浪費才能",
          "description": "魔法師象徵著創造力和意志力...",
          "keywords": ["創造", "意志", "技能"]
        },
        "is_reversed": true
      },
      {
        "position": "present",
        "card": {
          "id": "the_high_priestess",
          "name": "女祭司",
          "name_en": "The High Priestess",
          "number": 2,
          "arcana": "major",
          "upright_meaning": "直覺、智慧、神秘",
          "reversed_meaning": "隱藏的動機、秘密、困惑",
          "description": "女祭司代表直覺和內在智慧...",
          "keywords": ["直覺", "智慧", "神秘"]
        },
        "is_reversed": false
      },
      {
        "position": "future",
        "card": {
          "id": "the_empress",
          "name": "皇后",
          "name_en": "The Empress",
          "number": 3,
          "arcana": "major",
          "upright_meaning": "豐饒、母性、創造",
          "reversed_meaning": "依賴、過度保護、空虛",
          "description": "皇后象徵著豐饒和母性力量...",
          "keywords": ["豐饒", "母性", "創造"]
        },
        "is_reversed": false
      }
    ],
    "interpretation": {
      "past": "過去的影響是...",
      "present": "目前的情況是...",
      "future": "未來的發展將是..."
    }
  },
  "message": "抽取成功"
}
```

---

### 6. 取得特定牌資訊

**GET** `/api/card/<card_id>`

取得特定塔羅牌的詳細資訊。

**路徑參數**:
- `card_id`: 牌的 ID（例如: `the_fool`, `the_magician`）

**成功回應** (200):
```json
{
  "success": true,
  "data": {
    "id": "the_fool",
    "name": "愚者",
    "name_en": "The Fool",
    "number": 0,
    "arcana": "major",
    "upright_meaning": "新的開始、冒險、自由",
    "reversed_meaning": "魯莽、猶豫、恐懼",
    "description": "愚者代表新的開始和冒險精神...",
    "keywords": ["開始", "冒險", "自由"]
  },
  "message": "查詢成功"
}
```

**錯誤回應** (404):
```json
{
  "success": false,
  "data": null,
  "message": "找不到該牌"
}
```

---

### 7. 儲存占卜結果

**POST** `/api/save-reading`

儲存占卜結果到伺服器。

**請求 body**:
```json
{
  "question": "使用者的問題",
  "spread_type": "single",
  "cards": ["the_fool"],
  "is_reversed": [false],
  "interpretation": "占卜解讀內容",
  "user_notes": "使用者備註（選填）"
}
```

**成功回應** (200):
```json
{
  "success": true,
  "data": {
    "reading_id": "uuid-1234-5678",
    "timestamp": "2026-08-02T12:00:00Z"
  },
  "message": "儲存成功"
}
```

---

## 錯誤碼

| 狀態碼 | 說明 |
|--------|------|
| 200 | 成功 |
| 400 | 請求格式錯誤 |
| 404 | 資源不存在 |
| 500 | 伺服器內部錯誤 |

## 資料結構

### 塔羅牌 (Card)
```json
{
  "id": "string",           // 牌的唯一識別碼
  "name": "string",         // 中文名稱
  "name_en": "string",      // 英文名稱
  "number": "integer",      // 牌號
  "arcana": "string",       // "major" 或 "minor"
  "suit": "string",         // 牌組（僅小阿爾克那）
  "upright_meaning": "string",  // 正位含義
  "reversed_meaning": "string", // 逆位含義
  "description": "string",  // 詳細描述
  "keywords": ["string"]    // 關鍵詞陣列
}
```

### 占卜結果 (Reading)
```json
{
  "question": "string",         // 使用者問題
  "spread_type": "string",      // "single" 或 "three_cards"
  "cards": ["string"],          // 牌 ID 陣列
  "is_reversed": ["boolean"],   // 是否逆位
  "interpretation": "string",   // 解讀內容
  "user_notes": "string",       // 使用者備註
  "timestamp": "datetime"       // 時間戳
}
```

## 使用範例

### cURL 範例

**抽取單張牌**:
```bash
curl -X POST http://localhost:5000/api/draw-single \
  -H "Content-Type: application/json" \
  -d '{"question": "我的愛情運勢如何？"}'
```

**抽取三張牌**:
```bash
curl -X POST http://localhost:5000/api/draw-three \
  -H "Content-Type: application/json" \
  -d '{"question": "我的事業發展？"}'
```

**查詢特定牌**:
```bash
curl http://localhost:5000/api/card/the_fool
```

### JavaScript 範例

```javascript
// 抽取單張牌
async function drawSingleCard(question) {
  const response = await fetch('/api/draw-single', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ question })
  });
  return await response.json();
}

// 使用範例
const result = await drawSingleCard('我的愛情運勢如何？');
console.log(result.data.card.name);
```

### Python 範例

```python
import requests

# 抽取單張牌
response = requests.post(
    'http://localhost:5000/api/draw-single',
    json={'question': '我的愛情運勢如何？'}
)
result = response.json()
print(result['data']['card']['name'])
```
