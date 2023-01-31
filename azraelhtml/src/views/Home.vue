<template>
  <div class="hsome">
    <el-row :gutter="20">
      <el-col :xs="24" :lg="24">
        <div class="grid-content bg-purple">
          <div class="dweb" style="height: 800px"></div>
        </div>
      </el-col>
      <!-- <el-col :xs="24" :lg="8">
        <div class="grid-content bg-purple">
          <div class="dweb" style="height: 200px"></div>
        </div>
      </el-col>
      <el-col :xs="24" :lg="8">
        <div class="grid-content bg-purple">
          <div class="dweb" style="height: 200px"></div>
        </div>
      </el-col> -->
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      number: 4,
      screenWidth: document.body.clientWidth,
    };
  },
  watch: {
    screenWidth() {
      console.log(this.screenWidth);
      if (this.screenWidth <= 1200) {
        this.number = 1;
      } else {
        this.number = 3;
      }
    },
  },
  mounted() {
    this.change_el_col();
    const that = this;
    window.onresize = () => {
      return (() => {
        that.screenWidth = document.body.clientWidth;
      })();
    };
  },
  methods: {
    change_el_col() {
      // console.log(this.screenWidth);
      if (this.screenWidth <= 1200) {
        this.number = 1;
      }
    },
  },
};
</script>

<style lang="scss"></style>
