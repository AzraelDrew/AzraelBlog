import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import Qs from 'qs';
import router from '../router';
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    currentname: '',
    userinfo: {},
  },
  getters: {
    // 查询登录状态
    loginState(state) {
      return state.userinfo.token;
    },
  },
  // mutations用于更改state 且只能在mutations中更改
  mutations: {
    svaeUserInfo(state, userinfo) {
      state.userinfo = userinfo;
    },
    // 清楚用户登录状态
    clearUserInfo(state) {
      state.userinfo = {};
    },
  },
  actions: {
    // 登录
    // 第一个参数为调用mutations中的方法的函数  第二个参数为 Vue component中的数据
    blogLogin({ commit }, fromData) {
      axios({
        url: 'http://127.0.0.1:8000/api/azrael-login/',
        method: 'POST',
        data: Qs.stringify(fromData),
      }).then((res) => {
        if (res.data === 'none') {
          alert('用户名不存在!');
          return;
        }
        if (res.data === 'pwderr') {
          alert('密码错误');
          return;
        }
        commit('svaeUserInfo', res.data);
        // 缓存token到本地实现自动登录
        localStorage.setItem('token', res.data.token);
        // 缓存username
        localStorage.setItem('username', res.data.nickname);
        this.state.currentname = res.data.nickname;
        router.push({ name: 'Home' });
      });
    },
    // 注册
    blogRegister({ commit }, fromData) {
      axios({
        url: 'http://127.0.0.1:8000/api/azrael-register/',
        method: 'POST',
        data: Qs.stringify(fromData),
      }).then((res) => {
        if (res.data === 'repeat') {
          alert('用户名已存在!');
          return;
        }
        commit('svaeUserInfo', res.data);
        // 缓存token到本地实现自动登录
        localStorage.setItem('token', res.data.token);
        // 缓存username
        localStorage.setItem('username', res.data.nickname);
        this.state.currentname = res.data.nickname;
        router.push({ name: 'Home' });
      });
      window.location.href = window.location.href;
    },

    // 自动登录
    autoLogin({ commit }) {
      let token = localStorage.getItem('token');
      this.state.currentname = localStorage.getItem('username');
      if (token) {
        axios({
          url: 'http://127.0.0.1:8000/api/auto-login/',
          method: 'POST',
          data: Qs.stringify({ token }),
        }).then((res) => {
          if (res.data === 'TokenTimeOut') {
            alert('用户信息过期,请重新登录');
            return;
          }
          commit('svaeUserInfo', res.data);
          // 缓存token到本地实现自动登录
          localStorage.setItem('token', res.data.token);
          // 缓存username
          localStorage.setItem('username', res.data.nickname);
          router.push({ name: 'Home' });
        });
      }
    },
    // 登出
    blogLogOut({ commit }, token) {
      commit('clearUserInfo');
      localStorage.removeItem('token');
      localStorage.removeItem('username');
      axios({
        url: 'http://127.0.0.1:8000/api/azrael-logout/',
        method: 'POST',
        data: Qs.stringify({ token }),
      }).then((res) => {});
    },
    // 用户权限判断
    async checkUserPerm({ getters }, checkInfo) {
      // 用户
      let token = getters.loginState;
      // 表
      let contentType = checkInfo.contentType;
      // 权限
      let permissions = checkInfo.permissions;

      // 鉴权结果   必须等axios请求完成返回结果后才执行后面的代码
      let perm_data;
      await axios({
        url: 'http://127.0.0.1:8000/api/azrael-checkperm/',
        method: 'POST',
        data: Qs.stringify({
          token,
          contentType,
          permissions: JSON.stringify(permissions),
        }),
      }).then((res) => {
        if (res.data === 'nologin') {
          perm_data = false;
          alert('用户信息错误');
          return;
        }
        if (res.data === 'nopermission') {
          perm_data = false;
          alert('用户权限不足，请联系管理员');
          return;
        }
        if (res.data === 'OK') {
          perm_data = true;
        }
      });
      return perm_data;
    },
  },
  modules: {},
});
