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
          <i-Input type="text" v-model="formInline.user" placeholder="Username or Email" clearable>
            <Icon type="ios-person" slot="prepend" size="16"></Icon>
          </i-Input>
        </FormItem>
        <FormItem prop="password">
          <div class="prompt" style="float: left">Password</div>
          <div class="prompt" style="float: right">
            <a>Forgot password?</a>
          </div>
          <i-Input type="password" v-model="formInline.password" placeholder="Password" clearable>
            <Icon type="ios-lock" slot="prepend" size="16"></Icon>
          </i-Input>
        </FormItem>
        <FormItem>
          <Button
            class="btn"
            type="success"
            size="large"
            long
            :loading="modal_loading"
            @click="handleSubmit('formInline')"
          >Sign in</Button>
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
// @符号指的是src路径
export default {
  // vue页面中双向绑定数据
  data () {
    return {title: '测试axios'}
  },
  // vue生命周期中挂在的函数
  mounted () {

  },
  methods: {
    requetLogin () {
      // 获取小结的内容
      let username = 'admin'
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
