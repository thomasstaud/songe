<template>
    <div class="p-5">
        <button @click="get_data()" class="btn">Get Data</button>

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
                    <button class="btn btn-ghost" @click="play_track(t)">Play</button>
                </td>
            </tr>
            </tbody>
        </table>
    </div>
</template>


<script>
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
        async play_track(track) {
            console.log("emitting event!");
            this.$store.commit('set_id', track);
            console.log(this.$store.state.playingTrack);
        }
    },
}
</script>