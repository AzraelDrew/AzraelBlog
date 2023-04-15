<template>
  <div class="flex flexWarp flexDirectionColumn">
    <div class="article" v-for="post in posts" :key="post.id">
      <div style="margin-left: 40px">
        <h2>{{ post.title }}</h2>
        <div class="flex flexJustifyStart">
          <TheAvatar class="avatar" :size="40" :src="post.userAvatar" />

          <span style="display: flex; align-content: center">{{ post.belonguser }}</span>
        </div>
        <p>发布于:{{ post.date.split('T')[0] }}</p>
      </div>

      <div class="md">
        <v-md-preview
          :text="post.content.substring(0, 400)"
          :default-show-toc="true"
          @copy-code-success="handleCopyCodeSuccess"
        ></v-md-preview>
      </div>
      <div class="iconButton flex flexWarp flexJustifySpaceBetween">
        <div class="flex flexJustifySpaceBetween">
          <TheIcon icon="iconview" :size="30" />
          <p>{{ post.viewNumber || '' }}</p>
        </div>
        <div class="flex flexJustifySpaceBetween">
          <TheIcon icon="iconpinglun2" :size="25" />
          <p>{{ post.commentNumber || '' }}</p>
        </div>
        <div class="flex flexJustifySpaceBetween">
          <TheIcon
            icon="icondianzan"
            :class="{ likeFavor: post.likeStatus }"
            :size="30"
            @click="LikeFavor('like', post.id, userstore.userInfo.id)"
          />
          <p>{{ post.likeNumber || '' }}</p>
        </div>
        <div class="flex flexJustifySpaceBetween">
          <TheIcon
            icon="iconshoucang5"
            :class="{ likeFavor: post.favorStatus }"
            :size="30"
            @click="LikeFavor('favor', post.id, userstore.userInfo.id)"
          />
          <p>{{ post.favouriteNumber || '' }}</p>
        </div>
        <TheButton text="阅读全文" @click="viewArticle(post.id)" />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
// import axios from 'axios';
import { useRouter } from 'vue-router';
import { ElNotification } from 'element-plus';
import { useUserStore } from '../stores/user';
import TheIcon from './TheIcon.vue';
import TheButton from './TheButton.vue';
import TheAvatar from '@/components/TheAvatar.vue';

import useAxios from '../composables/useAxios';

const userstore = useUserStore();
const axios = useAxios();
const router = useRouter();

interface RowsItem {
  [key: string]: any;
}

interface Props {
  posts: Array<RowsItem>;
}

const props = defineProps<Props>();

function handleCopyCodeSuccess() {
  ElNotification({
    title: 'Success',
    message: '复制成功',
    type: 'success',
  });
}

function viewArticle(id: any) {
  router.push({ name: 'ViewArticle', params: { id: id } });
}

async function LikeFavor(type: 'like' | 'favor', id: number | string, userId: number | string) {
  if (!userstore.userInfo.token) {
    ElNotification({
      title: 'Warning',
      message: '请登录',
      type: 'warning',
    });
  } else {
    let res = await axios({
      url: '/api/article/' + type + '/' + '?id=' + id + '&userId=' + userId,
      method: 'GET',
    });
    let result = res.data;
    if (type == 'like') {
      for (const item of props.posts) {
        if (item.id == id) {
          if (result.status) {
            item.likeNumber++;
          } else {
            item.likeNumber--;
          }
          item.likeStatus = result.status;
        }
      }
    } else {
      for (const item of props.posts) {
        if (item.id == id) {
          if (result.status) {
            item.favouriteNumber++;
          } else {
            item.favouriteNumber--;
          }
          item.favorStatus = result.status;
        }
      }
    }
  }
}
</script>

<style scoped>
.article {
  margin: 40px 0;
  padding: 20px;
  min-width: 60vw;
  border-radius: 11px;
  background: ffffff;
  box-shadow: 9px 9px 18px #d3d3d3, -9px -9px 18px #ededed;
}

.avatar {
  margin-right: 10px;
}
.md {
  min-width: 40vw;
  max-width: 60vw;
  max-height: 420px;
  margin-bottom: 20px;
  margin-top: -30px;
  overflow: hidden;
}
.iconButton {
  margin: 0 40px;
}
.preAndNext {
  min-width: 60vw;
}
</style>
