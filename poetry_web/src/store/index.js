import { createStore } from 'vuex'

export default createStore({
    state: {
        userInfo: {}
    },
    mutations: {
        setUserInfo(state, userInfo) {
            state.userInfo = userInfo;
        }
    },
    actions: {
        // 异步操作
    },
    modules: {}
})