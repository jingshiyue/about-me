<template>
    <div id="about">
        <div class="left-title about-title">关于</div>
        <div class="about-content">
            <div>
              <p>本站前后端分离，响应式布局。前端使用 Vue，后端使用 <a href="http://www.django-rest-framework.org/">Django REST framework</a>。</p>
              <p>部署在阿里云服务器。</p>
            </div>
            <div>
              <p>后台演示：</p>
              <a :href="pro_host+'admin'" target="_blank">{{pro_host+'admin/'}}</a>
              <p>账号：test</p>
              <p>密码：test.123</p>
            </div>
            <div>
              <p>部分 api 如下：</p>
              <a :href="pro_host+'api'" target="_blank">{{pro_host+'api/'}}</a>
            </div>
            <div>
              <p>api 默认文档：</p>
              <a :href="pro_host+'docs'" target="_blank">{{pro_host+'docs/'}}</a>
            </div>
            <div>
              <p>兼容性：</p>
              <p>本站使用了一些较新技术，对IE浏览器的兼容性有待改善。</p>
            </div>              
            
        </div>
    </div>
</template>

<script>
export default {
  name: "about",
  data() {
    return {
      host: "http://127.0.0.1:8000/",
      pro_host:'http://api.innocosme.com/'
    };
  }
};
</script>

<style>
#about {
  margin-top: 0.2rem;
  width: 100%;
}
.about-content {
  padding: 0.15rem;
  font-size: 0.14rem;
  background-color: #fff;
}
.about-title {
  background-image: url(./img/关于.png);
  background-size: 0.22rem 0.22rem;
}
.about-content > div:nth-child(1) ~ div {
  margin-top: 0.1rem;
}
</style>
