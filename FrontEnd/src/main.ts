import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
import router from './router';

import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';

import './assets/icon/iconfont.css';

import VueMarkdownEditor from '@kangc/v-md-editor';
import '@kangc/v-md-editor/lib/style/base-editor.css';
import vuepressTheme from '@kangc/v-md-editor/lib/theme/vuepress.js';
import '@kangc/v-md-editor/lib/theme/style/vuepress.css';
import VMdPreview from '@kangc/v-md-editor/lib/preview';
import '@kangc/v-md-editor/lib/style/preview.css';

import createHighlightLinesPlugin from '@kangc/v-md-editor/lib/plugins/highlight-lines/index';
import '@kangc/v-md-editor/lib/plugins/highlight-lines/highlight-lines.css';

import createTodoListPlugin from '@kangc/v-md-editor/lib/plugins/todo-list/index';
import '@kangc/v-md-editor/lib/plugins/todo-list/todo-list.css';

import createEmojiPlugin from '@kangc/v-md-editor/lib/plugins/emoji/index';
import '@kangc/v-md-editor/lib/plugins/emoji/emoji.css';

import createKatexPlugin from '@kangc/v-md-editor/lib/plugins/katex/cdn';

import Prism from 'prismjs';

import './assets/main.css';
const app = createApp(App);

VueMarkdownEditor.use(vuepressTheme, {
  Prism,
})
  .use(createTodoListPlugin())
  .use(createHighlightLinesPlugin())
  .use(createKatexPlugin())
  .use(createEmojiPlugin());

VMdPreview.use(vuepressTheme, {
  Prism,
})
  .use(createTodoListPlugin())
  .use(createHighlightLinesPlugin())
  .use(createKatexPlugin())
  .use(createEmojiPlugin());
app.use(VueMarkdownEditor);
app.use(VMdPreview);
app.use(ElementPlus);
app.use(createPinia());
app.use(router);
app.mount('#app');
