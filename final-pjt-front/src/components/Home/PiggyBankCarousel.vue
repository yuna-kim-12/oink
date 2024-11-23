<template>
    <div class="piggy-bank-carousel">
      <p>{{ currentPiggy.percentage }}% </p>
      <img :src="currentPiggy.image" :alt="currentPiggy.color + ' 돼지 저금통'">
      <div class="carousel-indicators">
        <span v-for="(piggy, index) in piggyBanks" 
              :key="index" 
              :class="['indicator', { 'active': index === currentIndex }]">
        </span>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, onUnmounted } from 'vue'
  
  const piggyBanks = [
    { color: '핑크', image: 'src/assets/images/pink-pig(25).png', percentage: '0 - 25' },
    { color: '블루', image: 'src/assets/images/green-pig(50).png', percentage: '26 - 50' },
    { color: '그린', image: 'src/assets/images/blue-pig(75).png', percentage: '51 - 75' },
    { color: '골드', image: 'src/assets/images/yellow-pig(100).png', percentage: '76 - 100' }
  ]
  
  const currentIndex = ref(0)
  const currentPiggy = ref(piggyBanks[0])
  
  const updatePiggy = () => {
    currentIndex.value = (currentIndex.value + 1) % piggyBanks.length
    currentPiggy.value = piggyBanks[currentIndex.value]
  }
  
  let intervalId
  
  onMounted(() => {
    intervalId = setInterval(updatePiggy, 2000) // 2초마다 변경
  })
  
  onUnmounted(() => {
    clearInterval(intervalId)
  })
  </script>
  
  <style scoped>
  .piggy-bank-carousel {
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .piggy-bank-carousel img {
    width: 200px;
    height: 200px;
    object-fit: contain;
  }
  
  .piggy-bank-carousel p {
    margin-top: 10px;
    color: var(--sub-text-color);
    font-weight: bold;
    font-size: 20px;
  }
  
  .carousel-indicators {
    display: flex;
    justify-content: center;
    margin-top: 10px;
  }
  
  .indicator {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background-color: #ccc;
    margin: 0 5px;
    transition: all 0.3s ease;
  }
  
  .indicator.active {
    width: 20px;
    border-radius: 4px;
    background-color: var(--sub-text-color);
  }
  </style>