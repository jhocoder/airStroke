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
        page_num = request.args.get("page", default=1, type=1)
        productsOrder = shoesFront.getAsc(page_num)
        
        return jsonify({
            "products": productsOrder["products"],
            "totalPages": productsOrder["totalPages"]
        })
    
    
    
    @app.route("/products/filterDesc", methods=['GET'])
    def orderDesc():
        page_num = request.args.get("page", default=1, type=int)
        productsOrder = shoesFront.getDesc(page_num) 

        return jsonify({
        "products": productsOrder["products"],
        "totalPages": productsOrder["totalPages"]
    })

    
    @app.route("/registerSend", methods = ['POST'])
    def registerUser():
        data = request.get_json()
        userRegister = shoesFront.addUser(data["nombre"], data["apellido"], data["email"], data["password"])
        if userRegister:
            return jsonify({"message": "User Register", "data": data})
