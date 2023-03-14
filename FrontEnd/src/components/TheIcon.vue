<template>
  <div>
    <span class="icon iconfont" :class="icon" :size="size"></span>
  </div>
</template>

<script setup lang="ts">
interface Props {
  icon: string;
  size: number;
}
defineProps<Props>();
</script>

<style scoped>
.icon {
  font-size: v-bind(size + 'px');
  margin: 0 10px;
}
</style>
