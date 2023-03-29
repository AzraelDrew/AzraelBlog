import { createRouter, createWebHistory } from 'vue-router';
const Home = () => import('../views/Home.vue');
const Login = () => import('../views/Login.vue');
const Profile = () => import('../views/Profile.vue');
const ProfileEditing = () => import('../views/ProfileEditing.vue');
const ViewArticle = () => import('../views/ViewArticle.vue');
const EditArticle = () => import('../views/EditArticle.vue');
const PostArticle = () => import('../views/PostArticle.vue');

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
});

export default router;
