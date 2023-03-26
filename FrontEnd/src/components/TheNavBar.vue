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
      <div>
        <span @click.stop="toggleDark()" style="font-size: 15px">
          <TheIcon v-if="isDark" class="home icon linkColor" icon="iconmoon_fill" :size="20" />
          <TheIcon v-else class="home icon linkColor" icon="iconsun" :size="20" />
        </span>
      </div>
    </div>
  </nav>
</template>

<script lang="ts" setup>
import { useDark, useToggle } from '@vueuse/core';
import TheIcon from './TheIcon.vue';
const isDark = useDark();
const toggleDark = useToggle(isDark);
</script>

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
  margin-left: 4vw;
}
</style>
