import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import RecommendView from '@/views/RecommendView.vue'
import RecommendDetail from '@/views/RecommendDetailView.vue'
import MapView from '@/views/MapView.vue'
import CommunityView from '@/views/CommunityView.vue'
import CreatePostView from '@/views/CreatePostView.vue'
import UpdatePostView from '@/views/UpdatePostView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ProfileView from '@/views/ProfileView.vue'
import UpdateUserView from '@/views/UpdateUserView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/recommend',
      name: 'recommend',
      component: RecommendView
    },
    {
      path: '/recommend/:category/:productId',
      name: 'recommendDetail',
      component: RecommendDetail
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
    {
      path: '/community',
      name: 'community',
      component: CommunityView,
    },
    {
      path: '/community/:postId',
      name: 'postdetail',
      component: CommunityView,
    },
    {
      path: '/createPost',
      name: 'createPost',
      component: CreatePostView
    },
    {
      path: '/updatePost/:postId',
      name: 'updatePost',
      component: UpdatePostView
    },
    {
      path:'/exchange',
      name:'exchange',
      component: ExchangeView,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path:'/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path:'/profile',
      name:'profile',
      component:ProfileView,
    },
    {
      path:'/updateUser',
      name:'updateUser',
      component:UpdateUserView
    }
  ],
})

export default router
