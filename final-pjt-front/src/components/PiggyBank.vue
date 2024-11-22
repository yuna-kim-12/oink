<template>
    <div class="container">
        <div class="piggybank-main">
            <div class="piggybank-img">
                <img src="@/assets/images/돼지 그림.png" alt="">
                <span ref="weightDisplay" class="weight">0kg</span>
                <div class="progress-outer">
                    <div class="progress-container">
                        <div class="progress-bar" ref="progressBar"></div>
                        <div class="indicator-wrapper" ref="indicatorWrapper">
                            <img class="progress-indicator" src="@/assets/images/indicator.png" alt="">
                        </div>
                    </div>
                </div>
            </div>
            <div class="piggybank-intro">
                <span class="piggy-nickname-btn">저금통 애칭</span>
                <p class="piggy-nickname">살 수 있어 서울 자가^^</p>
                <p class="duration">만기일까지 <span>D-15</span></p>
                <div class="real-intro">
                    <p data-label="상품명"><span>SH해양플라스틱Xero적금</span></p>
                    <p data-label="저축기간"><span>24.09.02 ~ 24.10.03</span></p>
                    <p data-label="금리"><span>20%</span></p>
                    <p data-label="목표 무게"><span>30kg (300만원)</span></p>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const progressBar = ref(null);
const weightDisplay = ref(null);
const indicatorWrapper = ref(null);

onMounted(() => {
    // curWeight 현재까지 모은 무게 넣기
    const curWeight = 27;
    const duration = 1500;

    let startTime = null;
    const animate = (timestamp) => {
        if (!startTime) startTime = timestamp;
        const elapsed = timestamp - startTime;
        const progress = Math.min(elapsed / duration, 1);

        const currentValue = Math.round(curWeight * progress);
        if (weightDisplay.value) {
            weightDisplay.value.textContent = `${currentValue}kg`;
        }
        
        if (progressBar.value) {
            // `${progress * 100}%` 100 자리에 얼만큼 달성했는지 적기
            progressBar.value.style.width = `${progress * 100}%`;
        }

        if (indicatorWrapper.value) {
            indicatorWrapper.value.style.left = `${progress * 90}%`;
        }

        if (progress < 1) {
            requestAnimationFrame(animate);
        }
    };

    requestAnimationFrame(animate);
});
</script>

<style scoped>
.piggybank-main {
    width: 740px;
    height: 400px;
    margin: 50px auto;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 3px 3px 4px rgb(230, 229, 229);
    border-radius: 15px;
}

.piggybank-img {
    display: flex;
    flex-direction: column;
    width: 200px;
    height: 200px;
    margin-right: 100px;
    margin-bottom:67px;
}


.piggybank-intro {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.piggy-nickname-btn {
    font-size: 12px;
    background-color: var(--main-color);
    color: white;
    border-radius: 15px;
    margin: 0 auto 10px;
    padding: 2px 7px;
}

.piggy-nickname {
    color: var(--sub-text-bold-color);
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 5px;
}

.duration {
    font-size: 13px;
    color: var(--sub-text-color);
    margin-bottom: 10px;
}

.duration>span {
    color: #FF8686;
}

.real-intro {
    display: table;
    text-align: start;
    font-size: 15px;
    margin-top: 10px;
}

.real-intro>p {
    display: table-row;
    color: var(--main-color);
    font-weight: 700;
}

.real-intro>p::before {
    display: table-cell;
    content: attr(data-label);
    padding-right: 10px;
    padding-bottom: 5px;
    white-space: nowrap;
}

.real-intro>p>span {
    display: table-cell;
    color: var(--sub-text-color);
    font-weight: 500;
    padding-left: 5px;
}

.progress-outer {
    width: 100%;
    margin-top: 15px;
    display: flex;
    justify-content: center;
}

.progress-container {
    width: 150px;
    height: 8px;
    background-color: #DDDDDD;
    border-radius: 4px;
    position: relative;
}

.progress-bar {
    position: absolute;
    left: 0;
    top: 0;
    height: 100%;
    width: 0;
    background-color: #2ECC71;
    border-radius: 4px;
}

.weight {
    margin-left: auto;
    margin-right: auto;
    font-weight: 700;
    color: #a8a8a8;
    margin-top: 10px;
    font-size: 20px;
}

.indicator-wrapper {
    position: absolute;
    left: 0;
    top: 0;
    height: 100%;
}

.progress-indicator {
    position: absolute;
    width: 20px;
    height: 20px;
    right: -10px;
    top: 50%;
    transform: translateY(-50%);
    z-index: 2;
}
</style>