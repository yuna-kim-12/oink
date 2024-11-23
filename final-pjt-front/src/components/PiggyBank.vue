<template>
  <div class="container">
    <div class="piggy-text">
      <p v-if="userStore.isLoggedIn && userStore.user" class="piggy-user"><span>{{ userStore.user.name }}</span>님의 돼지
        저금통</p>
      <p v-else class="piggy-recommend">나만의 <span>돼지 저금통</span>을 만들어 금융 자산을 관리하고,<br>
        저금통을 무겁게 만들 <span>금융 상품</span>을 추천 받아보세요!</p>
    </div>

    <div class="piggybank-main">
      <!-- 로그인 안한 사용자는 예시 내용 보여주기, 로그인 했는데 저금통 있는 사람 그 정보 보여주기  -->
      <div class="is-piggybank" v-if="true">
        <div class="piggybank-img">
          <img src="@/assets/images/pink-pig(25).png" alt="pink-pig-img">
          <span ref="weightDisplay" class="weight">{{ curWeight }}kg</span>
          <div class="progress-outer">
            <div class="progress-container">
              <div class="progress-bar" ref="progressBar"></div>
              <div class="indicator-wrapper" ref="indicatorWrapper">
                <img class="progress-indicator" src="@/assets/images/indicator.png" alt="indicator-img">
              </div>
            </div>
          </div>
        </div>
        <div class="piggybank-intro">
          <span class="piggy-nickname-btn">저금통 애칭</span>
          <p class="piggy-nickname"></p>
          <!-- span 태그에 현재날짜부터 만기일까지의 날짜 계산 -->
          <p class="duration">만기일까지 <span>D-날짜 계산</span></p>
          <div class="real-intro">
            <p data-label="상품명"><span></span></p>
            <p data-label="저축기간"><span></span></p>
            <p data-label="금리"><span>%</span></p>
            <p data-label="목표 무게"><span>kg (만원)</span></p>
            <p data-label="응원 받은 수"><span></span></p>
          </div>
        </div>
        <!-- 로그인 했지만 저금통 없는 사람들에게 보여주기 -->
      </div>
      <div class="no-piggybank" v-if="false">
        <img src="@/assets/images/no-piggybank.png" alt="no-piggybank-img">
        <p>현재 만들어진 돼지 저금통이 없어요</p>
        <!-- 버튼에 팝업 창 연결 -->
        <button>돼지 저금통 만들기</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useUserStore } from '@/stores/user';

const userStore = useUserStore()

const progressBar = ref(null);
const weightDisplay = ref(null);
const indicatorWrapper = ref(null);
const piggyExam = ref({
  name: '살 수 있어 서울 자가^^', // 저금통 애칭
  duration: '15', // 만기일까지 남은 날짜
  productName: 'SH해양플라스틱Xero적금', // 상품명
  period: '24.09.02 ~ 24.10.03', // 저축 기간
  interest_rate: 20, // 금리
  weight: 300, // 목표 금액
  cheerupCnt: 45, // 응원 수
  piggyImg: '@/assets/images/yellow-pig(100).png' // 돼지 이미지
})

onMounted(() => {
  // 1. progress bar 애니매이션
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
      // `${progress * 100}%` 80 자리에 얼만큼 달성했는지 적기
      progressBar.value.style.width = `${progress * 80}%`;
    }

    if (indicatorWrapper.value) {
      indicatorWrapper.value.style.left = `${progress * 80}%`;
    }

    if (progress < 1) {
      requestAnimationFrame(animate);
    }
  };

  requestAnimationFrame(animate);
});
</script>

<style scoped>
.container {
  margin: 50px 0 100px;
}

.piggy-text p {
  width: 740px;
  margin: 0 auto;
  padding-left: 20px;
  font-size: 25px;
  font-weight: 700;
  color: var(--sub-text-color);
}

.piggy-text span {
  font-weight: 700;
  color: var(--main-text-color);
}

.piggy-recommend {
  text-align: center;
}

.piggy-recommend span:last-child {
  color: var(--point-color);
}

.piggybank-main {
  width: 740px;
  height: 400px;
  margin: 20px auto;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 3px 3px 15px rgb(230, 229, 229);
  border-radius: 15px;
}

.is-piggybank {
  display: flex;
  justify-content: center;
  align-items: center;
}

.piggybank-img {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 200px;
  height: 200px;
  margin-right: 100px;
}

.piggybank-img>img {
  width: 200px;
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

.weight {
  margin-top: 20px;
  font-weight: 700;
  color: var(--sub-text2-color);
  font-size: 24px;
}

.progress-outer {
  width: 100%;
  margin-top: 20px;
  display: flex;
  justify-content: center;
}

.progress-container {
  width: 250px;
  height: 15px;
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

.no-piggybank {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.no-piggybank>img {
  width: 250px;
}

.no-piggybank>p {
  margin-top: 15px;
  font-size: 20px;
  font-weight: 700;
  color: var(--sub-text2-color);
}

.no-piggybank>button {
  margin-top: 30px;
  padding: 5px 15px;
  border-radius: 15px;
  color: #fff;
  background-color: var(--point-color);
  cursor: pointer;
}

.no-piggybank>button:hover {
  background-color: var(--main-color);
  transition: all 300ms ease-in-out;
}
</style>