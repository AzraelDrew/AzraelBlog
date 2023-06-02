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
  const index = ref(0);
  const profileIndex = ref(0);

  const isLogin = computed(() => {
    return userInfo.token ? true : false;
  });
  function ChangeIndex(tab: number) {
    index.value = tab;
  }
  function ChangeProfileIndex(tab: number) {
    profileIndex.value = tab;
  }

  async function userLogin(username: string, password: string) {

    let res = await axios.post('api/login/', {
      username:username,
      password:password
    });
    const result = res.data;
    if (result == 'pwderr' || result == 'none') {
      return result;
    } else {
      localStorage.setItem('token', result.token);
      userInfo.token = result.token;
      userInfo.id = result.userId;
      userInfo.username = result.name;
      userInfo.name = result.nickname;
      userInfo.avatar = result.avatar;
      userInfo.phone = result.phone;
      userInfo.desc = result.desc;
      return 'OK';
    }
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

    let res = await axios.post('api/get/userinfo/', {
      token:token
    });
    const result = res.data;
    userInfo.id = result.userId;
    userInfo.username = result.name;
    userInfo.name = result.nickname;
    userInfo.avatar = result.avatar;
    userInfo.phone = result.phone;
    userInfo.desc = result.desc;
  }
  return {
    isLogin,
    userInfo,
    userLogin,
    GetUserInfo,
    userLogout,
    index,
    ChangeIndex,
    profileIndex,
    ChangeProfileIndex,
  };
});
