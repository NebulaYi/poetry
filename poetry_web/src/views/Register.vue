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
            <span>注册</span>
          </div>
        </template>
        <el-form @submit.prevent="handleRegister" label-width="auto">
          <el-form-item label="用户名">
            <el-input v-model="user_name" placeholder="请输入用户名" clearable></el-input>
          </el-form-item>
          <el-form-item label="邮箱">
            <el-input type="email" v-model="user_email" placeholder="请输入邮箱" clearable></el-input>
          </el-form-item>
          <el-form-item label="密码">
            <el-input type="password" v-model="user_password" placeholder="请输入密码" clearable></el-input>
          </el-form-item>
          <el-button type="primary" @click="handleRegister">注册</el-button>
          <span class="login-text" :style="{ marginTop: '10px' }">已有账户？<router-link to="/login" class="highlight">登录</router-link></span>
        </el-form>
      </el-card>
    </div>
  </div>
</template>

<script>
import {post} from "@/axios/http";

export default {
  name: 'Register',
  data() {
    return {
      user_name: '',
      user_email: '',
      user_password: '',
      fullWidth: document.documentElement.clientWidth,
      fullHeight: document.documentElement.clientHeight,
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
    async handleRegister() {
      try {
        console.log(this.user_password)
        const response = await post("/api/v1.0/user/register", {
          username: this.user_name,
          email: this.user_email,
          password: this.user_password,
        });
        if (response.code === 1) {
          sessionStorage.setItem("uName", this.user_name)
          sessionStorage.setItem("uEmail", this.user_email)
          sessionStorage.setItem("uPassword", this.user_password)
          console.log("用户名："+sessionStorage.getItem("uName"))
          console.log("账号："+sessionStorage.getItem("uEmail"))
          console.log("密码："+sessionStorage.getItem("uPassword"))
          this.$router.push('/home')
          this.$message.success("注册成功！");
        } else {
          this.$message.error("注册失败！"+response.msg);
        }
      } catch (error) {
        console.error(error);
      }
    },
    // 处理设备宽高
    handleResize () {
      this.fullWidth = document.documentElement.clientWidth - 16
      this.fullHeight = document.documentElement.clientHeight - 16
      this.curWidth = this.fullWidth + 'px'
      this.curHeight = this.fullHeight + 'px'
      console.log('curWidth=' + this.curWidth + ',curHeight=' + this.curHeight)
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
  align-items: flex-start; /* 调整到上方 */
  width: 100%;
  height: 100%;
}

.box-card {
  width: 400px; /* 增加宽度 */
  padding: 20px; /* 增加内边距 */
  background-color: rgba(255, 255, 255, 0.8); /* 半透明浅色背景 */
  border-radius: 10px; /* 圆角 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 添加阴影 */
  margin-top: 12%; /* 调整上方间距 */
}

.header-card {
  text-align: center;
}

.login-text {
  display: block;
  text-align: center;
}

.highlight {
  color: #409EFF;
  cursor: pointer;
}
</style>
