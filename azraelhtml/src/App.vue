<template>
  <div id="app">
    <link rel="stylesheet" href="//at.alicdn.com/t/font_1261797_48wm20jf8z.css" />

    <!-- 顶部导航 -->
    <div id="top-menu" class="dweb">
      <div>
        <p v-if="authUserLogin" :class="'user_name ' + left + mobile_left">
          <span>Welcome Back {{ this.$store.state.currentname }}</span>
          <el-button
            id="logout"
            :class="mobile_left"
            @click="blogLogOut()"
            v-if="authUserLogin"
            type="danger"
            size="medium"
            round
            style="margin-left:20px"
            >Logout</el-button
          >
        </p>
      </div>
    </div>
    <!-- 左侧边栏导航 -->
    <div id="left-menu" :class="'dweb ' + mobile_left">
      <i v-if="authUserLogin" @click="showHideLeftMenu" id="left-btn" :class="hideMenu"></i>
      <!-- 导航栏 -->
      <el-col :span="24" style="margin-top: 70px">
        <el-menu
          class="el-menu-vertical-demo"
          background-color="#00000000"
          text-color="#fff"
          active-text-color="#FFCD77"
          @select="choosMenu"
          :default-active="activeIndex"
        >
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-folder-opened"></i>
              <span>文章管理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="/add-article">发布文章</el-menu-item>
              <el-menu-item index="/article-list">文章列表</el-menu-item>
              <el-menu-item index="/all-article-list">所有文章</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-menu-item index="/user-permission">
            <i class="el-icon-user"></i>
            <span slot="title">用户管理</span>
          </el-menu-item>
          <el-menu-item index="/lanmu-admin">
            <i class="el-icon-s-operation"></i>
            <span slot="title">栏目管理</span>
          </el-menu-item>
          <el-menu-item index="/user-info">
            <i class="el-icon-user"></i>
            <span slot="title">用户信息</span>
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
        <span>Azrael For Graduation Project </span
        ><span @click="open_github"
          ><i style="font-size:20px" class="iconfont iconGitHub"></i
        ></span>
      </div>
    </div>
  </div>
</template>

<script>
import { Loading } from 'element-ui';
import EventBus from './EventBus.js';
let loadingInstance = Loading.service({ fullscreen: true, text: '拼命加载中.......' });
setTimeout(() => {
  loadingInstance.close();
}, 2000);
export default {
  data() {
    return {
      activeIndex: '1',
      screenWidth: document.body.clientWidth,
      hideMenu: 'el-icon-s-fold',
      mobile_left: '',
      mobile_content: '',
      left: 'left',
      show_login_btn: false,
      // left_user: false,
      // left_lanmu: false,
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
        this.$router.push({ name: 'Login' });
      }
      if (this.$store.getters.loginState) {
        this.mobile_left = '';
        this.mobile_content = '';
      }

      // let checkInfo_user = {
      //   contentType: 'auth_user',
      //   permissions: ['add', 'change', 'delete', 'view'],
      // };
      // this.$store.dispatch('checkUserPerm', checkInfo_user).then((res) => {
      //   if (res) {
      //     this.left_user = true;
      //   }
      // });
      // let checkInfo_article = {
      //   contentType: 'Blog_article',
      //   permissions: ['add', 'change', 'delete', 'view'],
      // };
      // this.$store.dispatch('checkUserPerm', checkInfo_article).then((res) => {
      //   if (res) {
      //     this.left_lanmu = true;
      //   }
      // });
    },
  },
  created() {
    this.$store.dispatch('autoLogin');
    EventBus.$on('gotolanmu', (url) => {
      this.activeIndex = url;
    });
  },
  mounted() {
    this.changeDevice();
    if (!this.$store.getters.loginState) {
      this.mobile_left = 'xs';
      this.mobile_content = 'xs';
    }
  },

  methods: {
    choosMenu(index) {
      this.$router.push({ path: index });
    },
    changeDevice() {
      if (this.screenWidth <= 500) {
        this.mobile_left = 'xs';
        this.mobile_content = 'xs';
        this.show = false;
      }
    },
    showHideLeftMenu() {
      if (this.mobile_left === '') {
        this.mobile_left = 'xs';

        this.left = '';
      } else {
        this.mobile_left = '';
        this.left = '';
      }
      if (this.hideMenu === 'el-icon-s-fold') {
        this.hideMenu = 'el-icon-s-unfold';
      } else {
        this.hideMenu = 'el-icon-s-fold';
      }
      // 宽屏
      if (this.screenWidth > 500) {
        if (this.mobile_content === '') {
          this.mobile_content = 'xs';
        } else {
          this.mobile_content = '';
        }
        this.show_login_btn = !this.show_login_btn;
      }
    },
    blogLogOut() {
      this.$store.dispatch('blogLogOut', this.$store.getters.loginState);
      this.mobile_content = 'xs';
      this.mobile_left = 'xs';
    },
    open_github() {
      window.open('https://github.com/AzraelDrew/AzraelBlog');
    },
  },
};
</script>

<style>
.el-col {
  margin-top: 5px;
}
</style>
