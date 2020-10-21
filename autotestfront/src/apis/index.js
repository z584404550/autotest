/* eslint-disable */
// 接口信息，生成请求方法
// 引用 get方法，post方法

import {get, post} from './index'

// 用户登录
export const login = (params, headers) => post('/user/login/', params ,headers)
