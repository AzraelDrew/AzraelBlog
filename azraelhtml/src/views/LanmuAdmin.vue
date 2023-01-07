<template>
  <div>
    <!-- 面包屑导航 -->
    <BreadMenu class="nav" :page_name="'栏目管理'"></BreadMenu>
    <div class="body dweb">
      <el-row :gutter="10">
        <el-col :span="6"
          ><div class="dweb">
            <h5>栏目树形图</h5>
          </div>
          <div class="tree body dweb" style="display: flex">
            <el-input v-model="new_lanmu_name" placeholder="请输入新栏目名称"></el-input>
            <el-button @click="pushLanmuList()" type="success">保存</el-button>
          </div>
          <div class="tree body dweb">
            <el-tree
              :data="lanmu_tree"
              node-key="id"
              default-expand-all
              draggable
              :render-content="renderContent"
              @node-click="choosed_lanmu_articleList"
              style="border-radius: 5px"
            >
            </el-tree>
          </div>
          <div class="save-tree tree body dweb" style="float: left">
            <el-button @click="saveLanmuTree()" type="success" size="mini">保存结构</el-button>
            <el-button @click="getLanmuTree()" type="warning" size="mini">恢复结构</el-button>
            <el-button @click="getArticleList(1, 'all')" type="primary" size="mini"
              >全部文章</el-button
            >
            <el-button @click="getArticleList(1, 'nobelong')" type="primary" size="mini"
              >未知栏目</el-button
            >
          </div>
        </el-col>
        <el-col :span="18">
          <div class="body dweb">
            <h5>文章列表</h5>
          </div>
          <!-- 文章列表 -->
          <div class="dweb" style="margin-top: 10px; min-height: 45vh">
            <el-row v-loading="loading" element-loading-text="拼命加载中">
              <el-col v-show="!loading" :span="24">
                <div class="card dweb">
                  <span style="color:white">栏目名称：{{ this.currentLanmu | lanmuset }}</span>
                </div></el-col
              >
              <el-col :span="24" v-for="item in article_list" :key="item.id">
                <div class="card dweb">
                  <el-row>
                    <el-col :xs="24" :lg="6">
                      <el-image style="height: 80px" :src="item.cover" :fit="'cover'"></el-image>
                    </el-col>
                    <el-col class="text-item" :xs="24" :lg="4">
                      <span>{{ item.title }}</span>
                    </el-col>
                    <el-col class="text-item" :xs="12" :lg="7">
                      <span>发布者:{{ item.nickName }}</span>
                    </el-col>
                    <el-col class="text-item" :xs="12" :lg="7">
                      <el-popover placement="right" width="200" trigger="click">
                        <el-tree
                          :data="lanmu_tree"
                          node-key="id"
                          default-expand-all
                          @node-click="choosed_lanmu"
                        >
                        </el-tree>
                        <el-button
                          type="warning"
                          icon="el-icon-plus"
                          circle
                          slot="reference"
                        ></el-button>
                        <el-button size="mini" type="warning" @click="saveArticleToLanmu(item.id)"
                          >确定</el-button
                        >
                      </el-popover>
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
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import BreadMenu from '../components/BreadMenu.vue';
import axios from 'axios';
import Qs from 'qs';
export default {
  data() {
    return {
      loading: true,
      maxId: 0,
      currentPpage: 1,
      currentLanmu: 'nobelong',
      pageSize: 5,
      total: 100,
      article_list: [],

      // 新栏目名称

      new_lanmu_name: '',
      // 栏目结构数据
      lanmu_tree: [],
      // 文章栏目分配
      choosed_lanmu_id: 0,
      choosed_article_id: 0,
    };
  },
  components: {
    BreadMenu,
  },
  filters: {
    lanmuset: function(lanmu) {
      lanmu == 'all' ? (lanmu = '所有文章') : lanmu;
      lanmu == 'nobelong' ? (lanmu = '未知栏目') : lanmu;
      return lanmu;
    },
  },
  mounted() {
    this.getArticleList(this.currentPpage, this.currentLanmu);
    this.getLanmuTree();
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
    // 选择栏目查看文章
    choosed_lanmu_articleList(node) {
      let lanmu_name = node.label;
      this.getArticleList(1, lanmu_name);
    },
    // 选择文章保存栏目
    choosed_lanmu(node) {
      this.choosed_lanmu_id = node.id;
      this.choosed_lanmu_name = node.label;
    },
    saveArticleToLanmu(article_id) {
      axios({
        url: this.$store.state.baseurl + 'api/add-article/',
        method: 'PUT',
        data: Qs.stringify({
          token: this.$store.getters.loginState,
          lanmu_id: this.choosed_lanmu_id,
          article_id: article_id,
        }),
      }).then((res) => {
        if (res.data == 'nologin') {
          this.messageNotify('警告', '尚未登录!', 'warning');
          return;
        }
        if (res.data == 'noperm') {
          this.messageNotify('警告', '权限不足!', 'warning');
          return;
        }
        if (res.data == 'OK') {
          this.messageNotify('成功', '保存成功', 'success');
          this.getArticleList(1, this.choosed_lanmu_name);
          this.getLanmuTree();
        }
      });
    },
    // 获取栏目数据
    getLanmuTree() {
      axios({
        url: this.$store.state.baseurl + 'api/azrael-lanmu/',
        method: 'GET',
      }).then((res) => {
        this.lanmu_tree = res.data;
        // console.log(res.data);
      });
    },
    // 保存栏目结构
    saveLanmuTree() {
      axios({
        url: this.$store.state.baseurl + 'api/azrael-lanmu/',
        method: 'PUT',
        data: Qs.stringify({
          token: this.$store.getters.loginState,
          lanmu_tree: JSON.stringify(this.lanmu_tree),
        }),
      }).then((res) => {
        if (res.data == 'nologin') {
          this.messageNotify('警告', '尚未登录!', 'warning');
          return;
        }
        if (res.data == 'noperm') {
          this.messageNotify('警告', '权限不足!', 'warning');
          return;
        }
        if (res.data == 'OK') {
          this.messageNotify('成功', '保存成功', 'success');
          return;
        }
      });
    },
    // 新栏目名称
    pushLanmuList() {
      let checkTree = this.loopCheckData(this.lanmu_tree);
      let new_lanmu = {
        id: this.maxId + 1,
        label: this.new_lanmu_name,
        children: [],
      };
      if (this.new_lanmu_name == '') {
        this.messageNotify('警告', '栏目名称不能为空', 'warning');
      } else {
        if (checkTree === false) {
          this.new_lanmu_name = '';
          return;
        }
        this.lanmu_tree.push(new_lanmu);
        this.new_lanmu_name = '';
      }
    },
    loopCheckData(tree) {
      let checkTree = true;
      //检查新栏目数据
      tree.forEach((obj) => {
        if (obj.id > this.maxId) {
          this.maxId = obj.id;
        }
        if (obj.label === this.new_lanmu_name) {
          this.messageNotify('警告', '栏目名重复!', 'warning');
          checkTree = false;
          return checkTree;
        }
        if (obj.children) {
          if (obj.children.length > 0) {
            this.loopCheckData(obj.children);
          }
        }
      });
      return checkTree;
    },
    getArticleList(page, lanmu) {
      this.loading = true;
      axios({
        url: this.$store.state.baseurl + 'api/article-list/',
        method: 'GET',
        params: {
          page,
          currentname: this.$store.state.currentname,
          pageSize: this.pageSize,
          lanmu: lanmu,
        },
      }).then((res) => {
        this.article_list = res.data.data;
        this.total = res.data.total;
        this.loading = false;
        return;
      });
      this.currentLanmu = lanmu;
      return;
    },
    currentChange(val) {
      this.currentPpage = val;
      this.getArticleList(val, this.currentLanmu);
    },
    remove(node, data) {
      axios({
        url: this.$store.state.baseurl + 'api/azrael-lanmu/',
        method: 'DELETE',
        data: Qs.stringify({
          token: this.$store.getters.loginState,
          id: data.id,
        }),
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      }).then((res) => {
        if (res.data == 'nologin') {
          this.messageNotify('警告', '尚未登录!', 'warning');
          return;
        }
        if (res.data == 'noperm') {
          this.messageNotify('警告', '权限不足!', 'warning');
          return;
        }
        if (res.data == 'OK') {
          this.getLanmuTree();
          this.messageNotify('成功', '删除成功', 'success');
          return;
        }
      });
    },

    renderContent(h, { node, data, store }) {
      return (
        <span class="custom-tree-node">
          <span>{node.label}</span>
          <span> ({node.data.article_num})</span>
          <span>
            <el-button
              size="mini"
              type="text"
              style="position:absolute;right: 10px;"
              on-click={() => this.remove(node, data)}
            >
              删除
            </el-button>
          </span>
        </span>
      );
    },
  },
};
</script>

<style scoped>
.nav {
  margin-bottom: 10px;
}
.dweb {
  padding: 20px 10px;
}
.tree.body.dweb {
  /* padding: 20px;
   */
  margin-top: 10px;
}
.card.dweb .text-item {
  color: #fff;
  height: 80px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.text-item span {
  height: 40px;
  line-height: 20px;
  text-overflow: ellipsis;
  overflow: hidden;
}
.save-tree button {
  margin: 5px;
}
.body.dweb h5 {
  color: #fff;
  font-weight: 500;
}
</style>
