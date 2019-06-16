import { http } from "../utils";

export default {
  props: ["hash"],
  async render() {
    const { url } = await http.get(`/urls/${this.hash}`);
    window.location = url;
  }
};
