<template>
  <div class="main-body">
    <div class="form">
      <h1 class="login-title">欢迎登录</h1>
    </div>
    <div class="login">
      <el-form ref="formInline" :model="formInline" :rules="ruleInline">
        <el-form-item prop="username">
          <el-input
            type="text"
            v-model="formInline.username"
            placeholder="请输入用户名"
            prefix-icon="el-icon-user"
            :rules="[
              { required: true, message: '用户名不能为空'}
              ]"
            clearable>
          </el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input
            v-model="formInline.password"
            placeholder="请输入密码"
            prefix-icon="el-icon-lock"
            :rules="[
              { required: true, message: '密码不能为空'}
              ]"
            show-password>
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="handleSubmit">登录</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>
<script>
import { login } from '@/apis/index'
export default {
  data () {
    return {
      modal_loading: false,
      formInline: {
        username: '',
        password: ''
      },
      ruleInline: {
        username: [
          {
            required: true,
            message: 'Please enter the user name',
            trigger: 'blur'
          }
        ],
        password: [
          {
            required: true,
            message: 'Please enter the password',
            trigger: 'blur'
          }
        ]
      }
    }
  },
  methods: {
    handleSubmit () {
      // 获取小结的内容
      let username = this.formInline.username
      let password = '123456'
      login(username, password).then((resp) => {
        // resp: django后端返回的数
        console.log(resp)
      }).concat((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style scoped>
.form {
  text-align: center;
  width: 400px;
  margin: 0 auto;
  margin-top: 30px;
  margin-bottom: 25px;
}
.form h1 {
  font-size: 24px;
  font-weight: 100;
  letter-spacing: -0.5px;
}
.login {
  width: 308px;
  margin: 0 auto;
  border: 1px solid #d8dee2;
  height: 257px;
  border-radius: 5px;
  padding: 20px;
  font-size: 14px;
  margin-bottom: 15px;
}
.prompt {
  font-size: 13px;
  font-weight: 600;
}
.btn {
  font-weight: 600;
}
.register-link {
  margin: 0 auto;
  width: 308px;
  padding: 15px 20px;
  text-align: center;
  border: 1px solid #d8dee2;
  border-radius: 5px;
}
</style>
