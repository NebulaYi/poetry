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

      inputText: '' // 用于绑定输入框的文本
    };
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
      } else if(this.currentType === '藏头诗'){
        //this.$message('藏头诗生成')
        //传输数据
        const respAcrGenerate = await post('/api/v1.0/poetry/acrosticGenerate', {email: this.$store.state.user.uEmail, keyword: this.inputText, style: this.currentStyle});
        if (respAcrGenerate.code === 1){
          this.$message.success('生成成功')
          console.log(respAcrGenerate)
          console.log(respAcrGenerate.data)
          //将数据传至结果显示组件
          //this.$router.push({name: 'ResultArea', query: {poem: respAcrGenerate.data}});
        }else {
          this.$message.error("生成失败")
        }
      } else if(this.currentType === '智能作诗'){
        this.$message('自定义诗词生成')
        // 传输数据
        // const respCusGenerate = await put('', {email: this.$store.state.user.email, keyword: this.inputText, style: this.currentStyle});
        // if (respCusGenerate.code === 1){
        //   this.$message.success('生成成功')
        //   console.log(respCusGenerate)
        //   //将数据传至结果显示组件
        //   this.$router.push({name: 'ResultArea', query: {poem: respCusGenerate.data}});
        // }else {
        //   this.$message.error("生成失败")
        // }
      }
      // 这里使用setTimeout模拟异步请求
      setTimeout(() => {
        this.$emit('generate', { text: this.inputText, type: this.currentType, style: this.currentStyle }); // 触发事件，传递输入的文本和选择
      }, 1000);
    },
    reset() {
      this.inputText = '';  // 重置输入框文本
      this.$emit('reset');   // 触发重置事件
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
  padding: 24px 0;
}
/*
选择类型
 */
.navbar1 {
  background-color: transparent;
  color: white;
  width: 100%;
  margin: 20px 0;
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
  background-color: rgba(140, 238, 194, 0.68); /* 背景色 */
  border-radius: 10px;
  height:32px;
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
  margin: 16px 0;
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
  