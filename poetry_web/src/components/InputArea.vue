<template>
  <!-- 选择 -->
  <div class="navbarContainer">
    <!-- 第一排选择：智能作诗、藏头诗 -->
    <el-row class="navbar1">
      <el-col :span="12"><li @click="selectType('智能作诗')" :class="{ active: currentType === '智能作诗' }">智能作诗</li></el-col>
      <el-col :span="12"><li @click="selectType('藏头诗')" :class="{ active: currentType === '藏头诗' }">藏头诗</li></el-col>
    </el-row>
    <nav class="navbar2">
      <ul>
        <!-- 第二排选择：诗歌体裁 -->
        <li v-for="style in styles" :key="style"
            :class="{ active: style === currentStyle }"
            @click="selectStyle(style)">{{ style }}
        </li>
      </ul>
    </nav>
  </div>
  <!-- 输入框 -->
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
      currentType: '智能作诗', // 默认选择智能作诗
      currentStyle: '五言绝句', // 默认选择五言绝句
      styles: ['五言绝句', '五言律诗', '七言绝句', '七言律诗'],

      inputText: '' // 用于绑定输入框的文本
    };
  },
  methods: {
    selectType(type) {
      this.currentType = type;
    },
    selectStyle(style) {
      this.currentStyle = style;
    },

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

/*
选择
 */
.navbarContainer{
  width: 60%;
  margin: 0 auto;
}
/*
选择类型
 */
.navbar1 {
  background-color: transparent;
  color: white;
  width: 100%;
  margin: 20px;
}
.el-col {
  border-radius: 10px;
}

.navbar1 li {
  flex: 1; /* 每个li元素占据相等空间 */
  cursor: pointer;
  text-align: center; /* 文本居中 */
  padding: 0.5rem 1rem;
  background-color: rgba(140, 238, 194, 0.68); /* 背景色 */
  border-radius: 10px;
//transition: background-color 0.3s; /* 平滑过渡背景色变化 */
}

.navbar1 li:hover {
  background-color: rgba(140, 238, 194, 0.68); /* 鼠标悬浮时更深的背景色 */
}

.navbar1 .active {
  background-color: #33c5cb; /* 选中时更深的背景色 */
}

/*
选择体裁
 */
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
  border-radius: 8px;
}

.navbar2 li:hover {
  background-color: rgb(187, 156, 29); /* 鼠标悬浮时更深的背景色 */
  color: white;
}

.navbar2 .active {
  background-color: #9c2e33; /* 选中时的背景色 */
  color: white;
}

/*
输入
 */
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
  