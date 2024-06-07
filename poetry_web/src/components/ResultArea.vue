<template>
  <div class="result-area">
    <!-- 展示诗歌标题 -->
    <h1 class="poem-title">{{ poem.title }}</h1>
    <!-- 展示诗歌内容，当没有数据或正在加载时不显示 -->
    <div class="poem-content" v-if="poem.lines">
      <p v-for="(line, index) in formattedLines" :key="index" class="poem-line">
        {{ line }}
      </p>
    </div>
    <!-- 加载状态提示 -->
    <div v-else-if="loading" class="loading-content">
      加载中...
    </div>
    <!-- 默认欢迎消息 -->
    <p v-else>
      欢迎使用诗词生成系统
    </p>
  </div>
</template>

<script>
export default {
  name: 'ResultArea',
  props: ['inputText'], // 从父组件接收输入文本
  data() {
    return {
      poem: {
        title: '欢迎使用', // 初始欢迎消息
        lines: ''
      }, // 用于存储从后端接收的诗歌数据
      loading: false, // 加载状态
    };
  },
  computed: {
    formattedLines() {
      // 如果存在诗句，按'。'分割并去除空白，否则返回空数组
      return this.poem.lines ? this.poem.lines.split('。').map(part => part.trim()) : [];
    }
  },
  methods: {
    updatePoemData(title, lines) {
      this.poem = { title, lines: lines + '。' }; // 更新诗歌数据
      this.loading = false; // 数据加载完成后，停止加载动画
    },
    resetPoemData() {
      this.poem = { title: '欢迎使用', lines: '' }; // 重置诗歌数据为初始欢迎消息
      this.loading = false;
    }
  },
  watch: {
    inputText(newText) {
      if (newText) {
        this.loading = true; // 输入文本存在时，显示加载状态
        // 模拟从后端接收数据的异步操作
        setTimeout(() => {
          // 假设后端返回的数据
          this.updatePoemData('新生成的诗歌', '床前明月光，疑是地上霜。举头望明月，低头思故乡。');
        }, 1000);
      } else {
        this.resetPoemData(); // 重置诗歌数据
      }
    }
  }
};
</script>

<style scoped>
.result-area {
  text-align: center;
  margin: 2rem auto;
  font-size: 1.2rem;
  width: 50%;
  height: 300px;
  background-color: #bb9c1d;

  background-image: url('../assets/display.jpg'); /* 替换为你的图片路径 */
  background-size: 100% 100%; /* 使背景图覆盖整个元素 */
  background-repeat: no-repeat; /* 背景图不重复 */
  background-position: center center; /* 背景图居中显示 */
}

.poem-title {
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

.poem-content {
  text-align: center;
  margin-top: 1rem;
}

.poem-line {
  margin: 0.5rem 0;
  white-space: pre-wrap; /* 保留空白符和换行符 */
}

.loading-content {
  text-align: center;
  margin: 2rem auto;
  font-size: 1.2rem;
  color: #050505; /* 加载提示文字颜色 */
}
</style>