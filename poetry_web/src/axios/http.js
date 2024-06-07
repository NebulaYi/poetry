import axios from "axios";

const instance = axios.create({
    //baseURL: 'http://10.135.2.25:5000',
    baseURL: 'http://127.0.0.1:5000',
    // timeout: 3000,
});


// 添加请求拦截器
instance.interceptors.request.use(function (config) {
    // let token = localStorage.getItem('token')
    // if (token){
    //     config.headers['token'] = token
    // }
    // 在发送请求之前做些什么
    return config;
}, function (error) {
    // 对请求错误做些什么
    return Promise.reject(error);
});

// 添加响应拦截器
instance.interceptors.response.use(function (response) {
    // 对响应数据做点什么
    return response;
}, function (error) {
    // 对响应错误做点什么
    console.log('请求错误')
    return Promise.reject(error);
});



export  const get = (url, data = {}) => {
    return  new  Promise(resolve => {
        instance.get(url, {
            params:data
        }).then(e => {
            resolve(e.data)
        })
    })
}

export const post = (url, data = {}) => {
    return  new  Promise(resolve => {
        instance.post(url, data).then(e => {
            resolve(e.data)
        })
    })
}
export const put = (url, data = {}) => {
    return new Promise(resolve => {
        instance.put(url, data).then(e => {
            resolve(e.data)
        })
    })
}

