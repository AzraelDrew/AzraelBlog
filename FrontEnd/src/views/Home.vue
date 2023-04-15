<template>
  <TheNavBar>
    <template #avatarAndNickname>
      <TheAvatar class="avatar" :size="40" :src="userstore.userInfo.avatar" />

      <span>{{ userstore.userInfo.name }}</span>
    </template>
    <template #input>
      <svg class="icon" aria-hidden="true" viewBox="0 0 24 24">
        <g>
          <path
            d="M21.53 20.47l-3.66-3.66C19.195 15.24 20 13.214 20 11c0-4.97-4.03-9-9-9s-9 4.03-9 9 4.03 9 9 9c2.215 0 4.24-.804 5.808-2.13l3.66 3.66c.147.146.34.22.53.22s.385-.073.53-.22c.295-.293.295-.767.002-1.06zM3.5 11c0-4.135 3.365-7.5 7.5-7.5s7.5 3.365 7.5 7.5-3.365 7.5-7.5 7.5-7.5-3.365-7.5-7.5z"
          ></path>
        </g>
      </svg>
      <input placeholder="Search" type="search" class="input" @keyup.enter="Search" />
    </template>
    <template #postIcon v-if="userstore.isLogin">
      <router-link to="/postArticle" class="link linkColor postArticle"
        ><TheIcon icon="iconbianji4" :size="22"
      /></router-link>
    </template>
    <template #dropDown>
      <el-dropdown v-if="userstore.isLogin">
        <span class="el-dropdown-link flex">
          个人中心<el-icon class="el-icon--right"><arrow-down /></el-icon>
        </span>
        <template #dropdown>
          <el-dropdown-menu class="dropDown">
            <el-dropdown-item command="a">
              <router-link class="flex link linkColor" to="/profile">
                <span>个人信息</span>
                <TheIcon icon="iconmy" :size="18" />
              </router-link>
            </el-dropdown-item>
            <el-dropdown-item command="b" @click="Logout">
              <span>退出登录</span>
              <TheIcon icon="iconlogout" :size="18"
            /></el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
      <div v-else>
        <a class="link linkColor" @click="Login">登录</a>
      </div>
    </template>
  </TheNavBar>
  <div>
    <transition name="fade" appear>
      <TheArtcile :search="search" />
    </transition>
  </div>
</template>
<script setup lang="ts">
import { ref } from 'vue';
import { RouterLink, useRouter } from 'vue-router';
import { ArrowDown } from '@element-plus/icons-vue';
import { useUserStore } from '@/stores/user';

import TheArtcile from '@/components/TheArtcile.vue';
import TheIcon from '@/components/TheIcon.vue';
import TheNavBar from '@/components/TheNavBar.vue';
import TheAvatar from '@/components/TheAvatar.vue';

const router = useRouter();

const userstore = useUserStore();

const search = ref('');

function Search(e: any) {
  search.value = e.target.value;
  e.target.value = '';
}
function Login() {
  router.replace({ name: 'Login' });
}

function Logout() {
  userstore.userLogout();
  router.replace({ name: 'Home' });
}
</script>

<style scoped>
.avatar {
  margin-right: 10px;
}

.postArticle {
  margin-right: 10px;
}
.input {
  width: 40vw;
  height: 40px;
  line-height: 28px;
  padding: 0 1rem;
  padding-left: 2.5rem;
  border: 2px solid transparent;
  border-radius: 8px;
  outline: none;
  background-color: #f3f3f4;
  color: #0d0c22;
  transition: 0.3s ease;
}

.input::placeholder {
  color: #00000040;
}

.input:focus,
input:hover {
  outline: none;
  border-color: #749cf1;
  background-color: #fff;
  box-shadow: 0 0 0 4px #749cf130;
}
.icon {
  position: absolute;
  left: 1rem;
  fill: #749cf1;
  width: 1rem;
  height: 1rem;
}

.example-showcase .el-dropdown-link {
  cursor: pointer;
  color: var(--el-color-primary);
  display: flex;
  align-items: center;
}

.linkColor {
  color: #000;
}
.linkColor:hover {
  color: #749cf1;
}
</style>
