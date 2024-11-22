<template>
    <div class="recommendation-container">
      <h2 class="title">금융상품추천</h2>
      <ProductRecommend />
      <ProductList />
    </div>
  </template>
  
  <script setup>
  import { onMounted, ref, computed } from 'vue';
  import { gsap } from 'gsap';
  import { useUserStore } from '@/stores/user';
  import { useRecommendStore } from '@/stores/recommend';
  import ProductRecommend from '@/components/ProductRecommend.vue';
  import ProductList from '@/components/ProductList.vue';

  const userStore = useUserStore();
  const recommendStore = useRecommendStore();
  const category = ref(false); // false는 예금, true는 적금
  
  const setCategory = (value) => {
    category.value = value;
  };
  
  const sliderStyle = computed(() => ({
    transform: category.value ? 'translateX(100%)' : 'translateX(0)'
  }));
  
  const getBankLogo = (categoryName) => {
    const bankName = categoryName.split(' > ').pop();
    const bankLogos = {
      'KB국민은행': 'src/assets/images/kb.png',
      '신한은행': 'src/assets/images/shinhan.png',
      '하나은행': 'src/assets/images/hana.png',
      '우리은행': 'src/assets/images/woori.png',
      'NH농협은행': 'src/assets/images/nh.png',
      'IBK기업은행': 'src/assets/images/IBK.png',
      'KDB산업은행': 'src/assets/images/KDB.png',
      'SC제일은행': 'src/assets/images/sc.png',
      '부산은행': 'src/assets/images/BUSAN.png',
      'iM뱅크': 'src/assets/images/IM.png',
      'SH수협은행': 'src/assets/images/SH.png',
      '경남은행': 'src/assets/images/BUSAN.png',
      '카카오뱅크': 'src/assets/images/kakao.png',
      '광주은행': 'src/assets/images/KWANGJU.png',
      '토스뱅크': 'src/assets/images/toss.png',
      '전북은행': 'src/assets/images/JEONBUK.png',
      '케이뱅크': 'src/assets/images/kbank.png',
      '제주은행': 'src/assets/images/shinhan.png',
    };
    return bankLogos[bankName] || '/images/default.png';
  };
  
  onMounted(() => {
    recommendStore.getProduct();
    const productItems = document.querySelectorAll('.product-item');
    
    gsap.fromTo(".recommendation-container", 
      { opacity: 0, y: -50 }, 
      { 
        opacity: 1, 
        y: 0, 
        duration: 1, 
        delay: 0.8,
        ease: "power2.out",
        onComplete: () => {
          productItems.forEach((item, index) => {
            const card = item.querySelector('.product-card-inner');
            let isAnimating = true;
            const animationDelay = index * 0.6;
            const animationDuration = 3;
            const totalAnimationTime = (animationDelay + animationDuration) * 1000;
            
            setTimeout(() => {
              isAnimating = false;
            }, totalAnimationTime);
            
            item.addEventListener('mouseenter', () => {
              if (!isAnimating) {
                card.style.animation = 'none';
                item.classList.add('hover-effect');
              }
            });
            
            item.addEventListener('mouseleave', () => {
              if (!isAnimating) {
                item.classList.remove('hover-effect');
              }
            });
          });
        }
      }
    );
  });
  </script>
  
  <style scoped>

  .recommendation-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin: 150px auto 0px;
    width: 1280px;
}

.recommendation-container {
  text-align: center;
}

.title {
    display: flex;
    justify-content: center;
    align-content: center;
    color: var(--main-color);
    font-weight: bold;
    margin-bottom: 70px;
  }

  </style>
