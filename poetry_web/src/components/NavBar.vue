<template>
  <div class="navbarContainer">
    <nav class="navbar1">
      <ul>
        <!-- 第一排选择：智能作诗、藏头诗 -->
        <li @click="selectType('智能作诗')" :class="{ active: currentType === '智能作诗' }">智能作诗</li>
        <li @click="selectType('藏头诗')" :class="{ active: currentType === '藏头诗' }">藏头诗</li>
      </ul>
    </nav>
    <nav class="navbar2">
      <ul>
        <!-- 第二排选择：诗歌体裁 -->
        <li v-for="style in styles" :key="style"
            :class="{ active: style === currentStyle }"
            @click="selectStyle(style)">{{ style }}</li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'PoetryNavBar',
  data() {
    return {
      currentType: '智能作诗', // 默认选择智能作诗
      currentStyle: null, // 默认没有选择诗歌体裁
      styles: ['五言绝句', '五言律诗', '七言绝句', '七言律诗']
    };
  },
  methods: {
    selectType(type) {
      this.currentType = type;
      // 可以在这里添加逻辑，比如通知父组件或者发送数据到后端
    },
    selectStyle(style) {
      this.currentStyle = style;
      // 可以在这里添加逻辑，比如通知父组件或者发送数据到后端
    }
  }
}
</script>

<style scoped>
.navbarContainer{
  width: 60%;
  margin: 0 auto;
}

.navbar1 {
  background-color: #9c2e33;
  color: white;
  width: 100%;
}

.navbar1 ul {
  list-style-type: none;
  display: flex;
  justify-content: center; /* 水平居中排列 */
}

.navbar1 li {
  flex: 1; /* 每个li元素占据相等空间 */
  cursor: pointer;
  text-align: center; /* 文本居中 */
  padding: 0.5rem 1rem;
  margin: 0 0.5rem; /* 为按钮添加外边距 */
  background-color: #9c2e33; /* 背景色 */
  transition: background-color 0.3s; /* 平滑过渡背景色变化 */
}

.navbar1 li:hover {
  background-color: rgba(124, 30, 35, 0.26); /* 鼠标悬浮时更深的背景色 */
}

.navbar1 .active {
  background-color: #fc071a; /* 选中时更深的背景色 */
}

.navbar2 {
  background-color: transparent;
  color: rgb(29, 31, 31);
  width: 100%;
}

.navbar2 ul {
  list-style-type: none;
  display: flex;
  justify-content: space-around; /* 均匀分布空间 */
  padding: 0;
  margin: 0;
}

.navbar2 li {
  flex: 1; /* 每个li元素占据相等空间 */
  cursor: pointer;
  text-align: center; /* 文本居中 */
  background-color: transparent; /* 初始背景色 */
  transition: background-color 0.3s; /* 平滑过渡背景色变化 */
  margin: 8px;
}

.navbar2 li:hover {
  background-color: rgb(187, 156, 29); /* 鼠标悬浮时更深的背景色 */
  color: white;
}

.navbar2 .active {
  background-color: #9c2e33; /* 选中时的背景色 */
  color: white;
}
</style>