<template>
  <div id="article">
    <!-- 导航 -->
    <BreadMenu :page_name="article_data.title" :lanmu="article_data.lanmu"></BreadMenu>
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
          <!-- <div class="article-content" v-html="article_data.content"></div> -->
          <!-- markdown渲染 -->
          <v-md-preview :text="article_data.content" @image-click="click_image()"></v-md-preview>
        </div>
        <div class="clear"></div>
        <div class="body dweb">
          <el-button
            v-if="article_data.pre_id == 0"
            @click="toOtherPage(article_data.pre_id)"
            type="info"
            >上一页</el-button
          >
          <el-button v-else @click="toOtherPage(article_data.pre_id)" type="success"
            >上一页</el-button
          >
          <el-button
            v-if="article_data.next_id == 0"
            @click="toOtherPage(article_data.next_id)"
            type="info"
            >下一页</el-button
          >
          <el-button v-else @click="toOtherPage(article_data.next_id)" type="success"
            >下一页</el-button
          >
        </div>
      </el-col>
      <el-col :xs="24" :lg="8">
        <div class="body dweb">
          <el-image :src="article_data.cover" :fit="'cover'"></el-image>
        </div>
        <div class="body dweb">
          <el-calendar v-model="value"> </el-calendar>
        </div>
        <!-- 点赞收藏打赏 -->
        <div class="body dweb like-btn">
          <el-row>
            <el-col :span="12">
              <i
                v-if="user_article_info.like"
                class="iconfont icondianzan1"
                style="color: #a85652"
                @click="toLike()"
              ></i>
              <i v-else @click="toLike()" class="iconfont icondianzan1"></i>
            </el-col>
            <el-col :span="12">
              <i
                v-if="user_article_info.favor"
                class="iconfont iconshoucang"
                style="color: #f5c328"
                @click="toFavor()"
              ></i>
              <i v-else @click="toFavor()" class="iconfont iconshoucang"></i>
            </el-col>
          </el-row>
        </div>
        <div v-if="show_ping_lun" class="body dweb">
          <div v-for="(item, index) in pinglun_data" :key="index" class="body dweb pinglun-item">
            {{ item.nickName }}说:<br />
            {{ item.text }}
          </div>
        </div>
        <div v-if="show_ping_lun" class="dweb">
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
        <div class="body dweb  flex" @keyup.ctrl.enter="saveNewPinglun()">
          <el-input
            type="textarea"
            :rows="2"
            placeholder="请输入内容"
            v-model="new_pinglun"
            :maxlength="120"
          >
          </el-input>
          <el-button @click="saveNewPinglun()" type="success">发表评论</el-button>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import BreadMenu from '../components/BreadMenu.vue';
import axios from 'axios';
import Qs from 'qs';
// import key from 'keymaster';

export default {
  data() {
    return {
      show_ping_lun: false,
      current_page: 1,
      value: new Date(),
      article_id: this.$route.query.id,
      article_data: {},
      // 评论
      new_pinglun: '',
      ping_lun_total: 100,
      ping_lun_pageSize: 5,
      pinglun_data: [],
      user_article_info: {},
    };
  },
  components: { BreadMenu },
  watch: {
    $route(to) {
      this.article_id = to.query.id;
      this.getArticleData(to.query.id);
      this.getAllPinglun(1, this.ping_lun_pageSize);
      this.getUserArticleInfo();
    },
  },
  mounted() {
    this.getArticleData(this.article_id);
    this.getAllPinglun(1, this.ping_lun_pageSize);
    this.getUserArticleInfo();
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

    click_image(images, currentIndex) {
      console.log(images, currentIndex);
    },
    // 打赏
    //点赞
    toLike() {
      axios({
        url: this.$store.state.baseurl + 'api/article-like/',
        method: 'post',
        data: Qs.stringify({
          token: this.$store.getters.loginState,
          article_id: this.article_id,
        }),
      }).then((res) => {
        if (res.data == 'nologin') {
          this.messageNotify('警告', '尚未登录!', 'warning');
          return;
        }
        if (res.data == 'ok') {
          this.getUserArticleInfo();
        }
      });
    },
    //收藏
    toFavor() {
      axios({
        url: this.$store.state.baseurl + 'api/article-favor/',
        method: 'post',
        data: Qs.stringify({
          token: this.$store.getters.loginState,
          article_id: this.article_id,
        }),
      }).then((res) => {
        if (res.data == 'nologin') {
          this.messageNotify('警告', '尚未登录!', 'warning');
          return;
        }
        if (res.data == 'ok') {
          this.getUserArticleInfo();
        }
      });
    },
    // 获取收藏等信息
    getUserArticleInfo() {
      let token = this.$store.getters.loginState;
      if (token) {
        axios({
          url: this.$store.state.baseurl + 'api/user-article-info/',
          method: 'POST',
          data: Qs.stringify({
            token: token,
            article_id: this.article_id,
          }),
        }).then((res) => {
          this.user_article_info = res.data;
        });
      }
    },
    // 获取所以评论
    getAllPinglun(page, pagesize) {
      axios({
        url: this.$store.state.baseurl + 'api/pinglun/',
        method: 'GET',
        params: {
          page,
          pagesize,
          article_id: this.article_id,
        },
      }).then((res) => {
        console.log('asdfasd', res.data);
        if (res.data.total) {
          this.show_ping_lun = true;
        }
        this.pinglun_data = res.data.data;
        this.ping_lun_total = res.data.total;
      });
    },
    // 发表评论
    saveNewPinglun() {
      if (this.new_pinglun.length == '') {
        this.messageNotify('警告', '评论内容不能为空!', 'warning');
        return;
      }
      axios({
        url: this.$store.state.baseurl + 'api/pinglun/',
        method: 'POST',
        data: Qs.stringify({
          token: this.$store.getters.loginState,
          article_id: this.article_id,
          text: this.new_pinglun,
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
        this.getAllPinglun(this.current_page, this.ping_lun_pageSize);
        this.new_pinglun = '';
      });
    },
    // 评论翻页
    pingluncurrentChange(page) {
      this.current_page = page;
      this.getAllPinglun(page, this.ping_lun_pageSize);
    },
    // 跳转文章
    toOtherPage(id) {
      if (id === 0) {
        this.messageNotify('警告', '没有了!', 'warning');
        return;
      }
      this.$router.push({ path: '/article', query: { id: id } });
    },
    getArticleData(id) {
      axios({
        url: this.$store.state.baseurl + 'api/article-data/',
        method: 'GET',
        params: {
          article_id: id,
        },
      }).then((res) => {
        this.article_data = res.data;
      });
    },
  },
};
</script>

<style scoped lang="scss">
.flex {
  display: flex;
  justify-content: center;
}
#article .dweb {
  margin-bottom: 10px;
}
.body.dweb {
  padding: 10px;
  /* color: #fff; */
  .describe {
    text-align: center;
    color: #fff;
    font-size: 12px;
    background: none;
  }
  &:last-child {
    margin-bottom: 0;
  }
}
.like-btn {
  text-align: center;
  color: #009186;
  i {
    font-size: 30px;
    cursor: pointer;
  }
}
.pinglun-item {
  color: #fff;
  font-size: 18px;
}
</style>
