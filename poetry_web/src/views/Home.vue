<template>
  <div class="background">
    <img :src="imgSrc" width="100%" height="100%" alt="" />
  </div>
  <div class="homeView">
    <Header />
    <Generate />
    <Footer />
  </div>
</template>

<script>
import Header from "../components/Header.vue";
import Footer from '../components/Footer.vue';
import Generate from "@/components/Generate.vue";

export default {
  name: 'Home',
  components: {
    Header,
    Generate,
    Footer
  },
  data(){
    return {
      imgSrc:require('../assets/img.jpg')
    }
  }
}
</script>

<style>
/* Add styles if necessary */

.background{
  width:100%;
  height:100%;  /**宽高100%是为了图片铺满屏幕 */
  z-index:-1;
  position: absolute;
  overflow: hidden; /* 添加此行以隐藏溢出内容 */
  //filter: brightness(0.8) contrast(0.8);
}

.homeView{
  width:100%;
  height:100%;
  z-index:1;
  position: absolute;
}
</style>
