import { createStore } from 'vuex'

export default createStore({
    state: {
        user: {
            uName: 'user@email.com',
            uEmail: '',
            uPwd: '1'
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