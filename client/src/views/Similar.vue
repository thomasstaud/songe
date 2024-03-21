<template>
    <div class="p-5">
        <p>Showing artists similar to {{ artist.name }} ...</p>
        <span v-if="similar == null" class="loading loading-dots loading-sm"></span>
        <table v-if="similar != null" class="table">
            <thead>
            <tr>
                <th>Artist</th>
                <th>Match</th>
                <th>Find similar</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="a in similar">
                <td>{{ a.name }}</td>
                <td>{{ a.match }}</td>
                <td>
                    <button class="fa fa-search btn btn-ghost" @click=""></button>
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
            artist: null,
            similar: null,
        }
    },
    async mounted() {
        this.artist = this.$route.params.artist;
        this.similar = await api.get_similar_artists(artist);
    }
}
</script>