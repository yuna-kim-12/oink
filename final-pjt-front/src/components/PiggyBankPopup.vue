<template>
  <div v-if="isOpen" class="piggybank-popup-container">
    <!-- 네모 박스 -->

    <div class="piggybank-popup">
      <!-- 예적금 만들기 또는 계좌 연동 버튼 선택 팝업 -->
      <div class="piggybank-join-btns" v-if="!isAccounts">
        <div class="piggybank-join-btn" @click="goRecommend">
          <p>새로운 걸로 할게요!</p>
          <p><span>{{ userStore.user.name }}</span>님께 맞는<br>예적금 상품을 추천받고
            <br>새로운 예적금을 만들어보세요!
          </p>
        </div>
        <div class="piggybank-join-btn" @click="goMaking">
          <p>연동된 계좌로 할게요!</p>
          <p><span>{{ userStore.user.name }}</span>님의<br>기존 예적금 상품으로
            <br>돼지 저금통을 만들어보세요!
          </p>
        </div>
      </div>

      <!-- 돼지 저금통 만들기(정보 입력) -->
      <div class="piggybank-join-info" v-if="isAccounts">
        <div class="piggybank-show">
          <span class="piggy-nickname-btn">저금통 애칭</span>
          <p class="piggy-nickname">{{ piggybankName || `${userStore.user.name}님의 저금통` }}</p>
          <div class="piggybank-img">
            <img src="@/assets/images/pink-pig(25).png" alt="pink-pig-img">
            <span ref="weightDisplay" class="weight">{{ goalAmount || 0 }}kg</span>
            <div class="progress-outer">
              <div class="progress-container">
                <div class="progress-bar" ref="progressBar"></div>
                <div class="indicator-wrapper" ref="indicatorWrapper">
                  <img class="progress-indicator" src="@/assets/images/indicator.png" alt="indicator-img">
                </div>
              </div>
            </div>
          </div>
        </div>
        <form @submit.prevent="makePiggybank">
          <div class="piggybank-input">
            <label for="piggybank-goal">목표 선택</label>
            <select name="piggybank-goal" id="piggybank-goal" v-model="goal">
              <option value="" disabled selected>목표를 입력하세요</option>
              <option v-for="(val, key) in goals" :key="key" :value="key">{{ val }}</option>
            </select>
          </div>
          <div class="piggybank-input">
            <label for="piggybank-name">돼지 저금통 애칭</label>
            <input type="text" id="piggybank-name" v-model="piggybankName" placeholder="저금통 애칭을 입력하세요 (15자 이내)"
              maxlength='15'>
          </div>
          <div class="piggybank-input goal-amount">
            <label for="piggybank-goal-amount">목표 금액</label>
            <input type="number" id="piggybank-goal-amount" v-model="goalAmount" placeholder="목표 금액을 입력하세요">
            <span v-if="showUnit">만원</span>
          </div>
          <div class="piggybank-input">
            <label for="piggybank-account">예적금 선택</label>
            <select name="piggybank-account" id="piggybank-account" v-model="account" placeholder="예적금을 선택하세요">
              <option value="" disabled selected>연동할 상품을 선택하세요</option>
              <option v-for="product in myProducts" :key="product.id" :value="product.id">
                {{ product.product.product_name }}({{ product.product.company_name }})
              </option>
            </select>
          </div>
          <button>만들기</button>
        </form>
      </div>

      <!-- 다음에 만들기 버튼 -->
      <button @click="closePopup">다음에 만들기</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, toRef } from 'vue';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user';
import axios from 'axios';

const router = useRouter()
const userStore = useUserStore()
const props = defineProps({
  isOpen: Boolean
})

// 1. 새로운 예적금 만들기 버튼 클릭 시 추천 페이지 이동
const goRecommend = function () {
  router.push({ name: 'recommend' })
}


// 2. 기존 예적금으로 만들기 버튼 클릭 시 저금통 만들기 진행
const isAccounts = ref(false)
const goMaking = function () {
  if (userStore.user.user_product.length) {
    getMyProduct()
    isAccounts.value = true
  } else {
    alert('먼저 예적금을 연동해주세요🐽')
    router.push({ name: 'profile', params: { userId: userStore.user.pk } })
    closePopup()
  }
}


// 3. 저금통 만들기
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

const goal = ref('')
const piggybankName = ref('')
const goalAmount = ref(null)
const account = ref('')


// 3-1. 사용자 예적금 가져오기
const myProducts = ref([]);

const getMyProduct = async () => {
	try {
	  const res = await axios({
		method: 'get',
		url: `${userStore.url}/bank_products/products_joined/${userStore.userPK}/`,
		headers: {
		  Authorization: `Token ${userStore.token}`,
		},
	  });
    console.log(res.data)
	  myProducts.value = res.data;
	} catch (err) {
	  console.error(err);
	}
  };

  // 3-2. 찐 저금통 만들기
const makePiggybank = async function () {
  // 입력 데이터 없을 때 경고창 띄우기
  if (!goal.value) {
    alert('목표를 선택해주세요🐽');
    return;
  }

  if (!piggybankName.value) {
    piggybankName.value = `${userStore.user.name}님의 저금통`
  }

  if (!goalAmount.value || goalAmount.value <= 0) {
    alert('목표 금액을 입력해주세요🐽');
    return;
  }

  if (!account.value) {
    alert('예적금을 선택해주세요🐽');
    return;
  }

  const requestData = {
    name: piggybankName.value,
    weight: Number(goalAmount.value) / 10,
    saving_purpose: goal.value,
    user_product: account.value
  };

  axios({
    method: 'post',
    url: `${userStore.url}/piggy_banks/`,
    data: requestData,
    headers: {
      'Authorization': `Token ${userStore.token}`,
      'Content-Type': 'application/json',
    }
  })
    .then(response => {
      console.log('Success:', response.data);
      alert('돼지 저금통 만들기 성공🐽')
      closePopup()
      window.location.reload()
    })
    .catch(err => {
      alert('이미 만들어진 돼지 저금통이 있어요🐽')
      closePopup()
    });
};

// 저금통 만들 때 '만원'이 따라다니기
const showUnit = computed(() => {
  return goalAmount.value !== '' && goalAmount.value !== '0';
})

// 다음에 만들기 버튼 클릭 시 팝업 창 닫기
const emit = defineEmits(['closePopup'])
const closePopup = function () {
  emit('closePopup')
}

// 저금통 만들다가 팝업창 닫은 후 다시 열었을 때 input값 초기화
const isOpen = toRef(props, 'isOpen')

watch(isOpen, (newVal) => {
  // isOpen이 false로 변경될 때(팝업창 닫힐 때)
  if (!newVal) {
    goal.value = ''
    piggybankName.value = ''
    goalAmount.value = null
    account.value = ''
  }
})
</script>

<style scoped>
.piggybank-popup-container {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(255, 255, 255, 0.5);
  z-index: 1000;
}

.piggybank-popup {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 800px;
  height: 450px;
  border-radius: 15px;
  box-shadow: 3px 3px 15px rgb(230, 229, 229);
  background-color: #fff;
}

/* 예적금 만들기 또는 계좌 연동 버튼 선택 팝업 */
.piggybank-join-btns {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 30px;
  text-align: center;
}

.piggybank-join-btn {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 300px;
  height: 300px;
  border-radius: 15px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
  cursor: pointer;
}

.piggybank-join-btn p:first-child {
  font-size: 25px;
  font-weight: 700;
}

.piggybank-join-btn p:last-child {
  margin-top: 15px;
  font-size: 14px;
  color: var(--sub-text-color);
  line-height: 20px;
}

.piggybank-join-btn p:last-child span {
  font-weight: 700;
  color: var(--sub-text-bold-color);
}

.piggybank-join-btn:first-child {
  background-color: #ECFFF6;
}

.piggybank-join-btn:first-child p:first-child {
  color: #34C987;
}

.piggybank-join-btn:last-child {
  background-color: #F3F2FF;
}

.piggybank-join-btn:last-child p:first-child {
  color: var(--main-color);
}

.piggybank-join-btn:hover {
  transform: scale(0.95);
  transition: all 300ms ease-in-out;
}

/* 돼지 저금통 만들기(정보 입력) */
.piggybank-join-info {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 100px;
}

.piggybank-show {
  width: 200px;
  text-align: center;
}

.piggy-nickname-btn {
  font-size: 12px;
  background-color: var(--main-color);
  color: white;
  border-radius: 15px;
  margin: 0 auto 0px;
  padding: 2px 7px;
}

.piggy-nickname {
  color: var(--sub-text-bold-color);
  font-size: 24px;
  font-weight: 700;
  margin-bottom: 30px;
}

.piggybank-img {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 200px;
  height: 200px;
}

.piggybank-img>img {
  width: 200px;
}


.weight {
  margin-top: 10px;
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
  width: 80%;
  background-color: #2ECC71;
  border-radius: 10px;
}

.indicator-wrapper {
  position: absolute;
  left: 80%;
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

.piggybank-input {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin: 10px 0;
}

.piggybank-input label {
  margin-bottom: 3px;
  color: var(--main-color);
  font-weight: 700;
}

.piggybank-input input,
.piggybank-input select {
  width: 300px;
  padding: 8px 10px;
  border: 1px solid var(--stroke-color);
  border-radius: 5px;
}


.piggybank-input select {
  padding-left: 5px;
  color: var(--sub-text-color);
  outline: none;
}

.goal-amount {
  position: relative;
}

.goal-amount input {
  width: 100%;
}

.goal-amount span {
  position: absolute;
  right: 10px;
  top: 33px;
  color: #666;
  font-size: 14px;
}

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
}

.piggybank-join-info form>button {
  display: block;
  margin: 20px auto 0;
  padding: 4px 10px;
  color: #fff;
  border-radius: 14px;
  background-color: var(--main-color);
}


/* 다음에 만들기 버튼 */
.piggybank-popup>button {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  padding: 8px 16px;
  border-radius: 8px;
  color: var(--sub-text-color);
  background-color: #F8F8F8;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}
</style>