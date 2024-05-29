<template>
  <header class="header">
    <el-dropdown @command="handleCommand">
      <span class="el-dropdown-link">
        userName<el-icon class="el-icon--right"><ArrowDown /></el-icon>
      </span>
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item command="a">修改密码</el-dropdown-item>
          <el-dropdown-item command="b">修改信息</el-dropdown-item>
          <el-dropdown-item command="c">历史记录</el-dropdown-item>
          <el-dropdown-item command="d">Action 4</el-dropdown-item>
          <el-dropdown-item command="e" divided @click="handleLogout">登出</el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>
  </header>
</template>

<script>
import { ElMessage, ElDropdown, ElDropdownMenu, ElDropdownItem, ElIcon } from 'element-plus'
import { ArrowDown } from '@element-plus/icons-vue'
import router from '../router/index.js' // 确保引入你的 Vue Router 实例

export default {
  name: 'Header',
  components: {
    ArrowDown,
    ElDropdown,
    ElDropdownMenu,
    ElDropdownItem,
    ElIcon
  },
  setup() {
    const handleCommand = (command) => {
      // 根据 command 执行不同的逻辑
      switch (command) {
        case 'a':
          // 打开修改密码的弹窗
          break
        case 'b':
          // 打开修改信息的弹窗
          break
        case 'c':
          // 跳转至历史记录页面
          //router.push('/history') // 确保 '/history' 是正确的路由路径
          break
        case 'd':
          // 执行 Action 4 的逻辑
          break
        case 'e':
          ElMessage(`已成功登出账号！`)// 执行登出逻辑
          break
      }
    }

    const handleLogout = () => {
      // 执行登出逻辑，比如清除本地存储的 token
      // 然后跳转至登录页面
      router.push('/login') // 确保 '/login' 是正确的路由路径
    }

    // 返回对象，包含需要在模板中使用的属性和方法
    return {
      handleCommand,
      handleLogout,
      ArrowDown
    }
  }
}
</script>

<style>
.header {
  height: 56px;
  display: flex;
  align-items: center; /*垂直居中对齐*/
  justify-content: flex-end; /* 使内容靠右对齐 */
  background-color: #f5f5f5;
}
.el-dropdown-link{
  display: flex;
  align-items: center; /* 确保userName和图标垂直居中 */
  margin-right: 64px;
}
</style>
