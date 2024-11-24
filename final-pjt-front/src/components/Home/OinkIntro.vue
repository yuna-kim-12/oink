<template>
    <div class="intro">
        <p class="main-text">목표 달성까지 쉽고, 재밌게.</p>
        <div class="logo-wrapper">
            <img src="/images/logo.png" alt="logo-img" class="logo-img">
            <img src="/images/logo.png" alt="logo-img" class="logo-img logo-glitch">
            <img src="/images/logo.png" alt="logo-img" class="logo-img logo-glitch-2">
            <img src="/images/logo.png" alt="logo-img" class="logo-img logo-glitch-3">
        </div>
        <div class="fabicon-container">
            <img :src="oinkImage" alt="" class="fabicon">
        </div>
    </div>
</template>

<script setup>

import oinkImage from '@/assets/images/bounce-oink.png'

</script>

<style scoped>
.intro {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100vh;
    background-image: url('/src/assets/images/intro-bg-img.png');
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center center;
}

.main-text {
    margin-bottom: 30px;
    font-size: 50px;
    font-weight: 900;
}

.logo-wrapper {
    position: relative;
    width: 250px;
}

.logo-img {
    width: 250px;
    position: absolute;
    left: 0;
}

.logo-glitch {
    opacity: 0.8;
    animation: glitch-1 2.5s infinite;
}

.logo-glitch-2 {
    opacity: 0.8;
    animation: glitch-2 3s infinite;
}

.logo-glitch-3 {
    opacity: 0.8;
    animation: old-tv 4s infinite;
}

.fabicon {
    width: 100px;
    height: 100px;
    animation: bounce 0.8s ease-in-out infinite;
    position: relative;
    z-index: 1;
    bottom: 193px;
    left: 255px;
}

.fabicon-container {
    position: relative;
    width: 100px;
    height: 100px;
}

.fabicon-container::after {
    content: '';
    position: absolute;
    bottom: 186px;
    left: 303px;
    transform: translateX(-50%);
    width: 80px;
    height: 20px;
    background: rgba(0, 0, 0, 0.1);
    border-radius: 50%;
    animation: shadow 0.8s ease-in-out infinite;
}

@keyframes bounce {
    0%, 100% {
        transform: translateY(0);
    }
    50% {
        transform: translateY(-20px);
    }
}

@keyframes shadow {
    0%, 100% {
        transform: translateX(-50%) scale(1);
        opacity: 0.5;
    }
    50% {
        transform: translateX(-50%) scale(0.5);
        opacity: 0.3;
    }
}

@keyframes glitch-1 {
    0%, 100% { 
        transform: translate(0);
        filter: brightness(1);
    }
    88% { 
        transform: translate(0);
        filter: brightness(1);
    }
    90% {
        transform: translate(-2px, 2px);
        filter: brightness(1.2);
    }
    92% {
        transform: translate(2px, -2px);
        filter: brightness(1.5);
    }
    94% {
        transform: translate(-2px, 2px);
        filter: brightness(1.2);
    }
    96% {
        transform: translate(2px, -2px);
        filter: brightness(1.5);
    }
    98% {
        transform: translate(-2px, 2px);
        filter: brightness(1.2);
    }
}

@keyframes glitch-2 {
    0%, 100% { 
        transform: translate(0);
        filter: brightness(1);
    }
    88% { 
        transform: translate(0);
        filter: brightness(1);
    }
    90% {
        transform: translate(2px, -2px);
        filter: brightness(1.3);
    }
    92% {
        transform: translate(-2px, 2px);
        filter: brightness(1.6);
    }
    94% {
        transform: translate(2px, -2px);
        filter: brightness(1.3);
    }
    96% {
        transform: translate(-2px, 2px);
        filter: brightness(1.6);
    }
    98% {
        transform: translate(2px, -2px);
        filter: brightness(1.3);
    }
}

@keyframes old-tv {
    0%, 100% {
        transform: translate(0) skew(0deg);
        filter: brightness(1);
    }
    20% {
        transform: translate(-3px) skew(-1deg);
        filter: brightness(1.1);
    }
    40% {
        transform: translate(3px) skew(1deg);
        filter: brightness(0.9);
    }
    42% {
        transform: translate(-5px) skew(-2deg);
        filter: brightness(1.2);
    }
    44% {
        transform: translate(5px) skew(2deg);
        filter: brightness(0.8);
    }
    46% {
        transform: translate(-3px) skew(-1deg);
        filter: brightness(1.3);
    }
    48% {
        transform: translate(3px) skew(1deg);
        filter: brightness(0.7);
    }
    50% {
        transform: translate(0) skew(0deg);
        filter: brightness(1);
    }
}
</style>