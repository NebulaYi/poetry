<template>
  <div class="background">
    <img :src="imgSrc" width="100%" height="100%" alt="" />
  </div>
  <div class="homeView">
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
