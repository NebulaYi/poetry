<template>
  <div>
    <Header />
    <NavBar />
    <InputArea />
    <ResultArea />
    <Footer />
  </div>
</template>

<script>
import Header from "@/views/Header.vue";
import NavBar from '../components/NavBar.vue'
import InputArea from '../components/InputArea.vue'
import ResultArea from '../components/ResultArea.vue'
import Footer from '../components/Footer.vue'

export default {
  name: 'Home',
  components: {
    Header,
    NavBar,
    InputArea,
    ResultArea,
    Footer
  }
}
</script>

<style>
/* Add styles if necessary */
</style>
