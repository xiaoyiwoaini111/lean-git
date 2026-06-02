<!-- <template>
  <div id="app">
    <h1>{{ message }}</h1>
    <button @click="changeText">点我改变文字</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const message = ref('Hello Vue!')

function changeText() {
  const texts = [
    '你点击了按钮！',
    'Vue 交互成功啦 🎉',
    '你好呀！',
    '今天也是写代码的一天~'
  ]
  const randomIndex = Math.floor(Math.random() * texts.length)
  message.value = texts[randomIndex]
}
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #359469;
}
</style> -->


<template>
  <div id="app">
    <!-- 1. 在这里使用标签，名字要和下面 import 的名字一致 -->
    <CounterDemo />
  </div>
</template>

<script setup>
// 2. 导入你的组件
// 注意：路径 ./CounterDemo.vue 必须和你左侧文件名完全一样（大小写敏感）
import CounterDemo from './CounterDemo.vue'
</script>

<style>
/* 3. 给个简单的居中样式，防止内容贴边 */
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>