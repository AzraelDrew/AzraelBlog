<template>
  <div>
    <TheNavBar>
      <template #avatarAndNickname>
        <router-link to="/" class="link" href=""
          ><TheIcon class="home icon" icon="iconzhuye3" :size="30" /></router-link
      ></template>
      <template #postIcon>
        <router-link to="/postArticle" class="link linkColor postArticle"
          ><TheIcon icon="iconbianji4" :size="25"
        /></router-link>
      </template>
      <template #dropDown>
        <el-dropdown v-if="userstore.isLogin">
          <a @click="Logout" class="link linkColor">退出登录</a>
        </el-dropdown>
        <div v-else>
          <router-link to="/">登录</router-link>
        </div>
      </template>
    </TheNavBar>
    <div class="profile flex">
      <div class="userInfo flex">
        <TheAvatar :size="200" :src="userstore.userInfo.avatar" />
        <div>
          <div class="flex flexJustifyStart">
            <h2 class="userName">{{ userstore.userInfo.name }}</h2>
            <router-link to="/profileEditing" class="flex link" href=""> 编辑个人信息</router-link>
          </div>
          <div class="flex flexJustifyStart">
            <pre class="desc">{{ userstore.userInfo.desc || '添加你的简介.....' }}</pre>
          </div>
        </div>
      </div>
    </div>
    <div class="articleList">
      <div class="flex">
        <TheIcon
          class="icon"
          v-for="(tab, index) in tabs"
          :icon="tab.icon"
          :size="40"
          :class="{ active: index === currentTab }"
          @click="GetArticle(index)"
        />
      </div>
      <div class="flexDirectionRow">
        <transition name="fade" appear>
          <TheArtcileList v-if="currentTab == 0" :posts="posts" />
          <TheArtcileList v-else-if="currentTab == 1" :posts="posts" />
          <TheArtcileList v-else-if="currentTab == 2" :posts="posts" />
        </transition>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, reactive, onMounted } from 'vue';
import { RouterLink, useRouter } from 'vue-router';

import TheArtcileList from '../components/TheArtcileList.vue';
import TheIcon from '../components/TheIcon.vue';
import TheNavBar from '@/components/TheNavBar.vue';
import TheAvatar from '@/components/TheAvatar.vue';
import TheButton from '@/components/TheButton.vue';

import { useUserStore } from '../stores/user';

import useAxios from '../composables/useAxios';
const axios = useAxios();

const router = useRouter();
const userstore = useUserStore();

const posts = ref([]);

const currentTab = ref(0);
const tabs = ref([
  {
    label: 'my',
    icon: 'iconmy',
  },

  {
    label: 'like',
    icon: 'icondianzan',
    number: 2,
  },
  {
    label: 'favourite',
    icon: 'iconshoucang5',
  },
]);

onMounted(async () => {
  let res = await AllArticle(userstore.userInfo.id, 'my');
  console.log(res);
  posts.value = res.data.data;
});

async function GetArticle(index: any) {
  currentTab.value = index;
  let res = await AllArticle(userstore.userInfo.id, tabs.value[currentTab.value].label);
  console.log(res);
  posts.value = res.data.data;
}
async function AllArticle(id: any, type: string) {
  let res = await axios({
    url: '/api/' + type + '/article/' + '?id=' + id,
    method: 'GET',
  });

  return res;
}

function Logout() {
  userstore.userLogout();
  router.replace({ name: 'Login' });
}
</script>
<style scoped>
.active {
  color: #0984e3;
}
.articleList {
  margin-top: 5vw;
}
.icon {
  margin: 0 5vw;
}
.profile {
  min-width: 60vw;
}
.userInfo {
  min-width: 40vw;
}

.avatar {
  margin-right: 5vw;
  box-shadow: 5px 0px 5px #d3d3d3, -5px 0px 5px #d3d3d3, 0px 5px 5px #d3d3d3;
}
.userName {
  margin-right: 40px;
}
.desc {
  max-width: 20vw;
}

.nav {
  padding: 10px 20px;
  height: 50px;
  border-radius: 15px;
  box-shadow: 50px 0px 20px #d3d3d3, -50px 0px 20px #d3d3d3;
  margin-bottom: 30px;
}
.home {
  margin-left: -10px;
  text-decoration: none;
  color: #000000;
}
.linkColor {
  text-decoration: none;
  color: #00000095;
}
.linkColor:hover {
  color: #87a4ed;
}
.postArticle {
  margin-right: 10px;
}
</style>
