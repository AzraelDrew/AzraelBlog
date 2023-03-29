import { fileURLToPath, URL } from 'node:url';

import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

import prismjs from 'vite-plugin-prismjs';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    prismjs({
      languages: 'all',
    }),
  ],
  build: {
    chunkSizeWarningLimit: 160000,
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
  define: {
    'process.env': {},
  },
});
