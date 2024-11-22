<template>
    <div class="post-body" v-if="post">
        <div class="post-info">
            <p>{{ communityStore.formatDate(post.created_at) }}  |  조회수 {{ post.num_seen }}</p>
            <div>
                <button @click="router.push({ name: 'updatePost', params: { postId: post.id } })"
                v-if="userStore.isLoggedIn && userStore.user.pk === post.user">수정</button>
                <button @click="deletePost" class="delete-btn"
                v-if="userStore.isLoggedIn && userStore.user.pk === post.user">삭제</button>
            </div>
		</div>
        <div class="content">{{ post.content }}</div>

        <div class="like_save_btn">
            <div class="like">
                <div :class="['like-btn', { 'liked': isLiked }]"
                    @click="toggleLike">
                    <i class="pi pi-heart-fill"></i>
                </div>
                    <p>{{ likeCount }}</p>
            </div>

            <div class="save">
                    <div :class="['save-btn', { 'saved': isSaved }]"
                    	@click="toggleSave">
                        <i class="pi pi-bookmark-fill"></i>
                </div>
                    <p>{{ saveCount }}</p>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useCommunityStore } from '@/stores/community';
import { useUserStore } from '@/stores/user';
import axios from 'axios';
import { onMounted, ref, watch, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const router = useRouter()
const route = useRoute()
const communityStore = useCommunityStore()
const userStore = useUserStore()

const props = defineProps({
    post: Object
})


const isLiked = ref(false);
const likeCount = ref(0);
const isSaved = ref(false);
const saveCount = ref(0);

const computedLikeCount = computed(() => {
    return props.post ? likeCount.value : 0;
});

// 좋아요 상태 가져오기
const getLikedStatus = async () => {
    if (!props.post) return;

    try {
        isLiked.value = props.post.like_users == userStore.user.pk;
        likeCount.value = props.post.like_count;
    } catch (err) {
        console.log('좋아요 상태 가져오기 오류', err);
    }
};

// 저장 상태 가져오기
const getSavedStatus = async () => {
    if (!props.post) return;

    try {
        isSaved.value = props.post.save_users == userStore.user.pk;
        saveCount.value = props.post.save_count;
    } catch (err) {
        console.log('저장 상태 가져오기 오류', err);
    }
};

// 좋아요 토글
const toggleLike = async () => {
    if (!userStore.isLoggedIn) {
        alert('로그인이 필요합니다.');
        return;
    }

    if (!props.post) return;

    isLiked.value = !isLiked.value;

    try {
        axios({
            method: 'post',
            url: `${communityStore.API_URL}/posts/like_post/${props.post.id}/`,
            headers: {
                Authorization: `Token ${userStore.token}`
            }
        })
        .then(res => {
            likeCount.value = res.data.like_count;
        })

    } catch (err) {
        console.log('좋아요 시 오류', err);
    }
};

// 저장 토글
const toggleSave = async () => {
    if (!userStore.isLoggedIn) {
        alert('로그인이 필요합니다.');
        return;
    }

    if (!props.post) return;

    isSaved.value = !isSaved.value;

    try {
        axios({
            method: 'post',
            url: `${communityStore.API_URL}/posts/save_post/${props.post.id}/`,
            headers: {
                Authorization: `Token ${userStore.token}`
            }
        })
        .then(res => {
            saveCount.value = res.data.save_count;
        })

    } catch (err) {
        console.log('좋아요 시 오류', err);
    }
};

// post 데이터 변화 감지
watch(() => props.post, (newPost) => {
    if (newPost) {
        likeCount.value = newPost.like_users?.length || 0;
        getLikedStatus();
		saveCount.value = newPost.save_users?.length || 0;
        getSavedStatus();
    }
}, { immediate: true });

onMounted(() => {
    if (props.post) {
        getLikedStatus();
		getSavedStatus();
    }
});

const deletePost = () => {
    axios({
      method: 'delete',
      url: `${communityStore.API_URL}/posts/detail/${props.post.id}/`,
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
    .then(res => {
          console.log(res)
          router.push({ name: 'community'})
          router.go(0)
      })
      .catch(err => console.log('게시글 삭제 오류', err))
}
</script>

<style scoped>

.post-body {
    margin: 10px 0;
}

.post-info {
    display: flex;
    justify-content: space-between;
    font-size: 12px;
}

.post-info button {
    text-decoration: underline;
    cursor: pointer;
}

.content {
    margin: 30px 0;
}

.like_save_btn {
    display: flex;
    justify-content: flex-end;
}

.like {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    margin: 10px;
}

.like-btn {
    margin-right: 5px;
    margin-bottom: 5px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-size: 24px;
}

.like-btn i {
    font-size: 16px;
    color: #bcbcbc;
}

.like-btn.liked i {
    color: crimson;
    animation: pulse 500ms ease;
}

.save {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    margin: 10px;
}

.save-btn {
    margin-right: 5px;
    margin-bottom: 5px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-size: 24px;
}

.save-btn i {
    font-size: 16px;
    color: #bcbcbc;
}

.save-btn.saved i {
    color: crimson;
    animation: pulse 500ms ease;
}

.delete-btn {
    margin-left: 10px;
}


/* 좋아요 버튼 눌렀을 때 크기 변하는 애니메이션 */
@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.2);
  }
  100% {
    transform: scale(1);
  }
}
</style>