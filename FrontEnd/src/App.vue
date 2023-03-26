<script setup lang="ts">
import { RouterView } from 'vue-router';
import { onMounted, watch } from 'vue';
import { useUserStore } from './stores/user';

import { useDark, useToggle } from '@vueuse/core';

const isDark = useDark();

const userstore = useUserStore();

onMounted(() => {
  userstore.GetUserInfo(userstore.userInfo.token);
  console.log(
    `%c
██╗  ██╗███████╗██╗     ██╗      ██████╗     ██╗    ██╗ ██████╗ ██████╗ ██╗     ██████╗ 
██║  ██║██╔════╝██║     ██║     ██╔═══██╗    ██║    ██║██╔═══██╗██╔══██╗██║     ██╔══██╗
███████║█████╗  ██║     ██║     ██║   ██║    ██║ █╗ ██║██║   ██║██████╔╝██║     ██║  ██║
██╔══██║██╔══╝  ██║     ██║     ██║   ██║    ██║███╗██║██║   ██║██╔══██╗██║     ██║  ██║
██║  ██║███████╗███████╗███████╗╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║  ██║███████╗██████╔╝
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ 
  `,
    'color:#7c9beb'
  );
});
watch(userstore.userInfo, () => {
  userstore.GetUserInfo(userstore.userInfo.token);
});
</script>

<template>
  <router-view> </router-view>
  <footer v-if="$route.name != 'Login'" class="footer">&copy;Azrael. All Rights Reserved.</footer>
  <el-backtop :bottom="40" :right="30">
    <div class="backTop">UP</div>
  </el-backtop>
</template>

<style scoped>
.footer {
  text-align: center;
  padding-top: 100px;
  padding-bottom: 40px;
  color: #828282;
}
.footer.inside {
  position: absolute;
  bottom: 20px;
  width: 100%;
}
.backTop {
  height: 100%;
  width: 100%;
  background-color: var(--el-bg-color-overlay);
  box-shadow: var(--el-box-shadow-lighter);
  text-align: center;
  line-height: 40px;
  color: #1989fa;
  border-radius: 50%;
  cursor: pointer;
}
</style>
