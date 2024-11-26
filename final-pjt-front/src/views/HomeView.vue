<template>
    <div>
        <OinkIntro />

        <div class="piggy-text scroll-animation">
            <p v-if="userStore.isLoggedIn && userStore.user" class="piggy-user">
                <span>{{ userStore.user.name }}</span>님의 돼지 저금통
            </p>
            <p v-else class="piggy-recommend">나만의 <span>돼지 저금통</span>을 만들어 금융 자산을 관리하고,<br>
                저금통을 무겁게 만들 <span>금융 상품</span>을 추천 받아보세요!</p>
        </div>
        
        <div class="scroll-animation">
            <PiggyBank />
        </div>

        <div class="scroll-animation">
            <PiggyBankInfo />
        </div>

        <div class="product-recommend scroll-animation">
            <h2 class="recommendation-badge" v-if="!userStore.isLoggedIn">돼지 저금통을 불릴 수 있는<br>예적금 상품을 추천해드려요.</h2>
            <ProductRecommend />
        </div>

        <button class="create-piggy" v-show="showButton && !userStore.isLoggedIn" @click="navigateToPiggyCreate">
            저금통 만들러 가기
        </button>

        <div class="community-intro scroll-animation">
            <div class="community-intro-text">
                <img src="@/assets/images/coin.png" alt="coin-img">
                <h2><span>나와 같은 목표</span>를 가진<br>사람들의 소식을 만나보실 수도 있어요</h2>
                <img src="@/assets/images/coin.png" alt="coin-img">
            </div>
            <img src="@/assets/images/community.png" alt="">
        </div>

        <div class="scroll-animation">
            <Cheerup />
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user';
import OinkIntro from '@/components/Home/OinkIntro.vue';
import PiggyBank from '@/components/PiggyBank.vue';
import PiggyBankInfo from '@/components/Home/PiggyBankInfo.vue';
import ProductRecommend from '@/components/ProductRecommend/ProductRecommend.vue';
import Cheerup from '@/components/Home/Cheerup.vue';

const router = useRouter();
const userStore = useUserStore()

const showButton = ref(false);

const handleScroll = () => {
    showButton.value = window.scrollY > 200;
};

const navigateToPiggyCreate = () => {
    router.push({ name: 'login' });
};

onMounted(() => {
    window.addEventListener('scroll', handleScroll);
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show');
            }
        });
    }, {
        threshold: 0.1
    });

    document.querySelectorAll('.scroll-animation').forEach((el) => observer.observe(el));
});

onUnmounted(() => {
    window.removeEventListener('scroll', handleScroll);
});
</script>

<style scoped>
/* 스크롤 애니메이션 */
.scroll-animation {
    opacity: 0;
    transform: translateY(50px);
    transition: all 1s ease;
}

.scroll-animation.show {
    opacity: 1;
    transform: translateY(0);
}

/* 돼지 저금통 큰 제목 */
.piggy-text {
    margin-top: 50px;
}

.piggy-text p {
    width: 740px;
    margin: 0 auto;
    padding-left: 20px;
    font-size: 25px;
    font-weight: 700;
    color: var(--sub-text-color);
}

.piggy-text span {
    font-weight: 700;
    color: var(--main-text-color);
}

.piggy-recommend {
    text-align: center;
}

.piggy-recommend span:last-child {
    color: var(--point-color);
}

/* 상품 추천 */
.product-recommend {
    text-align: center;
    padding: 50px 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: rgb(248, 248, 248);
}

.recommendation-badge {
    margin-bottom: 80px;
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

.create-piggy:hover {
    transform: translateX(-50%) translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

/* 커뮤니티 소개 */
.community-intro {
    margin: 100px auto 200px;
    text-align: center;
}

.community-intro>img {
    display: block;
    width: 80%;
    max-width: 1000px;
    margin: 30px auto 0;
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
</style>