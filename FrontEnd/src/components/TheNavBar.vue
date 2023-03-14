<template>
  <nav class="flex flexJustifySpaceBetween nav">
    <div class="flex">
      <slot name="avatarAndNickname"></slot>
    </div>

    <div class="group">
      <slot name="input"> </slot>
    </div>
    <div class="flex">
      <slot name="postIcon"></slot>
      <slot name="dropDown"> </slot>
    </div>
  </nav>
</template>

<script lang="ts" setup></script>

<style scoped>
.nav {
  padding: 10px 20px;
  height: 50px;
  border-radius: 15px;
  box-shadow: 50px 0px 20px #d3d3d3, -50px 0px 20px #d3d3d3;
}
.avatar {
  margin-right: 10px;
}
.group {
  display: flex;
  line-height: 28px;
  align-items: center;
  position: relative;
  max-width: 60vw;
}
</style>
