<template>
    <div class="p-5">
        <button @click="get_data()" class="btn">Get Data</button>
        
        <YouTube 
            v-if="url != null"
            :src="url"
            @ready="onReady"
            ref="youtube"
            hidden/>

        <table class="table">
            <thead>
            <tr>
                <th>Track</th>
                <th>Artist</th>
                <th>Playcount</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="t in tracks">
                <td>{{ t.name }}</td>
                <td>{{ t.artist }}</td>
                <td>{{ t.playcount }}</td>
                <td>
                    <button class="btn btn-ghost" @click="get_video(t)">Play</button>
                </td>
            </tr>
            </tbody>
        </table>
    </div>
</template>


<script>
import YouTube from 'vue3-youtube'

import * as api from "../api.js";

export default {
    data() {
        return {
            tracks: null,
            url: null,
        }
    },
    methods: {
        async get_data() {
            this.tracks = await api.get_tracks();
        },
        async get_video(track) {
            let id = await api.get_video_id(track);
            console.log(id);
            this.url = `https://www.youtube.com/watch?v=${id}`;
            console.log(this.url);
        },
        onReady() {
            this.$refs.youtube.playVideo()
        },
    },
    components: { YouTube },
}
</script>