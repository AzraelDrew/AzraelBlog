<template>
  <div id="app">
    <!-- 顶部导航 -->
    <div id="top-menu" class="dweb"></div>
    <!-- 左侧边栏导航 -->
    <div id="left-menu" :class="'dweb ' + mobile_left">
      <i @click="showHideLeftMenu" id="left-btn" class="el-icon-menu"></i>
      <!-- 导航栏 -->
      <el-col :span="24" style="margin-top: 70px">
        <el-menu
          class="el-menu-vertical-demo"
          background-color="#00000000"
          text-color="#fff"
          active-text-color="#FFCD77"
          @select="choosMenu"
        >
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-folder-opened"></i>
              <span>文章管理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="/add-article">发布文章</el-menu-item>
              <el-menu-item index="/article-list">文章列表</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-menu-item index="/user-permission">
            <i class="el-icon-user"></i>
            <span slot="title">用户管理</span>
          </el-menu-item>
          <el-menu-item index="3">
            <i class="el-icon-money"></i>
            <span slot="title">打赏记录</span>
          </el-menu-item>
          <el-menu-item index="/lanmu-admin">
            <i class="el-icon-s-operation"></i>
            <span slot="title">栏目管理</span>
          </el-menu-item>
          <el-menu-item @click="blogLogOut()" v-if="authUserLogin">
            <i class="el-icon-back"></i>
            <span slot="title">退出登录</span>
          </el-menu-item>
        </el-menu>
      </el-col>
    </div>
    <!-- 网页内容 -->
    <div id="content" :class="mobile_content">
      <router-view :screenWidth="screenWidth"></router-view>
      <div id="footer" class="dweb">
        <span>Copyright &2021 Azrael</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      screenWidth: document.body.clientWidth,
      mobile_left: "",
      mobile_content: "",
    };
  },
  computed: {
    // 验证用户是否登录
    authUserLogin() {
      return this.$store.getters.loginState;
    },
  },
  watch: {
    // 监听用户token
    authUserLogin(newVal) {
      if (newVal == null) {
        this.$router.push({ name: "Login" });
      }
    },
  },
  created() {
    this.$store.dispatch("autoLogin");
  },
  mounted() {
    this.changeDevice();
  },

  methods: {
    choosMenu(index) {
      // console.log(index);
      this.$router.push({ path: index });
    },
    changeDevice() {
      if (this.screenWidth <= 500) {
        this.mobile_left = "xs";
        this.mobile_content = "xs";
      }
    },
    showHideLeftMenu() {
      if (this.mobile_left === "") {
        this.mobile_left = "xs";
      } else {
        this.mobile_left = "";
      }
      // 宽屏
      if (this.screenWidth > 500) {
        if (this.mobile_content === "") {
          this.mobile_content = "xs";
        } else {
          this.mobile_content = "";
        }
      }
    },
    blogLogOut() {
      this.$store.dispatch("blogLogOut", this.$store.getters.loginState);
      // this.$store.commit("clearUserInfo");
      // this.$router.push({ name: "Home" });
    },
  },
};
</script>

<style>
.el-col {
  margin-top: 5px;
}
</style>