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
        <div v-if="type === 'following'">
          <!-- 팔로잉 목록 -->
           {{ store.user.followings }}
        </div>
        <div v-else>
          <!-- 팔로워 목록 -->
           {{ store.user.followers }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>

import { useUserStore } from '@/stores/user';

const store = useUserStore()

// 팝업창 팔로워, 팔로잉 탭 상태 확인, 이거 지우면 안됨
defineProps({
  type: {
    type: String,
    required: true,
  },
});

defineEmits(["close", "update:type"]);
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
  position: relative;
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
}
</style>
