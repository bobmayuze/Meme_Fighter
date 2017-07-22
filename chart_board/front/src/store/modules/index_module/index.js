import * as types from '../../mutation-types'

// initial state

const state = {
  test_state: false,
  data_arr:{},
  image_data:[],
  image_data_name: [],
}

// getters
const getters = {
  get_test: state => state.test_state,
  get_data_arr: state => state.data_arr,
  get_image_data: state => state.image_data,
  get_image_data_name: state => state.image_data_name,
}

// actions
const actions = {
  [types.TEST_INDEX_STATE] ({ commit, state }, is_true) {
    commit(types.TEST_INDEX_STATE, is_true)
  },

  [types.SET_DATA_ARR] ({ commit, state }, {data_name, data_val}) {
    commit(types.SET_DATA_ARR, {data_name, data_val});
  },
  [types.SET_IMAGE_DATA] ({ commit, state }, data) {
    commit(types.SET_IMAGE_DATA, data);
  },
  [types.SET_IMAGE_DATA_NAME] ({ commit, state }, data_name) {
    commit(types.SET_IMAGE_DATA_NAME, data_name);
  },
}

// mutations likes reducer
const mutations = {
  [types.TEST_INDEX_STATE] (state, is_true) {
    state.test_state = is_true
  },
  [types.SET_DATA_ARR] (state, {data_name, data_val}) {
    if(state.data_arr[data_name] === undefined)
      state.data_arr[data_name] = [];
    // let sum = 0;
    // state.data_arr[data_name].forEach((item_val) => {
    //   sum += item_val;
    // })
    state.data_arr[data_name].push(data_val);
  },

  [types.SET_IMAGE_DATA] (state, data) {
    state.image_data = data
  },
  [types.SET_IMAGE_DATA_NAME] (state, data_name) {
    state.image_data_name = data_name
  },
}

export default {
  state,
  getters,
  actions,
  mutations
}