<template>
    <div class="main-content">
        <div class="product-content">
            <p class = indexnum>{{ index+1 }} /</p>
            <img :src="getBankLogo(myProduct.product.company_name)" :alt="myProduct.product.company_name" class="bank-logo">
        </div>
        <div class="product">
            <div class="product-duration">
                <p class="bankname">{{ myProduct.product.company_name}}</p>
                <span>{{ myProduct.product.product_name}}</span>
                <div class="duration-section">
                    <p>가입일: {{ myProduct.join_date.slice(0,10) }}</p>
                    <p>만기일: {{ myProduct.expiration_date.slice(0,10) }} <span>(D-{{myProduct.d_day}})</span></p> 
                </div>
            </div>
            <div class="monthly-amount">
				<template  v-if="myProduct.product.category">
					<span>적용 금리: {{ myProduct.interest_rate }}%</span>
                	<p class="monthly">월 납입액: {{ (myProduct.monthly_amount*10000).toLocaleString(en-US)}}원</p>
                	<p class="amount">{{ (myProduct.remain_month*myProduct.monthly_amount*10000).toLocaleString(en-US) }}원</p>
				</template>
				<template v-else>
					<span>적용 금리: {{ myProduct.interest_rate }}%</span>
                	<p class="amount">{{ (myProduct.monthly_amount*10000).toLocaleString(en-US) }}원</p>
				</template>
            </div>
        </div>
    </div>
</template>

<script setup>
const props = defineProps({
    myProduct:Object,
    index:Number,
})

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
const defaultLogo = '/images/default.png';

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
};

</script>

<style scoped>

.main-content {
    display: flex;
    margin: 10px 0;
    border-bottom: 1px solid #BCBCBC;
    padding-bottom: 25px;
}

.product-content {
    display: flex;
}

.indexnum {
    font-size: larger;
}

.bank-logo {
    width: 35px;
    height: 35px;
    margin-left: 15px;
    margin-top: 5px;
}

.product {
    display: flex;
    justify-content: space-between;
    flex-grow: 2;
    
}

.product-duration {
    margin-left: 30px;
}

.product-duration > .bankname {
    color: #808080;
}

.product-duration > span {
    font-size: 18px;
    font-weight: 700;
}

.product-content {
    color: var(--main-color);
    font-size: 22px;
}

.duration-section > p {
    color: #BCBCBC;
    font-weight: 300;
}

.duration-section > p > span {
    color: var(--point-text-color);
}

.monthly-amount {
    align-self: end;
    text-align: end;
    margin-top: 73px;
}

.monthly-amount > span {
    color: #BCBCBC;
    font-weight: 300;
}

.monthly-amount > .monthly {
    color: #808080;
    font-weight: 700;
}

.monthly-amount > .amount {
    font-size: 20px;
    color: var(--main-color);
    font-weight: 700;

}

</style>