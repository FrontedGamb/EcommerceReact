
/**
 * Funcion par sumar los precios del checkout
 * @param {Array} products cartProduct: array of objects
 * @returns  {number} total price
 */

export const totalPrice = (products) => {
    let sum = 0;
  
    products.forEach((element) => {
      let price = parseInt(element.price, 10);
      if (!isNaN(price)) {
        sum += price;
      }
    });
  
    return sum;
  };