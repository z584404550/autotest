/* *axios封装
 * 请求拦截、相应拦截、错误统一处理
 */
import axios from 'axios'
import qs from 'qs'
// import Router from '../router/index.js'
//
// 环境的切换
if (process.env.NODE_ENV === 'development') {
  axios.defaults.baseURL = 'http://127.0.0.1:8000'
} else if (process.env.NODE_ENV === 'debug') {
  axios.defaults.baseURL = 'http://127.0.0.1:8000'
} else if (process.env.NODE_ENV === 'production') {
  axios.defaults.baseURL = 'http://127.0.0.1:8000'
}

// 请求超时时间
axios.defaults.timeout = 10000

// post请求头
// axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8'
// axios.defaults.headers.post['Content-Type'] = 'application/json'

// 请求拦截器
axios.interceptors.request.use(
  config => {
    // 每次发送请求之前判断是否存在token，如果存在，则统一在http请求的header都加上token，不用每次请求都手动添加了
    // 即使本地存在token，也有可能token是过期的，所以在响应拦截器中要对返回状态进行判断
    // const token = store.state.token
    // token && (config.headers.Authorization = token)
    return config
  },
  error => {
    return Promise.error(error)
  })

// 响应拦截器
axios.interceptors.response.use(
  response => {
    if (response.status === 200) {
      return Promise.resolve(response)
    } else {
      return Promise.reject(response)
    }
  }
)

// 定义登录方法
export const login = (username, password) => {
  return axios({
    url: '/login/',
    method: 'post', // post方法
    responseType: 'json', // json的格式
    // 对数据进行处理（否则后端接收不到）
    data: qs.stringify({ 'username': username, 'password': password })
  })
}
