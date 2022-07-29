<template>
  <v-app>
    <v-main>
      <background />
      <post />
      <div>&nbsp;</div>
      <div>&nbsp;</div>
      <v-row rows=3>
      <h3 align="center">아래 이미지에 마우스를 가져다 대 보세요!</h3>
      </v-row>
      <div>&nbsp;</div>
      <ShowExam />
    </v-main>

    <v-footer
    dark
    padless
  >
    <v-card
      class="flex"
      flat
      tile
    >
      <v-card-title class="teal">
        <strong class="subheading">Programmers B6 team project</strong>
        <v-spacer></v-spacer>
        <v-btn class="mx-4" dark icon @click="redirect_git">
          <v-icon size="24px">
          mdi-github
          </v-icon>
        </v-btn>
      </v-card-title>
      <v-card-text class="py-2 white--text text-center">
        {{ new Date().getFullYear() }} — <strong>Programmers</strong>
      </v-card-text>
    </v-card>
    </v-footer>
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
  },
  data: () => ({
      icons: [
        'mdi-github',
        'mdi-twitter',
        'mdi-linkedin',
        'mdi-instagram',
      ],
    }),
  methods: {
    redirect_git() {
      window.open("https://github.com/kdt-programmers-b6/MeowBowWow2emoji", "_blank")
    }
  }
};
</script>

