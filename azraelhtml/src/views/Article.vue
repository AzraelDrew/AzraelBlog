<template>
  <div id="article">
    <!-- 导航 -->
    <BreadMenu
      :page_name="article_data.title"
      :lanmu="article_data.lanmu"
    ></BreadMenu>
    <!-- 文章内容 -->
    <el-row :gutter="10">
      <el-col :xs="24" :lg="16">
        <div class="body dweb">
          <div class="header">
            {{ article_data.title }}
          </div>
        </div>
        <div class="body dweb">
          <div class="describe">
            {{ article_data.describe }}
          </div>
        </div>
        <div class="body dweb">
          <div class="article-content" v-html="article_data.content"></div>
        </div>
        <div class="clear"></div>
        <div class="body dweb">
          <el-button
            v-if="article_data.pre_id == 0"
            @click="toOtherPage(article_data.pre_id)"
            type="info"
            >上一页</el-button
          >
          <el-button
            v-else
            @click="toOtherPage(article_data.pre_id)"
            type="success"
            >上一页</el-button
          >
          <el-button
            v-if="article_data.next_id == 0"
            @click="toOtherPage(article_data.next_id)"
            type="info"
            >下一页</el-button
          >
          <el-button
            v-else
            @click="toOtherPage(article_data.next_id)"
            type="success"
            >下一页</el-button
          >
        </div>
      </el-col>
      <el-col :xs="24" :lg="8">
        <div class="body dweb">
          <el-image :src="article_data.cover" :fit="'cover'"></el-image>
        </div>
        <!-- 点赞收藏打赏 -->
        <div class="body dweb like-btn">
          <el-row>
            <el-col :span="8">
              <i class="iconfont icondianzan1"></i>
              <!-- <i class="iconfont icondianzan1" style="color: #a85652"></i> -->
            </el-col>
            <el-col :span="8">
              <i class="iconfont iconshoucang"></i>
              <!-- <i class="iconfont iconshoucang" style="color: #f5c328"></i> -->
            </el-col>
            <el-col :span="8">
              <i class="iconfont icondashang"></i>
              <!-- <i class="iconfont icondashang" style="color: #f5c328"></i> -->
            </el-col>
          </el-row>
        </div>
        <div class="body dweb">
          <div class="body dweb pinglun-item">
            admin 说：<br />
            hahahahahaah
          </div>
          <div class="body dweb pinglun-item">
            admin 说：<br />
            hahahahahaah
          </div>
          <div class="body dweb pinglun-item">
            a admin 说：<br />
            hahahahahaah
          </div>
          <div class="body dweb pinglun-item">
            admin 说：<br />
            hahahahahaah
          </div>
          <div class="body dweb pinglun-item">
            admin 说：<br />
            hahahahahaah
          </div>
          <div class="body dweb pinglun-item">
            admin 说：<br />
            hahahahahaah
          </div>
          <div class="body dweb pinglun-item">
            admin 说：<br />
            hahahahahaah
          </div>
        </div>
        <div class="dweb">
          <!-- 分页器 -->
          <el-pagination
            background
            small
            :pager-count="11"
            layout="prev, pager, next"
            :total="ping_lun_total"
            :page-size="ping_lun_pageSize"
            @current-change="pingluncurrentChange"
          >
          </el-pagination>
        </div>
        <div class="body dweb">
          <el-input
            type="textarea"
            :rows="2"
            placeholder="请输入内容"
            v-model="new_pinglun"
            :maxlength="100"
          >
          </el-input>
          <el-button type="success">发表评论</el-button>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import BreadMenu from "../components/BreadMenu.vue";
import axios from "axios";
import Qs from "qs";
export default {
  data() {
    return {
      article_id: this.$route.query.id,
      article_data: {},
      // 评论
      new_pinglun: "",
      ping_lun_total: 100,
      ping_lun_pageSize: 5,
    };
  },
  components: { BreadMenu },
  watch: {
    $route(to) {
      this.getArticleData(to.query.id);
    },
  },
  mounted() {
    this.getArticleData(this.article_id);
  },
  methods: {
    // 评论翻页
    pingluncurrentChange(page) {
      console.log(page);
    },
    // 跳转文章
    toOtherPage(id) {
      if (id === 0) {
        alert("没有了");
        return;
      }
      this.$router.push({ path: "/article", query: { id: id } });
    },
    getArticleData(id) {
      // console.log(id);
      axios({
        url: "http://localhost:9000/api/atricle-data/",
        method: "GET",
        params: {
          article_id: id,
        },
      }).then((res) => {
        // console.log(res.data);
        this.article_data = res.data;
      });
    },
  },
};
</script>

<style scoped>
.body.dweb {
  padding: 10px;
  /* color: #fff; */
}

.body.dweb .describe {
  text-align: center;
  color: #fff;
  font-size: 12px;
  background: none;
}
#article .dweb {
  margin-bottom: 10px;
}
#article .dweb:last-child {
  margin-bottom: 0;
}
.like-btn {
  text-align: center;
  color: #009186;
}
.like-btn i {
  font-size: 30px;
  cursor: pointer;
}
.pinglun-item {
  color: #fff;
  font-size: 18px;
}
</style>
