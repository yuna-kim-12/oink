<template>
  <div class="popup-overlay" @click.self="$emit('close')">
    <div class="popup-content">
      <div class="popup-header">
        <div class="tab-container">
          <div
            class="tab"
            :class="{ active: type === 'following' }"
            @click="$emit('update:type', 'following')"
          >
            <span class="following">팔로잉 </span>
            <span class="followings-count" style="color: var(--sub-text-color);">{{ store.user.followings_count }}</span>
            <!--도저히 귀찮아서 inline으로 적는 점 양해 좀-->
          </div>
          <div
            class="tab"
            :class="{ active: type === 'followers' }"
            @click="$emit('update:type', 'followers')"
          >
            <span class="follower">팔로워  </span>
            <span class="followers-count" style="color: var(--sub-text-color);">{{ store.user.followers_count }}</span>
          </div>
        </div>
    </div>
    <button class="close-btn" @click="$emit('close')">&times;</button>

      <div class="popup-body">
        <!-- 팔로잉 목록 -->
        <div v-if="type === 'following'">
          <div v-for="following in followingsList" 
              :key="following.pk" 
              class="real-following">
            <p><RouterLink :to="{ name: 'profile', params: { userId: following.pk } }">
              {{ following.name }}
            </RouterLink></p>
            <button 
              @click="handleFollow(following.pk)"
              :class="{ 'following-active': store.followStatus[following.pk] }"
            >
              {{ store.followStatus[following.pk] ? '팔로잉' : '팔로우' }}
            </button>
          </div>
        </div>
        <!-- 팔로워 목록 -->
        <div v-else>
          <div v-for="follower in followersList" 
              :key="follower.pk" 
              class="real-follower">
            <p><RouterLink :to="{ name: 'profile', params: { userId: following.pk } }">
              {{ following.name }}
            </RouterLink></p>
            <button 
              @click="handleFollow(follower.pk)"
              :class="{ 'following-active': store.followStatus[follower.pk] }"
            >
              {{ store.followStatus[follower.pk] ? '팔로잉' : '팔로우' }}
            </button>
          </div>
        </div>
      </div>
      
    </div>
  </div>
</template>

<script setup>

import { useUserStore } from '@/stores/user';
import { onMounted, ref } from 'vue'

const store = useUserStore()
const emit = defineEmits(["close", "update:type"])

// 로컬 상태로 목록 관리
const followingsList = ref([])
const followersList = ref([])

// 초기 데이터 설정
const initializeLists = () => {
  followingsList.value = [...store.user.followings]
  followersList.value = [...store.user.followers]
}

const handleFollow = async (userPK) => {
  try {
    await store.toggleFollow(userPK)
  } catch (error) {
    console.error('팔로우 처리 중 에러:', error)
  }
}

// 팝업 닫기 핸들러
const handleClose = async () => {
  // 팝업 닫기 전에 유저 정보 갱신
  await store.getUserInfo()
  emit('close')
}

onMounted(() => {
  store.getUserInfo().then(() => {
    store.setInitialFollowStatus()
    initializeLists()
  })
})

// const followCondition = () => {
//   if (store.user.is_following === true) {
//     store.user.is_following = false
//     console.log(store.user.is_following)
//   }
//   else {
//       store.user.is_following = true
//       console.log(store.user.is_following)
//     }
//   }
  

// onMounted(()=>{
//   followCondition()
// })


  // 팝업창 팔로워, 팔로잉 탭 상태 확인, 이거 지우면 안됨
  defineProps({
    type: {
      type: String,
      required: true,
    },
  });
  
  // defineEmits(["close", "update:type"]);
</script>

<style scoped>
.popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.popup-content {
  background: white;
  border-radius: 8px;
  width: 90%;
  max-width: 500px;
  max-height: 80vh;
  /* height: 80vh; */
  position: relative;
  /* display: flex;
  flex-direction: column; */
}

.popup-header {
padding: 15px;
border-bottom: 1px solid #eee;
display: flex;
justify-content: center;
align-items: center;
text-align: center;
}

.tab-container {
display: flex;
gap: 20px;
}

.following,
.follower {
color: var(--sub-text-color);
}

.tab.active .following,
.tab.active .follower {
color: var(--point-text-color);
}

.tab {
padding: 8px 16px;
cursor: pointer;
border-bottom: 2px solid transparent;
}

.tab.active {
border-bottom: 0.5px solid var(--sub-text-color);
font-weight: bold;
}

.close-btn {
position: absolute;
right: 8px;
top: 6px;
background-color: #eee;
border-radius: 100%;
padding: 0px 3.3px;
border: none;
font-size: 13px;
cursor: pointer;
}

.popup-body {
  padding: 20px;
  max-height: calc(80vh - 60px);
  overflow-y: auto;
  display: flex;
  justify-content: center;
}

.real-following, .real-follower {
  width: 400px;
  box-shadow: 0px 4px 4px #b2b2b2;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 15px 0;
  padding: 15px 20px 15px 50px;
}

.real-following, p {
  border-radius: 15px;
  }
  
.real-follower, p {
    border-radius: 15px;
}


.following-active {
  background-color: #e0e0e0;
}

button {
  padding: 0px 15px;
  height: 30px;
  border-radius: 20px;
  border: 1px solid #ccc;
  cursor: pointer;
  transition: all 0.3s ease;
  background-color: var(--point-color);
}

button:hover {
  background-color: var(--main-color);
}
</style>
