<template>
  <div>
    <h1>URL Shortener</h1>
    <h3>Simplify your links</h3>
    <form @submit="onSubmit">
      <input v-model="url" type="text" name="url" placeholder="Enter original URL here" required>
      <button type="submit">Shorten URL</button>
    </form>
    <div v-if="shortUrl">
      <p>Shortened URL:</p>
      <p>
        <a :href="shortUrl" rel="noreferrer noopener" alt="Shortened URL">
          <code>{{ fullShortUrl }}</code>
        </a>
      </p>
    </div>
  </div>
</template>

<script>
import { http } from "../utils";

export default {
  data() {
    return { url: "", shortUrl: null };
  },
  computed: {
    fullShortUrl() {
      return window.location.origin + this.shortUrl;
    }
  },
  methods: {
    async onSubmit(e) {
      e.preventDefault();
      const { hash } = await http.post("/urls", { url: this.url });
      this.shortUrl = `/${hash}`;
    }
  }
};
</script>
