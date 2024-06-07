<template>
  <div class="bg">
    <div class="img_box">
      <!-- 背景图片：动态绑定宽高 -->
      <img src="../assets/bg1.jpg" :style="{ height: fullHeight + 'px', width: fullWidth + 'px' }" />
    </div>
    <div class="content-wrapper">
      <el-card class="box-card">
        <template #header>
          <div class="header-card">
            <span>诗词生成系统</span>
          </div>
        </template>
        <el-form :model="user" :rules="rules" label-width="auto" ref="user">
          <el-form-item prop="user_email" label="账号">
            <el-input prefix-icon="User" v-model="user.user_email" clearable type="email" placeholder="请输入账号"></el-input>
          </el-form-item>
          <el-form-item prop="user_password" label="密码">
            <el-input prefix-icon="Lock" v-model="user.user_password" clearable type="password" placeholder="请输入密码"></el-input>
          </el-form-item>
          <el-button type="primary" @click="login" >登录</el-button>
          <span class="register-text" :style="{ marginTop: '10px' }">没有账号？请<span class="highlight" @click="register">注册</span></span>
        </el-form>
      </el-card>
    </div>
  </div>
</template>

<script>

export default {
  data () {
    return {
      // 获取设备宽度、高度
      fullWidth: document.documentElement.clientWidth,
      fullHeight: document.documentElement.clientHeight,
      // 初始化用户数据
      user: {
        user_email: '',
        user_password: ''
      },
      rules: {
        user_email: [{
          required: true,
          message: '请输入账号',
          trigger: 'blur'
        }],
        user_password: [{
          required: true,
          message: '请输入密码',
          trigger: 'blur'
        }],
      },
    }
  },
  created () {
    // 添加监听，监听设备宽高
    window.addEventListener('resize', this.handleResize)
  },
  beforeUnmount() {
    // 销毁监听
    window.removeEventListener('resize', this.handleResize)
  },
  methods: {
    // 处理设备宽高
    handleResize () {
      this.fullWidth = document.documentElement.clientWidth - 16
      this.fullHeight = document.documentElement.clientHeight - 16
      this.curWidth = this.fullWidth + 'px'
      this.curHeight = this.fullHeight + 'px'
      console.log('curWidth=' + this.curWidth + ',curHeight=' + this.curHeight)
    },
    login () {
      sessionStorage.setItem("user_email", this.user.user_email)
      console.log(sessionStorage.getItem("user_email"))
      this.$router.push('/home')
      console.log(sessionStorage.getItem("user_email"))
    },
    register () {
      this.$router.push('/register')
    }
  }
}
</script>

<style>
.bg {
  position: relative;
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.img_box img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -1;
}

.content-wrapper {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  width: 100%;
  height: 100%;
}

.box-card {
  width: 400px;
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-top: 12%; /* 调整上方间距 */
}

.header-card {
  text-align: center;
}

.register-text {
  display: block;
  text-align: center;
}

.highlight {
  color: #409EFF;
  cursor: pointer;
}
</style>
