const target = "http://0.0.0.0:5000";
module.exports = {
  transpileDependencies: [
    'vuetify'
  ],
  devServer:{
    port: 8080,
    proxy: {
      '^/api':{
        target,
        changeOrigin: true
      }
    
    }
  }
}
