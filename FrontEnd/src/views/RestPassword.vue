<template>
  <div class="flex flexWarp loginBox">
    <transition name="fade" appear>
      <!-- <img class="bg" src="../assets/imgs/avatar.jpg" alt="" /> -->
      <div class="felx login" @keydown.enter="restPassword">
        <div class="flex" style="margin-bottom: -50px;">
          <h1>修改密码</h1>
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
        </div>
        <div class="inputBox">
          <el-input
            v-model="password2"
            class="input"
            type="password"
            placeholder="确认密码"
            :show-password="true"
          />
        </div>

        <div class="flex inputBox flexJustifySpaceBetween" style="margin-top: -20px;">
          <TheButton class="loginButton" text="去登录" @click="toLogin" />
          <TheButton class="loginButton" text="修改" @click="restPassword" />
        </div>
      </div>
    </transition>
  </div>
</template>
<script setup lang="ts">
import { ref } from 'vue';
import { ElNotification } from 'element-plus';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user';
import TheButton from '@/components/TheButton.vue';
import useAxios from '@/composables/useAxios';


const name = ref('');
const password = ref('');
const password2 = ref('');
const router = useRouter();
const axios = useAxios()
const userstore = useUserStore()
async function restPassword() {
  if(password.value.length<8 ||password2.value.length<8){
    ElNotification({
      title: 'Error',
      message: '密码不能少于8个字符',
      type: 'error',
    });
    return;
  }
  if(password.value!=password2.value){
    ElNotification({
      title: 'Error',
      message: '两次密码不一致',
      type: 'error',
    });
    return;
  }
  let res = await axios.post('api/rest/password/', {
    username:name.value,
    password:password.value
  });
  console.log(res.data);
  if(res.data=='not_exist'){
    ElNotification({
      title: 'Error',
      message: '用户不存在',
      type: 'error',
    });
    return;
  }
  ElNotification({
    title: 'Success',
    message: '修改成功,请登录',
    type: 'success',
  });
  router.replace({ name: 'Login' });
  }


function toLogin() {
  router.replace({ name: 'Login' });
}
</script>

<style scoped lang="scss">
.loginBox {
  min-height: 100vh;
  border-radius: 15px;
  box-shadow: 10px -10px 10px #d3d3d3, -10px -10px 10px #d3d3d3, 10px 10px 10px #d3d3d3,
    -10px 10px 10px #ededed;
}
.bg {
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
  &:hover {
    color: #2d4d66;
  }
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
