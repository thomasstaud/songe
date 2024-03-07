import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { createStore } from 'vuex'

import { createRouter, createWebHistory } from 'vue-router'

import Home from './views/Home.vue'
import Artists from './views/Artists.vue'
import Tracks from './views/Tracks.vue'
import Statistics from './views/Statistics.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', name: 'home', component: Home },
        { path: '/artists', name: 'artists', component: Artists},
        { path: '/tracks', name: 'tracks', component: Tracks},
        { path: '/statistics', name: 'statistics', component: Statistics}
    ]
});

const store = createStore({
    state () {
      return {
        playingTrack: null
      }
    },
    mutations: {
      set_track (state, track) {
        state.playingTrack = track;
      }
    }
  })

const app = createApp(App)
app.use(router);
app.use(store);
app.mount('#app');
