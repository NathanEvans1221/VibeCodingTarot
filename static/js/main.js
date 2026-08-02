// 主要JavaScript功能

// 常數定義
const CONSTANTS = {
    // 動畫時間 (毫秒)
    CARD_FLIP_DELAY: 1000,
    BUTTON_PRESS_DELAY: 150,
    CARD_DRAW_ANIMATION: 600,
    RESULT_SHOW_DELAY: 100,

    // 訊息顯示時間 (毫秒)
    MESSAGE_DISPLAY_TIME: 3000,
    MESSAGE_ANIMATION_TIME: 300,

    // localStorage 設定
    MAX_READINGS: 100,

    // 頁面路徑
    PATHS: {
        SINGLE_CARD: '/single-card',
        THREE_CARDS: '/three-cards'
    }
};

// 分享結果
function shareResult(defaultTitle, defaultText) {
    if (navigator.share) {
        navigator.share({
            title: defaultTitle || '我的塔羅牌占卜結果',
            text: defaultText || '我在 VibeCodingTarot 進行了塔羅牌占卜，快來看看結果吧！',
            url: window.location.href
        });
    } else {
        const resultText = document.querySelector('.card-result, .three-cards-result')?.innerText;
        if (resultText) {
            navigator.clipboard.writeText(resultText).then(() => {
                alert('占卜結果已複製到剪貼板！');
            });
        }
    }
}

// 頁面載入完成後執行
document.addEventListener('DOMContentLoaded', function() {
    initializePage();
    addAnimationEffects();
    setupEventListeners();
});

// 初始化頁面
function initializePage() {
    console.log('VibeCodingTarot 網站已載入');
}

// 添加動畫效果
function addAnimationEffects() {
    // 為選項卡片添加懸停效果
    const optionCards = document.querySelectorAll('.option-card');
    optionCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });

    // 為塔羅牌預覽添加翻轉效果
    const cardPreviews = document.querySelectorAll('.card-preview .card-back');
    cardPreviews.forEach(card => {
        card.addEventListener('click', function() {
            this.style.transform = 'rotateY(180deg)';
            setTimeout(() => {
                this.style.transform = 'rotateY(0deg)';
            }, CONSTANTS.CARD_FLIP_DELAY);
        });
    });
}

// 設置事件監聽器
function setupEventListeners() {
    // 為抽牌按鈕添加點擊效果
    const drawButtons = document.querySelectorAll('.draw-button');
    drawButtons.forEach(button => {
        button.addEventListener('click', function() {
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, CONSTANTS.BUTTON_PRESS_DELAY);
        });
    });

    // 為動作按鈕添加點擊效果
    const actionButtons = document.querySelectorAll('.action-button');
    actionButtons.forEach(button => {
        button.addEventListener('click', function() {
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, CONSTANTS.BUTTON_PRESS_DELAY);
        });
    });
}

// 導航功能
function goToSingleCard() {
    window.location.href = CONSTANTS.PATHS.SINGLE_CARD;
}

function goToThreeCards() {
    window.location.href = CONSTANTS.PATHS.THREE_CARDS;
}

function goToCelticCross() {
    window.location.href = '/celtic-cross';
}

// 抽牌動畫效果
function animateCardDraw(cardElement, callback) {
    if (!cardElement) return;

    cardElement.style.transform = 'scale(0.8) rotateY(180deg)';
    cardElement.style.transition = 'all 0.6s ease';

    setTimeout(() => {
        cardElement.style.transform = 'scale(1) rotateY(0deg)';
        if (callback) callback();
    }, CONSTANTS.CARD_DRAW_ANIMATION);
}

// 顯示結果動畫
function animateResultShow(resultElement) {
    if (!resultElement) return;

    resultElement.style.opacity = '0';
    resultElement.style.transform = 'translateY(20px)';
    resultElement.style.transition = 'all 0.5s ease';

    setTimeout(() => {
        resultElement.style.opacity = '1';
        resultElement.style.transform = 'translateY(0)';
    }, CONSTANTS.RESULT_SHOW_DELAY);
}

// 添加CSS動畫
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    @keyframes slideOut {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 0; }
    }
    .error-message, .success-message {
        font-family: 'Noto Sans TC', sans-serif;
        font-weight: 500;
    }
`;
document.head.appendChild(style);

// 導出函數供其他腳本使用
window.VibeCodingTarot = {
    CONSTANTS,
    shareResult,
    goToSingleCard,
    goToThreeCards,
    animateCardDraw,
    animateResultShow
};
