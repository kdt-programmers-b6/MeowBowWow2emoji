<template>
  <v-app>
    <v-main>
      <background />
      <post />
      <h3 align="center">예시 이미지들 입니다.</h3>
      <ShowExam />
    </v-main>
  </v-app>
</template>

<script>
import background from './components/background.vue'
import post from './components/post.vue'
import ShowExam from './components/ShowExam.vue'

export default {
  name: 'App',
  components: {
    background,
    post,
    ShowExam,
  }
};
</script>

