import Vue from 'vue'
import Router from 'vue-router'
import store from '../store/store'
// import HelloWorld from '@/components/HelloWorld'
import Login from '../components/login/Login'
import Home from '../components/home/Home'
import Register from '../components/login/Register'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    // {
    //   path: '/',
    //   name: 'HelloWorld',
    //   component: HelloWorld
    // },
    {
      path: '/',
      redirect: '/home'
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/home',
      name: 'Home',
      meta: {
        requireAuth: true
      },
      component: Home
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.meta.requireAuth) {
    if (store.state.token) {
      next()
    } else {
      next({
        path: '/login',
        query: {redirect: to.fullPath}// 将跳转的路由path作为参数，登录成功后跳转到该路由
      })
    }
  } else {
    next()
  }
})
