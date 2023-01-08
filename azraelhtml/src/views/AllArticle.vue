<template>
  <div id="article-list">
    <!-- 面包屑导航 -->
    <div class="dweb">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>文章列表</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <!-- 文章列表 -->
    <div class="dweb" style="margin-top: 10px">
      <el-row>
        <el-col :span="24">
          <div class="card1 dweb">
            <el-row>
              <el-col class="text-item" :sm="4" :xs="4" :lg="4">
                <span>
                  封面
                </span>
              </el-col>
              <el-col class="text-item" :sm="8" :xs="8" :lg="8">
                <span>标题</span>
              </el-col>
              <el-col class="text-item" :sm="6" :xs="6" :lg="5">
                <span>作者</span>
              </el-col>
              <el-col class="text-item" :sm="6" :xs="6" :lg="7">
                <span>
                  操作
                </span>
              </el-col>
            </el-row>
          </div>
        </el-col>
      </el-row>
      <el-row
        v-loading="loading"
        element-loading-text="拼命加载中"
        element-loading-background="#00000060"
        element-loading-spinner="el-icon-s-promotion"
        style="min-height:10vh"
      >
        <el-col :span="24" v-for="item in article_list" :key="item.id">
          <div class="card dweb flex">
            <el-row>
              <el-col :sm="4" :xs="4" :lg="4">
                <el-image
                  class="flex text-item "
                  :src="item.cover"
                  :fit="'cover'"
                  :preview-src-list="srcList"
                ></el-image>
                <!-- <el-image
                  class="flex text-item"
                  v-else
                  :src="item.cover"
                  :fit="'cover'"
                  :preview-src-list="srcList"
                ></el-image> -->
              </el-col>
              <el-col class="text-item" :sm="8" :xs="8" :lg="8">
                <span>{{ item.title }}</span>
              </el-col>
              <el-col class="text-item" :sm="6" :xs="6" :lg="5">
                <span>{{ item.nickName }}</span>
              </el-col>
              <el-col class="text-item" :sm="6" :xs="6" :lg="7">
                <el-button type="success" icon="el-icon-search" circle @click="toArticle(item.id)">
                </el-button>

                <el-button
                  type="danger"
                  icon="el-icon-delete"
                  circle
                  @click="
                    dialogVisible = true;
                    article_id = item.id;
                  "
                >
                </el-button>
                <el-dialog
                  :show-close="false"
                  :center="true"
                  title="提示"
                  :visible.sync="dialogVisible"
                  width="30%"
                >
                  <span>确定删除吗?</span>
                  <span slot="footer" class="dialog-footer">
                    <el-button @click="dialogVisible = false">取 消</el-button>
                    <el-button type="primary" @click="deleteArticle(article_id)">确 定</el-button>
                  </span>
                </el-dialog>
              </el-col>
            </el-row>
          </div>
        </el-col>
      </el-row>
    </div>
    <div v-show="!loading" class="dweb flex" style="margin-top: 10px">
      <!-- 分页器 -->
      <el-pagination
        background
        layout="prev, pager, next"
        :total="total"
        :pager-count="showPagination"
        :page-size="pageSize"
        :current-page="prevPage"
        @current-change="currentChange"
      >
      </el-pagination>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Qs from 'qs';
export default {
  data() {
    return {
      showPagination: 5,
      article_id: Number,
      dialogVisible: false,
      srcList: [],
      loading: true,
      currentPage: 1,
      prevPage: this.$store.state.currentPage,

      currentLanmu: 'all',
      pageSize: 4,
      total: 100,
      article_list: [],
    };
  },
  mounted() {
    this.getArticleList(this.$store.state.currentPage, this.currentLanmu);
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

    // 跳转内容页
    toArticle(id) {
      this.$router.push({ path: '/article', query: { id: id } });
      this.$store.state.currentPage = this.currentPage;
    },
    // 获取文章列表
    getArticleList(page, lanmu) {
      this.loading = true;
      axios({
        url: this.$store.state.baseurl + 'api/article-list/',
        method: 'GET',
        params: {
          page,
          currentname: 'all_user',
          pageSize: this.pageSize,
          lanmu: lanmu,
        },
      }).then((res) => {
        this.article_list = res.data.data;
        this.total = res.data.total;
        this.srcList = [];
        for (let i = 0; i < res.data.data.length; i++) {
          this.srcList.push(res.data.data[i].cover);
        }
        this.loading = false;
        return;
      });
    },
    currentChange(val) {
      this.currentPage = val;
      this.getArticleList(val, this.currentLanmu);
      return;
    },
    // 删除文章
    deleteArticle(id) {
      if (this.dialogVisible) {
        let checkInfo = {
          contentType: 'Blog_article',
          permissions: ['delete'],
        };
        this.$store.dispatch('checkUserPerm', checkInfo).then((res) => {
          // 当有权限是才会跳转到用户管理页面  否则不会跳转(看不见用户管理界面)
          if (res) {
            axios({
              url: this.$store.state.baseurl + 'api/delete-article/',
              method: 'DELETE',
              data: Qs.stringify({
                id,
                token: this.$store.getters.loginState,
              }),
              headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
              },
            }).then((res) => {
              if (res.data === 'nologin') {
                this.messageNotify('警告', '用户登录信息错误!', 'error');
                return;
              }
              if (res.data === 'nopermission') {
                this.messageNotify('警告', '权限不足!', 'warning');
              }
              this.dialogVisible = false;
              this.getArticleList(this.currentPage, this.currentLanmu);
            });
          }
        });
      }
    },
  },
};
</script>

<style scoped lang="scss">
.flex {
  display: flex;
  justify-content: center;
  justify-items: center;
  align-content: center;
}
#article-list .dweb {
  padding: 20px 10px;
}
.card.dweb {
  height: 20vh; //同时改
}
.card.dweb .text-item {
  height: 12vh; //同时改
  color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
}
.card1.dweb .text-item {
  height: 12vh;
  color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
}

.el-image {
  width: 15vw;
}
.el-col.el-col-xs-6 {
  height: 12vh !important;
  .el-image {
    height: 12vh;
  }
}

.el-col-lg-5,
.el-col-lg-7 {
  height: 60px !important;
}
</style>
