<template>
    <div>
        <OinkIntro />
        <PiggyBank />
        <PiggyBankInfo />

        <div class="product-recommend">
            <h2 class="recommendation-badge1">돼지 저금통을 불릴 수 있는</h2>
            <h2 class="recommendation-badge2">예적금 상품을 추천해드려요.</h2>
            <ProductRecommend />
        </div>
        <button class="create-piggy" v-show="showButton" @click="navigateToPiggyCreate">
            저금통 만들러 가기
        </button>

        <div class="community-intro">
            <div class="community-intro-text">
                <img src="@/assets/images/coin.png" alt="coin-img">
                <h2><span>나와 같은 목표</span>를 가진<br>사람들의 소식을 만나보실 수도 있어요</h2>
                <img src="@/assets/images/coin.png" alt="coin-img">
            </div>
            <img src="@/assets/images/community.png" alt="">
        </div>

        <Cheerup />
    </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';
import OinkIntro from '@/components/OinkIntro.vue';
import PiggyBank from '@/components/PiggyBank.vue';
import PiggyBankInfo from '@/components/PiggyBankInfo.vue';
import RecommendView from './RecommendView.vue';
import ProductRecommend from '@/components/ProductRecommend.vue';
import Cheerup from '@/components/Cheerup.vue';

const showButton = ref(false);
const router = useRouter();

const handleScroll = () => {
    showButton.value = window.scrollY > 200;
};

const navigateToPiggyCreate = () => {
    router.push('/profile');
};

onMounted(() => {
    window.addEventListener('scroll', handleScroll);
});

onUnmounted(() => {
    window.removeEventListener('scroll', handleScroll);
});
</script>

<style scoped>
/* 상품 추천 */
.recommend {
  margin-bottom: 60px;
  text-align: center;
}

.recommendation-badge {
  margin-bottom: 5px;
  font-size: 30px;
  font-weight: 700;
  color: #020202;
}

/* 저금통 만들러 가기 버튼 */
.create-piggy {
    position: fixed;
    bottom: 65px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 999;
    padding: 12px 24px;
    border-radius: 15px;
    color: black;
    border: none;
    cursor: pointer;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    transition: all 0.3s ease;
    white-space: nowrap;
}

/* 커뮤니티 소개 */
.create-piggy:hover {
    transform: translateX(-50%) translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.community-intro {
    margin: 100px auto 200px;
    text-align: center;
}

.community-intro>img {
    width: 80%;
    max-width: 1000px;
}

.community-intro-text {
    position: relative;
    display: inline-block;
    margin: 100px 0;
    padding: 50px 0;
    text-align: center;
    color: var(--sub-text-bold-color);
}

.community-intro-text span,
.community-intro-text h2 {
    font-weight: 700;
}

.community-intro-text h2 {
    font-size: 30px;
}

.community-intro-text span {
    color: var(--main-text-color);
}

.community-intro-text img:first-child {
    position: absolute;
    top: 0;
    right: 166px;
    width: 50px;
    height: 50px;
    transform: rotate(-30deg);
}

.community-intro-text img:last-child {
    position: absolute;
    bottom: -27px;
    left: 110px;
    width: 70px;
    height: 70px;
    transform: rotate(-60deg);
}

.product-recommend {
    /* text-align: center; */
    
    padding: 50px 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: rgb(248, 248, 248);
}

.product-recommend-text {
    padding: 50px 0;
    font-size: 30px;
    font-weight: 700;
}

.recommend {
  margin-bottom: 80px;
  margin-top: 60px;
  text-align: center;
}
.recommendation-badge1,
.recommendation-badge2 {
  margin-bottom: 5px;
  font-size: 30px;
  font-weight: 700;
  color: #020202;
}

.recommendation-badge2{
    margin-bottom: 50px;
}

</style>