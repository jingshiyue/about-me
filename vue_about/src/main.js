// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import myApp from './App'
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: {
    myApp
  },
  template: '<my-app></my-app>'
  // 在index.html中创建一个<app></app>标签代替div#id=app标签，然后用App.vue里的内容在覆盖<app></app>。
  // 通常在componet中用template较多，直接在new Vue()的配置中添加template在以前学习时见得不多。
  // 本质：无论是new Vue()的instance还是component，它们的本质都是vue的instance，配置都差不多。
  // 即：组件是可复用的 Vue 实例。
})
