<template>
    <div class="p-5">
        <span v-if="artists == null" class="loading loading-dots loading-sm"></span>
        <table v-if="artists != null" class="table">
            <thead>
            <tr>
                <th>Artist</th>
                <th>Playcount</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="a in artists">
                <td>{{ a.name }}</td>
                <td>{{ a.playcount }}</td>
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
            artists: null,
        }
    },
    async mounted() {
        this.artists = await api.get_artists();
    }
}
</script>