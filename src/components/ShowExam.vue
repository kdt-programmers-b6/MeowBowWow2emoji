<template>
  <v-container>
    <v-card class="mx-auto" max-width="700" @mouseover="changeImageWhen('over')" @mouseout="changeImageWhen('out')" >
      <v-img :src="require('@/assets/sample_img/' + current_img1)" height="400px" width='400px' class="mx-auto" />
      <v-card-title class="justify-center">마우스를 올려주세요!</v-card-title>
    </v-card>
  </v-container>
</template>

<script>
export default {
  // eslint-disable-next-line
  name: 'show_example',
  data: () => ({
    mouse_event: {
      over: "1_fake.jpg",
      out: "1_real.jpg",
    },
    current_img1: "1_real.jpg"
 }),
 methods: {
   changeImageWhen (event) {
     this.current_img1 = this.mouse_event[event]
  }
 }
}
</script>