<template>
  <div class="container">
    <div class="search-product">
      <p>예적금 상품 둘러보기</p>
    </div>

    <div class="recommend-nav">
      <div class="select-container">
        <!-- 상품 옵션 선택 -->
        <select v-model="selectedProduct" @change="filterProducts" class="select-box">
          <option value="none" disabled>상품옵션</option>
          <option v-for="prdtoption in prdtoptions" :key="prdtoption" :value="prdtoption">
            {{ prdtoption }}
          </option>
        </select>

        <!-- 금융사 선택 -->
        <select v-model="selectedBank" @change="filterProducts" class="select-box">
          <option value="all">금융사</option>
          <option v-for="bank in banks" :key="bank" :value="bank">
            {{ bank }}
          </option>
        </select>

        <!-- 기간 선택 -->
        <select v-model="selectedCity" @change="filterProducts" class="select-box">
          <option value="all">저축기간(개월)</option>
          <option v-for="saving_period in saving_periods" :key="saving_period" :value="saving_period">
            {{ saving_period }}
          </option>
        </select>
      </div>

        <!-- 금리 정렬 버튼 -->
        <div class="filter-button">
          <button @click="setInterest(false)" :class="{ active: !interestRateType }" class="toggle-button">최고금리순</button>
          <button @click="setInterest(true)" :class="{ active: interestRateType }" class="toggle-button">기본금리순</button>
        </div>
      </div>


    <!-- 상품 리스트 -->
    <ProductListItem 
      v-for="(product, index) in paginatedProducts" 
      :key="product.pk" 
      :product="product" 
      :index="index"
      :pagenum="currentPage"
    />


  <!-- 페이지네이션 -->
  <div class="pagination">
  <button @click="goToPage(currentPage - 1)" :disabled="currentPage === 1">이전</button>
  
  <button 
    v-for="pageNumber in displayedPageNumbers" 
    :key="pageNumber" 
    @click="goToPage(pageNumber)"
    :class="{ active: currentPage === pageNumber }"
  >
    {{ pageNumber }}
  </button>
  
  <button @click="goToPage(currentPage + 1)" :disabled="currentPage === totalPages">다음</button>
  </div>

  </div>


</template>

<script setup>
import ProductListItem from './ProductListItem.vue';

import { onMounted, ref, watch, computed } from 'vue';
import { useRecommendStore } from '@/stores/recommend';

const recommendStore = useRecommendStore()

// 1. recommend-nav 변수
const selectedProduct = ref("예금")
const selectedBank = ref("all")
const selectedCity = ref("all")
const filteredProducts = ref([])

// 금리 정렬 변수
const interestRateType = ref(false) // false: 최고 금리, true: 기본 금리


// 데이터 옵션
const prdtoptions = ["예금", "적금"]
const banks = ['KB국민은행', '신한은행', '하나은행', '우리은행', 'NH농협은행', 'IBK기업은행', 'KDB산업은행', 'SC제일은행', '부산은행', 'iM뱅크', 'SH수협은행', '경남은행', '카카오뱅크', '광주은행', '토스뱅크', '전북은행', '케이뱅크', '제주은행']
const saving_periods = ["1", "3", "6", "12", "24", "36"]

// 금리 정렬 설정 함수
const setInterest = (value) => {
  interestRateType.value = value;
  filterProducts(); // 정렬 기준 변경 시 데이터 필터링
};

// 데이터 가져오기 함수 (초기 로딩)
onMounted(async () => {
  try {
    selectedBank.value = "all";
    selectedCity.value = "all";
    await recommendStore.getDeposits("prime_interest_rate");
    await recommendStore.getSavings("prime_interest_rate");
    filterProducts();
  } catch (error) {
    console.error("데이터 로딩 중 오류 발생:", error);
  }
});

// 필터링 함수
const filterProducts = () => {
  const allProducts =
    selectedProduct.value === "예금"
      ? recommendStore.depositLists
      : recommendStore.savingLists;

  filteredProducts.value = allProducts.filter((product) => {
    const matchesBank =
      selectedBank.value === "all" || product.company_name === selectedBank.value;

    const matchesPeriod =
      selectedCity.value === "all" ||
      product.join_period.split(",").map((p) => p.trim()).includes(selectedCity.value);

    return matchesBank && matchesPeriod;
  });

  sortProducts(); // 필터링 후 정렬 적용
};

// 정렬 함수
const sortProducts = () => {
  filteredProducts.value.sort((a, b) =>
    interestRateType.value
      ? b.interest_rate - a.interest_rate // 기본 금리순
      : b.prime_interest_rate - a.prime_interest_rate // 최고 금리순
  );
};

// 선택 값 변경 시 필터링 실행
watch([selectedProduct, selectedBank, selectedCity], filterProducts);


// 페이지네이션
// 페이지네이션 상태
const currentPage = ref(1); // 현재 페이지
const postsPerPage = 10; // 한 페이지에 보여줄 상품 개수

// 총 페이지 계산
const totalPages = computed(() => Math.ceil(filteredProducts.value.length / postsPerPage));

// 현재 페이지의 상품 리스트 계산
const paginatedProducts = computed(() => {
  const start = (currentPage.value - 1) * postsPerPage;
  return filteredProducts.value.slice(start, start + postsPerPage);
});

// 표시할 페이지 번호 계산
const displayedPageNumbers = computed(() => {
  const pageNumbers = [];
  let startPage = Math.max(1, currentPage.value - 2);
  let endPage = Math.min(totalPages.value, startPage + 4);

  if (endPage - startPage < 4) {
    startPage = Math.max(1, endPage - 4);
  }

  for (let i = startPage; i <= endPage; i++) {
    pageNumbers.push(i);
  }

  return pageNumbers;
});

// 페이지 이동 함수
const goToPage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
  }
};

</script>


<style scoped>

.container {
  margin: 100px auto;
  display: flex;
  flex-direction: column;
  /* justify-content: space-between; */
}

.search-product {
  margin-bottom: 50px;
}

.search-product > p {  
  text-align: center;
  font-size: 30px;
  font-weight: 700;
  color: rgb(92, 92, 92);
}

.recommend-nav {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
  border-bottom: #808080 1px solid;
}

.filter-button > button {
  padding: 10px;
  font-size: 15px;
  font-weight: bold;
  border: none;
  color: #808080;
  cursor: pointer;
}

.filter-button > button.active {
  color: var(--main-text-color); /* 활성화된 버튼 텍스트 색상 */
}

.filter-button > button:hover {
  color: var(--point-color); /* 호버 시 색상 */
}

.select-container > select {
  margin: 0 0 0 10px;
}

.select-box {
  padding: 8px 0px;
  cursor: pointer;
  border: none;
  outline: none;
  color: #808080;
  font-size: 15px;
  font-weight: 700;
  text-align: center;
}

.pagination {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
}

.pagination button {
    padding: 5px 10px;
    margin: 0 5px;
    background-color: #fff;
    color: #333;
    border: 1px solid #ddd;
    border-radius: 5px;
    cursor: pointer;
}

.pagination button:disabled {
    color: #ccc;
    cursor: not-allowed;
}

.pagination button.active {
    background-color: var(--main-text-color);
    color: white;
    border-color: var(--main-color);
}

.pagination button:hover:not(:disabled) {
    background-color: var(--main-color);
}
</style>