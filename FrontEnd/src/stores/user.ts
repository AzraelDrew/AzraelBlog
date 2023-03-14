import { ref, type Ref, reactive, computed } from 'vue';
import { defineStore } from 'pinia';

import useAxios from '@/composables/useAxios';
const axios = useAxios();

export const useUserStore = defineStore('user ', () => {
  interface UserInfo {
    id: string;
    username: string;
    name: string;
    token: string;
    avatar: string;
    phone: string;
    desc: string;
  }

  const userInfo = reactive<UserInfo>({
    token: localStorage.getItem('token') || '',
    id: '',
    username: '',
    name: '',
    avatar: '',
    phone: '',
    desc: '',
  });
  const isLogin = computed(() => {
    return userInfo.token ? true : false;
  });

  async function userLogin(username: string, password: string) {
    let data = new FormData();
    data.append('username', username);
    data.append('password', password);
    let res = await axios.post('api/login/', data);
    const result = res.data;
    localStorage.setItem('token', result.token);
    userInfo.token = result.token;
    userInfo.id = result.userId;
    userInfo.username = result.name;
    userInfo.name = result.nickname;
    userInfo.avatar = result.avatar;
    userInfo.phone = result.phone;
    userInfo.desc = result.desc;
  }
  async function userLogout() {
    localStorage.removeItem('token');
    userInfo.token = '';
    userInfo.id = '';
    userInfo.username = '';
    userInfo.name = '';
    userInfo.avatar = '';
    userInfo.phone = '';
    userInfo.desc = '';
  }
  async function GetUserInfo(token: string) {
    let data = new FormData();
    data.append('token', token);
    let res = await axios.post('api/get/userinfo/', data);
    const result = res.data;
    userInfo.id = result.userId;
    userInfo.username = result.name;
    userInfo.name = result.nickname;
    userInfo.avatar = result.avatar;
    userInfo.phone = result.phone;
    userInfo.desc = result.desc;
    console.log(result);
  }
  return { isLogin, userInfo, userLogin, GetUserInfo, userLogout };
});
