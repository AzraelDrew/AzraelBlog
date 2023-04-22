<template>
  <transition name="fade" appear>
    <div class="container editArticle">
      <div v-show="!isFullscreen" class="flex flexJustifySpaceBetween">
        <el-input v-model="title" class="input" placeholder="标题..." />

        <el-input v-model="desc" class="input" placeholder="描述..." />
      </div>
      <v-md-editor
        class="md"
        left-toolbar="undo redo clear | h bold italic strikethrough quote | emoji todo-list | ul ol table hr | link image code | save"
        v-model="text"
        :autofocus="true"
        @fullscreen-change="ChangeFullscreen"
        :disabled-menus="[]"
        @upload-image="handleUploadImage"
        height="76vh"
      ></v-md-editor>
      <div v-show="!isFullscreen" class="flex flexJustifyEnd cancelPost">
        <TheButton text="取消" @click="hendleCanel" class="button cancelButton" />
        <TheButton text="发布" @click="hendleSubmit" class="button" />
      </div>
    </div>
  </transition>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { ElNotification } from 'element-plus';
import { useRouter, useRoute } from 'vue-router';
import { useUserStore } from '@/stores/user';
import useAxios from '../composables/useAxios';
import TheButton from '@/components/TheButton.vue';
const markDownText = `
## 基础语法

# 一级标题
## 二级标题

- 无序列表1
- 无序列表2

1. 有序列表1
2. 有序列表2

> 这是一段引用

[baidu](https://www.baidu.com)这是一个链接

![这是一个图片](https://w.wallhaven.cc/full/zy/wallhaven-zyz25o.jpg)

`;
const router = useRouter();
const route = useRoute();
const userstore = useUserStore();
const axios = useAxios();
const text = ref(markDownText);
const title = ref('');
const desc = ref('');
const isFullscreen = ref(false);

function handleUploadImage(event: any, insertImage: any, files: any) {
  let img = files[0];
  let formData = new FormData();
  formData.append('imgnode', img);
  axios.post('api/article/img/', formData).then((res) => {
    insertImage({
      url: res.data.url,
      desc: '在这里插入图片描述',
    });
  });
}

function ChangeFullscreen() {
  isFullscreen.value = !isFullscreen.value;
}
function hendleCanel() {
  router.push({ name: 'Home' });
}

async function hendleSubmit() {
  if(title.value.length<1){
    ElNotification({
    title: 'Warning',
    message: '标题不能为空',
    type: 'warning',
  });
  return;
}
if(text.value.length<1){
  ElNotification({
  title: 'Warning',
  message: '文章不能为空',
  type: 'warning',
});
return;
}
  let data = new FormData();
  data.append('token', userstore.userInfo.token);
  data.append('title', title.value);
  data.append('describe', desc.value);
  data.append('content', text.value);
  data.append('cover', '');
  let res = await axios.post('api/add/article/', data);
  ElNotification({
    title: 'Success',
    message: '发布成功',
    type: 'success',
  });
  router.push({ name: 'ViewArticle', params: { id: res.data.id } });
}
</script>
<style scoped lang="scss">
.container {
  margin: 0 100px;
  border-radius: 20px;
  margin-bottom: -60px;
}

.input {
  margin: 20px 0;
  height: 50px;
  width: 40vw;
}
.md {
  border-radius: 40px;
  box-shadow: 50px 0px 20px #d3d3d3, -50px 0px 20px #d3d3d3;
}
.cancelPost {
  margin-top: 20px;
}
.button {
  margin: 0 20px;
}

button {
  padding: 17px 40px;
  border-radius: 50px;
  border: 0;
  box-shadow: rgb(0 0 0 / 5%) 0 0 8px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  font-size: 15px;
  transition: all 0.5s ease;
  &:hover {
  letter-spacing: 3px;
  background-color: hsl(261deg 80% 48%);
  color: hsl(0, 0%, 100%);
  box-shadow: rgb(93 24 220) 0px 7px 29px 0px;
}
}


</style>
