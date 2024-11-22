<template>
  <div class="container">
    <div class="search-product">
      <span>예적금 상품 둘러보기</span>
    </div>

    <div class="filter-container">
      <div class="select-container">
        <select v-model="selectedBank" @change="" class="select-box">
          <option value="">금융사</option>
          <option v-for="bank in banks" :key="bank" :value="bank">
            {{ bank }}
          </option>
        </select>
          <select v-model="selectedCity" @change="" class="select-box">
            <option value="">기간</option>
            <option v-for="saving_period in saving_periods" :key="saving_period" :value="saving_period">
              {{ saving_period }}
            </option>
          </select>
        </div>


      <div class="filter-button">
        <button>최고금리순</button> 
        <button>기본금리순</button>
      </div>
    </div>

    
    <div class="main-content">
        <div class="product-content">
            <p class = indexnum>1 /</p>
            <img src="#" alt="myProduct.product.company_name" class="bank-logo">
            <!-- <p class = indexnum>{{ index+1 }} /</p>
            <img :src="getBankLogo(myProduct.product.company_name)" :alt="myProduct.product.company_name" class="bank-logo"> -->
        </div>
        <div class="product">
            <div class="product-duration">
                <p class="bankname">국민은행</p>
                <span>KB국민튼튼적금</span>
                <!-- <p class="bankname">{{ myProduct.product.company_name}}</p>
                <span>{{ myProduct.product.product_name}}</span> -->
                <div class="duration-section">
                    <!-- <p>가입일: {{ myProduct.join_date.slice(0,10) }}</p>
                    <p>만기일: {{ myProduct.expiration_date.slice(0,10) }} <span>(D-{{myProduct.d_day}})</span></p>  -->
                    <p>가입일: 2024-11-01</p>
                    <p>만기일: 2025-10-31 <span>(D-365)</span></p> 
                </div>
            </div>
            <div class="monthly-amount">
                <!-- <span>적용 금리: {{ myProduct.interest_rate }}%</span>
                <p class="monthly">월 납입액: {{ (myProduct.monthly_amount*10000).toLocaleString(en-US)}}원</p>
                <p class="amount">{{ (myProduct.remain_month*myProduct.monthly_amount*10000).toLocaleString(en-US) }}원</p> -->
                <p>기준 금리: 5%</p>
                <p>우대 금리: 5%</p>
                <p class="amount">500,000원</p>
            </div>
        </div>
    </div>
    <div class="main-content">
        <div class="product-content">
            <p class = indexnum>1 /</p>
            <img src="#" alt="myProduct.product.company_name" class="bank-logo">
            <!-- <p class = indexnum>{{ index+1 }} /</p>
            <img :src="getBankLogo(myProduct.product.company_name)" :alt="myProduct.product.company_name" class="bank-logo"> -->
        </div>
        <div class="product">
            <div class="product-duration">
                <p class="bankname">국민은행</p>
                <span>KB국민튼튼적금</span>
                <!-- <p class="bankname">{{ myProduct.product.company_name}}</p>
                <span>{{ myProduct.product.product_name}}</span> -->
                <div class="duration-section">
                    <!-- <p>가입일: {{ myProduct.join_date.slice(0,10) }}</p>
                    <p>만기일: {{ myProduct.expiration_date.slice(0,10) }} <span>(D-{{myProduct.d_day}})</span></p>  -->
                    <p>가입일: 2024-11-01</p>
                    <p>만기일: 2025-10-31 <span>(D-365)</span></p> 
                </div>
            </div>
            <div class="monthly-amount">
                <!-- <span>적용 금리: {{ myProduct.interest_rate }}%</span>
                <p class="monthly">월 납입액: {{ (myProduct.monthly_amount*10000).toLocaleString(en-US)}}원</p>
                <p class="amount">{{ (myProduct.remain_month*myProduct.monthly_amount*10000).toLocaleString(en-US) }}원</p> -->
                <p>기준 금리: 5%</p>
                <p>우대 금리: 5%</p>
                <p class="amount">500,000원</p>
            </div>
        </div>
    </div>
    <div class="main-content">
        <div class="product-content">
            <p class = indexnum>1 /</p>
            <img src="#" alt="myProduct.product.company_name" class="bank-logo">
            <!-- <p class = indexnum>{{ index+1 }} /</p>
            <img :src="getBankLogo(myProduct.product.company_name)" :alt="myProduct.product.company_name" class="bank-logo"> -->
        </div>
        <div class="product">
            <div class="product-duration">
                <p class="bankname">국민은행</p>
                <span>KB국민튼튼적금</span>
                <!-- <p class="bankname">{{ myProduct.product.company_name}}</p>
                <span>{{ myProduct.product.product_name}}</span> -->
                <div class="duration-section">
                    <!-- <p>가입일: {{ myProduct.join_date.slice(0,10) }}</p>
                    <p>만기일: {{ myProduct.expiration_date.slice(0,10) }} <span>(D-{{myProduct.d_day}})</span></p>  -->
                    <p>가입일: 2024-11-01</p>
                    <p>만기일: 2025-10-31 <span>(D-365)</span></p> 
                </div>
            </div>
            <div class="monthly-amount">
                <!-- <span>적용 금리: {{ myProduct.interest_rate }}%</span>
                <p class="monthly">월 납입액: {{ (myProduct.monthly_amount*10000).toLocaleString(en-US)}}원</p>
                <p class="amount">{{ (myProduct.remain_month*myProduct.monthly_amount*10000).toLocaleString(en-US) }}원</p> -->
                <p>기준 금리: 5%</p>
                <p>우대 금리: 5%</p>
                <p class="amount">500,000원</p>
            </div>
        </div>
    </div>
    <div class="main-content">
        <div class="product-content">
            <p class = indexnum>1 /</p>
            <img src="#" alt="myProduct.product.company_name" class="bank-logo">
            <!-- <p class = indexnum>{{ index+1 }} /</p>
            <img :src="getBankLogo(myProduct.product.company_name)" :alt="myProduct.product.company_name" class="bank-logo"> -->
        </div>
        <div class="product">
            <div class="product-duration">
                <p class="bankname">국민은행</p>
                <span>KB국민튼튼적금</span>
                <!-- <p class="bankname">{{ myProduct.product.company_name}}</p>
                <span>{{ myProduct.product.product_name}}</span> -->
                <div class="duration-section">
                    <!-- <p>가입일: {{ myProduct.join_date.slice(0,10) }}</p>
                    <p>만기일: {{ myProduct.expiration_date.slice(0,10) }} <span>(D-{{myProduct.d_day}})</span></p>  -->
                    <p>가입일: 2024-11-01</p>
                    <p>만기일: 2025-10-31 <span>(D-365)</span></p> 
                </div>
            </div>
            <div class="monthly-amount">
                <!-- <span>적용 금리: {{ myProduct.interest_rate }}%</span>
                <p class="monthly">월 납입액: {{ (myProduct.monthly_amount*10000).toLocaleString(en-US)}}원</p>
                <p class="amount">{{ (myProduct.remain_month*myProduct.monthly_amount*10000).toLocaleString(en-US) }}원</p> -->
                <p>기준 금리: 5%</p>
                <p>우대 금리: 5%</p>
                <p class="amount">500,000원</p>
            </div>
        </div>
    </div>


  </div>
</template>

<script setup>

const banks = [
    'KB국민은행', '신한은행', '우리은행', 'NH농협은행', '하나은행', 'SC제일은행'
  ];

const saving_periods = [
  '1', '3', '6', '12', '24', '36'
];


</script>

<style scoped>

.container {
  margin: 100px auto;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.filter-container {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
  border-bottom: #808080 1px solid;
}

.filter-button > button {
  padding: 10px 5px 0;
  font-size: 15px;
  font-weight: 700;
  color: #808080;
}

.select-container > select {
  margin: 0 0 0 10px;
}

.select-box {
  padding: 8px 0px;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  min-width: 10px;
  background-color: white;
  cursor: pointer;
  font-size: 15px;
  font-weight: 700;
  color: #808080;
  outline: none;
}

.search-product {
  margin-bottom: 20px;
}

.search-product > span { 
  font-size: 18px;
  font-weight: 700;
  color: #808080;
}


.main-content {
    display: flex;
    margin: 10px 0;
    border-bottom: 1px solid #BCBCBC;
    padding-bottom: 25px;
    width: 650px;
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
    color: var(--main-color);
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
    color: var(--main-text-color);
    font-weight: 700;

}

</style>