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
        :autofocus="true"
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
import { ref } from 'vue';
import { ElNotification } from 'element-plus';
import { useRouter } from 'vue-router';
import TheButton from '@/components/TheButton.vue';
import useAxios from '../composables/useAxios';
import { useUserStore } from '@/stores/user';
const markDownText = `::: tip
  你可以点击 toolbar 中的 tip 来快速插入
:::

::: warning
  这是一段警告
:::

::: danger
  这是一个危险警告
:::

::: details
  这是一个详情块，在 IE / Edge 中不生效
:::

::: tip 自定义标题
  你也可以自定义块中的标题
:::

::: danger STOP
  危险区域，禁止通行
:::

`;
const router = useRouter();
const userstore = useUserStore();
const axios = useAxios();
const text = ref(markDownText);
const title = ref('');
const desc = ref('');

function hendleCanel() {
  router.push({ name: 'Home' });
}

async function hendleSubmit() {
  let data = new FormData();
  data.append('token', userstore.userInfo.token);
  data.append('title', title.value);
  data.append('describe', desc.value);
  data.append('content', text.value);
  data.append('cover', '');
  let res = await axios.post('api/add/article/', data);
  console.log(res);
  router.push({ name: 'Home' });
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
