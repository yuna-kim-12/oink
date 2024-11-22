<template>
  <div class="cheerup">
    <div class="cheerup-text">
      <h2>새롭게 저금통을 만든 사람들을 <span>응원</span>해보세요!</h2>
      <p>목표를 달성할 수 있도록 응원해주세요!</p>
    </div>

    <div class="cheerup-list">
      <div class="cheerup-item" v-for=" n in cheerupList">
        <p><span>오한나</span>님</p>
        <img src="@/assets/images/돼지 그림.png" alt="" class="cheerup-img">
        <p class="goal-name">결혼식 자금 모으기</p>
        <p class="cheerup-count">50</p>
        <button class="cheerup-btn">응원하기</button>
      </div>
    </div>
    <img src="@/assets/images/stage.png" alt="" class="stage">
  </div>
</template>

<script setup>
import { ref } from 'vue';

const cheerupList = ref(5)
</script>

<style scoped>
.cheerup {
  text-align: center;
  margin: 200px 0; 
}

.cheerup-text {
  margin-bottom: 30px;
}

.cheerup-text h2 {
  color: var(--sub-text-bold-color);
  font-weight: 700;
  font-size: 30px;
  margin-bottom: 20px;
}

.cheerup-text span {
  color: var(--main-text-color);
  font-weight: 700;

}

.cheerup-text p {
  margin-bottom: 100px;
  color: var(--sub-text-color);
  font-size: 18px;
}

.cheerup-list {
  display: flex;
  justify-content: center;
  align-items: center;

}

.cheerup-item {
  position: relative;
  box-shadow: 3px 5px 8px rgba(0, 0, 0, 0.25);
  padding: 20px 50px;
  border-radius: 15px;
  margin: 0px 15px;

}

.cheerup-item>p {
  color: #aaa;
  font-size: 20px;
  padding: 5px 10px;
}

.cheerup-item>p>span {
  color: var(--sub-text-color)
}

.cheerup-img {
  width: 150px;
  height: 150px;
  object-fit: cover;
}

.cheerup-item .goal-name {
  color: var(--sub-text-color);
  font-size: 14px;
  margin-top: 10px;
}

.cheerup-item .cheerup-count {
  color: var(--main-text-color);
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 30px;
  margin-top: 10px;
}

.cheerup-item button {
  position: absolute;
  background-color: var(--point-color);
  border-radius: 4px;
  color: white;
  font-size: 12px;
  padding: 6px;
  bottom: 11px;
  right: 12px;
}

.stage {
  width: 100vw;
  margin-top: 20px;
}
</style>