import Vue from 'vue'
import Vuex from 'vuex'
import index_state from './modules/index_module/';

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default  new Vuex.Store({
  modules: {
    index_state
  },
  strict: debug,
})