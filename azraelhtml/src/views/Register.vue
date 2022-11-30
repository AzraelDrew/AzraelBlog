<template>
  <div id="refister-page" class="flex">
    <div class="dweb refisterbox" @keyup.enter="blogRegister">
      <div class="header">注册</div>
      <el-divider></el-divider>
      <div class="box flex">
        <el-form :label-position="'left'" label-width="60px" :model="fromData">
          <div class="input_box">
            <el-form-item label="用户名">
              <el-input v-model="fromData.username"></el-input>
            </el-form-item>
            <el-form-item label="密码">
              <el-input v-model="fromData.password" type="password"></el-input>
            </el-form-item>
            <el-form-item label="密码">
              <el-input v-model="fromData.password2" type="password"></el-input>
            </el-form-item>
          </div>
          <el-form-item class="btn flex">
            <el-button @click="blogRegister" type="success" round
              >注册</el-button
            >
            <el-button @click="toLogin" type="warning" round
              >已有帐号登录</el-button
            >
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from "axios";
// import Qs from "qs";
export default {
  data() {
    return {
      fromData: {
        username: '',
        password: '',
        password2: '',
      },
    };
  },
  methods: {
    //提示框
    messageNotify(title, message, type) {
      this.$notify({
        title: title,
        message: message,
        type: type,
        showClose: true,
        center: true,
      });
    },
    blogRegister() {
      if (
        this.fromData.username.length == 0 ||
        this.fromData.password.length == 0 ||
        this.fromData.password2.length == 0
      ) {
        this.messageNotify('警告', '帐号或密码不能为空!', 'warning');

        return;
      }
      if (
        this.fromData.password.length < 7 ||
        this.fromData.password2.length < 7
      ) {
        this.messageNotify('警告', '密码不能低于8位!', 'warning');

        return;
      }
      if (this.fromData.password !== this.fromData.password2) {
        this.messageNotify('警告', '两次密码不一致!', 'warning');
        return;
      }

      this.$store.dispatch('blogRegister', this.fromData);
    },

    toLogin() {
      this.$router.push({ name: 'Login' });
    },
  },
};
</script>

<style scoped>
#refister-page {
  height: 85vh;
}
.flex {
  display: flex;
  justify-content: center;
  align-content: center;
  justify-items: center;
  align-items: center;
}
.refisterbox {
  padding: 20px;
  height: 70vh;
  width: 65vw;
}
.btn {
  position: relative;
  left: -1.8vw;
}
.el-input {
  width: 40vw;
  padding: 0;
  margin: 0;
}
</style>
