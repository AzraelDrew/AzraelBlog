<template>
  <el-avatar
    class="avatar"
    :class="{ commentAvatar: isCommentContent }"
    shape="circle"
    :size="size"
    :src="src"
  />
</template>

<script lang="ts" setup>
interface ProPs {
  size: number;
  src: string;
  isCommentContent?: boolean;
}
const props = withDefaults(defineProps<ProPs>(), {
  isCommentContent: () => false,
});
</script>

<style scoped>
.avatar {
  margin-right: 10px;
}
.commentAvatar {
  margin-top: 10px;
}
</style>
