<template>
  <v-container>
    <v-row>
      <v-col cols="4">
        <v-card class="mx-auto" max-width="500" @mouseover="changeImageWhen1('over')" @mouseout="changeImageWhen1('out')" >
          <v-card-title class="justify-center"></v-card-title>
          <v-img :src="require('@/assets/sample_img/1_'+ current_img1)" height="300px" width='300px' class="mx-auto" />
        </v-card>
      </v-col>

      <v-col cols="4">
        <v-card class="mx-auto" max-width="500" @mouseover="changeImageWhen2('over')" @mouseout="changeImageWhen2('out')" >
          <v-card-title class="justify-center"></v-card-title>
          <v-img :src="require('@/assets/sample_img/2_'+ current_img2)" height="300px" width='300px' class="mx-auto" />
        </v-card>
      </v-col>

      <v-col cols="4">
        <v-card class="mx-auto" max-width="500" @mouseover="changeImageWhen3('over')" @mouseout="changeImageWhen3('out')" >
          <v-card-title class="justify-center"></v-card-title>
          <v-img :src="require('@/assets/sample_img/3_'+ current_img3)" height="300px" width='300px' class="mx-auto" />
        </v-card>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
export default {
  // eslint-disable-next-line
  name: 'show_example',
  data: () => ({
    mouse_event: {
      over: "fake.jpg",
      out: "real.jpg",
    },
    current_img1: "real.jpg",
    current_img2: "real.jpg",
    current_img3: "real.jpg"
 }),
 methods: {
   changeImageWhen1 (event) {
     this.current_img1 = this.mouse_event[event]
  },
  changeImageWhen2 (event) {
     this.current_img2 = this.mouse_event[event]
  },
  changeImageWhen3 (event) {
     this.current_img3 = this.mouse_event[event]
  }
 }
}
</script>