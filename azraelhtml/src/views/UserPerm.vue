<template>
  <div id="user">
    <div class="dweb">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>文章列表</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div class="body dweb">
      <div class="dweb">
        <h5>用户组</h5>
        <el-divider></el-divider>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  components: {},
};
</script>

<style scoped>
#user .dweb {
  padding: 20px 10px;
}
.body.dweb {
  margin-top: 10px;
}
.body.dweb h5 {
  color: #fff;
  font-weight: 500;
}
.el-divider--horizontal {
  margin: 0 0;
}
/* .card.dweb .text-item {
  color: #fff;
  height: 80px;
  display: flex;
  justify-content: center;
  align-items: center;
} */
</style>