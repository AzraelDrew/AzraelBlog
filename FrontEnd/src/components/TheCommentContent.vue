<template>
  <div>
    <div class="grid commentTitle">
      <h4>{{ nickeName }}</h4>
      <p>{{ date }}</p>
    </div>
    <p class="commentContent">
      {{ text }}
    </p>
  </div>
</template>

<script lang="ts" setup>
interface Props {
  nickeName: string;
  date: string;
  text: string;
}
defineProps<Props>();
</script>

<style scoped>
.grid {
  display: grid;
  grid-template-columns: 1fr 9fr;
}
.commentTitle {
  justify-content: center;
  justify-items: center;
  align-content: center;
  align-items: center;
}
.commentContent {
  margin-top: -10px;
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
}
</style>
