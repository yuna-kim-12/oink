<template>
  <div class="piggybank-popup-container" v-if="openPopup">
    <!-- 네모 박스 -->

    <div class="piggybank-popup">
      <!-- 예적금 만들기 또는 계좌 연동 버튼 선택 팝업 -->
      <div class="piggybank-join-btns">
        <div class="piggybank-join-btn" @click="goRecommend">
          <p>새로운 걸로 할게요!</p>
          <p><span>username</span>님께 맞는<br>예적금 상품을 추천받고
            <br>새로운 예적금을 만들어보세요!
          </p>
        </div>
        <div class="piggybank-join-btn">
          <p>연동된 계좌로 할게요!</p>
          <p><span>username</span>님의<br>기존 예적금 상품으로
            <br>돼지 저금통을 만들어보세요!
          </p>
        </div>
      </div>

      <!-- 돼지 저금통 만들기(정보 입력) -->
      <div class="piggybank-join-info" v-if="false">
        <div class="piggybank-img">
          <span class="piggy-nickname-btn">저금통 애칭</span>
          <p class="piggy-nickname"></p>
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
        </div>
        <form>
          <div class="piggybank-input">
            <label for="piggybank-name">돼지 저금통 이름</label>
            <input type="text" id="piggybank-name" placeholder="저금통 이름을 입력하세요">
          </div>
          <div class="piggybank-input">
            <label for="piggybank-account">예적금 선택</label>
            <select name="" id="">
              <option value=""></option>
            </select>
          </div>
          <div class="piggybank-input">
            <label for="piggybank-name">목표 금액</label>
            <input type="text" id="piggybank-name" placeholder="목표 금액을 입력하세요">
            <span>만원</span>
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
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter()
const openPopup = ref(true)

// 새로운 예적금 만들기 버튼 클릭 시 추천 페이지 이동
const goRecommend = function () {
  router.push({ name: 'recommend' })
}

// 다음에 만들기 버튼 클릭 시 팝업 창 닫기
const closePopup = function () {
  openPopup.value = !openPopup.value
}
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
  z-index: 10;
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

.piggybank-popup button {
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