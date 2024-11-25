<template>
  <div class="piggybank-container">
    <div class="piggybank-main">
      <!-- 1. 로그인 안한 사용자는 예시 내용 보여주기, 로그인 했는데 저금통 있는 사람 그 정보 보여주기  -->
      <div class="is-piggybank" v-if="isPiggybank">
        <div class="piggybank-img">
          <img :src="piggybankImg" alt="piggy-img">
          <span ref="weightDisplay" class="weight">{{ amountEntered }}kg</span>
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
          <span class="piggy-nickname-btn">{{ goals[piggybankInfo.saving_purpose] }}</span>
          <p class="piggy-nickname">{{ piggybankInfo.name }}</p>
          <!-- span 태그에 현재날짜부터 만기일까지의 날짜 계산 -->
          <p class="duration" v-if="myPiggy">만기일까지 <span>D-{{ piggybankInfo.user_product.d_day }}</span></p>
          <div class="real-intro">
            <p data-label="상품명" v-if="myPiggy"><span>
                {{ piggybankInfo.user_product.product.product_name }} ({{
                  piggybankInfo.user_product.product.company_name }})
              </span></p>
            <p data-label="저축기간" v-if="myPiggy"><span>
                {{ piggybankInfo.user_product.join_date.slice(0, 10) }} ~ {{
                  piggybankInfo.user_product.expiration_date.slice(0, 10) }} ({{ piggybankInfo.user_product.remain_month
                }}달 째)
              </span></p>
            <p data-label="금리" v-if="myPiggy"><span>{{ piggybankInfo.user_product.interest_rate }}%</span></p>
            <p data-label="목표 무게"><span>{{ piggybankInfo.weight * 10 }}kg ({{ piggybankInfo.weight * 10 }}만원)</span></p>
            <p data-label="응원 받은 수"><span>{{ piggybankInfo.cheerup_count }}</span></p>
          </div>
        </div>
        <div class="delete-piggybank">
          <img src="/src/assets/images/Left-facing fist.png" alt="주먹 이미지">
          <button @click="deletePiggybank" v-if="myPiggy">저금통 뿌수기</button>
        </div>
      </div>


      <!-- 2. 로그인 했지만 저금통 없는 사람들에게 보여주기 -->
      <div class="no-piggybank" v-else>
        <img src="@/assets/images/no-piggybank.png" alt="no-piggybank-img">
        <p>현재 만들어진 돼지 저금통이 없어요</p>
        <!-- 버튼에 팝업 창 연결 -->
        <button @click="openPopup">돼지 저금통 만들기</button>
        <PiggyBankPopup :is-open="isOpen" @close-popup="closePopup" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import { useUserStore } from '@/stores/user';
import PiggyBankPopup from './PiggyBankPopup.vue';

const userStore = useUserStore()
const route = useRoute()

const progressBar = ref(null);
const weightDisplay = ref(null);
const indicatorWrapper = ref(null);

const goals = {
  'home': '내집마련',
  'education': '교육비',
  'medication': '의료비',
  'wedding': '결혼자금',
  'future': '노후자금',
  'seedmoney': '시드머니',
  'travel': '여행자금',
  'wishlist': '위시리스트'
}



// 돼지 저금통 정보
const piggybankInfo = ref({}) // 돼지 저금통 정보
const amountEntered = ref(30) // 지금까지 넣은 금액
const savingRate = ref(80) // 지금까지 모은 금액 비율
const piggybankImg = ref('/src/assets/images/pink-pig(25).png') // 돼지 저금통 이미지
const piggybankExam = {
  name: '살 수 있어 서울 자가^^',
  weight: 9.9,
  cheerup_count: 38,
  saving_purpose: "home",
  user_product: {
    join_date: '24.09.02',
    expiration_date: '25.09.01',
    d_day: '211',
    remain_month: 5,
    interest_rate: '4.3',
    product: {
      company_name: '수협은행',
      product_name: 'SH해양플라스틱Xero적금'
    }
  }
}



// 1. 내 저금통 조회하기
const isPiggybank = ref(false)
const myPiggy = ref(true)
const piggybank = ref(null)

// 1-1. 사용자 정보 가져오기
const getUserInfo = async function () {
  try {
    const response = await axios({
      method: 'get',
      url: `${userStore.url}/accounts/profile/${route.params.userId || userStore.userPK}/`,
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    });
    piggybank.value = response.data.piggy_bank;
    
  } catch (err) {
    console.log(err);
    throw err;  // 에러를 상위로 전파
  }
};

// 1-2. 로그인 유무, 저금통 소유 확인
const getPiggybankInfo = async function () {
  try {
    // 로그인을 하지 않은 사람
    if (!userStore.isLoggedIn) {
      isPiggybank.value = true;
      piggybankInfo.value = piggybankExam;
      return
    }

      // 로그인 한 사람
    if (userStore.isLoggedIn) {
      // await로 데이터를 기다림
      await getUserInfo();

      // 누구의 저금통인지 확인
      if (userStore.userPK == route.params.userId || !route.params.userId) {
        myPiggy.value = true;
      } else {
        myPiggy.value = false;
      }
      if (piggybank.value && piggybank.value.length) {
        isPiggybank.value = true;
        piggybankInfo.value = piggybank.value[0];
        amountEntered.value = piggybankInfo.value.user_product.remain_month *
          piggybankInfo.value.user_product.monthly_amount;
          savingRate.value = (amountEntered.value / (piggybankInfo.value.weight * 10)) * 100;
        ChangePiggyImg();
      } else {
        isPiggybank.value = false;
        piggybankInfo.value = {};
      }
    }
  } catch (err) {
    console.log('Error in getPiggybankInfo:', err);
    isPiggybank.value = false;
    piggybankInfo.value = {};
  }
};

// 모은 금액 비율에 따라 저금통 돼지 사진 변하게 하기
const ChangePiggyImg = function () {
  if (savingRate.value <= 25) {
    piggybankImg.value = '/src/assets/images/pink-pig(25).png'
  } else if (savingRate.value <= 50) {
    piggybankImg.value = '/src/assets/images/green-pig(50).png'
  } else if (savingRate.value <= 75) {
    piggybankImg.value = '/src/assets/images/blue-pig(75).png'
  } else {
    piggybankImg.value = '/src/assets/images/yellow-pig(100).png'
  }
}

// 2. 돼지 저금통 깨기(목표 무게 달성 시)
const deletePiggybank = function () {
  // - 지금까지 모은 금액이 목표 무게보다 클 경우에만 깨기 가능
  if (amountEntered.value >= piggybankInfo.value.weight* 10) {
    if (confirm("저금통을 삭제하시겠습니까?🐽")) {
      axios({
        method: 'delete',
        url: `${userStore.url}/piggy_banks/detail/${piggybankInfo.value.id}/`,
        headers: {
          Authorization: `Token ${userStore.token}`
        }
      })
        .then(res => {
          console.log('저금통 삭제 성공')
          window.location.reload()
        })
        .catch(err => console.log('저금통 삭제 실패', err))
    }
  } else {
    alert('목표 금액을 채우고 와주세요🐽')
  }
}


// 저금통 만들기 버튼 클릭 시 팝업 창 띄우기
const isOpen = ref(false)
const openPopup = function () {
  isOpen.value = !isOpen.value
}

// 팝업 창 닫기
const closePopup = function () {
  isOpen.value = !isOpen.value
}

onMounted(() => {
  // 1. 로그인 여부, 저금통 유무 확인
  getPiggybankInfo()

  // 2. progress bar 애니매이션
  const duration = 1500;

  let startTime = null;
  const animate = (timestamp) => {
    if (!startTime) startTime = timestamp;
    const elapsed = timestamp - startTime;
    const progress = Math.min(elapsed / duration, 1);

    const currentValue = Math.round(amountEntered.value * progress);
    if (weightDisplay.value) {
      weightDisplay.value.textContent = `${currentValue}kg`;
    }

    if (progressBar.value) {
      // `${progress * 100}%` 80 자리에 얼만큼 달성했는지 적기
      progressBar.value.style.width = `${Math.min(progress * savingRate.value, 100)}%`;
    }

    if (indicatorWrapper.value) {
      indicatorWrapper.value.style.left = `${Math.min(progress * savingRate.value, 100)}%`;
    }

    if (progress < 1) {
      requestAnimationFrame(animate);
    }
  };

  requestAnimationFrame(animate);
});

watch(() => route.params.userId, () => {
  getPiggybankInfo();
});
</script>

<style scoped>
.piggybank-container {
  margin: 0 0 100px;
}

.piggybank-main {
  position: relative;
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

.delete-piggybank {
  position: absolute;
  bottom: 15px;
  right: 15px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.delete-piggybank img {
  width: 30px;
  height: 30px;
  margin-bottom: 5px;
  display: none;
}

.delete-piggybank button {
  padding: 4px 8px;
  color: #fff;
  font-size: 12px;
  border-radius: 15px;
  background-color: var(--stroke-color);
}

.delete-piggybank:hover img {
  display: block;
}

.delete-piggybank:hover img {
  animation: moveUpDown 0.3s infinite alternate;
}

.delete-piggybank:hover button {
  transform: scale(0.95);
  transition: all 0.3s ease-in-out;
}

@keyframes moveUpDown {
  from {
    transform: translateY(0);
  }

  to {
    transform: translateY(-10px);
  }
}


/* 저금통 없는 사람들의 저금통 스타일 */
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