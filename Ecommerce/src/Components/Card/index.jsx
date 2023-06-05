import { useContext, useEffect } from 'react';
import { ShoppingCartContext } from '../../Context';
import { PlusIcon, CheckIcon } from '@heroicons/react/24/solid';

const Card = (data) => {
  const context = useContext(ShoppingCartContext);

  const ShowProduct = (productDetail) => {
    context.openProductDetail();
    context.setProductShow(productDetail);
  };

  const AddProductToCart = (event, productData) => {
    event.stopPropagation();
    context.setCartProducts([...context.cartProducts, productData]);
    context.openCheckoutSideMenu();
    context.closeProductDetail();
  };

  const renderIcon = (id) => {
    const isInCart = context.cartProducts.filter((product) => product.id === id).length > 0;

    if (isInCart) {
      return (
        <div
          className="absolute top-0 right-0 flex justify-center items-center bg-green-700  w-6 h-6 text-lg rounded-full m-2 p-1"
          onClick={(event) => AddProductToCart(event, data.data)}
        >
          <CheckIcon className="h-6 w-6 text-white" />
        </div>
      );
    } else {
      return (
        <div
          className="absolute top-0 right-0 flex justify-center items-center bg-white w-6 h-6 text-lg rounded-full m-2 p-1"
          onClick={(event) => AddProductToCart(event, data.data)}
        >
          <PlusIcon className="h-6 w-6 text-black" />
        </div>
      );
    }
  };

  useEffect(() => {
  
    context.setCount(context.cartProducts.length);
    if (context.cartProducts.length === 0) {
      context.CloseCheckoutSideMenuOpen();
    }
  }, [context.cartProducts]);

  return (
    <div
      className="bg-white cursor-pointer w-56 h-60 rounded-lg"
      onClick={() => {
        ShowProduct(data.data);
      }}
    >
      <figure className="relative mb-2 w-full h-4/5">
        <span className="absolute bottom-0 text-black text-xs left-0 bg-white/60 rounded-lg m-2 px-3 py-0.5">
          {data.data.categoryName}
        </span>
        <img className="w-full h-full object-cover rounded-lg" src={data.data.image} alt="" />
        {renderIcon(data.data.id)}
      </figure>

      <p className="flex justify-between">
        <span className="text-sm font-light">{data.data.title}</span>
        <span className="text-sm font-medium"> ${data.data.price}</span>
      </p>
    </div>
  );
};

export default Card;