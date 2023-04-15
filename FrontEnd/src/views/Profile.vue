<template>
  <div>
    <TheNavBar>
      <template #avatarAndNickname>
        <router-link to="/" class="link" href=""
          ><TheIcon class="home icon linkColor" icon="iconzhuye3" :size="30" /></router-link
      ></template>
      <template #postIcon>
        <router-link to="/postArticle" class="link linkColor postArticle"
          ><TheIcon icon="iconbianji4" :size="22" 
        /></router-link>
      </template>
      <template #dropDown>
        <div v-if="userstore.isLogin"><a @click="Logout" class="link linkColor"> 退出登录</a></div>

        <div v-else>
          <router-link class="link linkColor" to="/login">登录</router-link>
        </div>
      </template>
    </TheNavBar>
    <div class="profile flex">
      <div class="userInfo flex">
        <TheAvatar :size="200" :src="userstore.userInfo.avatar" />
        <div>
          <div class="flex flexJustifyStart">
            <h2 class="userName">{{ userstore.userInfo.name }}</h2>
            <router-link to="/profileEditing" class="flex link" href=""> 编辑个人信息</router-link>
          </div>
          <div class="flex flexJustifyStart">
            <pre class="desc">{{ userstore.userInfo.desc || '添加你的简介.....' }}</pre>
          </div>
        </div>
      </div>
    </div>
    <div class="articleList">
      <div class="flex">
        <TheIcon
          class="icon"
          v-for="(tab, index) in tabs"
          :icon="tab.icon"
          :size="40"
          :class="{ active: index == currentTab }"
          @click="GetArticle(index)"
        />
      </div>
      <div class="flexDirectionRow">
        <transition name="fade" appear>
          <TheArtcileList @deleteArticle="askDelete" v-if="currentTab == 0" :posts="posts" >
            <TheButton class="deleteArticle" text="删除"  />
          </TheArtcileList>
          <TheArtcileList v-else-if="currentTab == 1" :posts="posts" />
          <TheArtcileList v-else-if="currentTab == 2" :posts="posts" />
        </transition>
        <el-dialog
          v-model="dialogVisible"
          title=""
          width="40%"
          :show-close="false"
        >
          <span>确定删除吗？</span>
          <template #footer>
            <span class="dialog-footer">
              <el-button type="primary" @click="dialogVisible = false">取消</el-button>
              <el-button type="danger" @click="delArticle">
                确定
              </el-button>
            </span>
          </template>
        </el-dialog>
      </div>
    </div>
    
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, handleError } from 'vue';
import { RouterLink, useRouter } from 'vue-router';
import { ElNotification } from 'element-plus';
import { useUserStore } from '../stores/user';
import useAxios from '../composables/useAxios';
import TheArtcileList from '../components/TheArtcileList.vue';
import TheIcon from '../components/TheIcon.vue';
import TheNavBar from '@/components/TheNavBar.vue';
import TheAvatar from '@/components/TheAvatar.vue';
import TheButton from '@/components/TheButton.vue';

const axios = useAxios();

const router = useRouter();
const userstore = useUserStore();
const posts = ref([]);
const dialogVisible =ref(false)
const deleteArticleId = ref(0)
const currentTab = ref(userstore.profileIndex);
const tabs = ref([
  {
    label: 'my',
    icon: 'iconmy',
  },

  {
    label: 'like',
    icon: 'icondianzan',
  },
  {
    label: 'favourite',
    icon: 'iconshoucang5',
  },
]);

onMounted(async () => {
  let res = await AllArticle(userstore.userInfo.id, tabs.value[currentTab.value].label);
  posts.value = res.data.data;
});

async function GetArticle(index: any) {
  currentTab.value = index;
  userstore.ChangeProfileIndex(index);
  let res = await AllArticle(userstore.userInfo.id, tabs.value[currentTab.value].label);
  posts.value = res.data.data;
}
async function AllArticle(id: any, type: string) {
  let res = await axios({
    url: '/api/' + type + '/article/' + '?id=' + id,
    method: 'GET',
  });
  return res;
}

function askDelete(id:any){
  dialogVisible.value=true
  deleteArticleId.value = id
}

async function delArticle(){
  dialogVisible.value = false
  let formData = new FormData()
  formData.append("id",String(deleteArticleId.value))
  let delMessage =  await axios.post('api/delete/article/',formData)
  console.log(delMessage);
  if(delMessage.data=="ok"){
    ElNotification({
        title: 'Success',
        message: '删除成功',
        type: 'success',
        duration: 1000,
      });
      let res = await AllArticle(userstore.userInfo.id, tabs.value[currentTab.value].label);
      posts.value = res.data.data;
  }else{
    ElNotification({
        title: 'SucErrocess',
        message: '删除失败',
        type: 'error',
        duration: 1000,
      });
  }
}
function Logout() {
  userstore.userLogout();
  router.replace({ name: 'Home' });
}
</script>
<style scoped>
.active {
  color: #0984e3;
}
.articleList {
  margin-top: 5vw;
}
.icon {
  margin: 0 5vw;
}
.profile {
  min-width: 60vw;
}
.userInfo {
  min-width: 40vw;
}

.avatar {
  margin-right: 5vw;
  box-shadow: 5px 0px 5px #d3d3d3, -5px 0px 5px #d3d3d3, 0px 5px 5px #d3d3d3;
}
.userName {
  margin-right: 40px;
}
.desc {
  max-width: 20vw;
}

.nav {
  padding: 10px 20px;
  height: 50px;
  border-radius: 15px;
  box-shadow: 50px 0px 20px #d3d3d3, -50px 0px 20px #d3d3d3;
  margin-bottom: 30px;
}
.home {
  margin-left: -10px;
  text-decoration: none;
  color: #000000;
}
.linkColor {
  text-decoration: none;
  color: #00000095;
}
.linkColor:hover {
  color: #87a4ed;
}
.postArticle {
  margin-right: 10px;
}
.deleteArticle{
  margin-right: 20px;
  /* background-color: red; */
}
.deleteArticle.button {
  padding: 0.5em 0.8em;
  border: none;
  border-radius: 5px;
  font-weight: bold;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: red;
  transition: all 1000ms;
  font-size: 15px;
  position: relative;
  overflow: hidden;
  outline: 2px solid red;
}

.deleteArticle:hover {
  color: #ffffff;
  transform: scale(1.1);
  outline: 2px solid red;
  box-shadow: 4px 5px 17px -4px red;
  cursor: pointer;
}

.deleteArticle::before {
  content: '';
  position: absolute;
  left: -50px;
  top: 0;
  width: 0;
  height: 100%;
  background-color: red;
  transform: skewX(45deg);
  z-index: -1;
  transition: width 1000ms;
}


.dialog-footer button:first-child {
  margin-right: 10px;
}

</style>
