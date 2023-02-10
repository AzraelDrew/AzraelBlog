<template>
  <div id="login-page" class="flex">
    <div class="dweb loginbox" @keyup.enter="blogLogin()">
      <div class="header">用户登录</div>
      <el-divider></el-divider>
      <div class="box flex">
        <el-form
          :label-position="'left'"
          label-width="60px"
          :model="fromData"
          class="form_input_box"
        >
          <div class="input_box flex">
            <div>
              <el-input
                placeholder="用户名"
                v-model="fromData.username"
                style="height: 60px;"
              ></el-input>
            </div>
            <div>
              <el-input
                placeholder="密码"
                v-model="fromData.password"
                type="password"
                style="height: 60px;"
              ></el-input>
              <div style="display: flex;flex-direction: row-reverse;">
                <a href="" @click.prevent="toRestPwd()" style="color:aqua; ">忘记密码?</a>
              </div>
            </div>
          </div>
          <el-form-item class="btn flex">
            <el-button @click="toRegister()" class="btn_distance" type="warning" round
              >去注册</el-button
            >
            <el-button @click="blogLogin()" class="btn_distance" :plain="true" type="success" round
              >登录</el-button
            >
            <!-- <el-button @click.prevent="toRestPwd()" class="btn_distance" type="warning" round
              >忘记密码</el-button
            > -->
            <!-- <el-button @click="toRestPwd()" type="warning" round>忘记密码</el-button> -->
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
      if (this.fromData.username.length == 0 || this.fromData.password.length == 0) {
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
    toRestPwd() {
      this.$router.push({ name: 'RestPwd' });
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
  flex-wrap: wrap;
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
.form_input_box {
  position: relative;
  top: 10vh;
}

.btn_distance {
  margin: 20px 6vw;
}
</style>
