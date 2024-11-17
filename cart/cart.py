class Cart():
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            Cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, product):
        products_id = str(products_id)
        if products_id in self.cart:
            pass
        else:
            self.cart[products_id] = {'precio': str(product.precio)}

        self.session.modified = True