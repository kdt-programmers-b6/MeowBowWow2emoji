const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  devServer: {
     proxy: {
        '/':{
          target: "http://localhost:8000",
          changeOrigin: true,
        } 
      } 
    },
  transpileDependencies: [
    'vuetify'
  ]
})
