import axios from "axios";

const YOUTUBE_API_KEY = 'AIzaSyCYPPOOZYH8sZNS2rGr6Vux5qLE59Iq5DU';

export async function get_url(query) {
    const url = `https://www.googleapis.com/youtube/v3/search?key=${YOUTUBE_API_KEY}&type=video&part=snippet&q=${query}`;
  
    const response = await axios.get(url);
    console.log(response.data);
  
    return response.data;
}