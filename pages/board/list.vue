<template>
  <section class="container">
    <div>
      <h1 class="title">게시판</h1>
      <table id="board-list">
        <colgroup>
          <col width="10%">
          <col width="10%">
          <col width="70%">
          <col width="10%">
        </colgroup>
        <thead>
          <tr>
            <th>글번호</th>
            <th>작성자</th>
            <th style="text-align: left;">글제목</th>
            <th>작성일</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="data in list" :key="data.idx">
            <td>{{data.idx}}</td>
            <td>{{data.writer}}</td>
            <td style="text-align: left;"> <nuxt-link :to="`/board/view/${data.idx}`">{{data.subject}}</nuxt-link></td>
            <td>{{data.date.substr(5,5)}}</td>
          </tr>
        </tbody>
      </table>
      <div class="links">
        <nuxt-link v-if="this.$store.state.isMember" :to="`/board/write`" class="button--green">글작성</nuxt-link>
      </div>
    </div>
  </section>
</template>

<script>
import mh from '~/plugins/mh'
export default {
  async asyncData ({ params }, callback) {
    mh.getData('/board', data => {
      callback(null, {list:data})
    })
  },
  async data () {
    return {
      list: []
    }
  }
}
</script>

<style>

</style>
