<template>
  <div>
    测试axios-{{title}}
    <button @click="requetLogin">登录</button>
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
      // let date = {
      //   username: 'admin', password: '123456'
      // }
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

</style>
