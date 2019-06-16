<template>
  <div>
    <h1 class="title">Shortened URL</h1>
    <div class="field is-grouped">
      <div class="control is-expanded">
        <input type="text" class="input" :value="url" readonly>
      </div>
      <div class="control">
        <button type="button" class="button is-info">Copy</button>
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
export default {
  props: ["hash"],
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
