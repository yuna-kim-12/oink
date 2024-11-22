<template>
    <div class="piggy-bank-carousel">
      <img :src="currentPiggy.image" :alt="currentPiggy.color + ' 돼지 저금통'">
      <p>목표 {{ currentPiggy.percentage }}% 달성</p>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, onUnmounted } from 'vue'
  
  const piggyBanks = [
    { color: '핑크', image: 'src/assets/images/bank_logo/kb.png', percentage: '0 - 25' },
    { color: '블루', image: 'src/assets/images/bank_logo/woori.png', percentage: '26 - 50' },
    { color: '그린', image: 'src/assets/images/bank_logo/toss.png', percentage: '51 - 75' },
    { color: '골드', image: 'src/assets/images/bank_logo/sc.png', percentage: '76 - 100' }
  ]
  
  const currentIndex = ref(0)
  const currentPiggy = ref(piggyBanks[0])
  
  const updatePiggy = () => {
    currentIndex.value = (currentIndex.value + 1) % piggyBanks.length
    currentPiggy.value = piggyBanks[currentIndex.value]
  }
  
  let intervalId
  
  onMounted(() => {
    intervalId = setInterval(updatePiggy, 2000) // 3초마다 변경
  })
  
  onUnmounted(() => {
    clearInterval(intervalId)
  })
  </script>
  
  <style scoped>
  .piggy-bank-carousel {
    text-align: center;
  }
  
  .piggy-bank-carousel img {
    width: 200px;
    height: 200px;
    object-fit: contain;
  }
  
  .piggy-bank-carousel p {
    margin-top: 10px;
    font-weight: bold;
  }
  </style>