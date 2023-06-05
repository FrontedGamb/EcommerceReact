import {  useRoutes, BrowserRouter } from 'react-router-dom'
import './App.css'
import Home from '../home'
import MyAccount from '../MyAccount'
import MyOrders from '../MyOrders'
import NotFound from '../NotFound'
import SignIn from '../SignIn'
import NavBar from '../../Components/Navbar'
import MyOrder from '../MyOrder'
import { ShoppingCartProvider } from '../../Context'
import CheckoutSideMenu from '../../Components/CheckoutSideMenu'
const AppRoutes =()=>{
  let routes = useRoutes([
    {
      path: '/', 
      element:<Home/>
  },
  {
    path: '/clothes', 
    element:<Home/>
},
{
  path: '/electronics', 
  element:<Home/>
},
{
  path: '/toys', 
  element:<Home/>
},
{
  path: '/furniture', 
  element:<Home/>
},
{
  path: '/others', 
  element:<Home/>
},
  {
      path: '/my-account', 
      element:<MyAccount/>
  },
  {
    path: '/my-orders/last', 
    element:<MyOrders/>
  },
  {
    path: '/my-orders/:id', 
    element:<MyOrders/>
  },
  {
    path: '/my-order', 
    element:<MyOrder/>
  },
  {
    path: '/*', 
    element:<NotFound/>
  },
  {
    path: '/sign-in', 
    element:<SignIn/>
  }
  ])
  return routes;
}

function App() {
  
  return (
    <ShoppingCartProvider>
       <BrowserRouter>
      <AppRoutes/>
      <NavBar/>
      <CheckoutSideMenu/>
    </BrowserRouter>
    </ShoppingCartProvider>
   
  )
}

export default App
