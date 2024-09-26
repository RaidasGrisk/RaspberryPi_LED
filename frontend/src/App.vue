<script setup>
  import { ref, watch, onMounted } from 'vue'
  import { darkTheme } from 'naive-ui'

  const color = ref()
  const ip = ref('192.168.31.167')

  const changeColor = async (r, g, b) => {
    const url = `http://${ip.value}:5000/set_color?r=${r}&g=${g}&b=${b}`
    const _ = await fetch(url)
  }

  const setRainbow = async () => {
    const url = `http://${ip.value}:5000/rainbow`
    const _ = await fetch(url)
  }

  // watch if color picker value changed and send a fetch requests if so
  watch(color, async(newColor, oldColor) => {
    if (newColor) {
      const [r, g, b] = newColor.match(/\d+/g).map(Number)
      await changeColor(r, g, b)
    }
  })

  // we want to automatically detect the ip from the url bar
  // and send fetch requests to it
  onMounted(() => {
    const deafultIp = window.location.href
    console.log(window.location.href)
    if (deafultIp.includes('localhost')) {
      console.log('dev')
    } else {
      console.log(`setting default ip to ${deafultIp}`)
      ip.value = deafultIp
    }
  })

</script>

<template>
  <n-config-provider :theme="darkTheme">
    <n-flex justify="center" align="center" vertical>
      <br/>
      <n-color-picker 
        default-show 
        style="width: 240px" 
        default-value="rgb(50, 100, 250)"
        :show="true" 
        :show-alpha="false" 
        v-model:value="color" 
      />
      <div style="height: 260px;"/>
      <n-divider />
      <n-button tertiary type="primary" @click="setRainbow()">
        🌈
      </n-button>
      <n-button tertiary type="primary" @click="changeColor(0, 0, 0)">
        <n-icon>
          <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 6a7.75 7.75 0 1 0 10 0"></path><path d="M12 4v8"></path></g></svg>
        </n-icon>
      </n-button>
    </n-flex>
  </n-config-provider>
</template>

<style scoped>

</style>
