<template>
  <div id="login-page" class="flex">
    <div class="dweb loginbox" @keyup.enter="blogLogin()">
      <div class="header">用户登录</div>
      <el-divider></el-divider>
      <div class="box flex">
        <el-form :label-position="'left'" label-width="60px" :model="fromData">
          <div class="input_box ">
            <el-form-item label="用户名">
              <el-input v-model="fromData.username"></el-input>
            </el-form-item>
            <el-form-item label="密码  ">
              <el-input v-model="fromData.password" type="password"></el-input>
            </el-form-item>
          </div>
          <el-form-item class="btn flex">
            <el-button @click="blogLogin()" :plain="true" type="success" round
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
        username: '',
        password: '',
        // fullscreenLoading: false,
      },
    };
  },
  methods: {
    blogLogin() {
      if (
        this.fromData.username.length == 0 ||
        this.fromData.password.length == 0
      ) {
        this.$notify({
          title: '警告',
          message: '帐号或密码不能为空!',
          type: 'warning',
          showClose: true,
          center: true,
        });
        return;
      }

      this.$store.dispatch('blogLogin', this.fromData);
    },
    toRegister() {
      this.$router.push({ name: 'Register' });
      // this.fullscreenLoading = true;
      // setTimeout(() => {
      //   this.fullscreenLoading = false;
      // }, 500);
    },
  },
};
</script>

<style scoped>
#login-page {
  height: 83vh;
}
.flex {
  display: flex;
  justify-content: center;
  align-content: center;
  justify-items: center;
  align-items: center;
}
.loginbox {
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
