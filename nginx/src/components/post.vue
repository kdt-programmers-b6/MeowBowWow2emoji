<template>
    <v-container>
        <v-row>
          <v-row>
            <v-col cols="5">
              <v-file-input v-model="image"
                  prepend-icon="mdi-camera"
                  @change="[Preview_image(), add_image()]"
                  show-size label="개나 고양이의 이미지를 넣어주세요!"
                  ></v-file-input>
            </v-col>
            <v-col cols="1"> 
              <v-checkbox
              v-model="animal_check"
              :label="`${animal_check.toString()}`"
              false-value="Cat"
              true-value="Dog"
              hide-details
            ></v-checkbox>
            </v-col>
            <v-col cols="2">
              <v-btn @click="upload" color="indigo" class="mx-2" dark fab>
                <v-icon dark> mdi-camera-flip </v-icon>
              </v-btn>
            </v-col>
          </v-row>
          <v-row justify="space-around">
            <v-col cols="4">
              <v-card class="mx-auto" max-width="700" v-cloak @drop.prevent="addDropFile" @dragover.prevent>
                <v-img :src="url" contain id="img1" height="300px" width='300px' class="mx-auto"></v-img>
              <v-card-title class="justify-center"> 이미지를 드래그 해주세요! </v-card-title>
              </v-card>
            </v-col>  
          <v-col cols="4">
            <v-card class="mx-auto" max-width="700">
              <v-img id="img2" height="300px" width='300px' class="mx-auto" />
              <v-card-title class="justify-center">내가 출력되었다냥!</v-card-title>
            </v-card>
          </v-col>  
          </v-row>
        </v-row>
    </v-container>
</template>
<script>
import axios from 'axios'

export default {
    // eslint-disable-next-line
    name: 'post',
    components: { 
    },
    data: () => ({
    //
    files: [],
    animal_check: 'Cat',  
    url: null,
    image: null
      }),

  methods: {
    addDropFile(e) {
       this.image = e.dataTransfer.files[0]; 
       this.url= URL.createObjectURL(this.image)
       console.log(this.image)},
       

    async upload() {
      var fd = new FormData();
      fd.append('pet_images', this.image);
      fd.append('animal', this.animal_check);
      await axios.post('http://13.210.122.72:8000/emoji/',
          fd, {
            headers: {
              'Content-Type': 'multipart/form-data',
            }
          }
        ).then( Response => {
          console.log("Sucess");
          document.getElementById("img2").src = Response.data['img_path'][0]
          console.log(Response.data)
        })
        .catch(function () {
          console.log("Fail");
          console.log(fd)
        });
    },
    Preview_image() {
      this.url= URL.createObjectURL(this.image)
    },
    add_image() {
      console.log(this.image)
    },
  }
}
</script>

<style scoped>
  img1 {
    height: 400;
    width: 400;
  }
</style>