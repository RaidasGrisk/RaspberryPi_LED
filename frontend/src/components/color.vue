<template>
  <div class="center">
    <div>
      <textarea
        v-model="rpi_ip"
        class='textarea'
        style="resize: none;"
        placeholder="RPi ip"
      ></textarea>
      <color-picker
        theme="light"
        :color="color"
        :sucker-hide="false"
        :sucker-canvas="suckerCanvas"
        :sucker-area="suckerArea"
        @changeColor="changeColor"
        @openSucker="openSucker"
      />
    </div>
    <button @click="TurnOff">TurnOff</button>
    <button @click="Rainbow">Rainbow</button>
  </div>
</template>

<script>
import colorPicker from '@caohenghu/vue-colorpicker'
import axios from "axios"

export default {
  components: {
    colorPicker
  },
  data() {
    return {
      rpi_ip: '192.168.0.104',
      color: '#ffffff',
      suckerCanvas: null,
      suckerArea: [],
      isSucking: false
    }
  },
  methods: {

    changeColor(color) {
      const { r, g, b, a } = color.rgba
      this.color = `rgba(${r}, ${g}, ${b}, ${a})`

      axios.get(`http://${this.rpi_ip}:5000/set_color?r=${r}&g=${g}&b=${b}`)
      .then(function (response) {
        // handle success
        console.log(response);
      })
      .catch(function (error) {
        // handle error
        console.log(error);
      })
      .then(function () {
        // always executed
      });


    },

    TurnOff() {
      axios.get(`http://${this.rpi_ip}:5000/set_color?r=0&g=0&b=0`)
      .then(function (response) {
        // handle success
        console.log(response);
      })
      .catch(function (error) {
        // handle error
        console.log(error);
      })
      .then(function () {
        // always executed
      });
    },

    Rainbow() {
      axios.get(`http://${this.rpi_ip}:5000/rainbow`)
      .then(function (response) {
        // handle success
        console.log(response);
      })
      .catch(function (error) {
        // handle error
        console.log(error);
      })
      .then(function () {
        // always executed
      });
    },

    openSucker(isOpen) {
      if (isOpen) {
        // ... canvas be created
        // this.suckerCanvas = canvas
        // this.suckerArea = [x1, y1, x2, y2]
      } else {
        // this.suckerCanvas && this.suckerCanvas.remove
      }
    }
  }
}
</script>

<style>

.center {
  position: fixed; /* or absolute */
  top: 50%;
  left: 50%;
  /* bring your own prefixes */
  transform: translate(-50%, -50%);
}

.textarea{
  width:212px;
  height:20px;
  border:1px solid grey;
}

</style>
