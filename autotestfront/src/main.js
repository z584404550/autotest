// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import iView from 'iview'
import 'iview/dist/styles/iview.css'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import * as $http from './request/index'// 从index.js文件引入

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})

Vue.use(ElementUI)
Vue.use(iView)

Vue.config.productionTip = false
Vue.prototype.$http = $http
// 对于一个vue脚手架项目来说，在main.js里使用Vue.prototype声明的变量，
// 实际上是为Vue对象添加了一个原型属性，而不是一个全局变量。但是如果这个原型属性的值是引用类型的，
// 我们就可以借此实现全局变量 。当你在main.js里声明了Vue.prototype.a = 1后，因为你的每一个vue组件都是一个Vue对象的实例
// 所以即使你没有在组件内部使用data(){return{……}}声明a，你依然可以在组件中通过this.a来访问
