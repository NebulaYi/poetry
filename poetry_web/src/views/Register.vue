<template>
  <div class="register-container">
    <h2>注册</h2>
    <form @submit.prevent="handleRegister">
      <input type="text" placeholder="用户名" v-model="username" required />
      <input type="email" placeholder="邮箱" v-model="email" required />
      <input type="password" placeholder="密码" v-model="password" required />
      <button type="submit">注册</button>
    </form>
    <p>已有账户？<router-link to="/login">登录</router-link></p>
  </div>
</template>

<script>
export default {
  name: 'Register',
  data() {
    return {
      username: '',
      email: '',
      password: ''
    }
  },
  methods: {
    handleRegister() {
      // 实现注册逻辑
      this.$router.push('/login')
    }
  }
}
</script>

<style>
.register-container {
  text-align: center;
  margin-top: 50px;
}
.register-container input {
  display: block;
  margin: 10px auto;
  padding: 10px;
  width: 200px;
}
.register-container button {
  padding: 10px 20px;
}
</style>
