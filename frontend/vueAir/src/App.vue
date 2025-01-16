<script setup>
import { RouterLink, RouterView } from 'vue-router';
import Menu from './components/Menu.vue';
</script>

<template>
  <div id="app">
    <!-- Componente de menú -->
    <header>
      <Menu />
    </header>
  
    <!-- Capa oscura sobre el fondo -->
    <div class="background-overlay"></div>
  
    <!-- Área donde se renderizan los demás componentes -->
    <div class="content-area">
      <RouterView />
    </div>
  </div>
</template>

<style scoped>
/* Aplica el fondo a toda la aplicación */
#app {
  position: relative; /* Necesario para el posicionamiento */
  background: url('./assets/images/fondo.webp') no-repeat center center fixed; /* Fondo de pantalla */
  background-size: cover; /* Asegura que el fondo ocupe toda la pantalla */
  min-height: 100vh; /* Asegura que ocupe toda la altura de la pantalla */
  width: 100%;
  display: flex;
  flex-direction: column; /* Coloca el menú arriba y el contenido abajo */
  z-index: 0;
/* Asegura que el fondo esté debajo del contenido */
}

/* Capa oscura sobre el fondo */
.background-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5); /* Oscurece el fondo con un color negro semitransparente */
  z-index: -1; /* Mantiene la capa detrás del contenido */
}


/* Estilo opcional para la sección que contiene el contenido del RouterView */
.content-area {
  margin-top: 5vh;
}
</style>
