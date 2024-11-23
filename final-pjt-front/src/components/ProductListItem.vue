<template>
  <RouterLink
        :to="{ name: 'recommendDetail', params: { category: product.category ? 'savings' : 'deposit', productId: product.pk } }">
      <div class="productlist-item-container">
          <div class="product-content">
            <div class="product-index">
              <p class="indexnum">{{ index+1+(pagenum-1)*10 }} /</p>
              <img :src="getBankLogo(product.company_name)" :alt="product.company_name" class="bank-logo">
            </div>
            <div class="product-detail">
              <p class="bankname">{{ product.company_name }}</p>
              <p class="product-name">{{ product.product_name }}</p>
              <p class="join-way" v-for="join in (product.join_way || '').split(',')" :key="join">
                {{ join }}
              </p>
            </div>
          </div>

          <div class="product-interest-rate">
            <p class="prime_interest_rate">최고 {{ product.prime_interest_rate }}%</p>
            <p class="interest_rate">기본 {{ product.interest_rate }}%</p>
          </div>
        </div>
  </RouterLink>

</template>

<script setup>
import { ref } from 'vue';
import { RouterLink } from 'vue-router';

defineProps({
  product:Object,
  index:Number,
  pagenum:Number,
})



// 은행 로고 찾기
import kbLogo from '@/assets/images/bank_logo/kb.png';
import shinhanLogo from '@/assets/images/bank_logo/shinhan.png';
import hanaLogo from '@/assets/images/bank_logo/hana.png';
import wooriLogo from '@/assets/images/bank_logo/woori.png';
import nhLogo from '@/assets/images/bank_logo/nh.png';
import ibkLogo from '@/assets/images/bank_logo/IBK.png';
import kdbLogo from '@/assets/images/bank_logo/KDB.png';
import scLogo from '@/assets/images/bank_logo/sc.png';
import busanLogo from '@/assets/images/bank_logo/BUSAN.png';
import imBankLogo from '@/assets/images/bank_logo/IM.png';
import shLogo from '@/assets/images/bank_logo/SH.png';
import kakaoLogo from '@/assets/images/bank_logo/kakao.png';
import kwangjuLogo from '@/assets/images/bank_logo/KWANGJU.png';
import tossLogo from '@/assets/images/bank_logo/toss.png';
import jeonbukLogo from '@/assets/images/bank_logo/JEONBUK.png';
import kbankLogo from '@/assets/images/bank_logo/kbank.png';

// 기본 로고 (없을 경우 표시)
const defaultLogo = '@/assets/images/default.png'

// 은행 로고 매핑
const bankLogos = {
  'KB국민은행': kbLogo,
  '신한은행': shinhanLogo,
  '제주은행': shinhanLogo,
  '하나은행': hanaLogo,
  '우리은행': wooriLogo,
  'NH농협은행': nhLogo,
  'IBK기업은행': ibkLogo,
  'KDB산업은행': kdbLogo,
  'SC제일은행': scLogo,
  '부산은행': busanLogo,
  '경남은행': busanLogo,
  'iM뱅크': imBankLogo,
  'SH수협은행': shLogo,
  '카카오뱅크': kakaoLogo,
  '광주은행': kwangjuLogo,
  '토스뱅크': tossLogo,
  '전북은행': jeonbukLogo,
  '케이뱅크': kbankLogo,
};

// 로고 반환 함수
const getBankLogo = (categoryName) => {
  const bankName = categoryName.split(' > ').pop(); // 이름에서 마지막 값 추출
  return bankLogos[bankName] || defaultLogo; // 해당 로고가 없으면 기본 로고 반환
}

</script>

<style scoped>
.productlist-item-container {
    display: flex;
    justify-content: space-between;
    margin: 10px 0;
    border-bottom: 1px solid #BCBCBC;
    padding-bottom: 25px;
    width: 650px;
}

.product-content {
    display: flex;
    flex-grow: 1;
  }

.product-index {
  display: flex;
}

.indexnum {
    font-size: larger;
    color: var(--main-text-color);
    font-size: 25px;
}

.bank-logo {
    width: 35px;
    height: 35px;
    object-fit: contain;
    margin-left: 15px;
    margin-top: 5px;
}

.product-detail {
  margin-left: 30px;
  flex-grow: 1;
}

.product-detail > .bankname {
    font-size: 18px;
    color: #808080;
}

.product-detail > .product-name {
    font-weight: 700;
    font-size: 20px;
}

.product-detail > .join-way {
  display: inline-block;
  margin: 5px 4px 0 0px; 
  padding: 2px 8px;
  background-color: var(--box-bg-color);
  background-color: var(--stroke-color);
  border-radius: 25px;
  font-size: 12px;
  /* color: var(--sub-text-bold-color); */
  color: white;
}

.duration-section > p {
    color: #BCBCBC;
    font-weight: 300;
}

.duration-section > p > span {
    color: var(--main-color);
}

.product-interest-rate {
    text-align: end;
    margin-top: 30px;
}

.product-interest-rate .prime_interest_rate {
  font-size: 18px;
  font-weight: bold;
  color: var(--point-color);
}

.product-interest-rate .interest_rate {
  font-size: 12px;
  color: #999;
}

.product-interest-rate > span {
    color: #BCBCBC;
    font-weight: 300;
}

.product-interest-rate > .monthly {
    color: #808080;
    font-weight: 700;
}

.product-interest-rate > .amount {
    font-size: 20px;
    color: var(--main-text-color);
    font-weight: 700;

}
</style>