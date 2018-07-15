<template>
  <section class="container">
    <div>
      <h1 class="title">글작성</h1>
        <form action="" method="post" @submit="boardAdd" class="form">
          <table id="form-table">
            <colgroup>
              <col width="20%">
              <col width="80%">
            </colgroup>
            <tbody>
              <tr>
                <td>작성자</td>
                <td>
                  <label>
                    <input type="text" class="form-control" name="writer" placeholder="작성자" required>
                  </label>
                </td>
              </tr>
              <tr>
                <td>글제목</td>
                <td>
                  <label>
                    <input type="text" class="form-control" name="subject" placeholder="글제목" required>
                  </label>
                </td>
              </tr>
              <tr>
                <td>글내용</td>
                <td>
                  <label>
                    <textarea name="content" placeholder="글내용" required></textarea>
                  </label>
                </td>
              </tr>
              <tr>
                <td colspan="2">
                  <button type="submit" class="button--green">글작성</button>
                </td>
              </tr>
            </tbody>
          </table>
        </form>
    </div>
  </section>
</template>


<script>
import mh from '~/plugins/mh'
export default {
  created () {
    if (!this.$store.state.isMember){
      alert('로그인 후 이용 가능합니다.')
      this.$router.go(-1)
    }
  },
  methods: {
    async boardAdd (e) {
      e.preventDefault();
      const url = '/board'
      const frm = e.target
      const _this = this
      mh.postData(url, mh.serialize(frm), data => {
        alert('완료되었습니다.')
        _this.$router.push(`/board/list`)
      })
    }
  }
}
</script>

<style>

</style>
