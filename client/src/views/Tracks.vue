<template>
    <div class="p-5">
        <span v-if="tracks == null" class="loading loading-dots loading-sm"></span>
        <table v-if="tracks != null" class="table">
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
                    <button class="fa fa-play btn btn-ghost" @click="this.$store.commit('set_track', t)"></button>
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
    async mounted() {
        this.tracks = await api.get_tracks();
    }
}
</script>