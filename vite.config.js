import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue' // 1. 引入插件

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()] // 2. 在 plugins 数组里调用它
})