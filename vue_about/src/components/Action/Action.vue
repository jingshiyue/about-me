<template>
  <div id="action">
    <ul v-for="(item,index) in action_num_info" :key="index">
      <li>
        <div class="left-title action-title like-me" v-on:click="num_add_like(item.like_me_num)">喜欢我</div>
        <div class="action-num">{{item.like_me_num}}</div>
      </li>
      <li>
        <div class="left-title action-title not-like" v-on:click="num_add_not(item.not_like_num)">不喜欢</div>
        <div class="action-num">{{item.not_like_num}}</div>
      </li>
      <li>
        <div class="left-title action-title like-or-not" v-on:click="num_add_or(item.like_or_not_num)">再看看</div>
        <div class="action-num">{{item.like_or_not_num}}</div>
      </li>
      <li>
        <div class="left-title watch-num">浏览量</div>
        <div class="action-num">{{visite_num.visite_num}}</div>
      </li>
    </ul>
  </div>
</template>

<script>
import {
  get_action_num_info,
  get_visite_num,
  post_action_num_info
} from "../../api/api";
export default {
  // name: "action",
  data() {
    return {
      action_num_info: "",
      visite_num: ""
    };
  },
  methods: {
    // get_action_num_info: function() {
    //   get_action_num_info()
    //     .then(res => {
    //       console.log(res.data)
    //       this.action_num_info = res.data;
    //     })
    //     .catch(e => {
    //       console.log(e);
    //     });
    // },
    // es6简单语法。
    get_action_num_info() {
      get_action_num_info()
        .then(response => {
          this.action_num_info = response.data;
          // console.log(this.action_num_info[0])
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    get_visite_num() {
      get_visite_num()
        .then(response => {
          this.visite_num = response.data;
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    num_add_like: function(now_num) {
      var add_next_num = now_num + 1;
      // console.log(typeof add_next_num);
      post_action_num_info({ like_me_num: add_next_num }).then(response => {
        // console.log(this);必须用箭头函数
        var get_next_num = response.data.like_me_num;
        if (get_next_num == add_next_num) {
          this.get_action_num_info();
        }
      });
      // 今晚收获：对象形式的函数参数，arguments对象。eval，string to var。// 下面两个函数重复，没有找到很好的复用方法。
      // 执行两次，勉强用，但还是有不及时显示的情况。本质原因没有找到。//上面的是改正后的方法。
      // get_action_num_info().then(function(response) {
      //   console.log(response);
      // });
      // get_action_num_info();
    },
    num_add_not: function(now_num) {
      var add_next_num = now_num + 1;
      post_action_num_info({ not_like_num: add_next_num }).then(response => {
        // console.log(this);必须用箭头函数
        var get_next_num = response.data.not_like_num;
        if (get_next_num == add_next_num) {
          this.get_action_num_info();
        }
      });
    },
    num_add_or: function(now_num) {
      var add_next_num = now_num + 1;
      post_action_num_info({ like_or_not_num: add_next_num }).then(response => {
        // console.log(this);必须用箭头函数
        var get_next_num = response.data.like_or_not_num;
        if (get_next_num == add_next_num) {
          this.get_action_num_info();
        }
      });
    }
  },
  created() {
    this.get_action_num_info();
    this.get_visite_num();
  }
};
</script>

<style>
#action > ul {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}
#action > ul > li {
  width: 49%;
  margin-bottom: 0.05rem;
  background-color: #fff;
}
.like-me {
  background-image: url(./img/喜欢.png);
}
.not-like {
  background-image: url(./img/不喜欢.png);
  background-size: 0.32rem 0.32rem;
}
.like-or-not {
  background-image: url(./img/等待.png);
  background-size: 0.22rem 0.22rem;
}
.watch-num {
  background-image: url(./img/统计.png);
}
.action-title {
  cursor: pointer;
}
.action-num {
  line-height: 0.36rem;
  text-align: center;
}
</style>
