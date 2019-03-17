<template>
    <div id="send-message">
        <div class="left-title send-message-title">发消息</div>
        <form>
            <input type="text" placeholder='标题：' class="message-title" maxlength="30">
            <textarea name="" placeholder="必选，信息会通过邮件实时发送给作者。" required class="message-content" maxlength="200"></textarea>
            <input type="text" placeholder='联系：' class="message-contect" maxlength="30">
        </form>
        <button class="btn" v-on:click="send_message">发送</button>
    </div>
</template>

<script>
import { post_message_info } from "../../api/api";

export default {
  name: "send_message",
  methods: {
    send_message: function() {
      var message_title = document.querySelector(".message-title");
      var message_content = document.querySelector(".message-content");
      var message_contect = document.querySelector(".message-contect");
      if (message_content.value.length > 0) {
        post_message_info(
          message_title.value,
          message_content.value,
          message_contect.value
        ).then(function(res) {
          console.log(res);
          if (response.data == 1) {
            // console.log(response.data);
            alert("发送成功！");
          }else{
            // console.log(response)
            alert('发送失败，请重试！');
          }
        }).catch((e)=>{
          console.log(e);
        });
        message_title.value = "";
        message_content.value = "";
        message_contect.value = "";
      } else {
        alert("请输入要发送的消息！");
      }
    }
  }
};
</script>

<style scoped>
#send-message {
  width: 100%;
  margin-top: 0.2rem;
}
.send-message-title {
  background-image: url(./img/发消息.png);
  background-size: 0.22rem 0.22rem;
}
.message-title,
.message-contect {
  width: 100%;
  display: block;
  height: 0.26rem;
  padding-left: 0.05rem;
  border: none;
  box-sizing: border-box;
}
.message-content {
  box-sizing: border-box;
  resize: none;
  height: 0.8rem;
  width: 100%;
  display: block;
  padding: 0.06rem;
  font-size: 0.12rem;
  border-left: none;
  border-right: none;
}
.btn {
  display: block;
  width: 100%;
  height: 0.26rem;
}
</style>
