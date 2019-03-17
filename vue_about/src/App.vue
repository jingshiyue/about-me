<template>
  <div id="app">
    <div class="left-side">
      <Action/>
      <SendMessage/>
      <SideNav/>
      <About/>
    </div>

    <div class="right-side">
      <Ppt/>
      <InfoCard/>
    </div>

    <div class="side-btn" v-on:click="side_btn"></div>

    <!-- <Main/> -->
  </div>
</template>
<script>
import Action from "./components/Action/Action.vue";
import SendMessage from "./components/Send_message/Send_message";
import SideNav from "./components/Side_nav/Side_nav";
import About from "./components/About/About";

import Ppt from "./components/Ppt/Ppt";
import InfoCard from "./components/Info_card/Info_card";
export default {
  name: "App",
  components: {
    Action,
    SendMessage,
    SideNav,
    About,
    Ppt,
    InfoCard
  },
  methods: {
    side_btn: function() {
      var left_side = document.querySelector(".left-side");
      // var side_display = left_side.style.display;// 设置一个变量，后面不用重复写。但是这是写法没有效果，以前也遇见过这个问题。
      if (left_side.style.display == "") {
        left_side.style.display = "block";
        left_side.classList.add("side-block");
      } else {
        if (left_side.style.display == "block") {
          left_side.style.display = "none";
        } else {
          left_side.style.display = "block";
        }
      }
    }
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  width: 100%;
  max-width: 960px;
  min-width: 320px;
  margin: 0 auto;
  display: flex;
  font-size: 0.16rem;
}
.left-side {
  width: 25%;
}
.left-title {
  line-height: 0.36rem;
  padding-left: 0.4rem;
  background-repeat: no-repeat;
  background-size: 0.26rem 0.26rem;
  background-position: 0.1rem center;
  background-color: rgba(18, 150, 219, 1);
  color: #fff;
}
.right-side {
  width: 75%;
  margin-left: 0.2rem;
}
.side-btn {
  display: none;
  background-image: url(./components/App.vue/展开.png);
  background-size: 0.3rem 0.3rem;
  background-repeat: no-repeat;
  background-position: center;
}
.side-block {
  width: 70% !important; /* 为什么没有动画效果 */
  transition: all 2s;
  position: absolute;
  z-index: 99;
}
.side-none {
  transition: all 1s;
}
</style>
