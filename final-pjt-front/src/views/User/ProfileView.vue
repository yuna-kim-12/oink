<template>
  <div class="container">
    <h2 class="title">{{ isCurrentUser ? "마이 페이지" : `${userInfo?.name || ''}님의 프로필` }}</h2>
    <div class="content" v-if="userInfo">
      <div class="sub-title">
        <div class="user-info">
          <p class="user-name">
            <span class="user-realname">{{ userInfo.name }}</span>님
          </p>
          <button v-if="isCurrentUser" class="modify-btn" @click="router.push('/updateUser')">
            내 정보 수정
          </button>
          <button v-else 
            class="follow-btn"
            :class="{ 'following-active': store.followStatus[route.params.userId] }"
            @click="handleFollow"
          >
            {{ store.followStatus[route.params.userId] ? "팔로잉" : "팔로우" }}
          </button>
        </div>
        <div class="follow">
          <div class="stack-piggy">
            <p>{{ userInfo.piggy_bank.length }}</p>
            <span>누적 저금통</span>
          </div>
          <div class="following" :class="{ clickable: isCurrentUser }" @click="isCurrentUser && openFollowPopup('following')">
            <p>{{ userInfo.followings_count }}</p>
            <span>팔로잉</span>
          </div>
          <div class="follower" :class="{ clickable: isCurrentUser }" @click="isCurrentUser && openFollowPopup('followers')">
            <p>{{ userInfo.followers_count }}</p>
            <span>팔로워</span>
          </div>
        </div>
      </div>
      <PiggyBank 
        :is-current-user="isCurrentUser"
        :piggy-bank-pk="userInfo.piggy_bank.length ? userInfo.piggy_bank[0].pk : null"
      />
      <div class="product" v-if="isCurrentUser">
        <span>내가 가입한 예적금 상품</span>
        <button class="product-btn" @click="connectMyProduct">연동 하기</button>
      </div>
      <div class="product-items" v-if="isCurrentUser">
        <p class="no-product" v-if="myProducts.length == 0">
          아직 연동된 상품이 없습니다.
        </p>
        <template v-else>
          <ProfileUserProduct 
            v-for="(myProduct, index) in myProducts" 
            :key="myProduct.pk" 
            :my-product="myProduct" 
            :index="index"
          />
          <div class="chart">
            <p class="chart-title">내가 가입한 예적금 상품 금리</p>
            <ProfileChart :click-count="clickCount" />
          </div>
        </template>
      </div>
    </div>
    <br />
    <FollowPopUp 
      v-if="showFollowPopup && isCurrentUser" 
      v-model:type="popupType" 
      @close="closeFollowPopup"
    />
  </div>
</template>

<script setup>
import { onMounted, ref, computed, watch } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useUserStore } from "@/stores/user";
import ProfileUserProduct from "@/components/Profile/ProfileUserProduct.vue";
import ProfileChart from "@/components/Profile/ProfileChart.vue";
import FollowPopUp from "@/components/Profile/FollowPopUp.vue";
import PiggyBank from "@/components/PiggyBank.vue";
import axios from "axios";

const route = useRoute();
const router = useRouter();
const store = useUserStore();
const userInfo = ref(null);
const showFollowPopup = ref(false);
const popupType = ref("");
const myProducts = ref([]);
let clickCount = 0;

const isCurrentUser = computed(() => {
  return store.userPK === Number(route.params.userId);
});

const handleFollow = async () => {
  try {
    await store.toggleFollow(route.params.userId);
    getUserProfile(route.params.userId);
  } catch (err) {
    console.log(err);
  }
};

watch(
  () => route.params.userId,
  (newUserId) => {
    if (newUserId) {
      getUserProfile(newUserId);
      store.setInitialFollowStatus();
    }
  }
);

const getUserProfile = async (userId) => {
  try {
    const response = await axios({
      method: "get",
      url: `${store.url}/accounts/profile/${userId}/`,
      headers: {
        Authorization: `Token ${store.token}`,
      },
    });
    userInfo.value = response.data;
    console.log('User Profile Data:', userInfo.value);  // 데이터 확인
    console.log('Piggy Bank Data:', userInfo.value.piggy_bank);  // piggy_bank 데이터 확인
    if (isCurrentUser.value) {
      getMyProduct();
    }
  } catch (err) {
    console.log(err);
  }
};

const getMyProduct = () => {
  axios({
    method: "get",
    url: `${store.url}/bank_products/products_joined/${store.userPK}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      myProducts.value = res.data;
    })
    .catch((err) => console.log(err));
};

const connectMyProduct = () => {
  axios({
    method: "post",
    url: `${store.url}/bank_products/products_joined/${store.userPK}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      myProducts.value = res.data.data;
      clickCount += 1;
      alert(res.data.detail);
    })
    .catch((err) => console.log(err));
};

const openFollowPopup = (type) => {
  popupType.value = type;
  showFollowPopup.value = true;
};

const closeFollowPopup = () => {
  showFollowPopup.value = false;
};

onMounted(() => {
  if (route.params.userId) {
    getUserProfile(route.params.userId);
    store.setInitialFollowStatus();
  }
});
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 800px;
  margin: 0 auto;
  margin-top: 150px;
}

.title {
  margin: 0 auto;
  margin-bottom: 85px;
  color: var(--main-color);
  font-weight: bold;
}

.sub-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.user-info {
  display: flex;
  justify-content: center;
  align-items: flex-end;
}

.user-name {
  display: flex;
  justify-content: left;
  font-size: 25px;
  color: #bebebe;
  font-weight: 700;
}

.user-realname {
  color: #746ef4;
  font-weight: 700;
  margin-right: 5px;
}

.modify-btn {
  background-color: var(--main-color);
  color: white;
  border-radius: 20px;
  margin-left: 10px;
  margin-bottom: 6px;
  padding: 2px 8px;
  font-size: 12px;
  cursor: pointer;
}

.follow-btn {
  background-color: var(--point-color);
  color: white;
  border-radius: 20px;
  margin: 0px 10px;
  padding: 2px 8px;
  font-size: 12px;
  cursor: pointer;
  margin-bottom: 6px;
  border: 1px solid var(--point-color);
  transition: all 0.3s ease;
}

.follow-btn.following-active {
  background-color: #e0e0e0;
  border: 1px solid #ccc;
  color: var(--sub-text-color);
}

.follow-btn:hover {
  background-color: var(--main-color);
}

.follow-btn.following-active:hover {
  background-color: #d0d0d0;
}

.follow {
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.follow p {
  text-align: center;
  color: var(--sub-text-color);
  font-weight: 550;
}

.follow span {
  margin: 0 20px;
  color: var(--main-color);
  font-weight: 500;
}

.product {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.product > span {
  font-size: 18px;
  font-weight: 700;
  color: #808080;
}

.product > button {
  font-size: 12px;
  background-color: var(--main-color);
  color: white;
  padding: 0 8px;
  border-radius: 20px;
  cursor: pointer;
}

.product-items > .no-product {
  text-align: center;
  margin: 40px 0;
  font-size: 18px;
  font-weight: bold;
  color: #808080;
}

.chart {
  margin-top: 40px;
}

.chart > .chart-title {
  margin: 20px 0;
  font-size: 18px;
  font-weight: 700;
  color: #808080;
}

.chart > div {
  text-align: center;
}
</style>