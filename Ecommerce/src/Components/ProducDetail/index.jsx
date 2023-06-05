
import './styles.css'
import { useContext } from 'react'
import {XMarkIcon} from '@heroicons/react/24/solid'
import { ShoppingCartContext } from '../../Context'
const ProductDetail= ()=>{
    const context = useContext(ShoppingCartContext)
    console.log('PRODUCT TO SHOW', context.productShow)
   return (
    <aside 
    className={`${
        context.isProductDetailOpen ? 'translate-x-0' : 'translate-x-full'
      } product-detail flex-col fixed right-0 border border-black rounded-lg bg-white h-[calc(100vh-68px)] transition-transform duration-300 ease-in-out overflow-scroll`}
    >
        <div className='flex justify-between items-center p-6'>
            <h2 className='font-medium text-xl'>Detail</h2>
            <div onClick={context.CloseProductDetail}>
                <XMarkIcon className='h-6 w-6 text-black cursor-pointer'/>
            </div>
        </div>
        <figure className='px-6'>
            <img className='w-full h-full rounded-lg'
             src={context.productShow.image}
             alt="" />
        </figure>
        <p className='flex flex-col p-6'>
            <span className='font-medium text-2xl'>
                ${context.productShow.price}
            </span>
            <span className='font-medium text-md'>
                {context.productShow.title}
            </span>
            <span className='font-light text-sm'>
                {context.productShow.description}
            </span>
        </p>
    </aside>
   )
}

export default ProductDetail;