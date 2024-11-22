<template>
    <div class="container">
        <h2 class="title">게시글 수정하기</h2>

        <form class="post" @submit.prevent="store.createPost(title, content, selectedTag)">
            <div class="input-group">
                <input type="text" id="post-title" v-model.trim="title" placeholder="제목을 입력하세요">
            </div>
            <div class="input-group">
                <textarea name="post-content" id="post-content" class="post-textarea" v-model.trim="content" placeholder="내용을 입력하세요"></textarea>
            </div>

			<div class="main">
				<span class="category">카테고리</span>
				
				<span class="tag"
					:class="['account', { active: selectedTag === 'account' }]"
					@click="selectTag('account')"
				>예적금</span>
				<span class="tag"
					:class="['asset', { active: selectedTag === 'asset' }]"
					@click="selectTag('asset')"
				>부동산</span>
				<span class="tag"
					:class="['stock', { active: selectedTag === 'stock' }]"
					@click="selectTag('stock')"
				>주식</span>
				<span class="tag"
					:class="['etc', { active: selectedTag === 'etc' }]"
					@click="selectTag('etc')"
				>기타</span>
			</div>

            <button class="post-btn">수정하기</button>
        </form>
    </div>
</template>

<script setup>
import { useCommunityStore } from '@/stores/community';
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';

const router = useRouter()
const route = useRoute()
const store = useCommunityStore()

const selectedTag = ref('');
const title = ref('')
const content = ref('')

const selectTag = (tag) => {
    selectedTag.value = tag;
};


// 기존 게시글 데이터 불러오기
onMounted(async () => {
  try {
    const postData = await store.getPostDetail(route.params.postId);
    title.value = postData.title;
    content.value = postData.content;
    selectedTag.value = postData.category;
  } catch (err) {
    console.error('게시글 불러오기 오류', err);
  }
});
</script>

<style scoped>
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
}

.title {
    margin: 100px auto 30px;
    color: var(--main-color);
    text-align: center;
    font-weight: 600;
}

.main {
    width: 100%;
    margin-bottom: 10px;
    display: flex;
    /* flex-direction: column; */
	justify-items: center;
    align-items: center;
	justify-content: space-between;
	width: 400px;
}

.category {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 30px;
	color: var(--sub-text-color);
	font-weight: 600;
}

.tag {
    padding: 5px 15px;
    border: 1px solid var(--stroke-color);
    color: #888;
    border-radius: 20px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-size: 12px;
}

.tag.active {
    background-color: var(--main-color);
    color: white;
}

.post {
    display: flex;
    flex-direction: column;
    width: 100%;
}

.input-group {
    margin-bottom: 20px;
    width: 100%;
    
}

.input-group label {
    position: relative;
    display: block;
    margin-bottom: -11px;
    font-size: 16px;
    z-index: 1px;
    background-color: white;
    width: 40px;
    text-align: center;
    left: 15px;
}

.input-group input,
.input-group textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    outline: none;
}

.input-group input {
    height: 40px;
}

.input-group textarea {
    height: 400px;
    resize: none;
}

.post-btn {
    background-color: var(--point-color);
    color: white;
    padding: 8px;
    border-radius: 20px;
    font-size: 14px;
    cursor: pointer;
    width: 100px;
	margin-left: auto;
	display: block;
	margin-bottom: 50px;
}

.post-btn:hover {
    background-color: var(--main-color);
}

</style>

