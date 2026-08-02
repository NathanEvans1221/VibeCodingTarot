# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify, session
import json
import random
from datetime import datetime
import os
import secrets

app = Flask(__name__)

# 配置：SECRET_KEY 從環境變數讀取，未設定時自動生成隨機密鑰
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or secrets.token_hex(32)
app.config['JSON_AS_ASCII'] = False  # 支援中文JSON


def generate_csrf_token():
    """生成 CSRF token 並存入 session"""
    if '_csrf_token' not in session:
        session['_csrf_token'] = secrets.token_hex(32)
    return session['_csrf_token']


# 註冊 Jinja2 全域函數，模板中可使用 {{ csrf_token() }}
app.jinja_env.globals['csrf_token'] = generate_csrf_token


def validate_csrf_token():
    """驗證 CSRF token，失败時回傳 False"""
    token = request.headers.get('X-CSRF-Token') or (request.get_json() or {}).get('_csrf_token')
    return token and token == session.get('_csrf_token')

# 載入塔羅牌數據
def load_tarot_cards():
    """載入塔羅牌數據"""
    try:
        with open('data/tarot_cards.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# 全局變量存儲塔羅牌數據
tarot_cards = load_tarot_cards()

@app.route('/')
def index():
    """主頁"""
    return render_template('index.html', active_page='index')

@app.route('/single-card')
def single_card():
    """單張牌占卜頁面"""
    return render_template('single_card.html', active_page='single')

@app.route('/three-cards')
def three_cards():
    """三張牌占卜頁面"""
    return render_template('three_cards.html', active_page='three')

@app.route('/api/draw-single', methods=['POST'])
def draw_single_card():
    """抽取單張牌API"""
    if not validate_csrf_token():
        return jsonify({'success': False, 'message': 'CSRF 驗證失敗'}), 403
    try:
        data = request.get_json()
        question = data.get('question', '')
        
        # 隨機選擇一張牌
        card = random.choice(tarot_cards)
        
        # 隨機決定正位或逆位
        is_reversed = random.choice([True, False])
        
        result = {
            'card': card,
            'is_reversed': is_reversed,
            'question': question,
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify({
            'success': True,
            'data': result,
            'message': '抽牌成功'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'抽牌失敗: {str(e)}'
        }), 500

@app.route('/api/draw-three', methods=['POST'])
def draw_three_cards():
    """抽取三張牌API"""
    if not validate_csrf_token():
        return jsonify({'success': False, 'message': 'CSRF 驗證失敗'}), 403
    try:
        data = request.get_json()
        question = data.get('question', '')
        
        # 隨機選擇三張不同的牌
        selected_cards = random.sample(tarot_cards, 3)
        
        # 為每張牌隨機決定正位或逆位
        cards_with_position = []
        for i, card in enumerate(selected_cards):
            is_reversed = random.choice([True, False])
            cards_with_position.append({
                'card': card,
                'is_reversed': is_reversed,
                'position': ['過去', '現在', '未來'][i]
            })
        
        result = {
            'cards': cards_with_position,
            'question': question,
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify({
            'success': True,
            'data': result,
            'message': '抽牌成功'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'抽牌失敗: {str(e)}'
        }), 500

@app.route('/api/card/<card_id>')
def get_card_info(card_id):
    """獲取特定牌的信息API"""
    try:
        card = next((c for c in tarot_cards if c['id'] == card_id), None)
        if card:
            return jsonify({
                'success': True,
                'data': card,
                'message': '獲取牌信息成功'
            })
        else:
            return jsonify({
                'success': False,
                'message': '找不到指定的牌'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'獲取牌信息失敗: {str(e)}'
        }), 500

@app.route('/api/save-reading', methods=['POST'])
def save_reading():
    """保存占卜記錄API"""
    if not validate_csrf_token():
        return jsonify({'success': False, 'message': 'CSRF 驗證失敗'}), 403
    try:
        data = request.get_json()
        
        # 這裡可以實現保存到數據庫的邏輯
        # 目前只是簡單返回成功
        reading_id = f"reading_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        return jsonify({
            'success': True,
            'data': {'reading_id': reading_id},
            'message': '占卜記錄保存成功'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'保存占卜記錄失敗: {str(e)}'
        }), 500

if __name__ == '__main__':
    # 確保必要的目錄存在
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)
    os.makedirs('static/images/cards', exist_ok=True)
    os.makedirs('data', exist_ok=True)
    
    # Windows 上 Flask/Werkzeug 停止服務時常見的關閉訊息（WinError 10038），按 CTRL+C 後關閉 socket 觸發，屬於無害異常，可忽略。
    # 若想消除/減少這個訊息，可用以下參數： use_reloader=False
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)
