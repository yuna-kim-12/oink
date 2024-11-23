<template>
    <div class="container">
        <h2 class="title">마이 페이지</h2>
        
        <div class="content" v-if="store.user">
            <div class="sub-title">
                <div class="user-info">
                    <p class="user-name"><span class="user-realname">{{ store.user.name }}</span class="nim">님</p>
                    <button class="modify-btn" @click="router.push('/updateUser')">내 정보 수정</button>
                </div>
                <div class="follow">
                    <div class="stack-piggy">
                        <p>{{ store.user.piggy_bank.length }}</p>
                        <span>누적 저금통</span>
                    </div>
                    <div class="following" @click="openFollowPopup('following')">
                        <p>{{ store.user.followings_count }}</p>
                        <span>팔로잉</span>
                    </div>
                    <div class="follower" @click="openFollowPopup('followers')">
                        <p>{{ store.user.followers_count }}</p>
                        <span>팔로워</span>
                    </div>
                </div>
            </div>
            <div class="product">
                <span>내가 가입한 예적금 상품</span>
                <button class="product-btn" @click="connectMyProduct">연동 하기</button>
            </div>
            
            <div class ="product-items">
                <p class="no-product" v-if="myProducts.length==0">아직 연동된 상품이 없습니다.</p>
                <template v-else>
                    <ProfileUserProduct 
                        v-for="(myProduct, index) in myProducts"
                        :key="myProduct.pk"
                        :my-product="myProduct"
                        :index="index"
                    />
                    <div class="chart">
                        <p class="chart-title">내가 가입한 예적금 상품 금리</p>
                        <ProfileChart
                            :click-count="clickCount"
                        />
                    </div>
                </template>
            </div>
        </div>

        <br>

        <FollowPopUp
            v-if="showFollowPopup"
            v-model:type="popupType"
            @close="closeFollowPopup"
        />
    </div>
</template>

<script setup>

import ProfileUserProduct from '@/components/Profile/ProfileUserProduct.vue';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user';
import ProfileChart from '@/components/Profile/ProfileChart.vue';
import { onMounted, ref } from 'vue';
import axios from 'axios';
import { storeToRefs } from 'pinia';
import FollowPopUp from '@/components/Profile/FollowPopUp.vue';

const router = useRouter()
const store = useUserStore()
const showFollowPopup = ref(false) // 팔로우 팝업 창
const popupType = ref('') // 팔로잉이나 팔로워

const url = store.url
// const { userPK, token } = storeToRefs(useUserStore)
const userPK = ref(store.userPK)
const token = ref(store.token)
let clickCount = 0

const myProducts = ref([])

onMounted(() => {
    store.getUserInfo()
    getMyProduct()
    console.log(myProducts.value)
})

// 1. 연동된 경우, 바로 조회
const getMyProduct = () => {
    axios({
        method:'get',
        url:`${url}/bank_products/products_joined/${userPK.value}/`,
        headers:{
            Authorization:`Token ${token.value}`
        }
    })
    .then((res) => {
        myProducts.value = res.data
        console.log('조회요청함')
        // console.log(res.data)
    })
    .catch((err) => console.log(err, userPK.value, token.value))
}


// 2. 연동하기
const connectMyProduct = () => {
    axios({
        method:'post',
        url:`${url}/bank_products/products_joined/${userPK.value}/`,
        headers:{
            Authorization:`Token ${token.value}`
        }
    })
    .then((res) => {
        myProducts.value = res.data.data
        // console.log(res.data)
        clickCount += 1
        console.log(clickCount)
        alert(res.data.detail)
    })
    .catch((err) => console.log(err, userPK.value, token.value))
}


// 팔로잉 팝업 창 열기
const openFollowPopup = (type) => {
    popupType.value = type
    showFollowPopup.value = true
}

// 팔로잉 팝업 창 닫기
const closeFollowPopup = () => {
    showFollowPopup.value = false
}

</script>


<style scoped>
.container {
    display: flex;
    flex-direction: column;
    width: 60%;
    margin: 0 auto;
    margin-top: 150px;
}

/* .content {
    margin-left: 180px;
} */

.title {
    margin: 0 auto;
    margin-bottom: 85px;
    color: var(--main-color);
    font-weight: bold;
}

.sub-title {
    display: flex;
    justify-content: space-between  ;
    position: relative;
}

.user-info {
    display: flex;
}

.user-info button {
    margin-left: 10px;
}

.follow {
    display: flex;
    position: absolute;
    right: -16px;
    bottom: 26px;
    cursor: pointer;
}

.follow p {
    margin: 0 20px;
    text-align: center;
    color: var(--sub-text-color);
    font-weight: 550;
}

.follow span { 
    margin: 0 20px;
    color: var(--main-color);
    font-weight: 500;
}



.user-name {
    display: flex;
    justify-content: left;
    font-size: 20px;
    color: #bebebe;
    font-weight: 700;
}

.user-realname {
    color: #746EF4;
    font-weight: 700;
    margin-right: 5px;

}

.modify-btn {
    background-color: var(--main-color);
    color: white;
    border-radius: 20px;
    padding: 0 8px;
    margin-top: 10px;
    margin-bottom: 30px;
    cursor: pointer;
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
    /* margin-right: 250px ; */
    background-color: var(--main-color);
    color: white;
    padding: 0 8px;
    border-radius: 20px;
    cursor: pointer;
}

.product-content {
    display: flex;
}

.product-content > p {
    color: #FFA46B;
    font-size: 19px;
}

.product-content > span {
    margin-left: 37px;
    padding-top: 5px;
}

.product-duration {
    margin-left: 60px;
    font-size: 13px;
    color: #BCBCBC;
}

.duration-section {
    display: flex;
    justify-content: space-between;
}


.duration-section > span {
    margin-right: 253px;
}

.monthly-amount {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
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