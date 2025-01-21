<template>
    <div class="relative w-full">
      <!-- Menú de fondo con Tailwind -->
      <div class="bg-gray-900/70 flex h-32 mt-5 mr-3 ml-3 justify-between border-4 border-teal-500 ">

        <div class=" text-white text-[64px] font-bold items-center b w-[71vh] flex justify-center">
        AIR STROKE
      </div>
  
      <!-- Menú -->
      <div class="h-full  w-[120vh] flex justify-around items-center text-white font-bold text-2xl  ">
        <router-link to="/" class="mr-12">HOME</router-link>
        <router-link to="/products" class="mr-12 hover:text-teal-400" >PRODUCTS</router-link>
        <router-link to="/about" class="mr-12 hover:text-teal-400">ABOUT</router-link>
        <router-link to="/login" class="hover:text-teal-400">LOGIN</router-link>

      </div>

      </div>
  
      
    </div>
  </template>
  
  <script>
  export default {
    name: "Menu",
    data() {
      return {};
    },
  };
  </script>
  