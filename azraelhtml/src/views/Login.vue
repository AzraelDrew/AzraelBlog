<template>
  <div id="login-page">
    <div class="dweb loginbox" @keyup.enter="blogLogin()">
      <div class="header">用户登录</div>
      <el-divider></el-divider>
      <div class="box">
        <el-form :label-position="'left'" label-width="60px" :model="fromData">
          <div class="input_box">
            <el-form-item label="用户名">
              <el-input v-model="fromData.username"></el-input>
            </el-form-item>
            <el-form-item label="密码  ">
              <el-input v-model="fromData.password" type="password"></el-input>
            </el-form-item>
          </div>
          <el-form-item class="btn">
            <el-button @click="blogLogin()" type="success" round
              >登录</el-button
            >
            <el-button @click="toRegister()" type="warning" round
              >注册</el-button
            >
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      fromData: {
        // username: this.$store.state.currentname,
        username: '',
        password: '',
      },
    };
  },
  methods: {
    blogLogin() {
      if (
        this.fromData.username.length == 0 ||
        this.fromData.password.length == 0
      ) {
        alert('帐号或密码不能为空!');
        return;
      }

      this.$store.dispatch('blogLogin', this.fromData);
      // this.$store.state.currentname == this.fromData.username;
    },
    toRegister() {
      this.$router.push({ name: 'Register' });
    },
  },
};
</script>

<style scoped>
#login-page {
  height: 85vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
.loginbox {
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
  padding-left: 21vw;
  padding-top: 10vh;
}
.el-input {
  width: 300px;
}
</style>
