<template>
  <div class="login-container">
    <h2>登录</h2>
    <form @submit.prevent="handleLogin">
      <input type="text" placeholder="用户名" v-model="username" required />
      <input type="password" placeholder="密码" v-model="password" required />
      <button type="submit">登录</button>
    </form>
    <p>还没有账户？<router-link to="/register">注册</router-link></p>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    handleLogin() {
      // 实现登录逻辑
      this.$router.push('/home')
    }
  }
}
</script>

<style>
.login-container {
  text-align: center;
  margin-top: 50px;
}
.login-container input {
  display: block;
  margin: 10px auto;
  padding: 10px;
  width: 200px;
}
.login-container button {
  padding: 10px 20px;
}
</style>
