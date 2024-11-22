<template>
  <nav class="nav">
    <RouterLink :to="{name:'home'}" class="logo">
      <img src="/images/logo.png" alt="logo-img">
    </RouterLink>
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
import { onMounted } from 'vue'
import { gsap } from 'gsap'
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user';
import { useRoute } from 'vue-router';

const router = useRouter()
const store = useUserStore()

onMounted(() => {
  // Homepage container animation
  gsap.fromTo(".recommendation-container",
    { opacity: 0, y: -50 },
    { opacity: 1, y: 0, duration: 1, ease: "power2.out" }
  );
  
  // Navbar animation with timing sync
  const stagger = 0.6;
  const totalProducts = 5;
  const productAnimationDuration = 3;
  const totalDelay = (totalProducts * stagger + productAnimationDuration);
  
  gsap.fromTo(".nav",
    { opacity: 0, y: -50 },
    { 
      opacity: 1, 
      y: 0, 
      duration: 1,
      delay: 0.2,
      ease: "power2.out"
    }
  );
});
</script>

<style scoped>
.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1280px;
  min-width: 900px;
  margin: 0 auto;
  padding: 10px 20px;
  border-bottom: 1px solid var(--main-color);
  background: #fff;
  opacity: 80%;
}

.logo img {
  width: 90px;
}

.real-nav {
  display: flex;
}

.real-nav a {
  padding: 12px;
  color: #B9B9B9;
  font-size: 18px;
  font-weight: 600;
}

.real-nav a:hover {
  color: var(--main-text-color);
  transform: scale(1.1);
  transition: all 450ms ease-in-out;
}

.user-icon {
  cursor: pointer;
  padding: 10px;
  color: white;
  background-color: var(--main-color);
  border-radius: 50%;
  height: 32px;
  width: 35px;
  margin-right: 5px;
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