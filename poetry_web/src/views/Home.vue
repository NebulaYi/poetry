<template>
  <div>
    <Header />
    <InputArea />
    <ResultArea />
    <Footer />
  </div>
</template>

<script>
import Header from "../components/Header.vue";
import InputArea from '../components/InputArea.vue';
import ResultArea from '../components/ResultArea.vue';
import Footer from '../components/Footer.vue';

export default {
  name: 'Home',
  components: {
    Header,
    InputArea,
    ResultArea,
    Footer
  },
}
</script>

<style>
/* Add styles if necessary */
</style>
