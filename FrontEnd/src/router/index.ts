import { createRouter, createWebHistory } from 'vue-router';
// import Home from '../views/Home.vue';
// import Login from '../views/Login.vue';
// import Profile from '../views/Profile.vue';
// import ProfileEditing from '../views/ProfileEditing.vue';
// import ViewArticle from '../views/ViewArticle.vue';
// import PostArticle from '@/views/PostArticle.vue';

const Home = () => import('../views/Home.vue');
const Login = () => import('../views/Login.vue');
const Profile = () => import('../views/Profile.vue');
const ProfileEditing = () => import('../views/ProfileEditing.vue');
const ViewArticle = () => import('../views/ViewArticle.vue');
const EditArticle = () => import('../views/EditArticle.vue');
const PostArticle = () => import('../views/PostArticle.vue');
// const Home = ()=> import('../views/Home.vue')
// const Home = ()=> import('../views/Home.vue')

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile,
    },
    {
      path: '/profileEditing',
      name: 'ProfileEditing',
      component: ProfileEditing,
    },
    {
      path: '/viewArticle/:id',
      name: 'ViewArticle',
      component: ViewArticle,
    },
    {
      path: '/editArticle/:id',
      name: 'EditArticle',
      component: EditArticle,
    },
    {
      path: '/postArticle',
      name: 'PostArticle',
      component: PostArticle,
    },
  ],
  // scrollBehavior(to, from, savedPosition) {
  //   // 始终滚动到顶部
  //   return { top: 0, behavior: 'smooth' };
  // },
});

export default router;
