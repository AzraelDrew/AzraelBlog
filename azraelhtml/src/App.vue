<template>
  <div id="app" v-show="loadingstate">
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
        >

          <el-menu-item index="/all-article-list">
            <i class="el-icon-folder-opened"></i>
            <span  slot="title">所有文章</span>
          </el-menu-item>
          <el-menu-item index="/user-permission">
            <i class="el-icon-user"></i>
            <span slot="title">用户管理</span>
          </el-menu-item>
          <el-menu-item index="/lanmu-admin">
            <i class="el-icon-s-operation"></i>
            <span slot="title">栏目管理</span>
          </el-menu-item>

          <!-- <el-menu-item index="/user-info">
            <i class="el-icon-user"></i>
            <span slot="title">用户信息</span>
          </el-menu-item> -->
          <el-menu-item index="LogOut" @click="blogLogOut()" v-if="authUserLogin">
            <i class="el-icon-back"></i>
            <span slot="title">退出登录</span>
          </el-menu-item>
        </el-menu>
      </el-col>
    </div>
    <!-- 网页内容 -->
    <div id="content" :class="mobile_content">
      <router-view :screenWidth="screenWidth"> </router-view>
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
let loadingstate = false;
let loadingInstance = Loading.service({
  fullscreen: true,
  background: '#00000090',
  spinner: 'el-icon-s-promotion',
  text: '拼命加载中.......',
});
export default {
  data() {
    return {
      loadingstate: loadingstate,
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
    setTimeout(() => {
      loadingInstance.close();
      this.loadingstate = true;
    }, 50);
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
