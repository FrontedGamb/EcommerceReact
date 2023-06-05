import { useContext } from "react";
import { Link } from "react-router-dom";
import Layout from "../../Components/Layout";
import OrdersCard from "../../Components/OrdersCard";
import { ShoppingCartContext } from "../../Context";
import { ChevronLeftIcon } from "@heroicons/react/24/solid";

function MyOrder() {
  const context = useContext(ShoppingCartContext);
  console.log(context.order);
  return (
    <Layout>
      <div className="text-center mb-5">
        <h1>My Order</h1>
      </div>
      
      {context.order.length === 0 ? (
        <h2>No orders found</h2>
      ) : (
        context.order.map((order, index) => (
          <Link key={index} to={`/my-orders/${index}`}>
            <OrdersCard
              totalPrice={order.totalPrice}
              totalProducts={order.total}
              creationDate={order.date}
            />
          </Link>
        ))
      )}
    </Layout>
  );
}

export default MyOrder;