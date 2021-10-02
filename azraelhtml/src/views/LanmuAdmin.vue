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
            <el-input
              v-model="new_lanmu_name"
              placeholder="请输入新栏目名称"
            ></el-input>
            <el-button @click="pushLanmuList()" type="success">保存</el-button>
          </div>
          <div class="tree body dweb">
            <el-tree
              :data="lanmu_tree"
              node-key="id"
              default-expand-all
              draggable
            >
            </el-tree>
          </div>
          <div class="save-tree tree body dweb" style="float: left">
            <el-button type="warning" size="mini">恢复结构</el-button>
            <el-button @click="saveLanmuTree()" type="success" size="mini"
              >保存结构</el-button
            >
            <el-button type="primary" size="mini">全部文章</el-button>
          </div>
        </el-col>
        <el-col :span="18">
          <div class="body dweb">
            <h5>文章列表</h5>
          </div>
          <!-- 文章列表 -->
          <div class="dweb" style="margin-top: 10px; min-height: 780px">
            <el-row>
              <el-col :span="24" v-for="item in article_list" :key="item.id">
                <div class="card dweb">
                  <el-row>
                    <el-col :xs="24" :lg="6">
                      <el-image
                        style="height: 80px"
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
                        type="warning"
                        icon="el-icon-plus"
                        circle
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
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import BreadMenu from "../components/BreadMenu.vue";
import axios from "axios";
import Qs from "qs";
export default {
  data() {
    return {
      maxId: 0,
      currentPpage: 1,
      pageSize: 5,
      total: 100,
      article_list: [],

      // 新栏目名称

      new_lanmu_name: "",
      // 栏目结构数据
      lanmu_tree: [
        {
          id: 1,
          label: "一级 1",
          children: [
            {
              id: 4,
              label: "二级 1-1",
              children: [
                {
                  id: 9,
                  label: "三级 1-1-1",
                },
                {
                  id: 10,
                  label: "三级 1-1-2",
                },
              ],
            },
          ],
        },
        {
          id: 2,
          label: "一级 2",
          children: [
            {
              id: 5,
              label: "二级 2-1",
            },
            {
              id: 6,
              label: "二级 2-2",
            },
          ],
        },
        {
          id: 3,
          label: "一级 3",
          children: [
            {
              id: 7,
              label: "二级 3-1",
            },
            {
              id: 8,
              label: "二级 3-2",
              children: [
                {
                  id: 11,
                  label: "三级 3-2-1",
                },
                {
                  id: 12,
                  label: "三级 3-2-2",
                },
                {
                  id: 13,
                  label: "三级 3-2-3",
                },
              ],
            },
          ],
        },
      ],
    };
  },
  components: {
    BreadMenu,
  },
  mounted() {
    this.getArticleList(this.currentPpage, this.pageSize, this.total);
  },
  methods: {
    // 保存栏目结构
    saveLanmuTree() {
      // console.log(this.lanmu_tree);
      axios({
        url: "http://localhost:9000/api/azrael-lanmu/",
        method: "PUT",
        data: Qs.stringify({
          token: this.$store.getters.loginState,
          lanmu_tree: JSON.stringify(this.lanmu_tree),
        }),
      }).then((res) => {
        console.log(res.data);
        if (res.data == "nologin") {
          alert("尚未登录");
          return;
        }
        if (res.data == "noperm") {
          alert("权限不足");
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
      if (checkTree === false) {
        this.new_lanmu_name = "";
        return;
      }
      this.lanmu_tree.push(new_lanmu);
      this.new_lanmu_name = "";
    },
    loopCheckData(tree) {
      let checkTree = true;
      //检查新栏目数据
      tree.forEach((obj) => {
        if (obj.id > this.maxId) {
          this.maxId = obj.id;
        }
        if (obj.label === this.new_lanmu_name) {
          alert("栏目名重复");
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
</style>
