SELECT DISTINCT CART_ID
FROM CART_PRODUCTS
WHERE CART_ID = ANY(SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'Yogurt') AND
        CART_ID = ANY(SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'Milk')