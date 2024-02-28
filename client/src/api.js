import axios from "axios";

export async function get_video_id(track) {
    let query = `${track.name} ${track.artist}`;
    const response = await axios.get(`http://localhost:5000/search_video?query=${query}`, {});
    return response.data;
}

export async function get_artists() {
    const response = await axios.get(`http://localhost:5000/artists`, {});
    return response.data;
}

export async function get_tracks() {
    const response = await axios.get(`http://localhost:5000/tracks`, {});
    return response.data;
}