import axios from "axios";

const username = "GrafHoms";
const api_key = "7fc6fd54935e6fd5d017a1e324858509";

export async function get_library() {
    const url = `http://ws.audioscrobbler.com/2.0/?method=library.getartists&api_key=${api_key}&user=${username}&format=json`;
    const response = await axios.get(url, {});
    return response.data;  
}