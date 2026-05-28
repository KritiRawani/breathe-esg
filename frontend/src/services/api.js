import axios from "axios";

const API = axios.create({
  baseURL: "https://breathe-esg-enne.onrender.com",
});

export default API;