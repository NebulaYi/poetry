<template>
  <div class="background">
    <img :src="imgSrc" width="100%" height="100%" alt="" />
  </div>
  <div class="historyView">
    <Header />

    <nav class="navbar">
      <ul>
        <li v-for="style in styles" :key="style"
            :class="{ active: style === selectedStyle }"
            @click="selectStyle(style)">{{ style }}
        </li>
      </ul>
    </nav>

    <!-- 无限滚动的诗歌列表容器 -->
    <ul
        v-infinite-scroll="loadMore"
        class="infinite-list"
        style="overflow: auto;"
    >
      <li
          v-for="poem in filteredPoems"
          :key="poem.id"
          class="infinite-list-item"
      >
        <div class="poem">
          <div class="poem-st">
            <p class="poem-index">选择: {{ poem.functionName }}</p>
            <p class="poem-input">输入: {{ poem.description }}</p>
            <p class="poem-style">体裁: {{ poem.style }}</p>
          </div>
          <!-- 确保 result 标签独立占据一行 -->
          <p class="poem-result" v-for="(line, index) in splitResult(poem.result)" :key="index">{{ line }}</p>
        </div>
      </li>
    </ul>
    <Footer />
  </div>
</template>

<script setup>
import Header from "../components/Header.vue";
import Footer from '../components/Footer.vue';
import {computed, ref} from 'vue';
import {post} from "@/axios/http";

const imgSrc = require('../assets/img.jpg');
const poems = ref([]);

const styles = ['全部记录','五言绝句', '五言律诗', '七言绝句', '七言律诗'];
// 当前选中的风格
const selectedStyle = ref('全部记录');

// 根据选中的风格过滤诗歌列表的方法
const filteredPoems = computed(() => {
  return poems.value.filter(poem =>
      selectedStyle.value === '全部记录' || poem.style === selectedStyle.value
  );
});
const splitResult = (text) => text.split('。');
// 选择风格的处理函数
const selectStyle = (style) => {
  return selectedStyle.value = style;
};

//获取历史记录的函数
const fetchHistory = async () => {
  try {
    const response = await post('/api/v1.0/user/history', {email: sessionStorage.getItem('uEmail')});
    console.log(response.data)
    poems.value = response.data; // 更新poems数组
    console.log(poems.value)
  } catch (error) {
    console.error('获取历史记录失败：', error);
  }
};

// 组件挂载后获取数据
fetchHistory();


const loadMore = () => {
  // 这里可以添加逻辑来加载更多的诗歌
  // 例如，可以是一个API请求，然后更新poems数组
  //console.log('加载更多诗歌');
  // 模拟加载更多数据
  // setTimeout(() => {
  //   poems.value = [...poems.value, ...morePoems];
  // }, 1500);
};
</script>

<style>
/* Add styles if necessary */

.background{
  width:100%;
  height:100%;  /**宽高100%是为了图片铺满屏幕 */
  z-index:-1;
  position: absolute;
  overflow: hidden; /* 添加此行以隐藏溢出内容 */
}

.historyView{
  width:100%;
  height:100%;
  z-index:1;
  overflow: hidden; /* 隐藏外部滚动条 */
  position: absolute;
}

.infinite-list {
  width: 60%; /* 展示内容区域宽度 */
  height: 65%; /* 展示内容区域高度 */
  padding: 20px;
  margin: auto;
  overflow-y: scroll; /* 允许垂直滚动，但隐藏滚动条 */
  list-style-type: none;
  scrollbar-width: none; /* 隐藏滚动条 */
}

.infinite-list-item {
  margin-bottom: 20px;
  border-bottom: 1px solid #ddd;
  padding-bottom: 20px;
}

.poem-st {
  display: flex;
  justify-content: center;
  width: 100%;
}

.poem-index,
.poem-input,
.poem-style {
  margin: 5px 16px; /* 根据需要添加上下边距 */
}

.poem-result {
  width: 100%; /* 占满整行 */
  font-size: larger; /* 加大字体 */
  margin-top: 10px; /* 添加上边距 */
}

/*
选择体裁
 */
.navbar {
  width: 60%; /* 展示内容区域宽度 */
  background-color: transparent;
  color: rgb(29, 31, 31);
  margin: 20px auto;
}

.navbar ul {
  list-style-type: none;
  display: flex;
  justify-content: space-around; /* 均匀分布空间 */
  padding: 0;
  margin: 0;
}

.navbar li {
  flex: 1; /* 每个li元素占据相等空间 */
  cursor: pointer;
  text-align: center; /* 文本居中 */
  background-color: transparent; /* 初始背景色 */
  transition: background-color 0.3s; /* 平滑过渡背景色变化 */
  margin: 0 8px;
  border-radius: 8px;
  height: 28px;
  font-size: 20px;
  padding: 4px 0;
}

.navbar li:hover {
  background-color: rgb(187, 156, 29); /* 鼠标悬浮时更深的背景色 */
  color: white;
}

.navbar li.active {
  background-color: rgb(176, 147, 28); /* 选中时的背景色 */
  color: white;
}

</style>