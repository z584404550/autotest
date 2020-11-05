import Vue from 'vue'
import Vuex from 'vuex'
import  VuexPersistence from 'vuex-persist'

Vue.use(Vuex)
const vuexLocal =new VuexPersistence({
  storage: window.localStorage,
  reducer: state => ({
    token: state.token,
    WXTempKey: state.WXtempKey
  })
})

const store = new Vuex.Store({
  state:{
    token: "",
    WXTempKey: "",
    isLogin: false,
    uid: 0,
    name: "",
    avatar: ""
  },
  mutations: {
    setToken(state, token) {
      state.token = token
    },
    setLogin(state, flag) {
      state.isLogin = flag
    },
    estWXTempKey(state,WXTempKey) {
      state.WXTempKey = WXTempKey
    },
  },
  actions: {},
  plugins: [vuexLocal.plugin]
})

export default store
