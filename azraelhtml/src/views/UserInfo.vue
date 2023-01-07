<template>
  <div id="user-info">
    <el-row :gutter="10" class="dweb">
      <el-col :xs="24" :lg="24">{{ user_info.name }}</el-col>
    </el-row>
    <el-row :gutter="10" class="dweb">
      <el-col :xs="24" :lg="24">{{ user_info.belong }}</el-col>
    </el-row>
    <el-row :gutter="10" class="dweb">
      <el-col :xs="24" :lg="24"><img style="height:200px" :src="user_info.headimg" alt=""/></el-col>
    </el-row>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      user_info: {
        name: '',
        belong: '',
        headimg: '',
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
        method: 'GET',
      }).then((res) => {
        console.log(res.data);
        this.user_info = res.data;
      });
    },
  },
};
</script>

<style scoped>
.dweb {
  padding: 0;
  margin: 0;
}
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
