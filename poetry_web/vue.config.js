const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

// 配置跨域
// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true,
//   // lintOnSave:false,
//   devServer: {
//     port: 8080, // 端口
//     proxy: {
//       'http://127.0.0.1:5000/api/v1.0': {  //   若请求的前缀不是这个'/api'，那请求就不会走代理服务器
//         target: '',  //这里写路径
//         pathRewrite: { '^/api': '' }, //将所有含/api路径的，去掉/api转发给服务器
//         ws: true,  //用于支持websocket
//         changeOrigin: true   //用于控制请求头中的host值
//       },
//     }
//   }
//
// })

