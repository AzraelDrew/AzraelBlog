<template>
  <div id="add-atricle">
    <el-row :gutter="10">
      <el-col :xs="24" :lg="8">
        <div class="dweb">
          <el-form
            :label-position="'left'"
            label-width="80px"
            :model="article_info"
          >
            <el-form-item label="文章标题">
              <el-input v-model="article_info.title"></el-input>
            </el-form-item>
            <el-form-item label="描述">
              <el-input
                type="textarea"
                :rows="4"
                v-model="article_info.describe"
              ></el-input>
            </el-form-item>
          </el-form>
        </div>
      </el-col>
      <el-col :xs="24" :lg="16">
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
          <el-button @click="submitArticle" type="success" round
            >保存文章</el-button
          >
        </div>
      </el-col>
      <el-col :xs="24" :lg="24">
        <div class="dweb" id="summernote_area">
          <div id="summernote"></div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>


<script>
import $ from "jquery";
import axios from "axios";
import Qs from "qs";
export default {
  data() {
    return {
      article_info: {
        title: "",
        describe: "",
        contents: "",
      },
      cover_img: "",
      cover_list: [],
    };
  },
  mounted() {
    this.summernote();
  },
  methods: {
    summernote() {
      let self = this;
      $("#summernote").summernote({
        width: "100%",
        lang: "zh-CN",
        height: 500,
        callbacks: {
          // 输入时
          onChange(contents) {
            self.article_info.contents = contents;
          },
          // 本地图片上传
          onImageUpload(files) {
            let img = files[0];
            let imgData = new FileReader();
            imgData.readAsDataURL(img);
            imgData.onload = () => {
              //插入图片
              let imgnode = document.createElement("img");
              imgnode.src = imgData.result;
              $("#summernote").summernote("insertNode", imgnode);

              // 推入封面待选择
              self.cover_list.push(imgData.result);
            };
          },

          // 远程图片添加
          onImageLinkInsert(url) {
            let imgnode = document.createElement("img");
            imgnode.src = url;
            $("#summernote").summernote("insertNode", imgnode);
            self.cover_list.push(url);
          },
          onMediaDelete(target) {
            let imgData = target[0].src;
            for (let i = 0; self.cover_list.length; i++) {
              if (self.cover_list[i] === imgData) {
                self.cover_list.splice(i, 1);
              }
            }
          },
        },
      });
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
        .post(
          "http://139.224.209.63/api/add-article/",
          Qs.stringify(article_data)
        )
        //article_data作为第二个参数时是body请求
        .then((res) => {
          if (res.data === "title") {
            alert("文章标题不可为空");
            return;
          }
          if (res.data === "nologin") {
            alert("用户信息错误");
            return;
          }
          if (res.data === "OK") {
            window.location.reload();
          }
        });
    },
  },
};
</script>

<style scoped>
/* 使用scoped只会作用于当前组件 */
.dweb {
  min-height: 200px;
  padding: 20px 0;
  display: flex;
  justify-content: center;
  align-items: center;
}
.dweb .el-image:hover {
  border: 3px solid #ffcd77;
}
.dweb .el-image.cover {
  border: 3px solid #ffcd77;
}
#summernote_area {
  padding: 0;
}
.el-form-item {
  /* padding-top: 20px; */
  margin-top: 20px;
}
.dweb .el-button {
  position: fixed;
  right: 20px;
  /* top: 180px;*/
  margin-top: 260px;
  z-index: 1001;
}
</style>
