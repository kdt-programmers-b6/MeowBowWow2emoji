<template>
  <v-app>
    <v-main>
      <background />
      <post />
    </v-main>
  </v-app>
</template>

<script>
import background from './components/background.vue'
import post from './components/post.vue'

export default {
  name: 'App',
  components: {
    background,
    post,
  }
};
</script>

