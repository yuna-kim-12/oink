<template>
    <div class="intro">
        <p class="main-text">목표 달성까지 쉽고, 재밌게.</p>
        <img src="/images/logo.png" alt="logo-img" class="logo-img">
    </div>
</template>

<script setup>

</script>

<style scoped>
.intro {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100vh;
    background-image: url('src/assets/intro-bg-img.png');
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center center;
}

.main-text {
    margin-bottom: 30px;
    font-size: 50px;
    font-weight: 900;
}

.logo-img {
    width: 250px;
    margin-bottom: 200px;
}
</style>