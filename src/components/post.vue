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
            <v-col cols="2">
              <v-btn @click="upload" color="primary" class="ml-auto">이미지 변환하기</v-btn>
            </v-col>
          </v-row>
          <v-row justify="space-around">
            <v-col cols="auto">
              <v-img :src="url" contain id="img1" height="300px" width='300px' class="ml-auto"></v-img>
            </v-col>  
          <v-col cols="auto">
            <v-img :src="url" height="300px" width='300px' class="ml-auto" />
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
    url: null,
    image: null
      }),

  methods: {
    async upload() {
      var fd = new FormData();
      fd.append('pet_images', this.image);
      await axios.post('http://3.26.152.53/emoji/',
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