import axios from 'axios';

const state = {
  posts: null,
  post: null
};

const getters = {
  statePost: state => state.posts,
  statePosts: state => state.post,
};

const actions = {
  async createPost({dispatch}, post){
    await axios.post('posts',post);
    await dispatch('getPosts');
  },

  async getPosts({commit}){
    let {data} = await axios.get('posts');
    commit('setPosts', data);
  },

  async viewPost({commit}, pid){
    let {data} = await axios.get(`post/${pid}`);
    commit('setPost', data);
  },
  async updatePost(post){
    await axios.patch(`post/${post.pid}`, post.form);
  },
  async deletePost(pid){
    await axios.delete(`post/${pid}`);
  }

};

const mutations = {
  setPosts(state, posts){
    state.posts = posts;
  },
  setPost(state, post){
    state.post = post
  }
};

export default {
  state,
  getters,
  actions,
  mutations
};

