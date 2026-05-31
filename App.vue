<template>
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
</style>