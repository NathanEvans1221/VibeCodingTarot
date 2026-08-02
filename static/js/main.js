// 主要JavaScript功能

// HTML 轉義函數，防止 XSS
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

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
    // 初始化頁面
    initializePage();

    // 添加動畫效果
    addAnimationEffects();

    // 設置事件監聽器
    setupEventListeners();
});

// 初始化頁面
function initializePage() {
    console.log('VibeCodingTarot 網站已載入');
    
    // 檢查是否在占卜頁面
    if (window.location.pathname.includes('single-card') || window.location.pathname.includes('three-cards')) {
        initializeDivinationPage();
    }
}

// 初始化占卜頁面
function initializeDivinationPage() {
    // 設置問題輸入框的動態效果
    const questionInput = document.getElementById('questionInput');
    if (questionInput) {
        questionInput.addEventListener('focus', function() {
            this.style.borderColor = '#6c5ce7';
            this.style.boxShadow = '0 0 0 3px rgba(108, 92, 231, 0.1)';
        });
        
        questionInput.addEventListener('blur', function() {
            this.style.borderColor = '#e0e0e0';
            this.style.boxShadow = 'none';
        });
    }
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
            }, 1000);
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
            }, 150);
        });
    });
    
    // 為動作按鈕添加點擊效果
    const actionButtons = document.querySelectorAll('.action-button');
    actionButtons.forEach(button => {
        button.addEventListener('click', function() {
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
        });
    });
}

// 導航功能
function goToSingleCard() {
    window.location.href = '/single-card';
}

function goToThreeCards() {
    window.location.href = '/three-cards';
}

// 抽牌動畫效果
function animateCardDraw(cardElement, callback) {
    if (!cardElement) return;
    
    // 添加抽牌動畫
    cardElement.style.transform = 'scale(0.8) rotateY(180deg)';
    cardElement.style.transition = 'all 0.6s ease';
    
    setTimeout(() => {
        cardElement.style.transform = 'scale(1) rotateY(0deg)';
        if (callback) callback();
    }, 600);
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
    }, 100);
}

// 錯誤處理
function handleError(error, userMessage = '操作失敗，請稍後再試') {
    console.error('錯誤:', error);
    
    // 顯示用戶友好的錯誤訊息
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error-message';
    errorDiv.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: #ff6b6b;
        color: white;
        padding: 15px 20px;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        z-index: 1000;
        animation: slideIn 0.3s ease;
    `;
    errorDiv.textContent = userMessage;
    
    document.body.appendChild(errorDiv);
    
    // 3秒後自動移除錯誤訊息
    setTimeout(() => {
        errorDiv.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => {
            if (errorDiv.parentNode) {
                errorDiv.parentNode.removeChild(errorDiv);
            }
        }, 300);
    }, 3000);
}

// 成功訊息
function showSuccessMessage(message) {
    const successDiv = document.createElement('div');
    successDiv.className = 'success-message';
    successDiv.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: #51cf66;
        color: white;
        padding: 15px 20px;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        z-index: 1000;
        animation: slideIn 0.3s ease;
    `;
    successDiv.textContent = message;
    
    document.body.appendChild(successDiv);
    
    // 3秒後自動移除成功訊息
    setTimeout(() => {
        successDiv.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => {
            if (successDiv.parentNode) {
                successDiv.parentNode.removeChild(successDiv);
            }
        }, 300);
    }, 3000);
}

// 添加CSS動畫
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
    
    .error-message,
    .success-message {
        font-family: 'Noto Sans TC', sans-serif;
        font-weight: 500;
    }
`;
document.head.appendChild(style);

// 導出函數供其他腳本使用
window.VibeCodingTarot = {
    escapeHtml,
    shareResult,
    goToSingleCard,
    goToThreeCards,
    animateCardDraw,
    animateResultShow,
    handleError,
    showSuccessMessage
};
