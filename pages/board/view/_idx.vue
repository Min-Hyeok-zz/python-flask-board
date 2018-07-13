<template>
  <section class="container">
    <div>
      <h1 class="title">글보기</h1>
      <table id="view-table">
        <colgroup>
          <col width="15%">
          <col width="85%">
        </colgroup>
        <tbody>
          <tr>
            <td>작성자</td>
            <td v-text="view.writer"></td>
          </tr>
          <tr>
            <td>글제목</td>
            <td v-text="view.subject"></td>
          </tr>
          <tr>
            <td>글내용</td>
            <td v-text="view.content"></td>
          </tr>
          <tr>
            <td>작성일</td>
            <td v-text="view.date"></td>
          </tr>
          <tr>
            <td>조회수</td>
            <td v-text="view.hit"></td>
          </tr>
        </tbody>
      </table>
      <div class="links">
          <nuxt-link to="/board/list" class="button--green">뒤로가기</nuxt-link>
          <nuxt-link v-if="this.$store.state.isMember" :to="`/board/write/${$route.params.idx}`" class="button--green">수정하기</nuxt-link>
          <a href="#" v-if="this.$store.state.isMember" @click.prevent="boardDelete" class="button--green">삭제하기</a>
      </div>
    </div>
  </section>
</template>

<script>
import mh from '~/plugins/mh'
export default {
  asyncData ({ params }, callback) {
    mh.getData(`/board/${params.idx}`, (data) => {
      callback(null, {view : data})
      console.log(data)
    })
  },
  data () {
    return {
      view: []
    }
  },
  methods: {
    boardDelete (e) {
        const idx = this.$route.params.idx
        const url = `/delete/${idx}`
        const _this = this
        if (confirm('삭제하시겠습니까?')) {
          alert('삭제되었습니다.')
          _this.$router.push(`/board/list`)
          mh.postData(url, idx, data => {})
        }
    }
  }
}
</script>

<style>

</style>
