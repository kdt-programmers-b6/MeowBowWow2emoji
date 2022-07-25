import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import '@mdi/font/css/materialdesignicons.css'
// To use mdi, npm install @mdi/font -D 
Vue.use(Vuetify);

export default new Vuetify({
    theme: { dark: true },
    icons: {
        icontfont: "mdi"
    }
});
