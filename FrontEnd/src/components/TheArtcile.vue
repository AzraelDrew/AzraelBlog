<template>
  <div class="articleList">
    <h1 class="flex">最新博客</h1>
    <div class="flex">
      <TheIcon
        v-for="(tab, index) in tabs"
        :icon="tab.icon"
        :size="30"
        :class="{ active: index === currentTab }"
        @click="currentTab = index"
      />
    </div>
    <div class="flexDirectionRow">
      <transition name="fade">
        <component :is="tabs[currentTab].component" :number="7" :posts="allArticle"></component>
      </transition>
      <div class="flex flexJustifySpaceBetween preAndNext">
        <TheButton text="上一页" @click="CurrentPage(currentPage - 1)" />
        <TheButton text="下一页" @click="CurrentPage(currentPage + 1)" />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, watch, shallowRef, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { ElNotification } from 'element-plus';
import TheArtcileGrid from './TheArtcileGrid.vue';
import TheArtcileList from './TheArtcileList.vue';
import TheIcon from './TheIcon.vue';
import TheButton from './TheButton.vue';
import { useUserStore } from '@/stores/user';
import useAxios from '../composables/useAxios';
const axios = useAxios();
const userstore = useUserStore();

const currentTab = ref(0);

const totalPage = ref<number>(0);
const currentPage = ref(1);
const pageSize = ref(6);
const allArticle = ref([]);
const tabs = ref([
  {
    icon: 'icongrid',
    component: shallowRef(TheArtcileGrid),
  },
  {
    icon: 'iconunorderedlist',
    component: shallowRef(TheArtcileList),
  },
]);
watch(currentPage, async (newval, oldval) => {
  let res = await AllArticle(newval, pageSize.value, userstore.userInfo.id);
  console.log(res.data.data);
  allArticle.value = res.data.data;
});

async function CurrentPage(page: number) {
  if (page < 1) {
    ElNotification({
      title: 'Success',
      message: '没有了',
      type: 'success',
    });
  } else if (page > Math.ceil(totalPage.value / pageSize.value)) {
    ElNotification({
      title: 'Success',
      message: '没有了',
      type: 'success',
    });
  } else {
    currentPage.value = page;
  }
}
onMounted(async () => {
  let res = await AllArticle(
    currentPage.value,
    pageSize.value,
    userstore.userInfo.id ? userstore.userInfo.id : 0
  );
  totalPage.value = res.data.total;
  console.log(res);
  allArticle.value = res.data.data;
});
async function AllArticle(page: number, pageSize: number, userId?: number | string) {
  let res = await axios({
    url: '/api/all/article/' + '?page=' + page + '&pageSize=' + pageSize + '&userId=' + userId,
    method: 'GET',
  });

  return res;
}
</script>

<style scoped>
.active {
  color: #0984e3;
}
.preAndNext {
  margin: 0 20vw;
  min-width: 60vw;
}
</style>
