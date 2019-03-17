<template>
    <div id="side-nav">
        <ul>
          <div class="left-title side-nav-title">导航</div>
          <li v-for='title in title' :key="title.id"><a :href="'#'+title.id">{{title.title}}</a></li>
        </ul>
      </div>
</template>

<script>
export default {
  name: "side_nav",
  data() {
    return {
      title: [
        { title: "基本信息", id: "title-base" },
        { title: "教育经历", id: "title-edu" },
        { title: "工作经历", id: "title-job" },
        { title: "项目展示", id: "title-project" },
        { title: "技术栈", id: "title-stack" }
      ]
    };
  },
  methods: {},
};
</script>

<style>
#side-nav {
  width: 100%;
  margin-top: 0.2rem;
}
.side-nav-title {
  background-image: url(./img/导航.png);
  padding-left: 0.4rem;
  background-size: 0.22rem 0.22rem;
}
#side-nav > ul > li {
  /* text-align: center; */
  padding-left: 0.68rem;
  line-height: 0.5rem;
  background-image: url(./img/标题.png);
  background-position: 0.4rem center;
  background-repeat: no-repeat;
  background-size: 0.22rem 0.22rem;
  background-color: #fff;
  margin-bottom: 0.02rem;
}
</style>

