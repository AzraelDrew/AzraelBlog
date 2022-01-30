<template>
  <div id="refister-page">
    <div class="dweb refisterbox" @keyup.enter="blogRegister">
      <div class="header">注册</div>
      <el-divider></el-divider>
      <div class="box">
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
          <el-form-item class="btn">
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
    blogRegister() {
      if (
        this.fromData.username.length == 0 ||
        this.fromData.password.length == 0 ||
        this.fromData.password2.length == 0
      ) {
        alert('帐号或密码不能为空!');
        return;
      }
      if (this.fromData.password.length < 7) {
        alert('密码不能低于8位');
        return;
      }
      if (this.fromData.password !== this.fromData.password2) {
        alert('两次密码不一致!');
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
  display: flex;
  justify-content: center;
  align-items: center;
}
.refisterbox {
  padding: 20px;
  height: 60vh;
  width: 60vw;
}
.box {
  padding-top: 10vh;
}
.input_box {
  padding-left: 18vw;
}
.btn {
  padding-left: 20vw;
  padding-top: 3vh;
}
.el-input {
  width: 300px;
}</style
>e>
