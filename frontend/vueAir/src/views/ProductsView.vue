<script>
import ProductsList from "@/components/productsComponents/ProductsList.vue";
import ProductsServices from "@/services/ProductsServices.js";
import FilterComponent from "@/components/productsComponents/FilterComponent.vue";
import { ref } from "vue";

export default {
    name: "ProductsView",
    components: {
        ProductsList,
        FilterComponent,
    },
    data() {
        return {
            products: ref([]),
            currentPage: 1,
            totalPages: 1,
            order: 'default'
        };
    },
    methods: {
        updatedProducts(productsFiltered) {
            this.products.value = productsFiltered; // Actualiza los productos con los filtrados
            console.log('Productos filtrados:', productsFiltered);
        },
        async fetchProducts(page) {
            const service = new ProductsServices();
            await service.fetchAll(page);
            this.products.value = service.getProducts().value;
            this.totalPages = service.getTotalPages().value;

            console.log("Productos en ProductsView:", this.products.value); 
            console.log("Total de páginas:", this.totalPages);

            this.$router.push({ path: "/products", query: { page } });
        },
        nextPage() {
            if (this.currentPage < this.totalPages) {
                this.currentPage++;
                this.fetchProducts(this.currentPage);
            }
        },
        prevPage() {
            if (this.currentPage > 1) {
                this.currentPage--;
                this.fetchProducts(this.currentPage);
            }
        }
    },
    async mounted() {
        const page = parseInt(this.$route.query.page || 1);
        this.currentPage = page;
        await this.fetchProducts(page);
    },
    watch: {
        "$route.query.page"(newPage) {
            const page = parseInt(newPage || 1);
            this.fetchProducts(page);
        }
    }
};
</script>

<template>
    <div>
        <div class="border-2 border-teal-600 bg-teal-800 h-screen w-full flex">
            <FilterComponent @productsFiltered="updatedProducts" />
        <!-- Escucha el evento -->
             <ProductsList :products="products.value" /> 
        </div><!-- Pasamos los productos actualizados -->
        <div class="w-full items-center flex border-2 justify-center gap-3">
            <h2 class="hover:cursor-pointer" @click="prevPage">ANTERIOR</h2>
            <h2 class="hover:cursor-pointer" @click="nextPage">SIGUIENTE</h2>
        </div>
    </div>
</template>

<style scoped>
.product-list {
    list-style: none;
    padding: 0;
    text-align: center;
}
</style>
