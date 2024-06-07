import { createStore } from 'vuex'

export default createStore({
    state: {
        user: {
            uName: 'user@email.com',
            uEmail: '',
            uPwd: '',
            access_token: ''
        }
    },
    mutations: {
        setUserInfo(state, userInfo) {
            state.user = userInfo;
        }
    },
    actions: {
        // 异步操作
    },
    modules: {}
})