<template>
  <div class="recommendation-container">
    <div class="recommend">
      <h2 class="recommendation-badge">돼지 저금통을 불릴 수 있는</h2>
      <h2 class="recommendation-badge">예적금 상품을 추천해드려요.</h2>
    </div>

    <ProductRcommend/>
  </div>
</template>

<script setup>
import ProductRcommend from '@/components/ProductRecommend.vue'
</script>

<style scoped>
.recommendation-container {
  padding: 180px 0;
  margin: 100px auto;
  text-align: center;
  background-color: rgb(248, 248, 248);
}

.recommend {
  margin-bottom: 60px;
}

.recommendation-badge {
  margin-bottom: 5px;
  font-size: 30px;
  font-weight: 700;
  color: #020202;
}
</style>