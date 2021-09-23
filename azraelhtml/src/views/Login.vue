<template>
  <div id="login-page">
    <div class="dweb loginbox">
      <div class="header">用户登录</div>
      <el-divider></el-divider>
      <div class="box">
        <el-form :label-position="'left'" label-width="60px" :model="fromData">
          <div class="input_box">
            <el-form-item label="用户名">
              <el-input v-model="fromData.username"></el-input>
            </el-form-item>
            <el-form-item label="密码  ">
              <el-input v-model="fromData.password"></el-input>
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
// import axios from "axios";
// import Qs from "qs";
export default {
  data() {
    return {
      fromData: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    blogLogin() {
      if (
        this.fromData.username.length == 0 ||
        this.fromData.password.length == 0
      ) {
        alert("帐号或密码不能为空!");
        return;
      }
      // else {
      // axios({
      //   url: "http://localhost:9000/api/azrael-login/",
      //   method: "POST",
      //   data: Qs.stringify(this.fromData),
      // }).then((res) => {
      //   if (res.data === "none") {
      //     alert("用户名不存在!");
      //     return;
      //   }
      //   if (res.data === "pwderr") {
      //     alert("密码错误");
      //     return;
      //   }
      //   // console.log(res.data);
      // //this.$store.commit 调用mutations中的方法
      //   this.$store.commit("svaeUserInfo", res.data);
      // });
      // }

      // this.$store.dispatch 调用actions中的方法
      this.$store.dispatch("blogLogin", this.fromData);
    },
    toRegister() {
      this.$router.push({ name: "Register" });
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
