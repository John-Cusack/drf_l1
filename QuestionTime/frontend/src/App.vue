<template>
  <div id="app">
    <NavbarComponent />
    <router-view />
  </div>
</template>

<script>
import NavbarComponent from './components/Navbar.vue'
export default {
  name: "App",
  components: {

  }
}
</script>

<style>
    html, body {
        height: 100%;
        font-family: "Playfair Display", serif;
    }
</style>
