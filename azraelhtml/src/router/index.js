import Vue from 'vue';
import VueRouter from 'vue-router';
import store from '../store';
Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home'),
    beforeEnter(to, from, next) {
      if (store.state.userinfo.token) {
        next();
      } else {
        next('/login');
      }
    },
  },
  // 登录
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login'),
  },
  // 注册
  {
    path: '/register',
    name: 'Register',
    component: () => import('../views/Register'),
  },

  // 添加文章
  {
    path: '/add-article',
    name: 'AddAtricle',
    component: () => import('../views/AddArticle'),
    beforeEnter(to, from, next) {
      // 判断用户是否登录
      if (store.state.userinfo.token) {
        next();
      } else {
        next('/login');
      }
    },
  },
  //文章列表
  {
    path: '/article-list',
    name: 'Atricle-List',
    component: () => import('../views/ArticleList'),
    beforeEnter(to, from, next) {
      if (store.state.userinfo.token) {
        next();
      } else {
        next('/login');
      }
    },
  },
  // 用户管理
  {
    path: '/user-permission',
    name: 'UserPerm',
    component: () => import('../views/UserPerm'),
    beforeEnter(to, from, next) {
      if (store.state.userinfo.token) {
        // 判断用户权限
        let checkInfo = {
          contentType: 'auth_user',
          permissions: ['add', 'change', 'delete', 'view'],
        };
        store.dispatch('checkUserPerm', checkInfo).then(res => {
          console.log(res);
          // 当有权限是才会跳转到用户管理页面  否则不会跳转(看不见用户管理界面)
          if (res) {
            next();
          }
        });
      } else {
        next('/login');
      }
    },
  },
  // 栏目管理
  {
    path: '/lanmu-admin',
    name: 'LanmuAdmin',
    component: () => import('../views/LanmuAdmin'),
    beforeEnter(to, from, next) {
      if (store.state.userinfo.token) {
        // 判断用户权限
        let checkInfo = {
          contentType: 'Blog_lanmu',
          permissions: ['add', 'change', 'delete', 'view'],
        };
        store.dispatch('checkUserPerm', checkInfo).then(res => {
          // console.log(res);
          // 当有权限是才会跳转到用户管理页面  否则不会跳转(看不见用户管理界面)
          if (res) {
            next();
          }
        });
      } else {
        next('/login');
      }
    },
  },
  // 文章内容
  {
    path: '/article',
    name: 'Article',
    component: () => import('../views/Article'),
    beforeEnter(to, from, next) {
      if (store.state.userinfo.token) {
        // 判断用户权限
        let checkInfo = {
          contentType: 'Blog_article',
          permissions: ['view'],
        };
        store.dispatch('checkUserPerm', checkInfo).then(res => {
          // console.log(res);
          // 当有权限是才会跳转到用户管理页面  否则不会跳转(看不见用户管理界面)
          if (res) {
            next();
          }
        });
      } else {
        next('/login');
      }
    },
  },
];

const routerPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
  return routerPush.call(this, location).catch(err => err);
};

const router = new VueRouter({
  routes,
});

// // 全局路由守卫
// router.beforeEach((to, from, next) => {
//   console.log(from.path);
//   console.log(to.path);
//   next();
// });
export default router;
