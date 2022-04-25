<template>
    <v-container>
        <video-background
            class="video-container"
            :src='require("@/assets/mp4/catdog2emoji.mp4")'
            style="max-height: 600px; height: 100vh;"
            overlay="linear-gradient(0deg, rgba(0, 0, 0, 0.88), rgba(251, 148, 158, 0.22), rgba(251, 148, 158, 0.42))"
            res=991
        >
            <div class="d-flex justify-content-center align-items-center h-50 px-2">
                <h1 class="text-white d-none d-md-block" style="font-weight: 1000; ">MeowBow emoji Project!</h1>
            </div>
        </video-background>
    </v-container>
</template>
<script>
export default {
    // eslint-disable-next-line
    name: 'background'
}
</script>
