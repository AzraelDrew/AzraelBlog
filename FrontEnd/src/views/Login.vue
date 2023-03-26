<template>
  <div class="flex flexWarp loginBox">
    <transition name="fade" appear>
      <!-- <img class="bg" src="../assets/imgs/avatar.jpg" alt="" /> -->
      <div class="felx login" @keydown.enter="login">
        <div class="flex">
          <h1>AzraelBlog</h1>
        </div>
        <div class="inputBox">
          <el-input v-model="name" class="input" placeholder="用户名" />
        </div>
        <div class="inputBox">
          <el-input
            v-model="password"
            class="input"
            type="password"
            placeholder="密码"
            :show-password="true"
          />
          <div class="flex flexJustifyEnd" style="margin-top: 10px">
            <a class="forgetPwd link" href="">忘记密码?</a>
          </div>
        </div>

        <div class="flex inputBox flexJustifySpaceBetween">
          <TheButton class="loginButton" text="注册" />
          <TheButton class="loginButton" text="登录" @click="login" />
        </div>
      </div>
    </transition>
  </div>
</template>
<script setup lang="ts">
// import axios from 'axios';
import { ref } from 'vue';
import { ElNotification } from 'element-plus';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user';
import TheButton from '@/components/TheButton.vue';
const userstore = useUserStore();

const name = ref('');
const password = ref('');
const router = useRouter();
async function login() {
  let res = await userstore.userLogin(name.value, password.value);
  if (res == 'pwderr') {
    ElNotification({
      title: 'Error',
      message: '密码错误',
      type: 'error',
    });
    return;
  } else if (res == 'none') {
    ElNotification({
      title: 'Error',
      message: '用户不存在',
      type: 'error',
    });
    return;
  }
  if (res == 'OK') {
    console.log(
      `%c
       ███████╗██╗   ██╗ ██████╗ ██████╗███████╗███████╗███████╗██╗
       ██╔════╝██║   ██║██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝██║
       ███████╗██║   ██║██║     ██║     █████╗  ███████╗███████╗██║
       ╚════██║██║   ██║██║     ██║     ██╔══╝  ╚════██║╚════██║╚═╝
       ███████║╚██████╔╝╚██████╗╚██████╗███████╗███████║███████║██╗
       ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝╚═╝
    `,
      'color:#7c9beb'
    );
    ElNotification({
      title: 'Success',
      message: '登录成功',
      type: 'success',
      duration: 1000,
    });
    router.replace({ name: 'Home' });
  }
}
</script>

<style scoped>
.loginBox {
  min-height: 100vh;
  border-radius: 15px;
  box-shadow: 50px -50px 50px #d3d3d3, -50px -50px 50px #d3d3d3, 50px 50px 50px #d3d3d3,
    -50px 50px 50px #ededed;
}
.bg {
  /* max-width: 40vw; */
  min-height: 30vh;
  max-height: 60vh;
  margin-right: 5vw;
  border-radius: 15px;
  background: #e0e0e0;
  box-shadow: 20px 20px 40px #d3d3d3, -20px -20px 40px #ededed, -20px 0 40px #d3d3d3,
    0 -20px 40px #d3d3d3;
}
.login {
  padding: 60px;
  min-height: 30vh;
  min-width: 30vw;
  max-height: 60vh;
  border-radius: 15px;
  background: #e0e0e060;
  box-shadow: 20px 20px 40px #d3d3d3, -20px -20px 40px #ededed, -20px 0 40px #d3d3d3,
    0 -20px 40px #d3d3d3;
}
.forgetPwd {
  color: #6bb4f1;
}
.forgetPwd:hover {
  color: #2d4d66;
}

.inputBox {
  position: relative;
  margin: 60px 0;
}

.input {
  height: 50px;
}

.loginButton {
  min-width: 100px;
  max-width: 10vw;
  height: 45px;
  font-size: 18px;
}
</style>
