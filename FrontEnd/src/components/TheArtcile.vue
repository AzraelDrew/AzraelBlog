<template>
  <div class="articleList">
    <h1 class="flex">最新博客</h1>
    <div class="flex">
      <TheIcon
        v-for="(tab, index) in tabs"
        :icon="tab.icon"
        :size="30"
        :class="{ active: index === userstore.index }"
        @click="userstore.ChangeIndex(index)"
      />
    </div>
    <div class="flexDirectionRow">
      <transition name="fade">
        <component
          :is="tabs[userstore.index].component"
          :number="7"
          :posts="allArticle"
        ></component>
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
import { ElNotification } from 'element-plus';
import { useUserStore } from '@/stores/user';
import useAxios from '../composables/useAxios';
import TheArtcileGrid from './TheArtcileGrid.vue';
import TheArtcileList from './TheArtcileList.vue';
import TheIcon from './TheIcon.vue';
import TheButton from './TheButton.vue';
const props = defineProps(['search']);
const axios = useAxios();
const userstore = useUserStore();

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
watch(props, async (newval) => {
  console.log(newval.search);
  let res = await axios({
    url:
      '/api/all/article/' +
      '?page=' +
      1 +
      '&pageSize=' +
      pageSize.value +
      '&userId=' +
      userstore.userInfo.id +
      '&search=' +
      newval.search,
    method: 'GET',
  });
  allArticle.value = res.data.data;
});
watch(currentPage, async (newval, oldval) => {
  let res = await AllArticle(newval, pageSize.value, userstore.userInfo.id);
  allArticle.value = res.data.data;
});
watch(userstore.userInfo, async (newval, oldval) => {
  let res = await AllArticle(currentPage.value, pageSize.value, userstore.userInfo.id);
  allArticle.value = res.data.data;
});

async function CurrentPage(page: number) {
  if (page < 1) {
    ElNotification({
      title: 'Warning',
      message: '没有了',
      type: 'warning',
    });
  } else if (page > Math.ceil(totalPage.value / pageSize.value)) {
    ElNotification({
      title: 'Warning',
      message: '没有了',
      type: 'warning',
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
  allArticle.value = res.data.data;
});
async function AllArticle(page: 1 | number, pageSize: number, userId?: number | string) {
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
