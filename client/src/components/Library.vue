<script setup>
</script>

<template>
    <div class="p-5">
        <h1>LIBRARY</h1>
        <button @click="get_data()" class="btn">Get Data</button>
        <p>{{ data }}</p>
    </div>
</template>


<script>
import * as api from "../api.js";

export default {
    data() {
        return {
            data: "",
        }
    },
    methods: {
        async get_data() {
            this.data = await api.get_library();
        }
    },
}
</script>