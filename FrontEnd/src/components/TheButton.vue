<template>
  <button class="button">{{ text }}</button>
</template>

<script lang="ts" setup>
import { computed } from 'vue';
interface Props {
  text: string;
  color?: string;
}
defineProps<Props>();
</script>

<style scoped>
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
  transform: skewX(-45deg);
  z-index: -1;
  transition: width 1000ms;
}

button:hover::before {
  width: 250%;
}
</style>
