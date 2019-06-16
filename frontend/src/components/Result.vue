<template>
  <div>
    <h1 class="title">Shortened URL</h1>
    <div class="field is-grouped">
      <div class="control is-expanded">
        <input type="url" class="input" :value="url" id="result" readonly>
      </div>
      <div class="control">
        <button
          type="button"
          class="button is-info"
          data-clipboard-target="#result"
          @click="copy"
        >Copy</button>
      </div>
    </div>
    <section class="hero">
      <div class="container">
        <button class="button" @click="restart">Shorten another</button>
      </div>
    </section>
  </div>
</template>

<script>
import Clipboard from "clipboard/dist/clipboard.min.js";

export default {
  props: ["hash"],
  data() {
    return { clipboard: null };
  },
  mounted() {
    this.clipboard = new Clipboard(".button");
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
