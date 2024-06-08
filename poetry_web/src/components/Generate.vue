<template>
  <div>
    <!-- 选择 -->
    <div class="navbarContainer">
      <!-- 第一排选择：智能作诗、藏头诗 -->
      <nav class="navbar1">
        <ul>
          <li @click="selectType('智能作诗')" :class="{ active: currentType === '智能作诗' }">智能作诗</li>
          <li @click="selectType('藏头诗')" :class="{ active: currentType === '藏头诗' }">藏头诗</li>
        </ul>
      </nav>
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
      <input type="text" placeholder="请输入句子、段落或者关键词（关键词以空格隔开）"
             @input="handleInput"
             @keypress="handleKeyPress"
             :maxlength="getMaxInputLength()" />
      <button @click="generatePoetry">生成诗歌</button>
      <button @click="reset">重置</button>
    </div>

    <!-- 结果展示 -->
    <div class="result-area">
      <!-- 标题 -->
      <h1 class="poem-title">欢迎使用</h1>
      <!-- 展示诗歌内容，当没有数据或正在加载时不显示 -->
      <div class="poem-content" >
        <div v-if="poem">
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
          欢迎使用智能诗词生成系统
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { ElMessage } from 'element-plus'
import {post} from "@/axios/http";
export default {
  name: 'InputArea',
  data() {
    return {
      currentType: '智能作诗', // 默认选择智能作诗
      currentStyle: '五言绝句', // 默认选择五言绝句
      styles: ['五言绝句', '五言律诗', '七言绝句', '七言律诗'],

      inputText: '', // 用于绑定输入框的文本

      poem: '', // 用于存储从后端接收的诗歌数据
      loading: false, // 加载状态

      u_email: sessionStorage.getItem("uEmail"),
    };
  },
  computed: {
    formattedLines() {
      // 如果存在诗句，按'。'分割并去除空白，否则返回空数组
      return this.poem ? this.poem.split('。').map(part => part.trim()) : [];
    }
  },
  methods: {
    /*
    选择诗歌类型和体裁
     */
    selectType(type) {
      this.currentType = type;
    },
    selectStyle(style) {
      this.currentStyle = style;
    },

    /*
    处理输入内容
     */
    handleInput(event) {
      this.inputText = event.target.value;
      //console.log("输入框："+this.inputText);
    },
    handleKeyPress(event) {
      // 如果输入超过限制长度，则阻止输入
      if (event.target.value.length >= this.getMaxInputLength()) {
        event.preventDefault();
      }
    },
    getMaxInputLength() {
      // 根据当前选择返回最大输入长度
      if (this.currentType === '智能作诗') {
        return this.currentStyle.includes('绝句') ? 4 : 8;
      } else if (this.currentType === '藏头诗') {
        return this.currentStyle.includes('绝句') ? 4 : 8;
      }
      return Infinity; // 默认无限制
    },

    /*
    生成诗词
     */
    async generatePoetry() {
      // 校验文字合法
      const isInputValid = /^[\u4e00-\u9fff\s]*$/.test(this.inputText);
      if (!isInputValid) {
        ElMessage.error('请输入中文');
        return;
      }
      // 根据当前选择确定所需输入长度
      const maxLength = this.getMaxInputLength();
      if (this.inputText.length === 0) {
        // 如果未输入，设置错误提示信息
        ElMessage.error('请输入内容');
        return; // 阻止进一步的诗歌生成
      } else if (this.currentType === '藏头诗' && this.inputText.length < maxLength) {
        // 如果藏头诗输入字数不够，设置错误提示信息
        ElMessage.error('请输入完整内容');
        return; // 阻止进一步的诗歌生成
      }

      // 设置加载状态为 true
      this.poem = '';
      this.loading = true;

      // 根据选择的诗歌类型生成诗歌
      let poemData;
      if (this.currentType === '智能作诗') {
        const respCusGenerate = await post('/api/v1.0/poetry/customizeGenerate', {email: this.u_email, keyword: this.inputText, style: this.currentStyle});
        if (respCusGenerate.code === 1) {
          this.$message.success('生成成功');
          poemData = respCusGenerate.data;
        } else {
          this.$message.error("生成失败");
          this.loading = false; // 后端返回错误时，取消加载状态
          return;
        }
      } else if (this.currentType === '藏头诗') {
        const respAcrGenerate = await post('/api/v1.0/poetry/acrosticGenerate', {email: this.u_email, keyword: this.inputText, style: this.currentStyle});
        if (respAcrGenerate.code === 1) {
          this.$message.success('生成成功');
          poemData = respAcrGenerate.data;
        } else {
          this.$message.error("生成失败");
          this.loading = false; // 后端返回错误时，取消加载状态
          return;
        }
      }

      // 更新诗歌数据并取消加载状态
      this.updatePoemData(poemData);

      // 触发事件，传递输入的文本和选择
      this.$emit('generate', { text: this.inputText, type: this.currentType, style: this.currentStyle });
    },
    reset() {
      this.inputText = '';  // 重置输入框文本
      this.$emit('reset');   // 触发重置事件
    },

    /*
    结果展示
     */
    updatePoemData(poem) {
      this.poem = poem; // 更新诗歌数据
      this.loading = false; // 数据加载完成后，停止加载动画
    },
    resetPoemData() {
      this.poem = ''; // 重置诗歌数据为初始欢迎消息
      this.loading = false;
    },
  },
  watch: {
    inputText(newText) {
      if (newText) {
        //this.loading = true; // 输入文本存在时，显示加载状态
        // 模拟从后端接收数据的异步操作
        setTimeout(() => {
          // 假设后端返回的数据
          this.updatePoemData(this.poem);
        }, 1000);
      } else {
        this.resetPoemData(); // 重置诗歌数据
      }
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
  padding: 16px 0;
}
/*
选择类型
 */
.navbar1 {
  background-color: transparent;
  color: white;
  width: 100%;
  margin: 20px 0;
  padding-bottom: 16px;
}
.navbar1 ul {
  list-style-type: none;
  display: flex;
  justify-content: space-around; /* 均匀分布空间 */
  padding: 0;
  margin: 0;
}

.navbar1 li {
  flex: 1; /* 每个li元素占据相等空间 */
  cursor: pointer;
  text-align: center; /* 文本居中 */
  padding: 0.5rem 1rem;
  background-color: rgba(132, 110, 78, 0.6); /* 背景色 */
  border-radius: 10px;
  height:32px;
//transition: background-color 0.3s; /* 平滑过渡背景色变化 */
}

.navbar1 li:hover {
  background-color: rgba(210, 180, 124, 0.68); /* 鼠标悬浮时更深的背景色 */
}

.navbar1 .active {
  background-color: rgb(55, 114, 25); /* 选中时更深的背景色 */
}

/*
选择体裁
 */
.navbar2 {
  background-color: transparent;
  color: rgb(29, 31, 31);
  width: 100%;
  margin: 20px 0;
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
  margin: 0 8px;
  border-radius: 8px;
  height: 28px;
}

.navbar2 li:hover {
  background-color: rgb(187, 156, 29); /* 鼠标悬浮时更深的背景色 */
  color: white;
}

.navbar2 .active {
  background-color: rgb(55, 114, 25); /* 选中时的背景色 */
  color: white;
}

/*
输入
 */
.input-area {
  display: flex;
  justify-content: center;
  margin: 0 auto;
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

/*
结果
 */
.result-area {
  display: flex;
  flex-direction: column; /* 子元素垂直排列 */
  text-align: center;
  margin: 2rem auto;
  font-size: 1.2rem;
  width: 50%;
  height: 300px;
  background-color: #bb9c1d;
  background-image: url('../assets/display.jpg');
  background-size: 100% 100%;
  background-repeat: no-repeat;
  background-position: center center;
}

.poem-title {
  flex: 0 1 20%; /* 不超过15%的高度，但至少15% */
  display: flex;
  align-items: center; /* 垂直居中 */
  justify-content: center; /* 水平居中 */
  font-size: 1.5rem;
  font-weight: bold;
}

.poem-content {
  flex: 0 1 60%; /* 至少75%的高度，可以占据剩余空间 */
  display: flex;
  flex-direction: column; /* 子元素垂直排列 */
  align-items: center; /* 水平居中 */
  justify-content: center; /* 垂直居中 */
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
