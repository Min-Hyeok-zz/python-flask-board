<template>
  <div>
    <header id="header">
      <div class="logo"><nuxt-link :to="`/`"><app-logo class="app-logo"></app-logo></nuxt-link></div>
      <nav id="nav">
        <ul id="gnb">
          <li><nuxt-link :to="`/board/list`">게시판</nuxt-link></li>
          <li v-if="!this.$store.state.isMember"><nuxt-link :to="`/member/join`">회원가입</nuxt-link></li>
          <li v-if="!this.$store.state.isMember"><nuxt-link :to="`/member/login`">로그인</nuxt-link></li>
          <li v-if="this.$store.state.isMember"><a @click="Logout">로그아웃</a></li>
        </ul>
      </nav>
    </header>
    <nuxt/>
    <footer id="footer">Copyright (c) 2018 김민혁 All rights reserved.</footer>
  </div>
</template>
<script>
import AppLogo from '~/components/AppLogo.vue'
import mh from '~/plugins/mh'

export default {
  components: {
    AppLogo
  },
  methods: {
    Logout(){
      const _this = this
      if (confirm('로그아웃 하시겠습니까?')) {
        _this.$store.commit('logout')
        mh.postData('/api/logout')
        alert('로그아웃 되었습니다')
        _this.$router.push('/')
      }
    }
  }
}
</script>
<style src="~/assets/css/style.css" />
