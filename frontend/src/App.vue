<template>
  <div id="app">
    <h1>URL Shortener</h1>
    <h3>Simplify your links</h3>
    <form @submit="onSubmit">
      <input v-model="url" type="text" name="url" placeholder="Enter original URL here" required>
      <button type="submit">Shorten URL</button>
    </form>
  </div>
</template>

<script>
import { postJSON } from "./utils";
export default {
  data() {
    return { url: "" };
  },
  methods: {
    onSubmit(e) {
      e.preventDefault();
      postJSON("http://localhost:8000/urls", { url: this.url })
        .then(res => res.json())
        .then(console.log);
    }
  }
};
</script>

<style>
#app {
  font-family: Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
