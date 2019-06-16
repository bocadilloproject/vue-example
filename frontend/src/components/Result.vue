<template>
  <div class="hero">
    <h1 class="title">Shortened URL</h1>
    <div class="field is-grouped">
      <div class="control is-expanded">
        <input type="url" class="input" :value="url" id="result" readonly>
      </div>
      <div class="control">
        <button type="button" class="button is-info" data-clipboard-target="#result">Copy</button>
      </div>
    </div>
    <div class="container">
      <button class="button" @click="restart">Shorten another</button>
    </div>
  </div>
</template>

<script>
import Clipboard from "clipboard/dist/clipboard.min.js";

export default {
  props: ["hash"],
  inject: ["heroOptions"],
  data: () => ({ clipboard: null }),
  mounted() {
    this.clipboard = new Clipboard(".button");
    this.heroOptions.isSuccess = true;
  },
  destroyed() {
    this.clipboard && this.clipboard.destroy();
  },
  computed: {
    path() {
      return `/${this.hash}`;
    },
    url() {
      return window.location.origin + this.path;
    }
  },
  methods: {
    restart() {
      this.$emit("restart");
    }
  }
};
</script>
