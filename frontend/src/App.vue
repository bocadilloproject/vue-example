<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  mounted() {
    document.title = "URL Shortener";
  }
};
</script>
