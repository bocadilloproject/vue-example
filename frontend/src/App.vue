<template>
  <div id="app">
    <h1>URL Shortener</h1>
    <h3>Simplify your links</h3>
    <form @submit="onSubmit">
      <input v-model="url" type="text" name="url" placeholder="Enter original URL here" required>
      <button type="submit">Shorten URL</button>
    </form>
    <div v-if="shortUrl">
      <p>Shortened URL:</p>
      <p>
        <code>{{ shortUrl }}</code>
      </p>
    </div>
  </div>
</template>

<script>
import { postJSON, makeFullUrl } from "./utils";
export default {
  data() {
    return { url: "", shortUrl: null };
  },
  methods: {
    onSubmit(e) {
      e.preventDefault();
      postJSON("/urls", { url: this.url }).then(
        ({ hash }) => (this.shortUrl = makeFullUrl(`/urls/${hash}`))
      );
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
