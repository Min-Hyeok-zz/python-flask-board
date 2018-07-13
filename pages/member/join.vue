<template>
  <section class="container">
    <div>
      <h1 class="title">회원가입</h1>
        <form action="" method="post" class="form" @submit="memberAdd">
            <input type="text" name="id" placeholder="아이디" class="form-control" required>
            <input type="password" name="pw" placeholder="비밀번호" class="form-control" required>
            <input type="text" name="name" placeholder="이름" class="form-control" required>
            <button type="submit" class="button--green">회원가입</button>
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
        memberAdd(e){
            e.preventDefault()
            const frm = e.target
            const url = `/member`
            const _this = this
            mh.postData(url, mh.serialize(frm), data => {
                if (data == false) {
                    alert('중복된 아이디 입니다.')
                } else {
                    alert('회원가입이 완료되었습니다.')
                    _this.$router.push(`/member/login`)
                }
            })
        }
    }
}
</script>

<style>

</style>
