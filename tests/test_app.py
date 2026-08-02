import sys
import os
import unittest

# 將專案根目錄加入 sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from app import app


class TestTarotApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_page(self):
        """測試首頁渲染"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('VibeCodingTarot'.encode('utf-8'), response.data)

    def test_single_card_page(self):
        """測試單張牌頁面渲染（包含 csrf_token）"""
        response = self.app.get('/single-card')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Divination.init('.encode('utf-8'), response.data)

    def test_three_cards_page(self):
        """測試三張牌頁面渲染"""
        response = self.app.get('/three-cards')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Divination.init('.encode('utf-8'), response.data)

    def test_celtic_cross_page(self):
        """測試凱爾特十字頁面渲染"""
        response = self.app.get('/celtic-cross')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Divination.init('.encode('utf-8'), response.data)

    def test_history_page(self):
        """測試歷史記錄頁面渲染"""
        response = self.app.get('/history')
        self.assertEqual(response.status_code, 200)

    def test_api_draw_single_without_csrf(self):
        """測試無 CSRF Token 的請求應被拒絕 (403)"""
        response = self.app.post('/api/draw-single', json={'question': '測試問題'})
        self.assertEqual(response.status_code, 403)

    def test_api_draw_single_valid_csrf(self):
        """測試合法 CSRF Token 的抽牌 API"""
        with self.app.session_transaction() as sess:
            sess['_csrf_token'] = 'valid_test_token'
        response = self.app.post(
            '/api/draw-single',
            json={'question': '測試問題'},
            headers={'X-CSRF-Token': 'valid_test_token'}
        )
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertTrue(json_data['success'])
        self.assertIn('card', json_data['data'])


if __name__ == '__main__':
    unittest.main()
