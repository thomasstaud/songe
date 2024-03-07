<script setup>
import {VuePlotly} from 'vue3-plotly';
</script>

<template>
<div class="centered">
    <vue-plotly :data="data" :layout="layout"></vue-plotly>
</div>
</template>

<script>
import * as api from "../api.js";

export default {
    data() {
        return {
            data: "",
            layout: { title: "Plays by Artist" }
        }
    },
    async mounted() {
        let artists = await api.get_artists();
        this.data = [{
            x: artists.map((a) => a.name),
            y: artists.map((a) => a.playcount),
            type: "bar"
        }];
    }
}
</script>