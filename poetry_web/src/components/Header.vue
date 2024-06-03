<template>
  <header class="header">
    <!-- 右上角用户设置 -->
    <el-dropdown @command="handleCommand">
      <span class="el-dropdown-link">
        userName<el-icon class="el-icon--right"><ArrowDown /></el-icon>
      </span>
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item command="a" @click="openChangePasswordDialog">修改密码</el-dropdown-item>
          <el-dropdown-item command="b">修改信息</el-dropdown-item>
          <el-dropdown-item command="c">历史记录</el-dropdown-item>
          <el-dropdown-item command="d" divided @click="handleLogout">登出</el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>

    <!-- 修改密码对话框 -->
    <el-dialog v-model="dialogFormVisible1" title="修改密码" width="500">
      <el-form :model="codeForm" @submit.prevent="confirmPasswordChange">
        <el-form-item label="原密码：" :label-width="formLabelWidth">
          <el-input v-model="codeForm.oldPwd" type="password" autocomplete="off" />
        </el-form-item>
        <el-form-item label="新密码：" :label-width="formLabelWidth">
          <el-input v-model="codeForm.newPwd1" type="password" autocomplete="off" />
        </el-form-item>
        <el-form-item label="确认密码：" :label-width="formLabelWidth">
          <el-input v-model="codeForm.newPwd2" type="password" autocomplete="off" />
        </el-form-item>
      </el-form>
      <template v-slot:footer>
        <span class="dialog-footer">
          <el-button @click="dialogFormVisible1 = false">取消</el-button>
          <el-button type="primary" @click="confirmPasswordChange">确认</el-button>
        </span>
      </template>
    </el-dialog>

    <!-- 修改信息（昵称）对话框 -->
    <el-dialog v-model="dialogFormVisible2" title="修改信息" width="500">
      <span>username: </span>
      <el-input v-model="newName" type="uname" autocomplete="off" />
      <template v-slot:footer>
        <span class="dialog-footer">
          <el-button @click="dialogFormVisible2 = false">取消</el-button>
          <el-button type="primary" @click="confirmNameChange">确认</el-button>
        </span>
      </template>
    </el-dialog>
  </header>
</template>

<script>
import { ElMessage, ElDropdown, ElDropdownMenu, ElDropdownItem, ElIcon, ElDialog, ElForm, ElFormItem, ElInput } from 'element-plus'
import { ArrowDown } from '@element-plus/icons-vue'
import router from '../router'

export default {
  name: 'Header',
  components: {
    ElDropdown,
    ElDropdownMenu,
    ElDropdownItem,
    ElIcon,
    ElDialog,
    ElForm,
    ElFormItem,
    ElInput,
    ArrowDown
  },
  data() {
    return {
      dialogFormVisible1: false,
      dialogFormVisible2: false,
      formLabelWidth: '90px',
      codeForm: {
        oldPwd: '',
        newPwd1: '',
        newPwd2: ''
      },
      newName: '',
    }
  },
  methods: {
    handleCommand(command) {
      switch (command) {
        case 'a':
          this.openChangePasswordDialog();
          break;
        case 'b':
          this.dialogFormVisible2 = true;
          break;
        case 'c':
          router.push('/history');
          break;
        case 'd':
          this.handleLogout();
          break;
      }
    },
    openChangePasswordDialog() {
      this.dialogFormVisible1 = true;
    },
    handleLogout() {
      // 执行登出逻辑，比如清除本地存储的 token
      this.clearAuthToken();
      ElMessage('已成功登出账号！');
      router.push('/login');
    },
    clearAuthToken() {
      // 清除token的逻辑
      // 例如: localStorage.removeItem('token');
    },
    confirmPasswordChange() {
      if (this.codeForm.newPwd1 === this.codeForm.newPwd2) {
        // 密码匹配，提交更改
        ElMessage.success('密码修改成功！');
        this.dialogFormVisible1 = false;
        // 这里可以添加提交新密码到服务器的代码
      } else {
        // 密码不匹配，提示用户
        ElMessage.error('两次输入的密码不一致');
      }
    },
    confirmNameChange() {
      ElMessage.success(this.newName + '信息修改成功！');
      this.dialogFormVisible2 = false;
    },
  }
}
</script>

<style scoped>
.header {
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  background-color: #f5f5f5;
}
.el-dropdown-link {
  display: flex;
  align-items: center;
  margin-right: 64px;
  font-size: 18px;
  cursor: pointer;
}
.dialog-footer {
  display: flex;
  justify-content: center;
}
</style>