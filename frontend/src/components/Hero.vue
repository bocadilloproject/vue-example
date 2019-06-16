<template>
  <section
    class="hero is-fullheight has-text-centered"
    :class="isSuccess ? 'is-success' : 'is-dark'"
  >
    <div class="hero-body">
      <div class="container">
        <slot></slot>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data: () => ({ isSuccess: false }),
  provide() {
    const heroOptions = {};
    Object.defineProperty(heroOptions, "isSuccess", {
      enumerable: true,
      get: () => this.isSuccess,
      set: value => (this.isSuccess = value)
    });
    return { heroOptions };
  }
};
</script>
