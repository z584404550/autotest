import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    // 存储token
    Authorization: localStorage.getItem('Authorization') ? localStorage.getItem('Authorization') : '',
    UserName: localStorage.getItem('UserName') ? localStorage.getItem('UserName') : ''
  },
  getters: {
    getToken: function (state) {
      if (!state.Authorization) {
        state.Authorization = JSON.parse(localStorage.getItem('Authorization'))
      }
      return state.Authorization
    },
    getUserName: function (state) {
      if (!state.UserName) {
        state.UserName = JSON.parse(localStorage.getItem('UserName'))
      }
      return state.UserName
    }
  },
  mutations: {
    setToken (state, token) {
      state.Authorization = token
      localStorage.setItem('Authorization', token)
    },
    setUserName (state, user) {
      state.user = user
      localStorage.setItem('UserName', user)
    }
  },
  actions: {

  }
})

export default store
