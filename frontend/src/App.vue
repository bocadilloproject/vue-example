<template>
  <div id="app">
    <h1>URL Shortener</h1>
    <h3>Simplify your links</h3>
    <form @submit="onSubmit">
      <input type="text" name="url" placeholder="Enter original URL here" required>
      <button type="submit">Shorten URL</button>
    </form>
  </div>
</template>

<script>
export default {
  methods: {
    onSubmit(e) {
      e.preventDefault();
      fetch("http://localhost:8000/urls", { method: "POST" })
        .then(res => res.json())
        .then(console.log);
    }
  }
};
</script>


<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
