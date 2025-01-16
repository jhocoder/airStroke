<template>
  <div class="h-screen w-full  items-center flex flex-col">
    <Title class="mt-32"></Title>
    <ButtonView></ButtonView>

  </div>
</template>

<script>
import ButtonView from "@/components/homeComponents/ButtonView.vue";
import Title from "../components/homeComponents/Title.vue"


export default {
  name: "HomeView",
  components: {
    Title, ButtonView
  },
  data() {
    return {}
  }
}
</script>

<style>

</style>