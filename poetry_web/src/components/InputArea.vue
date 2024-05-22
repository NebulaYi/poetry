<template>
    <div class="input-area">
      <input type="text" placeholder="请输入句子、段落或者关键词（关键词以空格隔开）" />
      <button @click="generatePoetry">生成诗歌</button>
      <button @click="reset">重置</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'InputArea',
    methods: {
      generatePoetry() {
        // 实现生成诗歌的逻辑
      },
      reset() {
        // 实现重置的逻辑
      }
    }
  }
  </script>
  
  <style>
  .input-area {
    display: flex;
    justify-content: center;
    margin: 1rem 0;
  }
  .input-area input {
    width: 60%;
    padding: 0.5rem;
    margin-right: 1rem;
  }
  .input-area button {
    padding: 0.5rem 1rem;
    margin-right: 0.5rem;
    cursor: pointer;
  }
  </style>
  