import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

//引入summernote
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.css';
import 'popper.js';
import 'summernote';
import 'summernote/lang/summernote-zh-CN.js';
import 'summernote/dist/summernote.css';
import './assets/css/index.css';
import './assets/iconfont/iconfont.css';

// markdown编辑器
import VMdEditor from '@kangc/v-md-editor';
import VueMarkdownEditor from '@kangc/v-md-editor';
import '@kangc/v-md-editor/lib/style/base-editor.css';
import vuepressTheme from '@kangc/v-md-editor/lib/theme/vuepress.js';
import '@kangc/v-md-editor/lib/theme/style/vuepress.css';

import VMdPreview from '@kangc/v-md-editor/lib/preview';
import '@kangc/v-md-editor/lib/style/preview.css';

import createLineNumbertPlugin from '@kangc/v-md-editor/lib/plugins/line-number/index';

import Prism from 'prismjs';

VMdEditor.use(vuepressTheme, {
  Prism,
});
// 编辑组件
Vue.use(VMdEditor);

// 渲染组件
VMdPreview.use(vuepressTheme, {
  Prism,
});
Vue.use(VMdPreview);

// 代码快显示行号
VueMarkdownEditor.use(createLineNumbertPlugin());
Vue.use(VueMarkdownEditor);

Vue.config.productionTip = false;
Vue.use(ElementUI);

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
