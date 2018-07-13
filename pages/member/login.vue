<template>
  <section class="container">
    <div>
      <h1 class="title">로그인</h1>
        <form action="" method="post" class="form" @submit="memberLogin">
            <input type="text" name="id" placeholder="아이디" class="form-control" required>
            <input type="password" name="pw" placeholder="비밀번호 =" class="form-control" required>
            <button type="submit" class="button--green">로그인</button>
        </form>
    </div>
  </section>
</template>

<script>
import mh from '~/plugins/mh'
export default {
  created () {
    if (this.$store.state.isMember) {
      alert('이미 로그인 하셨습니다')
      this.$router.go(-1)
    }
  },
  methods: {
    memberLogin (e) {
      e.preventDefault()
      const frm = e.target
      const url = '/login'
      const _this = this
      mh.postData(url, mh.serialize(frm), data => {
        console.log(data)
        if (!data) {
          alert('아이디 또는 비밀번호가 일치하지 않습니다.')
        } else{
          _this.$store.commit('login',data)
          alert('로그인 되었습니다.')
          _this.$router.push(`/`)
        }
      })
    }
  }
}
</script>

<style>

</style>
