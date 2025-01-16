from flask import jsonify, request
from db import shoesFront

def setup_routes(app):
    @app.route("/")
    def home():
        return jsonify("ruta home")
    
    @app.route("/products", methods=['GET'])
    def products():

        page_num = request.args.get('page', default=1, type=int)


        products = shoesFront.getAll(page_num)

        print("Total de páginas:", products["totalPages"])  
        print("Productos:", products["products"])           

        return jsonify({"products": products["products"], "totalPages": products["totalPages"]})
        
    
    @app.route("/products/<int:product_id>")
    
    def productsId(product_id):
        productdb = shoesFront.getShoesProduct(product_id)
        return jsonify(productdb)
    
    @app.route("/products/filterAsc")
    def orderAsc():
        productsOrder = shoesFront.getAsc()
        return jsonify(productsOrder)
    
    @app.route("/products/filterDesc")
    def orderDesc():
        productsOrder = shoesFront.getDesc()
        return jsonify(productsOrder)