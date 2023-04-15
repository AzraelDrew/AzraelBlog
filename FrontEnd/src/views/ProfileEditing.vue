<template>
  <TheNavBar>
    <template #avatarAndNickname>
      <router-link to="/" class="link" href=""
        ><TheIcon class="home icon linkColor" icon="iconzhuye3" :size="30" /></router-link
    ></template>

    <template #dropDown>
      <div>
        <a @click="Logout" class="link linkColor">退出登录</a>
      </div>
    </template>
  </TheNavBar>
  <transition name="fade" appear>
    <div class="profileEditing flex">
      <div class="flex flexDirectionColumn box">
        <div class="flex flexJustifyStart changeAvatar">
          <TheAvatar :size="50" :src="form.avatar" />
          <el-upload
            class="upload-demo flex"
            multiple
            :limit="3"
            name="avatar"
            action="http://127.0.0.1:8000/api/upload/avatar/"
            :on-success="Upload"
          >
            <el-button class="uploadAvatar" round>修改头像</el-button>
          </el-upload>
        </div>
        <div class="form">
          <el-form :model="form" label-width="120px">
            <el-form-item class="flex" label="用户名:">
              <el-input class="input" v-model="form.name" />
            </el-form-item>
            <el-form-item class="flex" label="昵称:">
              <el-input class="input" v-model="form.nickName" />
            </el-form-item>
            <el-form-item class="flex" label="电话:">
              <el-input class="input" v-model="form.phone" />
            </el-form-item>
            <el-form-item class="flex" label="简介:">
              <el-input
                class="input"
                type="textarea"
                :rows="8"
                v-model="form.desc"
                :maxlength="200"
              />
            </el-form-item>
            <el-form-item class="button">
              <el-button type="primary" @click="onSubmit">Submit</el-button>
              <el-button @click="onCancel">Cancel</el-button>
            </el-form-item>
          </el-form>
        </div>
      </div>
    </div>
  </transition>
</template>

<script lang="ts" setup>
import { reactive } from 'vue';
import { ElNotification } from 'element-plus';
import { useRouter, RouterLink } from 'vue-router';
import { useUserStore } from '@/stores/user';
import useAxios from '@/composables/useAxios';
import TheAvatar from '@/components/TheAvatar.vue';
import TheNavBar from '@/components/TheNavBar.vue';
import TheIcon from '@/components/TheIcon.vue';

const axios = useAxios();

const userstore = useUserStore();

const router = useRouter();
// do not use same name with ref

const form = reactive({
  name: userstore.userInfo.username,
  nickName: userstore.userInfo.name,
  avatar: userstore.userInfo.avatar,
  phone: userstore.userInfo.phone,
  desc: userstore.userInfo.desc,
});

async function Upload(e: any) {
  form.avatar = '';
  form.avatar = e.url;
}
// watch(userstore.userInfo, async () => {
//   userstore.GetUserInfo(userstore.userInfo.token);
// });
async function onSubmit() {
  console.log(
    `%c
███████╗██╗   ██╗██████╗ ███╗   ███╗██╗████████╗██╗
██╔════╝██║   ██║██╔══██╗████╗ ████║██║╚══██╔══╝██║
███████╗██║   ██║██████╔╝██╔████╔██║██║   ██║   ██║
╚════██║██║   ██║██╔══██╗██║╚██╔╝██║██║   ██║   ╚═╝
███████║╚██████╔╝██████╔╝██║ ╚═╝ ██║██║   ██║   ██╗
╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝   ╚═╝   ╚═╝
  `,
    'color:#7c9beb'
  );

  if(form.name.length<1||form.nickName.length<1){
    ElNotification({
    title: 'Warning',
    message: '用户名或昵称不能为空',
    type: 'warning',
  });
  return;
  }
  let formData = new FormData();
  formData.append('token', userstore.userInfo.token);
  formData.append('name', form.name);
  formData.append('nickName', form.nickName);
  formData.append('avatar', form.avatar);
  formData.append('phone', form.phone);
  formData.append('desc', form.desc);
  let res = await axios.post('api/update/userinfo/', formData);
  userstore.GetUserInfo(userstore.userInfo.token);
  ElNotification({
    title: 'Success',
    message: '修改成功',
    type: 'success',
  });
  router.replace({ name: 'Profile' });
}
function onCancel() {
  console.log(
    `%c
  ██████╗ █████╗ ███╗   ██╗ ██████╗███████╗██╗     ██╗
  ██╔════╝██╔══██╗████╗  ██║██╔════╝██╔════╝██║     ██║
  ██║     ███████║██╔██╗ ██║██║     █████╗  ██║     ██║
  ██║     ██╔══██║██║╚██╗██║██║     ██╔══╝  ██║     ╚═╝
  ╚██████╗██║  ██║██║ ╚████║╚██████╗███████╗███████╗██╗
   ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚══════╝╚═╝
  `,
    'color:#7c9beb'
  );

  router.replace({ name: 'Profile' });
}
function Logout() {
  userstore.userLogout();
  router.replace({ name: 'Home' });
}
</script>
<style scoped>
.profileEditing {
  margin-top: 50px;
  min-width: 60vw;
}
.box {
  padding: 50px 0;
  align-content: flex-start;
  justify-content: flex-start;
  border-radius: 11px;
  background: ffffff;
  box-shadow: 9px 9px 18px #d3d3d3, -9px -9px 18px #ededed;
  padding-right: 90px;
  min-height: 520px;
  min-width: 520px;
}
.changeAvatar {
  min-width: 30vw;
  margin-left: 20px;
  margin-bottom: 20px;
}
.uploadAvatar {
  margin-left: 20px;
  padding: 15px 15px;
}
.input {
  margin: 5px 0;
  min-width: 30vw;
  height: 40px;
}

.button {
  position: relative;
  bottom: -130px;
}
.home {
  margin-left: -10px;
  text-decoration: none;
  color: #000000;
}
.linkColor {
  text-decoration: none;
  font-size: 14px;
  color: #000;
}
.linkColor:hover {
  color: #87a4ed;
}
</style>
