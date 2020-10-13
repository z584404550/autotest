import axios from 'axios' // 相当于js中的ajax
import { LoadingBar } from 'iview'
// import qs from 'qs' // 处理数据以便传给后端

const isDev = process.env.NODE_ENV === 'development' // 判断是否为开发环境

// 定义变量ajax（相当于ajax等价于axios）
const ajax = axios.create({
  baseURL: isDev ? 'http://172.0.0.1:8000' : 'http://172.0.0.1:8000'
  // 前者：开发环境
  // 后者：非开发环境（因为没有部署到服务器，所以都设置为本地，django运行端口为8000
})

// 设置拦截器（vue中的操作，异步操作请求前与请求后的响应）
ajax.interceptors.request.use((config) => {
  LoadingBar.start()
  return config
})

ajax.interceptors.response.use((resp) => {
  if (resp.status === 200) {
    LoadingBar.finish()
    return resp.data
  }
})

// 定义登录方法
// 用户登录（需要传给后端一个headers）
export const userLogin = (username, password, headers) => {
  return ajax({
    url: '/login',
    method: 'post', // post方法
    responseType: 'josn', // json格式
    // 对数据进行处理（否则后端接受不到）
    data: qs.stringify({'username': username, 'password': password}),
    headers: {
      'X-CSRFToken': headers
    }
  })
}
