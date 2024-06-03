<template>
  <div class="input-area">
    <input type="text" placeholder="请输入句子、段落或者关键词（关键词以空格隔开）" @input="handleInput" />
    <button @click="generatePoetry">生成诗歌</button>
    <button @click="reset">重置</button>
  </div>
</template>
  
<script>
  export default {
    name: 'InputArea',
    data() {
      return {
        inputText: '' // 用于绑定输入框的文本
      };
    },
    methods: {
      handleInput(event) {
        this.inputText = event.target.value;
        console.log("输入框："+this.inputText);
      },
      generatePoetry() {
        // 假设调用后端接口获取诗歌数据
        // 这里使用setTimeout模拟异步请求
        setTimeout(() => {
          this.$emit('generate', this.inputText); // 触发事件，传递输入的文本
        }, 1000);
      },
      reset() {
        this.inputText = ''; // 重置输入框文本
        this.$emit('reset'); // 触发重置事件
      }
    }
  }
</script>

<style>
  .input-area {
    display: flex;
    justify-content: center;
    margin: 1rem auto;
    width: 60%;
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
  