import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useUserStore } from "./user";

export const useRecommendStore = defineStore("recommend", () => {
  const API_URL = 'http://127.0.0.1:8000';
  const userStore = useUserStore()
  const depositProducts = ref([])
  const savingsProducts = ref([])

  // 1. 저금 목표에 가장 잘 맞는 상품 가져오기
  const getProduct = function () {
    const params = userStore.isLoggedIn ? userStore.user.saving_purpose : []
    axios({
      method: 'get',
      url: `${API_URL}/bank_products/products_recommend/`,
      params: {
        saving_purpose: JSON.stringify(params)
      }
    })
      .then(res => {
        depositProducts.value = res.data.deposit_products
        savingsProducts.value = res.data.savings_products
      })
      .catch(err => console.log('예적금 상품 목록 조회 실패', err))
  }


  // 2. 상품 상세 정보 가져오기
  const product = ref({})
  const getProductDetail = async (category, productId) => {
    axios({
      method: 'get',
      url: `${API_URL}/bank_products/${category}_detail/${productId}/`
    })
    .then(res => {
      product.value = res.data
    })
    .catch(err => console.error(`상품 ID ${productId}를 찾을 수 없습니다.`, err))
  };


  const depositLists = ref([])
  const savingLists = ref([])

  // 3. 모든 예금 상품 가져오기
  const getDeposits = async (value) => {
    try {
      const response = await axios.get(`${API_URL}/bank_products/deposits/`, {
        params: { order_by: value },
      });
      depositLists.value = response.data;
    } catch (error) {
      console.error("예금 상품 목록 조회 실패:", error);
    }
  }
  
  // 4. 모든 적금 상품 가져오기
  const getSavings = async (value) => {
    try {
      const response = await axios.get(`${API_URL}/bank_products/savings/`, {
        params: { order_by: value },
      });
      savingLists.value = response.data;
    } catch (error) {
      console.error("적금 상품 목록 조회 실패:", error);
    }
  };


  return { getProduct, depositProducts, savingsProducts, getProductDetail, product, 
    getDeposits, getSavings, depositLists, savingLists };
}, { persist: true });