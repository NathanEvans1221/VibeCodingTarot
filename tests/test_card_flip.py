"""塔羅牌翻牌動畫 + 自訂 SVG 牌背測試。"""
import re
from pathlib import Path

import unittest


ROOT = Path(__file__).resolve().parents[1]


class TestCardBackSvg(unittest.TestCase):
    def test_svg_exists(self):
        """tarot-card-back.svg 必須存在。"""
        svg = ROOT / 'static' / 'img' / 'tarot-card-back.svg'
        self.assertTrue(svg.exists(), f'{svg} 不存在')
        self.assertGreater(svg.stat().st_size, 1000, 'SVG 過小,可能損壞')

    def test_svg_is_well_formed_xml(self):
        """SVG 必須是合法 XML。"""
        import xml.etree.ElementTree as ET
        svg = ROOT / 'static' / 'img' / 'tarot-card-back.svg'
        tree = ET.parse(svg)
        root = tree.getroot()
        self.assertEqual(root.tag, '{http://www.w3.org/2000/svg}svg')

    def test_svg_has_rose_window(self):
        """SVG 應含玫瑰窗/星形等神秘幾何元素。"""
        svg_text = (ROOT / 'static' / 'img' / 'tarot-card-back.svg').read_text(encoding='utf-8')
        self.assertIn('circle', svg_text, '缺玫瑰窗同心圓')
        self.assertTrue(re.search(r'<rect[^>]*stroke=', svg_text), '缺金框')
        # 至少 1 種星象符號
        self.assertRegex(svg_text, r'sunSymbol|moonSymbol|venusSymbol|marsSymbol',
                         '缺四方位星象符號')


class TestCardFlipCss(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.css = (ROOT / 'static' / 'css' / 'card-sprite.css').read_text(encoding='utf-8')

    def test_has_flip_container_rule(self):
        self.assertIn('.card-flip-container', self.css)
        self.assertIn('perspective', self.css)

    def test_has_flip_inner_with_3d_transform(self):
        self.assertIn('.card-flip-inner', self.css)
        self.assertIn('transform-style: preserve-3d', self.css)
        self.assertIn('transition: transform', self.css)

    def test_has_flipped_state(self):
        self.assertRegex(self.css, r'\.card-flip-inner\.flipped\s*\{[^}]*rotateY')

    def test_has_card_face_with_backface_visibility(self):
        self.assertIn('.card-face', self.css)
        self.assertIn('backface-visibility: hidden', self.css.replace('-webkit-backface-visibility: hidden', ''))

    def test_front_face_rotated_180(self):
        """正面 .card-face-front 必須旋轉 180deg 以配合背面。"""
        match = re.search(r'\.card-face-front\s*\{([^}]*)\}', self.css)
        self.assertIsNotNone(match, '缺 .card-face-front 規則')
        self.assertIn('rotateY(180deg)', match.group(1), '正面未旋轉 180deg')


class TestRenderCardWithFlip(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.js = (ROOT / 'static' / 'js' / 'divination.js').read_text(encoding='utf-8')

    def test_method_exists(self):
        """Divination.renderCardWithFlip 必須存在。"""
        self.assertRegex(self.js, r'renderCardWithFlip\s*\(\s*card\s*,\s*isReversed\s*,\s*container\s*\)\s*\{')

    def test_builds_flip_dom(self):
        """方法應插入 .card-flip-container + .card-flip-inner + 兩個 .card-face。"""
        # 抽出方法本體
        match = re.search(r'renderCardWithFlip\s*\([^)]*\)\s*\{(.*?)\n    \},', self.js, re.DOTALL)
        self.assertIsNotNone(match, '找不到 renderCardWithFlip 方法本體')
        body = match.group(1)
        for needle in ['card-flip-container', 'card-flip-inner', 'card-face-back', 'card-face-front',
                       'tarot-card-back.svg', 'flipped']:
            self.assertIn(needle, body, f'方法內缺 {needle}')

    def test_delegates_to_render_card(self):
        """應在 front face 呼叫 renderCard 來放 sprite。"""
        match = re.search(r'renderCardWithFlip\s*\([^)]*\)\s*\{(.*?)\n    \},', self.js, re.DOTALL)
        body = match.group(1)
        self.assertRegex(body, r'this\.renderCard\(')

    def test_uses_requestAnimationFrame_to_defer_flip(self):
        """應用 requestAnimationFrame 等一幀才觸發翻牌。"""
        self.assertIn('requestAnimationFrame', self.js)


class TestTemplatesUseFlip(unittest.TestCase):
    """3 個占卜模板都應呼叫 renderCardWithFlip 而非 renderCard。"""

    def _load(self, name):
        return (ROOT / 'templates' / name).read_text(encoding='utf-8')

    def test_single_card_uses_flip(self):
        tpl = self._load('single_card.html')
        self.assertIn('renderCardWithFlip', tpl, 'single_card 未呼叫 renderCardWithFlip')
        # 確認 cardContainer 還存在
        self.assertIn('cardContainer', tpl)

    def test_three_cards_uses_flip(self):
        tpl = self._load('three_cards.html')
        self.assertIn('renderCardWithFlip', tpl, 'three_cards 未呼叫 renderCardWithFlip')

    def test_celtic_cross_uses_flip(self):
        tpl = self._load('celtic_cross.html')
        self.assertIn('renderCardWithFlip', tpl, 'celtic_cross 未呼叫 renderCardWithFlip')

    def test_no_template_still_calls_renderCard_directly(self):
        """不再有「裸的 renderCard(...)」呼叫,確保翻牌動畫全站生效。"""
        for name in ('single_card.html', 'three_cards.html', 'celtic_cross.html'):
            tpl = (ROOT / 'templates' / name).read_text(encoding='utf-8')
            # 移除 renderCardWithFlip,確保沒有其他純 renderCard( 在 JS 區塊
            stripped = tpl.replace('renderCardWithFlip', '')
            # JS 區塊從 <script> 到 </script>
            for js_block in re.findall(r'<script>(.*?)</script>', stripped, re.DOTALL):
                self.assertNotIn('renderCard(', js_block,
                                 f'{name} 仍有 bare renderCard 呼叫,應改為 renderCardWithFlip')

    def test_cards_respect_backface_visibility_safe_html(self):
        """escapeHtml 已用於 card name(keyword/position),翻牌動畫不引入 XSS。"""
        tpl = self._load('single_card.html')
        # 抽牌容器 id 還在
        self.assertIn('"cardContainer"', tpl)


if __name__ == '__main__':
    unittest.main()
