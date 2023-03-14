<template>
  <transition name="fade" appear>
    <div class="flex">
      <div class="grid">
        <div class="article" v-for="post in posts" :key="post.id">
          <div class="content flex flexJustifySpaceBetween">
            <p class="contenTitle">{{ post.title }}</p>
            <p>{{ post.date.split('T')[0] }}</p>
          </div>
          <div class="contentButton flex flexWarp flexJustifySpaceBetween">
            <div class="articleInfo flex flexJustifySpaceBetween">
              <TheIcon icon="iconview" :size="20" />
              <p>{{ post.viewNumber }}</p>
            </div>
            <div>
              <slot></slot>
              <TheButton @click="viewArticle(post.id)" text="阅读全文" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script lang="ts" setup>
import TheIcon from './TheIcon.vue';
import TheButton from './TheButton.vue';
import { useRouter } from 'vue-router';
interface RowsItem {
  [key: string]: string;
}

interface Props {
  posts: Array<RowsItem>;
}

defineProps<Props>();

const router = useRouter();

function viewArticle(id: any) {
  router.push({ name: 'ViewArticle', params: { id: id } });
}
</script>
<style scoped>
.grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
}
.article {
  margin: 20px;
  padding: 20px;
  min-width: 30vw;
  max-width: 50vw;
  min-height: 5vh;
  border-radius: 11px;
  background: ffffff;
  box-shadow: 9px 9px 18px #d3d3d3, -9px -9px 18px #ededed;
}
.content {
  margin-bottom: 20px;
  margin-right: 10px;
}
.contenTitle {
  margin-left: 10px;
}
.articleInfo {
  margin-right: 20px;
}
.contentButton {
  margin-bottom: 10px;
  margin-right: 10px;
}
.button {
  padding: 0.5em 0.8em;
  border: none;
  border-radius: 5px;
  font-weight: bold;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: #699df8;
  transition: all 1000ms;
  font-size: 15px;
  position: relative;
  overflow: hidden;
  outline: 2px solid #699df8;
}

button:hover {
  color: #ffffff;
  transform: scale(1.1);
  outline: 2px solid #699df8;
  box-shadow: 4px 5px 17px -4px #699df8;
  cursor: pointer;
}

button::before {
  content: '';
  position: absolute;
  left: -50px;
  top: 0;
  width: 0;
  height: 100%;
  background-color: #699df8;
  transform: skewX(45deg);
  z-index: -1;
  transition: width 1000ms;
}

button:hover::before {
  width: 250%;
}
</style>
