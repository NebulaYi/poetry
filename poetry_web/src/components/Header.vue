<template>
  <header class="header">
    <!-- 右上角用户设置 -->
    <el-dropdown @command="handleCommand">
      <span class="el-dropdown-link" :key="uName">
        {{ uName  }}<el-icon class="el-icon--right"><ArrowDown /></el-icon>
      </span>
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item command="a">修改密码</el-dropdown-item>
          <el-dropdown-item command="b">修改信息</el-dropdown-item>
          <el-dropdown-item command="c">{{ dynamicHistoryText }}</el-dropdown-item>
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
          <el-tooltip content="由8-16位数字、大小写英文组成，不含特殊字符" placement="bottom">
            <el-input v-model="codeForm.newPwd1" type="password" autocomplete="off" />
          </el-tooltip>
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
      <span>当前昵称: {{ uName }}</span>
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
import { ArrowDown } from '@element-plus/icons-vue'
import router from '../router'
import {put} from '@/axios/http'

export default {
  name: 'Header',
  components: {
    ArrowDown
  },
  data() {
    return {
      uName: sessionStorage.getItem("uName"),
      dialogFormVisible1: false,
      dialogFormVisible2: false,
      formLabelWidth: '90px',
      codeForm: {
        oldPwd: '',
        newPwd1: '',
        newPwd2: ''
      },
      newName: '',
      historyText: '历史记录', // 初始化显示文本
    }
  },
  computed: {
    dynamicHistoryText() {
      // 根据当前路由判断显示文本
      return this.$route.path === '/history' ? '回到首页' : '历史记录';
    },
  },
  methods: {
    // async test(){
    //   const r = await get('/api/v1.0/test')
    //   console.log(r)
    //   if(r.code === 1){
    //     this.$message.success(111);
    //   }else{
    //     this.$message.error(r.msg);
    //   }
    // },

    /*
    处理下拉设置的逻辑
     */
    handleCommand(command) {
      switch (command) {
        case 'a'://显示密码修改框
          this.dialogFormVisible1 = true;
          break;
        case 'b'://显示用户名修改框s
          this.dialogFormVisible2 = true;
          break;
        case 'c'://历史记录查看
          // 如果当前路径是 '/history'，则跳转到首页
          if (this.$route.path === '/history') {
            router.push('/home');
          } else {
            // 否则，跳转到历史记录页
            router.push('/history');
          }
          break;
        case 'd'://退出登录
          this.handleLogout();
          break;
      }
    },
    /*
    退出登录函数
     */
    handleLogout() {
      // 执行登出逻辑，比如清除本地存储的token
      this.clearAuthToken();
      //清除本地用户信息
      router.push('/login');
      this.$message('已成功登出账号！');
    },
    clearAuthToken() {
      // 清除token的逻辑
      // 例如: localStorage.removeItem('token');
      sessionStorage.clear();
    },
    /*
    提交密码修改
     */
    async confirmPasswordChange() {
      if(this.codeForm.oldPwd === sessionStorage.getItem('uPassword')){
        if (this.codeForm.newPwd1 === this.codeForm.newPwd2) {
          // 密码匹配，提交更改
          try {
            const response = await put("/api/v1.0/user/modifyPassword", {
              email: sessionStorage.getItem('uEmail'),
              originPsw: this.codeForm.oldPwd,
              currentPsw: this.codeForm.newPwd1
            });
            console.log("登录："+response)
            if (response.code === 1) {
              sessionStorage.setItem("uPassword", this.codeForm.newPwd1)
              console.log("密码："+sessionStorage.getItem("uPassword"))
              this.dialogFormVisible1 = false;
              this.$message.success("修改成功！");
            } else {
              this.$message.error("修改失败！"+response.msg);
            }
          } catch (error) {
            console.error(error);
          }
        } else {
          // 密码不匹配，提示用户
          this.$message.error('两次输入的密码不一致');
        }
      } else{
        // 原密码错误
        this.$message.error('原密码错误！');
      }
    },
    /*
    提交用户名修改
     */
    async confirmNameChange() {
      if(this.newName){
        // 输入不为空，提交更改
        try {
          const respName = await put('/api/v1.0/user/modifyUsername', {
            email: sessionStorage.getItem('uEmail'),
            username: this.newName,
          });
          if(respName.code === 1){
            this.$message.success(this.newName + '信息修改成功！');
            //更新存储的用户名
            console.log(sessionStorage.getItem('uName'),)
            sessionStorage.setItem('uName', this.newName);
            this.uName = this.newName; // 这里直接更新 uName 来触发视图更新
            this.dialogFormVisible2 = false;
          }else{
            this.$message.error(respName.msg);
          }
        } catch (error) {
          console.error(error);
        }
      } else{
        this.$message.error('姓名不得为空！');
      }
    },
  },
}
</script>

<style scoped>
.header {
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  background-color: transparent;
}
.el-dropdown-link {
  display: flex;
  align-items: center;
  margin-right: 64px;
  font-size: 24px;
  font-weight: bold;
  font-family: '楷体', 'KaiTi', '楷体_GB2312';
  cursor: pointer;
}
.dialog-footer {
  display: flex;
  justify-content: center;
}


.el-popper.is-customized {
  /* Set padding to ensure the height is 32px */
  padding: 6px 12px;
  background: linear-gradient(90deg, rgb(159, 229, 151), rgb(204, 229, 129));
}

.el-popper.is-customized .el-popper__arrow::before {
  background: linear-gradient(45deg, #b2e68d, #bce689);
  right: 0;
}
</style>