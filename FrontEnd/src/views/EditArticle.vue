<template>
  <transition name="fade" appear>
    <div class="container">
      <div class="flex flexJustifySpaceBetween">
        <el-input v-model="title" class="input" placeholder="标题..." />

        <el-input v-model="desc" class="input" placeholder="描述..." />
      </div>
      <v-md-editor
        class="md"
        left-toolbar="undo redo clear | h bold italic strikethrough quote | emoji todo-list | ul ol table hr | link image code | save"
        v-model="text"
        height="70vh"
      ></v-md-editor>
      <div class="flex flexJustifyEnd cancelPost">
        <TheButton text="取消" @click="hendleCanel" class="button cancelButton" />
        <TheButton text="发布" @click="hendleSubmit" class="button" />
      </div>
    </div>
  </transition>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import { ElNotification } from 'element-plus';
import { useRouter, useRoute } from 'vue-router';
import TheButton from '@/components/TheButton.vue';
import useAxios from '../composables/useAxios';
import { useUserStore } from '@/stores/user';

const router = useRouter();
const route = useRoute();
const userstore = useUserStore();
const axios = useAxios();
const text = ref('');
const title = ref('');
const desc = ref('');

onMounted(async () => {
  console.log(route.params);
  console.log(router.currentRoute.value);
  console.log(route.params);
  let res = await axios({
    url: 'api/article/?' + 'id=' + route.params.id + '&userId=' + userstore.userInfo.id,
    method: 'GET',
  });
  let result = res.data;
  console.log('article', result);
  title.value = result.title;
  text.value = result.content;
  desc.value = result.ddescribe;
});

function hendleCanel() {
  router.push({ name: 'ViewArticle', params: { id: route.params.id } });
}
async function hendleSubmit() {
  console.log(route.params.id);
  let data = new FormData();
  data.append('articleId', route.params.id as string);
  data.append('token', userstore.userInfo.token);
  data.append('title', title.value);
  data.append('describe', desc.value);
  data.append('content', text.value);
  data.append('content', text.value);
  let res = await axios.post('api/upadte/article/', data);
  console.log(res);
  router.push({ name: 'ViewArticle', params: { id: route.params.id } });
}
</script>
<style scoped>
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
  background-color: white;
  box-shadow: rgb(0 0 0 / 5%) 0 0 8px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  font-size: 15px;
  transition: all 0.5s ease;
}

button:hover {
  letter-spacing: 3px;
  background-color: hsl(261deg 80% 48%);
  color: hsl(0, 0%, 100%);
  box-shadow: rgb(93 24 220) 0px 7px 29px 0px;
}
</style>
