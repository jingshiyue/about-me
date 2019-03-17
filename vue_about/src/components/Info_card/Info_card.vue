<template>
  <div id="info-card">
    <div class="base-info">
      <h2 class="title-l2" :id="title[0].id">{{title[0].title}}</h2>
      <ul v-for="(item,index) in base_info" :key="index">
        <li>
          <div>姓名：</div>
          <div>{{item.name}}</div>
        </li>
        <li>
          <div>性别：</div>
          <div>{{item.sex}}</div>
        </li>
        <li>
          <div>年龄：</div>
          <div>{{item.age}}</div>
        </li>
        <li>
          <div>学历：</div>
          <div>本科 / 统招</div>
        </li>
        <li>
          <div>手机：</div>
          <div>
            <a :href="'tel:'+item.mobile_phone">{{item.mobile_phone}}</a>
          </div>
        </li>
        <li>
          <div>邮箱：</div>
          <div>
            <a :href="'mailto:'+item.email">{{item.email}}</a>
          </div>
        </li>
        <li>
          <div>住址：</div>
          <div>{{item.address}}</div>
        </li>
      </ul>
    </div>

    <div class="edu-info">
      <h2 class="title-l2" :id="title[1].id">{{title[1].title}}</h2>
      <ul v-for="(item,index) in edu_info" class="clearfix" :key="index">
        <li class="title-num">{{index+1}}</li>
        <li>{{item.university}}</li>
        <li>{{item.major}}</li>
        <li>{{item.date_begin|date_y_m}} — {{item.date_end|date_y_m}}</li>
      </ul>

      <div class="certificate clearfix">
        <div class="title-small certificate-title">证书</div>
        <ul v-for="(item,index) in certificate_info" class="clearfix" :key="index">
          <li class="title-num">{{index+1}}</li>
          <li>{{item.name}}</li>
        </ul>
      </div>
    </div>

    <div class="job-info">
      <h2 class="title-l2" :id="title[2].id">{{title[2].title}}</h2>
      <ul v-for="(item,index) in job_info" :key="index">
        <li class="title-num">{{index+1}}</li>
        <li>{{item.company}}</li>
        <li>{{item.position_name}}</li>
        <li>{{item.date_begin|date_y_m}} — {{item.date_end|date_y_m}}</li>
        <li>
          <div class="title-small">工作描述</div>
          <div class="text-desc">{{item.position_desc}}</div>
        </li>
        <li>
          <div class="title-small">离职原因</div>
          <div class="text-desc">{{item.why_leave}}</div>
        </li>
      </ul>
    </div>

    <div class="project-info">
      <h2 class="title-l2" :id="title[3].id">{{title[3].title}}</h2>
      <ul v-for="(item,index) in project_info" class="clearfix" :key="index">
        <li class="title-num">{{index+1}}</li>
        <li>{{item.pro_name}}</li>
        <li>
          <a class="pro_url" :href="item.pro_url" target="_blank">{{item.pro_url}}</a>
        </li>
        <li>
          <div class="title-small">项目描述</div>
          <div class="text-desc">{{item.desc}}</div>
        </li>
        <li>
          <div class="title-small">使用技术</div>
          <div class="text-desc">{{item.technology_stack}}</div>
        </li>
      </ul>
    </div>

    <div class="stack">
      <h2 class="title-l2" :id="title[4].id">{{title[4].title}}</h2>
      <ul v-for="(item,index) in stack_info" :key="index">
        <li class="title-small stack-title">{{item.name}}</li>
        <li>
          <ul v-for="(tech,index) in item.techs" class="tech-list clearfix" :key="index">
            <li :title="tech.desc">{{tech.name}}</li>
            <li>{{tech.degress}}</li>
            <!-- <li :style="'width:'+ tech.degress_precentage*0.7+'%'">{{tech.degress_precentage}}</li> -->
            <!-- <li>{{tech.desc}}</li> -->
            <li
              :style="{width:tech.degress_precentage*0.7+'%',backgroundColor:'rgba(18,150,219,'+tech.degress_precentage/100+')' }"
            >{{tech.degress_precentage}}</li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import {
  get_base_info,
  get_edu_info,
  get_certificate_info,
  get_job_info,
  get_project_info,
  get_stack_info
} from "../../api/api";

export default {
  name: "info_card",
  data() {
    return {
      title: [
        { title: "基本信息", id: "title-smallase" },
        { title: "教育经历", id: "title-edu" },
        { title: "工作经历", id: "title-job" },
        { title: "项目展示", id: "title-project" },
        { title: "技术栈", id: "title-stack" }
      ],
      base_info: "",
      edu_info: "",
      certificate_info: "",
      job_info: "",
      project_info: "",
      stack_info: ""
    };
  },
  methods: {
    get_base_info() {
      get_base_info({
        // params: {}
      })
        .then(response => {
          // console.log(response.data);
          this.base_info = response.data;
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    get_edu_info() {
      get_edu_info({
        // params: {}
      })
        .then(response => {
          // console.log(response.data);
          this.edu_info = response.data;
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    get_certificate_info() {
      get_certificate_info({})
        .then(response => {
          // console.log(response.data);
          this.certificate_info = response.data;
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    get_job_info() {
      get_job_info({})
        .then(response => {
          // console.log(response.data);
          this.job_info = response.data;
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    get_project_info() {
      get_project_info({})
        .then(response => {
          // console.log(response.data);
          this.project_info = response.data;
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    get_stack_info() {
      get_stack_info({})
        .then(response => {
          // console.log(response.data);
          this.stack_info = response.data;
        })
        .catch(function(error) {
          console.log(error);
        });
    }
  },
  filters: {
    date_y_m: function(val) {
      return val.slice(0, 7);
    }
  },
  created() {
    this.get_base_info();
    this.get_edu_info();
    this.get_certificate_info();
    this.get_job_info();
    this.get_project_info();
    this.get_stack_info();
  }
};
</script>

<style>
.base-info,
.base-info ~ div {
  box-sizing: border-box;
  padding: 0.1rem 0.2rem;
  width: 100%;
  border-radius: 0.1rem;
  margin-top: 0.2rem;
  background-color: #fff;
}

.title-l2 {
  font-weight: normal;
  font-size: 0.16rem;
  width: 1rem;
  color: #fff;
  height: 0.3rem;
  line-height: 0.3rem;
  text-align: center;
  margin: 0 auto;
  margin-top: -0.25rem;
  border-radius: 0.1rem;
  background-color: #1296db;
}
.title-num {
  width: 10%;
  text-align: center;
  font-weight: bold;
}
.title-small {
  background-color: #41abe2;
  color: #fff;
  text-align: center;
  width: 0.8rem;
}
.base-info > ul {
  display: flex; /* 方法一，使用flex。*/
  flex-wrap: wrap;
}
.base-info > ul > li {
  width: 33.333%;
  border-bottom: #aaa solid 1px;
  display: flex;
}
.base-info > ul > li:last-child {
  width: 50%;
  text-align: left;
}
.base-info div {
  line-height: 0.3rem;
  height: 0.3rem;
}
.base-info > ul div:nth-child(odd) {
  flex: 1;
  color: #aaa;
}
.base-info > ul div:nth-child(even) {
  flex: 2;
}
.edu-info > ul > li {
  float: left; /* 方法二，使用float*/
  line-height: 0.3rem;
  border-bottom: #aaa solid 1px;
}
.edu-info > ul > li:nth-child(1) {
  width: 10%;
}
.edu-info > ul > li:nth-child(2) {
  width: 40%;
}
.edu-info > ul > li:nth-child(3) {
  width: 20%;
}
.edu-info > ul > li:nth-child(4) {
  width: 30%;
  text-align: center;
}
.certificate-title {
  line-height: 0.3rem;
  margin: 0.1rem 0 0.05rem;
}
.edu-info > div:nth-child(4) > ul {
  width: 50%;
  float: left;
  border-bottom: #aaa solid 1px;
}

.edu-info > div:nth-child(4) > ul > li {
  /* 在这里遇到一点小问题，讲nth-child(4)，写成了3。for 循环，两个*/
  /* 要想自动换行后文字不重叠，不要设置高度，可以只设置行高。 */
  float: left;
  line-height: 0.3rem;
}
.edu-info > div:nth-child(4) > ul > li:nth-child(1) {
  width: 20%;
}

.text-desc {
  padding-left: 0.06rem;
  background-color: #eee;
  display: inline-block;
  width: 100%;
}

.job-info > ul {
  font-size: 0;
  padding-top: 0.06rem;
  padding-bottom: 0.04rem;
  border-bottom: #aaa solid 1px;
}

.job-info > ul > li {
  display: inline-block; /* 方法三，使用inline-block。*/
  font-size: 0.16rem;
  line-height: 0.3rem;
}

.job-info > ul > li:nth-child(1) {
  width: 10%;
}
.job-info > ul > li:nth-child(2) {
  width: 40%;
}
.job-info > ul > li:nth-child(3) {
  width: 20%;
}
.job-info > ul > li:nth-child(4) {
  width: 30%;
  text-align: center;
}
.job-info > ul > li:nth-child(5),
.job-info > ul > li:nth-child(6) {
  display: flex;
  width: 100%;
  font-size: 0.14rem;
  line-height: 0.26rem;
}
.job-info > ul > li:nth-child(6) {
  margin-top: 0.02rem;
}
.project-info > ul {
  padding-top: 0.06rem;
  padding-bottom: 0.04rem;
  border-bottom: #aaa solid 1px;
}
.project-info > ul > li {
  float: left;
  line-height: 0.3rem;
}
.project-info > ul > li:nth-child(1) {
  width: 10%;
}
.project-info > ul > li:nth-child(2) {
  width: 40%;
}
.project-info > ul > li:nth-child(3) {
  width: 50%;
}
.project-info > ul > li:nth-child(3) > a {
  /* text-decoration: underline; */
  background-color: #ccc;
}
.project-info > ul > li:nth-child(4),
.project-info > ul > li:nth-child(5) {
  display: flex;
  width: 100%;
  font-size: 0.14rem;
  line-height: 0.26rem;
}
.project-info > ul > li:nth-child(5) {
  margin-top: 0.02rem;
}
/* .project-info .pro_url{
  text-decoration: none;
} */
.stack-title {
  margin: 0.1rem 0 0.05rem;
  line-height: 0.3rem;
}
.tech-list > li {
  float: left;
  line-height: 0.2rem;
  font-size: 0.14rem;
}
.tech-list > li:nth-child(1) {
  width: 25%;
  border-bottom: #aaa solid 1px;
}
.tech-list > li:nth-child(2) {
  width: 10%;
  border-bottom: #aaa solid 1px;
  text-align: center;
}
.tech-list > li:nth-child(3) {
  background-color: #aaa;
  color: #fff;
  border-radius: 0.1rem;
  text-align: center;
  height: 0.14rem;
  line-height: 0.17rem;
  margin-left: 0.1rem;
  margin-top: 0.03rem;
}
</style>
