<template>
    <v-container>
        <v-file-input v-model="image" @change="Preview_image" show-size label="Image"></v-file-input>
        <v-btn color="green" @click="add_image">아래 이미지 추가하기</v-btn>
        <v-btn @click="upload" color="primary">이미지 변환하기</v-btn>
        <v-img :src="url" contain height="400px" width="400px"></v-img>
        <img id="img2" />
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
      for(let i=0; i<this.files.length; ++i){
        fd.append('pet_images', this.files[i]);
        }
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
      this.files.push(this.image)
      console.log(this.files)
    }
}
}
</script>

<style>
  
</style>