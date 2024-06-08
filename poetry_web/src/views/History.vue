<template>
  <div class="background">
    <img :src="imgSrc" width="100%" height="100%" alt="" />
  </div>
  <div class="historyView">
    <Header />
    <!-- 无限滚动的诗歌列表容器 -->
    <ul
        v-infinite-scroll="loadMore"
        class="infinite-list"
        style="overflow: auto;"
    >
      <li
          v-for="poem in poems"
          :key="poem.id"
          class="infinite-list-item"
      >
        <div class="poem">
          <p class="poem-title">输入: {{ poem.description }}</p>
          <p class="poem-style">风格: {{ poem.style }}</p>
          <p class="poem-result">{{ poem.result }}</p>
        </div>
      </li>
    </ul>
    <Footer />
  </div>
</template>

<script setup>
import Header from "../components/Header.vue";
import Footer from '../components/Footer.vue';
import { ref } from 'vue';
import {post} from "@/axios/http";

const imgSrc = require('../assets/img.jpg');
const poems = ref([]);
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
  height: 60%; /* 展示内容区域高度 */
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

</style>