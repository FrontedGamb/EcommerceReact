import { XMarkIcon } from "@heroicons/react/24/solid"
import './styles.css'
const OrdersCard = props => {
    const { totalPrice, totalProducts, creationDate} = props
    return (
        <div className="flex justify-between items-center p-3 w-80 p-4 card-detail rounded-lg mb-4">
            <p className="flex justify-between w-80">
                <div className="flex flex-col w-full">
                    <div className="flex justify-between w-auto">
                        <p>Date: </p>
                        <span>{creationDate}</span>
                    </div>

                    <div className="flex justify-between w-full">
                        <p>Products:  </p>
                        <span>{totalProducts}</span>
                    </div>
                    <div className="flex justify-between w-full">
                        <p>Price:  </p>
                        <span className="font-medium text-1xl">{totalPrice}</span>
                    </div>

                    
                </div>

               
            </p>


        </div>
    )
}
export default OrdersCard;