import Vue from 'vue'
import Router from 'vue-router'

//pages

import Hack from '@/views/Hack';
import Detail from '@/views/Detail';
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Hack
    },
    {
      path: '/detail',
      name: 'Detail',
      component: Detail
    }
  ]
})
