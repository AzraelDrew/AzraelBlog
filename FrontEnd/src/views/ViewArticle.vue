<template>
  <TheNavBar>
    <template #avatarAndNickname>
      <router-link class="flex link linkColor" to="/">
        <TheAvatar :size="40" :src="userstore.userInfo.avatar" />
        <span>{{ userstore.userInfo.name }}</span>
      </router-link>
    </template>
    <template #postIcon v-if="userstore.isLogin">
      <router-link to="/postArticle" class="link linkColor postArticle"
        ><TheIcon icon="iconbianji4" :size="25"
      /></router-link>
    </template>
    <template #dropDown>
      <el-dropdown v-if="userstore.isLogin">
        <span class="el-dropdown-link flex">
          个人中心<el-icon class="el-icon--right"><arrow-down /></el-icon>
        </span>
        <template #dropdown>
          <el-dropdown-menu class="dropDown">
            <el-dropdown-item command="a">
              <router-link class="flex link linkColor" to="/profile">
                <span>个人信息</span>
                <TheIcon icon="iconmy" :size="18" />
              </router-link>
            </el-dropdown-item>
            <el-dropdown-item command="b" @click="Logout">
              <span>退出登录</span>
              <TheIcon icon="iconlogout" :size="18"
            /></el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
      <div v-else>
        <a class="link linkColor" @click="Login">登录</a>
      </div>
    </template>
  </TheNavBar>
  <div class="flex">
    <transition name="fade" appear>
      <div class="article">
        <div style="margin-left: 40px">
          <h2>{{ artcileData.title }}</h2>
          <div class="flex flexJustifyStart">
            <TheAvatar :size="40" :src="artcileData.avatar" />
            <span style="display: flex; align-content: center">{{
              artcileData.nickeName
            }}</span>
          </div>
          <div class="flex flexJustifyStart">
            <p>发布于:{{ artcileData.date.split("T")[0] }}</p>
            <div class="flex">
              <TheIcon icon="iconview" :size="25" />
              <p>{{ artcileData.viewNumber || "" }}</p>
            </div>
          </div>
        </div>

        <div class="md">
          <v-md-preview
            :text="artcileData.content"
            :default-show-toc="true"
            @copy-code-success="handleCopyCodeSuccess"
          ></v-md-preview>
        </div>
      </div>
    </transition>

    <div class="articleButton iconButton flex flexWarp flexJustifySpaceEvenly">
      <div class="flex flexJustifySpaceBetween">
        <TheIcon
          icon="icondianzan"
          :class="{ likeFavor: artcileData.likeStatus }"
          :size="30"
          @click="LikeFavor('like', route.params.id, userstore.userInfo.id)"
        />
        <p>{{ artcileData.likeNumber || "" }}</p>
      </div>
      <div class="flex flexJustifySpaceBetween">
        <TheIcon
          icon="iconshoucang5"
          :class="{ likeFavor: artcileData.favorStatus }"
          :size="30"
          @click="LikeFavor('favor', route.params.id, userstore.userInfo.id)"
        />
        <p>{{ artcileData.favouriteNumber || "" }}</p>
      </div>
      <div class="flex flexJustifySpaceBetween" @click="showComments()">
        <TheIcon icon="iconpinglun2" :size="25" />
        <p>{{ artcileData.commentNumber || "" }}</p>
      </div>
      <div
        v-show="userstore.userInfo.id == artcileData.belongUser"
        class="flex flexJustifySpaceBetween"
        @click="editArticle(artcileData.id)"
      >
        <TheIcon icon="iconedit_light" :size="27" />
      </div>
    </div>

    <el-drawer
      v-model="commentsDrawer"
      :title="'评论' + artcileData.commentNumber"
      direction="rtl"
      :size="commentWidth"
    >
      <div class="flex flexWarp iconAdnButton" style="align-items: start">
        <el-input
          class="input"
          v-model="input"
          type="textarea"
          :rows="8"
          placeholder="Please input"
        />
        <div
          class="flex flexJustifySpaceBetween iconAdnButton"
          style="margin: 10px 20px 0px 20px"
        >
          <TheAvatar :size="40" :src="userstore.userInfo.avatar" />
          <el-button
            type="primary"
            @click="addComment(artcileData.id, userstore.userInfo.id)"
            >发布评论</el-button
          >
        </div>
      </div>
      <Comment v-for="(comment, index) in comments" :key="index">
        <template #avatar>
          <TheAvatar
            :size="40"
            :isCommentContent="true"
            :src="comment.avatar"
          />
        </template>
        <template #articleContent>
          <div class="grid commentTitle">
            <h4 style="justify-self: start">
              {{ comment.nickName.substring(0, 20) }}
            </h4>
            <p style="justify-self: end">{{ comment.date.split("T")[0] }}</p>
          </div>
          <div style="margin-bottom: 10px">
            <p
              class="commentContent commentDetail"
              @click="
                showCommentDetails(
                  comment.text,
                  comment.avatar,
                  comment.nickName,
                  comment.date
                )
              "
            >
              {{ comment.text }}
            </p>
            <div style="display: flex; justify-content: end">
              <TheButton
                text="删除"
                style="display: flex"
                @click="deleteComment(comment.id)"
              />
            </div>
          </div>
        </template>
      </Comment>
    </el-drawer>

    <el-drawer
      v-model="commentDeatilDrawer"
      title="评论"
      direction="ltr"
      :size="commentWidth"
    >
      <div class="grid comment">
        <div>
          <TheAvatar
            :size="40"
            :isCommentContent="true"
            :src="commentDetailAvatar"
          />
        </div>
        <div>
          <div class="grid commentTitle">
            <h4>{{ commentDeatilNickName.substring(0, 20) }}</h4>
            <p style="justify-self: end">
              {{ commentDetailDate.split("T")[0] }}
            </p>
          </div>
          <div style="margin-bottom: 10px">
            <p class="commentDetail">{{ commentDetail }}</p>
          </div>
        </div>
      </div>
    </el-drawer>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, reactive, computed } from "vue";
import { ElNotification } from "element-plus";
import { RouterLink, useRouter, useRoute } from "vue-router";
import { ArrowDown } from "@element-plus/icons-vue";
import { useUserStore } from "../stores/user";
import useAxios from "../composables/useAxios";
import TheIcon from "../components/TheIcon.vue";
import TheButton from "@/components/TheButton.vue";
import TheNavBar from "@/components/TheNavBar.vue";
import Comment from "@/components/TheComment.vue";
import TheAvatar from "@/components/TheAvatar.vue";

const axios = useAxios();

/* this.$route：当前激活的路由的信息对象。每个对象都是局部的，可以获取当前路由的 path, name, params, query 等属性。

this.$router：全局的 router 实例。通过 vue 根实例中注入 router 实例，然后再注入到每个子组件，从而让整个应用都有路由功能。

其中包含了很多属性和对象（比如 history 对象），任何页面也都可以调用其 push(), replace(), go() 等方法。 */
const router = useRouter();
const route = useRoute();
const userstore = useUserStore();

const commentWidth = computed(() =>
  document.body.clientWidth < 500 ? 300 : "40%"
);
const commentsDrawer = ref(false);
const commentDeatilDrawer = ref(false);
const text = ref("");

const artcileData = reactive({
  id: "",
  belongUser: "0",
  title: "",
  content: "",
  nickeName: "",
  date: "",
  avatar: "",
  viewNumber: 0,
  commentNumber: 0,
  likeNumber: 0,
  favouriteNumber: 0,
  favorStatus: false,
  likeStatus: false,
});

const input = ref("");
interface RowsItem {
  [key: string]: string;
}

const comments = ref<RowsItem[]>();
const commentDetail = ref("");
const commentDetailAvatar = ref("");
const commentDeatilNickName = ref<string>("");
const commentDetailDate = ref<string>("");

// const commentDetail

function handleCopyCodeSuccess() {
  ElNotification({
    title: "Success",
    message: "复制成功",
    type: "success",
  });
}
onMounted(async () => {
  let res = await axios({
    url:
      "api/article/?" +
      "id=" +
      route.params.id +
      "&userId=" +
      userstore.userInfo.id,
    method: "GET",
  });
  let result = res.data;
  artcileData.id = result.id;
  artcileData.belongUser = result.belongUser;
  text.value = result.content;
  artcileData.avatar = result.avatar;
  artcileData.nickeName = result.nickName;
  artcileData.date = result.date;
  artcileData.title = result.title;
  artcileData.content = result.content;
  artcileData.commentNumber = result.commentNumber;
  artcileData.favouriteNumber = result.favouriteNumber;
  artcileData.likeNumber = result.likeNumber;
  artcileData.viewNumber = result.viewNumber;
  artcileData.likeStatus = result.likeStatus;
  artcileData.favorStatus = result.favorStatus;
});

async function editArticle(id: any) {
  router.push({ name: "EditArticle", params: { id: route.params.id } });
}

async function showComments() {
  commentsDrawer.value = true;
  let res = await axios({
    url: "api/comment/" + "?id=" + route.params.id,
    method: "GET",
  });
  comments.value = res.data.data;
}
async function deleteComment(id: any) {
  let data = new FormData();
  data.append("id", id);
  data.append("userId", userstore.userInfo.id);
  let res = await axios.post("api/delete/comment/", data);
  console.log(res.data);
  if (res.data == "OK") {
    ElNotification({
      title: "Success",
      message: "删除成功",
      type: "success",
    });
    let res = await axios({
      url:
        "api/article/?" +
        "id=" +
        route.params.id +
        "&userId=" +
        userstore.userInfo.id,
      method: "GET",
    });
    let result = res.data;
    artcileData.commentNumber = result.commentNumber;
    showComments();
  } else {
    ElNotification({
      title: "Warning",
      message: "不能删除他人的评论",
      type: "warning",
    });
  }
}
async function addComment(articleId: any, currentId: any) {
  if (!userstore.userInfo.token) {
    ElNotification({
      title: "Warning",
      message: "请登录",
      type: "warning",
    });
  } else if (input.value == "") {
    ElNotification({
      title: "Warning",
      message: "评论不能为空",
      type: "warning",
    });
  } else {
    let data = new FormData();
    data.append("id", articleId);
    data.append("userId", currentId);
    data.append("text", input.value);
    let res = await axios.post("api/add/comment/", data);
    artcileData.commentNumber = res.data.commentNumber;
    ElNotification({
      title: "Success",
      message: "发布成功",
      type: "success",
    });
    input.value = "";
    showComments();
  }
}
function showCommentDetails(
  commentText: string,
  commentAvatar: string,
  commentNickName: string,
  commentDate: string
) {
  commentDeatilDrawer.value = true;
  commentDetail.value = commentText;
  commentDetailAvatar.value = commentAvatar;
  commentDeatilNickName.value = commentNickName;
  commentDetailDate.value = commentDate;
}
function Login() {
  router.replace({ name: "Login" });
}
function Logout() {
  userstore.userLogout();
  router.replace({ name: "Home" });
}

async function LikeFavor(
  type: "like" | "favor",
  id: number | string | string[],
  userId: number | string
) {
  if (!userstore.userInfo.token) {
    ElNotification({
      title: "Warning",
      message: "请登录",
      type: "warning",
    });
  } else {
    let res = await axios({
      url: "/api/article/" + type + "/" + "?id=" + id + "&userId=" + userId,
      method: "GET",
    });
    console.log(res.data);
    let result = res.data;
    if (type == "like") {
      if (result.status) {
        artcileData.likeNumber += 1;
      } else {
        artcileData.likeNumber -= 1;
      }
      artcileData.likeStatus = result.status;
    } else {
      if (result.status) {
        artcileData.favouriteNumber += 1;
      } else {
        artcileData.favouriteNumber -= 1;
      }
      artcileData.favorStatus = result.status;
    }
  }
}
</script>

<style scoped lang="scss">
.grid {
  display: grid;
  // gap:20px;
  grid-template-columns: 80px 9fr;
}

// .commentDetail{
//   grid-column-end: 3;
// }
.postArticle {
  margin-right: 10px;
}
.article {
  margin: 40px 0;
  padding: 20px;
  min-width: 60vw;
  border-radius: 11px;
  background: ffffff;
  box-shadow: 9px 9px 18px #d3d3d3, -9px -9px 18px #ededed;
}

.avatar {
  margin-right: 10px;
}
.articleContent {
  height: 200px;
  overflow: hidden;
}
.md {
  min-width: 40vw;
  max-width: 65vw;
  margin-top: -30px;
  margin-bottom: 20px;
  overflow: hidden;
}
.iconButton {
  position: fixed;
  bottom: 80px;
  margin: 0 40px;
  padding: 5px 0;
  padding-right: 10px;
  min-width: 40vw;
  max-width: 720px;
  background: #ffffff;
  height: 50px;
  border-radius: 15px;
  box-shadow: 5px 0px 10px #6e6e6e, -5px 0px 10px #6e6e6e;
}

.nav {
  padding: 10px 20px;
  height: 50px;
  border-radius: 15px;
  box-shadow: 50px 0px 20px #d3d3d3, -50px 0px 20px #d3d3d3;
}

.icon {
  position: absolute;
  left: 1rem;
  fill: #749cf1;
  width: 1rem;
  height: 1rem;
}
.linkColor {
  color: #000000;
  &:hover {
    color: #000000;
  }
}
.iconAdnButton {
  width: 100%;
  margin-top: -20px;
  margin-bottom: 5px;
}
.comment {
  margin-top: 20px;
  padding: 5px 20px;
  border-radius: 11px;
  box-shadow: 5px 0px 10px #d3d3d3, -5px 0px 10px #ededed, 0px 5px 10px #d3d3d3,
    0px -5px 10px #ededed;
}
.commentTitle {
  justify-content: center;
  align-content: center;
  align-items: center;
  margin-left: -20px;
}
.commentContent {
  margin-top: -10px;

  width: 25vw;
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
}
.commentDetail {
  margin-top: -10px;
  margin-left: -20px;
}
</style>
