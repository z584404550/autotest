<template>
  <div class="main-body">
    <div class="form">
      <Icon type="logo-octocat" size="60" />
      <h1>Create your account</h1>
    </div>
    <div class="login">
      <Form ref="formInline" :model="formInline" :rules="ruleInline">
        <FormItem prop="user">
          <div class="prompt">Username</div>
          <Input type="text" v-model="formInline.user" placeholder="Username" clearable>
            <Icon type="ios-person" slot="prepend" size="16"></Icon>
          </Input>
        </FormItem>
        <FormItem prop="email">
          <div class="prompt">Email address</div>
          <Input type="text" v-model="formInline.email" placeholder="Email address" clearable>
            <Icon type="ios-mail" slot="prepend" size="16"></Icon>
          </Input>
        </FormItem>
        <FormItem prop="password">
          <div class="prompt">Password</div>
          <Input
            type="password"
            v-model="formInline.password"
            placeholder="Password"
            clearable
            @keyup.enter.native="handleSubmit('formInline')"
          >
            <Icon type="ios-lock" slot="prepend" size="16"></Icon>
          </Input>
        </FormItem>
        <FormItem>
          <Button
            class="btn"
            type="primary"
            size="large"
            long
            :loading="modal_loading"
            @click="handleSubmit('formInline')"
          >Create new</Button>
        </FormItem>
      </Form>
    </div>
    <p class="register-link">
      Have a JiaGE account?
      <router-link to="/account/login">Sign in.</router-link>
    </p>
  </div>
</template>

<script>
export default {
  methods: {
    handleSubmit (name) {
      this.$refs[name].validate(valid => {
        if (valid) {
          this.modal_loading = true
          var username = this.formInline.user
          var password = this.formInline.password
          var email = this.formInline.email
          this.$http
            .userRegister(
              email,
              username,
              password,
              this.getCookie('csrftoken')
            )
            .then(resp => {
              if (resp.result.code === '200') {
                this.$router.push({
                  path: '/login'
                })
                this.$Message.success(resp.result.msg)
              } else {
                this.$Message.error(resp.result.msg)
              }
              this.modal_loading = false
            })
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
