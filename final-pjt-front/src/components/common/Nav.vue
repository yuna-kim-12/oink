<template>
  <nav class="nav scrolled">
    <h1 class="logo">
      <RouterLink :to="{name:'home'}">
        <img src="/images/logo.png" alt="logo-img">
      </RouterLink>
    </h1>
    <div class="real-nav">
      <RouterLink :to="{name:'recommend'}">금융상품추천</RouterLink>
      <RouterLink :to="{name:'map'}">지도</RouterLink>
      <RouterLink :to="{name:'community'}">커뮤니티</RouterLink>
      <RouterLink :to="{name:'exchange'}">환율 계산기</RouterLink>
    </div>

    <div class="is-logged-in" v-if="store.isLoggedIn">
      <button @click="router.push({ name: 'profile', params: { userId: store.userPK }})">
        <i class="pi pi-user user-icon"></i>
      </button>
      <button @click="store.logOut" class="logout-btn">
      로그아웃
      </button>
    </div>

  <RouterLink
  v-else
  :to="{name: 'login'}" class="login-btn">로그인</RouterLink>
 
  </nav>
</template>

<script setup>
import { onMounted, onUnmounted } from 'vue'
import { gsap } from 'gsap'
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user';

const router = useRouter()
const store = useUserStore()

const handleScroll = () => {
  const nav = document.querySelector('.nav');
  if (window.scrollY > 0) {
    nav.classList.remove('scrolled');
  } else {
    nav.classList.add('scrolled');
  }
};

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
});
</script>

<style scoped>
.nav {
  position: fixed;
  top: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  min-width: 900px;
  margin: 0 auto;
  padding: 10px 15%;
  background-color: #fff;
  z-index: 100;
  border-bottom: none;
}

.nav.scrolled {
  border-bottom: 1px solid var(--main-color);
  background-color: rgba(255, 255, 255, 0.8);
  transition: all 0.3s ease; 
}

.logo img {
  width: 90px;
}

.real-nav {
  display: flex;
}

.real-nav a {
  padding: 12px 30px;
  color: #B9B9B9;
  font-size: 18px;
  font-weight: 600;
}

.real-nav a:hover {
  color: var(--main-text-color);
  transform: scale(1.1);
  transition: all 450ms ease-in-out;
}

.real-nav a.router-link-exact-active {
  color: var(--main-text-color);
}

.is-logged-in button:first-child {
  background-color: transparent;
}

.user-icon {
  cursor: pointer;
  padding: 10px;
  color: white;
  background-color: var(--main-color);
  border-radius: 50%;
  height: 32px;
  width: 35px;
  margin-right: 20px;
}


.login-btn,
.logout-btn {
  background-color: var(--main-color);
  color: white;
  padding: 5px 12px;
  border-radius: 30px;
  width: 83px;
  font-size: 13px;
  width: 83px;
  height: 29px;
  text-align: center;
}

button.login-btn {
  border: none;
  cursor: pointer;
  padding: 5px 12px;
  font-size: 13px;
  width: 83px;
  height: 29px;
  margin-top: 10px;
}
</style>