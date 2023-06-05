import './styles.css';
import { useContext } from 'react';
import { Link } from 'react-router-dom';
import { XMarkIcon } from '@heroicons/react/24/solid';
import { ShoppingCartContext } from '../../Context';
import OrderCard from '../OrderCard';
import { totalPrice } from '../../utils';

const CheckoutSideMenu = () => {
    const context = useContext(ShoppingCartContext);
    const handleDelete = (id) => {
        const filteredProducts = context.cartProducts.filter((product) => product.id != id);
        context.setCartProducts(filteredProducts);
    };

    const currentDate = new Date();
    const options = {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
    };
    const formattedDate = currentDate.toLocaleString('es', options);

    console.log(formattedDate);

    const handleCheckout = () => {
        const orderToAdd = {
            date: formattedDate,
            product: context.cartProducts,
            total: context.cartProducts.length,
            totalPrice: totalPrice(context.cartProducts),
        };
        context.setOrder([...context.order, orderToAdd]);
        context.setCartProducts([]);
        context.CloseCheckoutSideMenuOpen();
    }
    return (
        <aside
            className={`${context.isCheckoutSideMenuOpen ? 'translate-x-0' : 'translate-x-full'
                } product-detail flex-col fixed right-0 border border-black rounded-lg bg-white h-[calc(100vh-68px)] transition-transform duration-300 ease-in-out overflow-scroll`}
        >
            <div className='flex justify-between items-center p-6'>
                <h2 className='font-medium text-xl'>Detail</h2>
                <div onClick={context.CloseCheckoutSideMenuOpen}>
                    <XMarkIcon className='h-6 w-6 text-black cursor-pointer' />
                </div>
            </div>

            <div className='px-6 flex-1'>
                {context.cartProducts.length === 0 ? (
                    <h2>No products found</h2>
                ) : (
                    context.cartProducts.map((product) => (
                        <OrderCard
                            key={product.id}
                            id={product.id}
                            title={product.title}
                            imageURL={product.image}
                            price={product.price}
                            handleDelete={handleDelete}
                        />
                    ))
                )}
            </div>

            <div className='px-6 mb-2'>
                <p className='flex justify-between items-center mb-3'>
                    <span className='font-light'>Total: </span>
                    <span className='font-medium text-2xl'>${totalPrice(context.cartProducts)}</span>
                </p>
                <Link to="/my-orders/last">
                    <button
                        onClick={() => handleCheckout()}
                        className='w-full bg-black py-3 text-white rounded-lg'
                        disabled={context.cartProducts.length === 0}
                    >
                        Checkout
                    </button>
                </Link>
            </div>
        </aside>
    );
};

export default CheckoutSideMenu;