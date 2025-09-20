const { createApp } = Vue

const app = createApp({
  data() {
    return {
      message: "Hi Rahul"
    }
  }
})

app.mount('#app')
