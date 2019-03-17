import axios from 'axios'
// let host = 'http://127.0.0.1:8000/api/';
// let host = 'http://api.innocosme.com/api/';
const host = process.env.NODE_ENV === 'development' ? 'http://127.0.0.1:8000/api/' : 'http://api.innocosme.com/api/';

// get
// export const get_base_info = () => {
//   return axios.get(host + 'base_info/')
// };
export const get_base_info = function () {
  return axios.get(host + 'base_info/')
};
export const get_edu_info = () => {
  return axios.get(host + 'edu_info/')
};
export const get_certificate_info = () => {
  return axios.get(host + 'certificate_info/')
};
export const get_project_info = () => {
  return axios.get(host + 'pro_info/')
};
export const get_job_info = () => {
  return axios.get(host + 'job_info/')
};
export const get_stack_info = () => {
  return axios.get(host + 'stack_info/')
};
export const get_job_want_info = () => {
  return axios.get(host + 'job_want/')
};
export const get_action_num_info = () => {
  return axios.get(host + 'action_num/')
};
export const get_visite_num = () => {
  return axios.get(host + 'visite_num/1/')
};

//put，修改已有的action数据。对比下一个函数，这里的参数要加{}，而下一个不加。
export const post_action_num_info = ({ like_me_num, not_like_num, like_or_not_num }
) => {
  return axios.put(host + 'action_num/1/', {
    like_me_num,
    not_like_num,
    like_or_not_num,
  })
};

//post，post信息数据。
export const post_message_info = (title, content, contect) => {
  return axios({
    method: 'post',
    url: host + 'message_info/',
    data: {
      title,
      content,
      contect,
    },
    // headers: {
    //     'Content-Type': 'application/x-www-form-urlencoded'
    // }
  })
};
