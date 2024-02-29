<template>
Now Playing ...

<YouTube 
    v-if="url != null"
    :src="url"
    @ready="onReady"
    ref="youtube"
    />
</template>

<script>
import YouTube from 'vue3-youtube'
import * as api from "../api.js";

export default {
    data() {
        return {
            url: null,
        }
    },
    methods: {
        async play_track(track) {
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
    // todo: watch playedTrack
}
</script>