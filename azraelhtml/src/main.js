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
import './assets/css/mystyle.css';
import './assets/iconfont/iconfont.css';

Vue.config.productionTip = false;

Vue.use(ElementUI);
new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
