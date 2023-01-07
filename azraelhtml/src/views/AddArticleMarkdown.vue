<template>
  <div id="add-article">
    <el-row :gutter="10">
      <el-col :xs="24" :lg="8">
        <div class="dweb">
          <el-form :label-position="'left'" label-width="80px" :model="article_info">
            <el-form-item label="文章标题">
              <el-input v-model="article_info.title"></el-input>
            </el-form-item>
            <el-form-item label="描述">
              <el-input type="textarea" :rows="4" v-model="article_info.describe"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </el-col>

      <el-col :xs="24" :lg="16">
        <!-- <el-button id="add_article" @click="submitArticle" type="success" round
          >保存文章</el-button
        > -->
        <div class="dweb">
          <div v-for="(img, i) in cover_list" :key="i">
            <el-image
              v-if="img === cover_img"
              class="cover"
              style="width: 150px; height: 150px; border-radius: 10px"
              :src="img"
              :fit="'cover'"
              @click="chooseCover(img)"
            ></el-image>

            <el-image
              v-else
              style="width: 150px; height: 150px; border-radius: 10px"
              :src="img"
              :fit="'cover'"
              @click="chooseCover(img)"
            ></el-image>
          </div>
          <el-button id="add_article" @click="submitArticle" type="success" round
            >保存文章</el-button
          >
          <el-button id="edit_switch" type="success" @click="switch_edit" round
            >使用富文本编辑器</el-button
          >
        </div>
      </el-col>
      <el-col :xs="24" :lg="24">
        <!-- markdown编辑器 -->
        <v-md-editor
          v-model="article_info.contents"
          left-toolbar="undo redo clear | h bold italic strikethrough quote | ul ol table hr | link image code | tip | save"
          height="55vh"
          :disabled-menus="[]"
          @upload-image="handleUploadImage"
          :autofocus="true"
          :tab-size="2"
        ></v-md-editor>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import axios from 'axios';
import Qs from 'qs';
import router from '../router';

const text = ``;
export default {
  data() {
    return {
      article_info: {
        title: '',
        describe: '',
        contents: text, //编辑区内容
      },
      cover_img: '',
      cover_list: [],
      screenHeight: document.body.clientHeight,
      screenWidth: document.body.clientWidth,
    };
  },
  mounted() {
    // this.summernote();
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
    // 切换编辑器
    switch_edit() {
      router.push({ name: 'AddArticleText' });
    },
    //markdown本地上传
    handleUploadImage(event, insertImage, files) {
      let self = this;
      // 拿到 files 之后上传到文件服务器，然后向编辑框中插入对应的内容
      let img = files[0];
      let imgData = new FileReader();
      imgData.readAsDataURL(img);
      imgData.onload = () => {
        //插入图片
        let imgnode = document.createElement('img');
        imgnode.src = imgData.result;
        // 推入封面待选择
        // self.cover_list.push(imgData.result);
        let src = {
          imgnode: imgnode.src,
        };
        console.log(imgData.result);
        // 讲图片存储在后端并返回对应都url
        axios.post(this.$store.state.baseurl + 'api/save-img/', Qs.stringify(src)).then((res) => {
          console.log(res.data);
          self.cover_list.push(res.data.url);
          insertImage({
            url: res.data.url,
            desc: '在这里插入图片描述',
          });
        });
      };
    },

    // 选择封面
    chooseCover(img) {
      this.cover_img = img;
    },
    // 提交文章
    submitArticle() {
      let article_data = {
        title: this.article_info.title,
        describe: this.article_info.describe,
        content: this.article_info.contents,
        cover: this.cover_img,
        token: this.$store.getters.loginState,
      };
      axios
        .post(this.$store.state.baseurl + 'api/add-article/', Qs.stringify(article_data))
        //article_data作为第二个参数时是body请求
        .then((res) => {
          console.log(res.data);
          if (res.data === 'notitle') {
            this.messageNotify('警告', '文章标题不可为空!', 'warning');
            return;
          }
          if (res.data === 'nologin') {
            this.messageNotify('警告', '用户信息错误!', 'warning');
            return;
          }
          if (res.data === 'OK') {
            this.messageNotify('成功', '发布成功', 'success');
            router.push({ name: 'LanmuAdmin' });
            this.$emit();
            return;
          }
        });
    },
  },
};
</script>

<style scoped lang="scss">
/* 使用scoped只会作用于当前组件 */
.dweb {
  min-height: 200px;
  padding: 20px 0;
  display: flex;
  justify-content: center;
  align-items: center;
  .el-button {
    position: fixed;
    right: 20px;
    margin-top: 260px;
    z-index: 1001;
  }
  .el-image.cover {
    border: 3px solid #ffcd77;
  }
  .el-image:hover {
    border: 3px solid #ffcd77;
  }
}
#summernote_area {
  padding: 0;
}
.el-form-item {
  margin-top: 20px;
}

.v-md-editor__preview-wrapper blockquote {
  border-left: 0.25em solid #42b98310 !important;
  p {
    color: #55efc490 !important;
  }
}
.v-md-editor-preview h1,
.v-md-editor-preview h2 {
  border-bottom: 1px solid #b2bec3 !important;
}
</style>
