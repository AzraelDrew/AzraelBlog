<template>
  <div id="user-info">
    <!-- <el-row :gutter="10" class="dweb">
      <el-col :xs="24" :lg="24">
        <div>
          <el-avatar :src="user_info.avatar"></el-avatar>
        </div>
        {{ user_info.name }}</el-col
      >
    </el-row> -->

    <el-row :gutter="10" class="dweb">
      点赞
      <el-col :xs="24" :lg="24">
        <div class="dweb" v-for="(fit, index) in user_info.like_data" :key="index">
          <el-image style="width: 100px; height: 100px" :src="fit.cover" :fit="'cover'"></el-image>
          <span class="demonstration">{{ fit.title }}</span>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import axios from 'axios';
import Qs from 'qs';
export default {
  data() {
    return {
      user_info: {
        name: '',
        avatar: '',
        like_data: [],
      },
    };
  },
  mounted() {
    this.get_user_info();
  },
  methods: {
    //提示框
    messageNotify(title, message, type) {
      this.$notify({
        title: title,
        message: message,
        type: type,
        showClose: true,
        center: true,
      });
    },
    get_user_info() {
      axios({
        url: this.$store.state.baseurl + 'api/user-info/',
        method: 'POST',
        data: Qs.stringify({ name: this.$store.state.currentname }),
      }).then((res) => {
        console.log(res.data);
        this.user_info = res.data;
      });
    },
  },
};
</script>

<style scoped>
.flex {
  display: flex;
  justify-content: center;
  align-content: center;
  justify-items: center;
  align-items: center;
}
.el-row {
  margin-bottom: 20px;

  padding: 10px;
}
</style>
