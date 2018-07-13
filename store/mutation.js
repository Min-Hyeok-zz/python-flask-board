const mutation = {
    login (state,data) {
        state.isMember = true
        state.member = data
    },
    logout (state) {
        state.isMember = false
        state.member = null
    }
}