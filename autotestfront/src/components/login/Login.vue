<template>
  <div class="main-body">
    <div class="form">
      <Icon type="logo-octocat" size="60" />
      <h1>Sign in to JiaGE</h1>
    </div>
    <div class="login">
      <Form ref="formInline" :model="formInline" :rules="ruleInline">
        <FormItem prop="user">
          <div class="prompt">Username or email address</div>
          <Input id="username" type="text" v-model="formInline.username" placeholder="请输入用户名" clearable>
            <Icon type="ios-person" slot="prefix" size="16"></Icon>
          </Input>
        </FormItem>
        <FormItem prop="password">
          <div class="prompt" style="float: left">Password</div>
          <div class="prompt" style="float: right">
            <a>Forgot password?</a>
          </div>
          <Input id="password" type="password" v-model="formInline.password" placeholder="请输入密码" clearable show-password>
            <Icon type="ios-lock" slot="prefix" size="16"></Icon>
          </Input>
        </FormItem>
        <FormItem>
          <Button id="submit" class="btn" type="primary" size="large" long :loading="modal_loading" @click="loginSubmit('formInline')">登&nbsp;&nbsp;录</Button>
        </FormItem>
      </Form>
    </div>
    <p class="register-link">
      New to JiaGE?
      <router-link to="/account/register">Create an account.</router-link>
    </p>
  </div>
</template>
<script>
import { login } from '@/apis/index'
// import store from '@/store'
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
            message: 'Please enter the username',
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
    loginSubmit (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.modal_loading = true
          let username = this.formInline.username
          let password = this.formInline.password
          login(username, password).then(resp => {
            console.log(resp)
            if (resp.data.status === 200) {
              this.$store.commit('setToken', resp.data.data.token)
              this.$store.commit('setUserName', resp.data.data.username)
              this.$router.push({path: '/home'})
            } else {

            }
          })
        }
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
