<template>
  <div class="piggy-bank-info-container">
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
          <img src="" alt="">
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
import PiggyBankCarousel from './PiggyBankCarousel.vue'
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
  justify-content: center;
  align-items: center;
  border-radius: 10px;
}
</style>