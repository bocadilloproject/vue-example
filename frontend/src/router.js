import Vue from "vue";
import VueRouter from "vue-router";
import Home from "./components/Home";
import Link from "./components/Link";

Vue.use(VueRouter);

export default new VueRouter({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/:hash",
      name: "link",
      component: Link,
      props: true
    }
  ]
});
