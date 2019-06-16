<template>
  <Hero>
    <Form v-if="!hash" @hash="hash = $event"/>
    <Result v-if="hash" :hash="hash" @restart="hash = null"/>
  </Hero>
</template>

<script>
import Hero from "./Hero";
import Form from "./Form";
import Result from "./Result";

export default {
  components: { Hero, Form, Result },
  data: () => ({ url: "", hash: null })
};
</script>
