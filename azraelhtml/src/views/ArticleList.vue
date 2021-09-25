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
        <el-col :span="24" v-for="item in article_list" :key="item.id">
          <div class="card dweb">
            <el-row>
              <el-col :xs="24" :lg="6">
                <el-image
                  v-if="screenWidth > 500"
                  style="height: 80px"
                  :src="item.cover"
                  :fit="'cover'"
                ></el-image>
                <el-image
                  v-else
                  style="width: 100%"
                  :src="item.cover"
                  :fit="'cover'"
                ></el-image>
              </el-col>
              <el-col class="text-item" :xs="24" :lg="4">
                <span>{{ item.title }}</span>
              </el-col>
              <el-col class="text-item" :xs="12" :lg="7">
                <span>发布者：admin</span>
              </el-col>
              <el-col class="text-item" :xs="12" :lg="7">
                <el-button
                  type="success"
                  icon="el-icon-search"
                  circle
                ></el-button>
                <el-button
                  type="danger"
                  icon="el-icon-delete"
                  circle
                  @click="deleteArticle(item.id)"
                ></el-button>
              </el-col>
            </el-row>
          </div>
        </el-col>
      </el-row>
    </div>
    <div class="dweb" style="margin-top: 10px">
      <!-- 分页器 -->
      <el-pagination
        background
        layout="prev, pager, next"
        :total="total"
        :page-size="pageSize"
        @current-change="currentChange"
      >
      </el-pagination>
    </div>
  </div>
</template>

<script>
// import store from "../store";
import axios from "axios";
import Qs from "qs";
export default {
  props: ["screenWidth"],
  data() {
    return {
      currentPpage: 1,
      pageSize: 5,
      total: 100,
      article_list: [],
    };
  },
  mounted() {
    this.getArticleList(this.currentPpage, this.pageSize, this.total);
  },
  methods: {
    getArticleList(page) {
      axios({
        url: "http://localhost:9000/api/atricle-list/",
        method: "GET",
        params: {
          page,
          pageSize: this.pageSize,
        },
      }).then((res) => {
        this.article_list = res.data.data;
        this.total = res.data.total;
      });
    },
    currentChange(val) {
      this.currentPpage = val;
      this.getArticleList(val);
    },
    // 删除文章
    deleteArticle(id) {
      if (confirm("Are you sure you want to delete")) {
        let checkInfo = {
          contentType: "Blog_article",
          permissions: ["delete"],
        };
        this.$store.dispatch("checkUserPerm", checkInfo).then((res) => {
          // console.log(res);
          // 当有权限是才会跳转到用户管理页面  否则不会跳转(看不见用户管理界面)
          if (res) {
            axios({
              url: "http://localhost:9000/api/delete-article/",
              method: "DELETE",
              data: Qs.stringify({
                id,
                token: this.$store.getters.loginState,
              }),
              headers: {
                "Content-Type": "application/x-www-form-urlencoded",
              },
            }).then((res) => {
              // console.log(res.data);
              if (res.data === "nologin") {
                alert("用户登录信息错误");
                return;
              }
              if (res.data === "nopermission") {
                alert("权限不足");
              }
              this.getArticleList(this.currentPpage);
            });
            // next();
          }
        });
      }
    },
  },
};
</script>

<style scoped>
#article-list .dweb {
  padding: 20px 10px;
}
.card.dweb .text-item {
  color: #fff;
  height: 80px;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>

