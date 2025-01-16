import { ref } from 'vue';

class ProductsServices {
    _products;
    _totalPages;

    constructor() {
        this._products = ref([]);
        this._totalPages = ref(1); // Inicializar total de páginas
    }

    getProducts() {
        return this._products; // Retornar los productos
    }

    getTotalPages() {
        return this._totalPages; // Retornar el total de páginas
    }

    async fetchAll(page = 1) {
        try {
            const apiProducts = `http://localhost:3030/products?page=${page}`;
            const response = await fetch(apiProducts);
            const json = await response.json();
            this._products.value = json.products; // Actualizar productos
            this._totalPages.value = json.totalPages; // Actualizar total de páginas
            // console.log(this._products.value, this._totalPages.value); // Comprobar los datos
        } catch (error) {
            console.error("Error fetching products:", error);
        }
    }

    async fetchDesc(page = 1) {
        try {
            const apiProducts = `http://localhost:3030/products/filterDesc?page=${page}`;
            const response = await fetch(apiProducts);
            const json = await response.json();
            this._products.value = json.products; // Actualizar productos
            this._totalPages.value = json.totalPages; // Actualizar total de páginas
            // console.log(this._products.value, this._totalPages.value); // Comprobar los datos
        } catch (error) {
            console.error("Error fetching products:", error);
        }
    }
}

export default ProductsServices;
