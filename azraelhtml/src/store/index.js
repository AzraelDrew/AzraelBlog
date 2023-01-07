import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import Qs from 'qs';
import router from '../router';
import { Notification } from 'element-ui';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    currentname: '',
    loginmessage: '',
    userinfo: {},
    baseurl: 'http://43.138.126.114:8000/',
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
        url: this.state.baseurl + 'api/azrael-login/',
        method: 'POST',
        data: Qs.stringify(fromData),
      }).then((res) => {
        if (res.data === 'none') {
          Notification({
            title: '错误',
            message: '用户不存在！',
            type: 'error',
          });
          return;
        }
        if (res.data === 'pwderr') {
          Notification({
            title: '错误',
            message: '密码错误！',
            type: 'error',
          });
          return;
        }

        commit('svaeUserInfo', res.data);
        // 缓存token到本地实现自动登录
        localStorage.setItem('token', res.data.token);
        this.state.currentname = res.data.nickname;
        router.push({ name: 'Home' });
      });
    },
    // 注册
    blogRegister({ commit }, fromData) {
      axios({
        url: this.state.baseurl + 'api/azrael-register/',
        method: 'POST',
        data: Qs.stringify(fromData),
      }).then((res) => {
        if (res.data === 'repeat') {
          Notification({
            title: '警告',
            message: '用户已注册！',
            type: 'warning',
          });

          return;
        }
        commit('svaeUserInfo', res.data);
        // 缓存token到本地实现自动登录
        localStorage.setItem('token', res.data.token);
        this.state.currentname = res.data.nickname;
        router.push({ name: 'Home' });
        console.log(res.data);
      });
      window.location.href = window.location.href;
    },

    // 自动登录
    autoLogin({ commit }) {
      let token = localStorage.getItem('token');
      this.state.currentname = localStorage.getItem('username');
      if (token) {
        axios({
          url: this.state.baseurl + 'api/auto-login/',
          method: 'POST',
          data: Qs.stringify({ token }),
        }).then((res) => {
          if (res.data === 'TokenTimeOut') {
            Notification({
              title: '错误',
              message: '用户信息过期,请重新登录',
              type: 'error',
            });
            // alert('用户信息过期,请重新登录');
            return;
          }
          commit('svaeUserInfo', res.data);
          // 缓存token到本地实现自动登录
          localStorage.setItem('token', res.data.token);
          this.state.currentname = res.data.nickname;
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
        url: this.state.baseurl + 'api/azrael-logout/',
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
        url: this.state.baseurl + 'api/azrael-checkperm/',
        method: 'POST',
        data: Qs.stringify({
          token,
          contentType,
          permissions: JSON.stringify(permissions),
        }),
      }).then((res) => {
        if (res.data === 'nologin') {
          perm_data = false;
          Notification({
            title: '错误',
            message: '用户信息错误',
            type: 'error',
          });
          // alert('用户信息错误');
          return;
        }
        if (res.data === 'nopermission') {
          perm_data = false;
          Notification({
            title: '错误',
            message: '用户权限不足，请联系管理员',
            type: 'error',
          });
          // alert('用户权限不足，请联系管理员');
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
