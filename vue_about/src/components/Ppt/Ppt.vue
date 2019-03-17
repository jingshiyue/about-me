<template>
    <div id = "ppt">
        <ul class="clearfix img-list">
            <li>
                <img src="./img/img5.png" alt="" class="ppt-img">
            </li>
            <li>
                <img src="./img/img1.png" alt="" class="ppt-img">
            </li>
            <li>
                <img src="./img/img2.png" alt="" class="ppt-img">
            </li>
            <li>
              <img src="./img/img3.png" alt="" class="ppt-img">
            </li>
            <li>
              <img src="./img/img4.png" alt="" class="ppt-img">
            </li>
            <li>
              <img src="./img/img5.png" alt="" class="ppt-img">
            </li>
            <li>
              <img src="./img/img1.png" alt="" class="ppt-img">
            </li>
        </ul>
        <div>
            <span class="active"></span><span></span><span></span><span></span><span></span>
        </div>
    </div>
</template>

<script>
export default {
  name: "ppt",
  methods: {
    ppt: function() {
      var img_num = document.getElementsByClassName("ppt-img").length;
      // var img_width1 = document.querySelector("#ppt").offsetWidth;
      // console.log('a',img_width1)
      // var img_width2 = document.getElementsByClassName("ppt-img")[0].width;// 两者的区别，offsetWidth(div,100%) 与 width(img,100%)
      // console.log('b',img_width2);
      var img_list = document.getElementsByClassName("img-list")[0];
      var img_index = document.getElementsByTagName("span");
      var index = 1;
      setInterval(function() {
        index++;
        // console.log(index);

        img_list.style.transition = "all 0.5s"; //兼容性问题，暂时略过
        img_list.style.transform = "translateX(" + -14.2857 * index + "%)";

        img_list.addEventListener("transitionend", function() {
          // 用 addEventListener 添加 transitionend 事件，ael与on的区别，不会覆盖。
          // 相当于一个中断。
          if (index >= 6) {
            index = 1;
            // 这里需要先清除过渡，不然显示的效果不是瞬间定位，而是有动画效果。
            img_list.style.transition = "none";
            img_list.style.transform =
              "translateX(" + -14.2857 * index + "%)";
          }
          for (var i = 0; i < img_index.length; i++) {
            img_index[i].classList.remove("active");
          }
          img_index[index - 1].classList.add("active");
        });
      }, 3000);
    }
  },
  mounted() {
    this.ppt();
  }
};
</script>

<style scoped>
#ppt {
  width: 100%;
  position: relative;
  overflow: hidden;
}
#ppt > ul {
  width: 700%;
  transform: translateX(-14.2857%);
}
#ppt > ul > li {
  width: 14.2857%;
  float: left;
}
.ppt-img {
  width: 100%;
}
#ppt > div {
  position: absolute;
  left: 50%;
  margin-left: -0.8rem;
  bottom: 0.15rem;
  z-index: 9;
  width: 1.6rem;
  display: flex;
  justify-content: space-between;
}
#ppt > div > span {
  display: block;
  height: 0.1rem;
  width: 0.1rem;
  background-color: #1296db;
  border-radius: 0.1rem;
  cursor: pointer;
}
#ppt .active {
  background-color: #fff;
}
</style>
