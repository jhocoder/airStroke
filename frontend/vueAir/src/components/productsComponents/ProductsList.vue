<script>
import FilterComponent from './FilterComponent.vue';

export default {
    name: "ProductsList",
    components:{
        FilterComponent
    } ,
    props: {
        products: {
            type: Array, 
            required: true
        }
    },
    mounted() {
        console.log("Productos recibidos en ProductsList:", this.products);

    }
};
</script>

<template>
    <div class="bg-white w-full"> 
        <ul class="justify-center mt-12 product-list w-[160vh] h-screen flex flex-wrap gap-24">
            <li v-for="(product, index) in products" :key="index" class="list-none">
                <div class="border-4 w-[40vh] h-[40vh] flex flex-col justify-center items-center">
            
                    <img :src="product[6]" alt="Imagen del producto" class="w-[80%] h-auto mt-2" />
                    <span>Nombre: {{ product[1] }}</span>
                    <span>Talla: {{ product[3] }}</span>
                    <span>Color: {{ product[4] }}</span>
                    <span>Precio: {{ product[5] }}</span>
                </div>
            </li>
        </ul>
    </div>
</template>

<style scoped>


</style>