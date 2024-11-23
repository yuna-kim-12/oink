<template>
  <div class="cheerup">
    <div class="cheerup-text">
      <h2>새롭게 저금통을 만든 사람들을 <span>응원</span>해보세요!</h2>
      <p>목표를 달성할 수 있도록 응원해주세요!</p>
    </div>

    <div class="cheerup-list">
      <div class="cheerup-container">
        <div class="cheerup-item" v-for="(item, index) in cheerupItems" :key="index">
          <p><span>오한나</span>님</p>
          <img src="@/assets/images/돼지 그림.png" alt="" class="cheerup-img">
          <p class="goal-name">결혼식 자금 모으기</p>
          <p class="cheerup-count">{{ item.count }}</p>
          <button class="cheerup-btn" @click="handleCheerup(index)">응원하기</button>
          <div class="bubble-wrapper">
            <div v-for="(bubble, bubbleIndex) in item.bubbles" 
                 :key="bubbleIndex" 
                 class="bubble-container">
              <img src="@/assets/images/cheerup.png" alt="" class="bubble-effect">
            </div>
          </div>
        </div>
        <div class="cheerup-item" v-for="(item, index) in cheerupItems" :key="index + cheerupItems.length">
          <p><span>오한나</span>님</p>
          <img src="@/assets/images/돼지 그림.png" alt="" class="cheerup-img">
          <p class="goal-name">결혼식 자금 모으기</p>
          <p class="cheerup-count">{{ item.count }}</p>
          <button class="cheerup-btn" @click="handleCheerup(index)">응원하기</button>
          <div class="bubble-wrapper">
            <div v-for="(bubble, bubbleIndex) in item.bubbles" 
                 :key="bubbleIndex" 
                 class="bubble-container">
              <img src="@/assets/images/cheerup.png" alt="" class="bubble-effect">
            </div>
          </div>
        </div>
      </div>
    </div>
    <img src="@/assets/images/stage.png" alt="" class="stage">
  </div>
</template>

<script setup>
import { ref } from 'vue';

const cheerupList = ref(5);
const cheerupItems = ref(Array(5).fill().map(() => ({
  count: 0,
  bubbles: []
})));

const handleCheerup = (index) => {
  cheerupItems.value[index].count++;
  const newBubble = Date.now();
  cheerupItems.value[index].bubbles.push(newBubble);
  
  setTimeout(() => {
    const bubbleIndex = cheerupItems.value[index].bubbles.indexOf(newBubble);
    if (bubbleIndex > -1) {
      cheerupItems.value[index].bubbles.splice(bubbleIndex, 1);
    }
  }, 1000);
};
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
  position: relative;
  overflow: hidden;
  width: 100%;
  padding: 10px 0;
}

.cheerup-container {
  display: flex;
  animation: slideLeft 20s linear infinite;
  width: fit-content;
}

.cheerup-container:hover {
  animation-play-state: paused;
  transition: all 500ms ease-in-out;
}

@keyframes slideLeft {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-50%);
  }
}

.cheerup-item {
  position: relative;
  width: 250px;
  box-shadow: 3px 5px 8px rgba(0, 0, 0, 0.25);
  padding: 20px 50px;
  border-radius: 15px;
  margin: 0px 15px;
  flex-shrink: 0;
}

.cheerup-item:hover {
  transform: scale(1.02);
  transition: tansform 500ms ease-in-out;
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
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
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
  border-radius: 8px;
  color: white;
  font-size: 12px;
  padding: 6px;
  bottom: 15px;
  right: 20px;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
}

.cheerup-item button:hover {
  transform: scale(1.05);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  opacity: 0.9;
}

.cheerup-item button:active {
  transform: scale(0.95);
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}

.stage {
  width: 100vw;
  margin-top: 20px;
}

.bubble-wrapper {
  position: absolute;
  bottom: 30px;
  right: 20px;
  pointer-events: none;
}

.bubble-container {
  position: absolute;
  bottom: 0;
  right: 0;
}

.bubble-effect {
  width: 30px;
  height: 30px;
  animation: bubbleFloat 1s ease-out forwards;
  opacity: 0;
}

@keyframes bubbleFloat {
  0% {
    transform: translateY(0) scale(0.5);
    opacity: 0;
  }
  10% {
    opacity: 1;
  }
  100% {
    transform: translateY(-100px) scale(1.2);
    opacity: 0;
  }
}
</style>