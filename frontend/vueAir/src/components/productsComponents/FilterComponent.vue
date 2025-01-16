<script>
import { ref } from 'vue';

export default {
    name: "FilterComponent",
    data() {
        return {
            products: [],
        };
    },
    methods: {
        async lowest() {
            const api = await fetch("http://localhost:3030/products/filterDesc");
            const json = await api.json();
            this.products = json;
            this.$emit("productsFiltered", this.products); 
        },
        async highest() {
            const api = await fetch("http://localhost:3030/products/filterAsc");
            const json = await api.json();
            this.products = json;
            this.$emit("productsFiltered", this.products);
        },
        async offer() {
            const api = await fetch("http://localhost:3030/products/filterOffer");
            const json = await api.json();
            this.products = json;
            this.$emit("productsFiltered", this.products);
        },
        async size() {
            const api = await fetch("http://localhost:3030/products/filterSize");
            const json = await api.json();
            this.products = json;
            this.$emit("productsFiltered", this.products);
        },
        async color() {
            const api = await fetch("http://localhost:3030/products/filterColor");
            const json = await api.json();
            this.products = json;
            this.$emit("productsFiltered", this.products);
        },
    },
};
</script>

<template>
    <div class="w-[40vh]">
        <div class=" w-[full] flex justify-between p-3 bg-teal-500 mb-5">
            <h3>Filter</h3>
            <i class="fa-solid fa-filter"></i>
        </div>
        <input
            class="border-2 border-teal-600 ml-3 bg-teal-300 shadow-inner w-[30vh] p-1"
            type="text"
            name=""
            id=""
            placeholder="Buscar"
        />
        <div class="gap-3 flex flex-col mt-10 text-2xl text-neutral-50 items-center">
            <button @click="lowest" class="p-2 rounded hover:bg-cyan-100">
                Lowest Price
            </button>
            <hr class="w-[25vh]" />
            <button @click="highest" class="p-2 rounded hover:bg-cyan-100">
                Highest Price
            </button>
            <hr class="w-[25vh]" />
            <button @click="offer" class="p-2 rounded hover:bg-cyan-100">
                Offer
            </button>
            <hr class="w-[25vh]" />
            <button @click="size" class="p-2 rounded hover:bg-cyan-100">
                Size
            </button>
            <hr class="w-[25vh]" />
            <button @click="color" class="p-2 rounded hover:bg-cyan-100">
                Color
            </button>
        </div>
    </div>
</template>

<style scoped>
/* Puedes agregar los estilos que prefieras */
</style>