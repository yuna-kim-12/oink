<template>
    <div>
        <OinkIntro/>
        <PiggyBank/>
        <PiggyBankInfo/>
        <RecommendView/>
        <button 
            class="create-piggy"
            v-show="showButton"
            @click="navigateToPiggyCreate"
        >
            저금통 만들러 가기
        </button>

        <div class="community-intro">
            <div class="community-intro-text">
                <img src="@/assets/images/coin.png" alt="coin-img">
                <p><span>나와 같은 목표</span>를 가진<br>사람들의 소식을 만나보실 수도 있어요</p>
                <img src="@/assets/images/coin.png" alt="coin-img">
            </div>
            <img src="@/assets/images/community.png" alt="">
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';
import OinkIntro from '@/components/OinkIntro.vue';
import PiggyBank from '@/components/PiggyBank.vue';
import PiggyBankInfo from '@/components/PiggyBankInfo.vue';
import RecommendView from './RecommendView.vue';

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

.community-intro {
    margin: 100px auto;
    text-align: center;
}

.community-intro > img {
    width: 80%;
    max-width: 1000px;
}
</style>