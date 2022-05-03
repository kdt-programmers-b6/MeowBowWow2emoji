<template>
    <v-container>
        <v-row>
          <v-row>
            <v-col cols="5">
              <v-file-input v-model="image"
                  prepend-icon="mdi-camera"
                  @change="[Preview_image(), add_image()]"
                  show-size label="개나 고양이의 이미지를 넣어주세요!"
                  accept="image/x-png,image/gif,image/jpeg"
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
            <v-col cols="1"> 
              <v-checkbox
              v-model="version"
              :label="`${version.toString()}`"
              false-value="V1"
              true-value="V2"
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
              <v-img :src="`data:image/png;base64, ${base64.encodedImage}`" height="300px" width='300px' class="mx-auto" />
              <v-card-title class="justify-center">출력 이미지</v-card-title>
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
    image: null,
    version: 'V1',
    base64: {
        encodedImage: null}
      }),

  methods: {
    addDropFile(e) {
       this.image = e.dataTransfer.files[0]; 
       this.url= URL.createObjectURL(this.image);
       if (this.image.type == 'image/x-png' || this.image.type == 'image/jpeg'){
         console.log(this.image)
       }
       else {
       this.showAlert("error", "The file-type doesn't belong to image")
       }
    },
       

    async upload() {
      var fd = new FormData();
      fd.append('pet_images', this.image);
      fd.append('animal', this.animal_check);
      fd.append('version', this.version);

      await axios.post('http://13.210.122.72/emoji/',
          fd, {
            headers: {
              'Content-Type': 'multipart/form-data',
            }
          }
        ).then( Response => {
          console.log("Sucess");
          this.base64.encodedImage = Response.data['img_path']
          console.log(this.base64.encodedImage)
          console.log(Response.headers)
        })
        .catch(function () {
          console.log("Fail");
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