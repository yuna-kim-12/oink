<template>
  <div class="piggy-bank-info-container" v-if="!userStore.isLoggedIn">
    <h2>가입한 예적금 상품에 연동해서<br>돼지 저금통을 만들어요.</h2>
    <div class="piggy-bank-info">
      <div class="piggy-bank-item">
        <div class="piggy-bank-item-text">
          <p>모은 금액이 늘어날수록<br>돼지 저금통의 <span>색상</span>이 변해요.</p>
          <p>저금통의 색상으로 목표 달성율을 확인할 수 있어요.</p>
        </div>
        <div class="piggy-bank-item-picture">
          <PiggyBankCarousel />
        </div>
      </div>
      <div class="piggy-bank-item">
        <div class="piggy-bank-item-picture">
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
        <div class="piggy-bank-item-text">
          <p>모은 금액을 <span>무게</span>로 확인해요.</p>
          <p>저금통의 목표 무게를 설정하고<br>무게로 목표를 달성하는 즐거움을 느껴보세요.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useUserStore } from '@/stores/user';
import PiggyBankCarousel from './PiggyBankCarousel.vue'

const userStore = useUserStore()

const progressBar = ref(null);
const weightDisplay = ref(null);
const indicatorWrapper = ref(null);

onMounted(() => {
    // curWeight 현재까지 모은 무게 넣기
    const maxWeight = 100; // 최대 무게 설정
    const duration = 5000; // 애니메이션 주기 (5초)

    const animate = (timestamp) => {
        const progress = (timestamp % duration) / duration;
        const currentWeight = Math.round(maxWeight * progress);

        if (weightDisplay.value) {
            weightDisplay.value.textContent = `${currentWeight}kg`;
        }
        
        if (progressBar.value) {
          // `${progress * 100}%` 100 자리에 얼만큼 달성했는지 적기
            progressBar.value.style.width = `${progress * 100}%`;
        }

        if (indicatorWrapper.value) {
            indicatorWrapper.value.style.left = `${progress * 100}%`;
        }

        requestAnimationFrame(animate);
    };

    requestAnimationFrame(animate);
});
// onMounted(() => {
    
//     const curWeight = 27;
//     const duration = 1500;

//     let startTime = null;
//     const animate = (timestamp) => {
//         if (!startTime) startTime = timestamp;
//         const elapsed = timestamp - startTime;
//         const progress = Math.min(elapsed / duration, 1);

//         const currentValue = Math.round(curWeight * progress);
//         if (weightDisplay.value) {
//             weightDisplay.value.textContent = `${currentValue}kg`;
//         }
        
//         if (progressBar.value) {
            
//             progressBar.value.style.width = `${progress * 75}%`;
//         }

//         if (indicatorWrapper.value) {
//             indicatorWrapper.value.style.left = `${progress * 75}%`;
//         }

//         if (progress < 1) {
//             requestAnimationFrame(animate);
//         }
//     };

//     requestAnimationFrame(animate);
// });
</script>

<style scoped>
.piggy-bank-info-container h2 {
  margin: 200px 0 130px;
  color: var(--sub-text-bold-color);
  text-align: center;
  font-size: 30px;
  font-weight: 700;
}

.piggy-bank-info {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: var(--sub-text-color);
}

.piggy-bank-item {
  display: flex;
  align-items: center;
  gap: 100px;
  margin-bottom: 100px;
}

.piggy-bank-item-text p:first-child {
  margin-bottom: 10px;
  font-size: 25px;
  font-weight: 700;
}

.piggy-bank-item-text p:last-child {
  font-size: 18px;
}

.piggy-bank-item-text span {
  font-weight: bold;
  font-size: 32px;
  color: var(--main-text-color);
}

.piggy-bank-item-picture {
  width: 250px;
  height: 250px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
}

.weight {
    font-weight: 700;
    color: var(--sub-text2-color);
    font-size: 28px;
}

.progress-outer {
    width: 100%;
    margin-top: 20px;
    display: flex;
    justify-content: center;
}

.progress-container {
    width: 250px;
    height: 18px;
    background-color: #DDDDDD;
    border-radius: 10px;
    position: relative;
}

.progress-bar {
    position: absolute;
    left: 0;
    top: 0;
    height: 100%;
    width: 0;
    background-color: #2ECC71;
    border-radius: 10px;
}

.indicator-wrapper {
    position: absolute;
    left: 0;
    top: 0;
    height: 100%;
}

.progress-indicator {
    position: absolute;
    width: 35px;
    height: 35px;
    right: -10px;
    top: 50%;
    transform: translateY(-50%);
    z-index: 2;
}
</style>