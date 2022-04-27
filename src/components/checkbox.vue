<template>
  <v-container>
    <v-checkbox
      v-model="checkbox1"
      :label="`고양이면 체크 해주세요!: ${checkbox1.toString()}`"
    ></v-checkbox>
  </v-container>
</template>


<script>
export default {
  // eslint-disable-next-line
    name: checkbox,
    data () {
        return {
            // If true > dog if False Cat
    checkbox1: true } 
    },
}
</script>