<template>
  <div>
    <h1 class="title">URL Shortener</h1>
    <h3 class="subtitle">Simplify your links</h3>
    <form @submit="onSubmit">
      <div class="field is-grouped">
        <p class="control is-expanded">
          <input v-model="url" class="input is-large" type="url" placeholder="http://…" required>
        </p>
        <p class="control">
          <button type="submit" class="button is-primary is-large">Shorten</button>
        </p>
      </div>
    </form>
  </div>
</template>

<script>
import { http } from "../utils";

export default {
  inject: ["heroOptions"],
  data: () => ({ url: "" }),
  mounted() {
    this.heroOptions.isSuccess = false;
  },
  methods: {
    async onSubmit(e) {
      e.preventDefault();
      const { hash } = await http.post("/urls", { url: this.url });
      this.$emit("hash", hash);
    }
  }
};
</script>
