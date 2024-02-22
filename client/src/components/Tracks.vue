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
                    <button class="btn btn-ghost">Play</button>
                </td>
            </tr>
            </tbody>
        </table>
    </div>
</template>


<script>
import * as api from "../api.js";
import youtubedl from 'youtube-dl-exec'

export default {
    data() {
        return {
            tracks: null,
        }
    },
    methods: {
        async get_data() {
            this.tracks = await api.get_tracks();
        },
        async download_track() {
            youtubedl('https://www.youtube.com/watch?v=6xKWiCMKKJg', {
                dumpSingleJson: true,
                noCheckCertificates: true,
                noWarnings: true,
                preferFreeFormats: true,
                addHeader: ['referer:youtube.com', 'user-agent:googlebot']
            }).then(output => console.log(output))
        }
    },
}
</script>