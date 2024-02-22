<template>
    <div class="p-5">
        <button @click="get_data()" class="btn">Get Data</button>

        <table class="table">
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
    methods: {
        async get_data() {
            this.artists = await api.get_artists();
        }
    },
}
</script>