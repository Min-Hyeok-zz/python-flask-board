import Vue from 'vue';
import Vuex from 'vuex'
import sessionStorage from 'sessionstorage'

Vue.use(Vuex)

const store = () => new Vuex.Store({
    state: {
        isMember: false,
        member: null
    },
    mutations: {
        login (state,data) {
            state.isMember = true
            state.member = data
            sessionStorage.setItem('member',JSON.stringify(data))
        },
        logout (state) {
            state.isMember = false
            state.member = null
            sessionStorage.clear()
        }
    },
    actions: {
        nuxtServerInit({ commit }, { req }) {
            if (req.session && req.session.member) {
                commit('login', req.session.member)
            }
        }
    }
})

export default store