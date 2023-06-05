import { useContext, useState, useEffect } from "react"
import Layout from "../../Components/Layout"
import Card from "../../Components/Card" 
import ProductDetail from "../../Components/ProducDetail"
import { ShoppingCartContext } from "../../Context"
import "./styles.css"
function Home() {
  
 const context = useContext(ShoppingCartContext)
 const renderView = () => {
    if(context.filterItems?.length>0){
      return(
        context.filterItems?.map(item=> (
          <Card key={item.id} data={item}/>
        ))
      )
    }
    else{
      return (
        <div>
          no results found :'(
        </div>
      )
    }
};

    return (
     
      <Layout className='App bg-red-100'>
        <div>
        <h1 className="text-center mb-6 font-medium text-xl">Exclusive Products</h1>
        </div>
        <input
        onChange={(event)=>{
          context.setSearchByTitle(event.target.value);

        }}
        className="rounded-lg border-black w-80 p-4 mb-4 focus:outline-none input"
        type="text"
         placeholder="Search a product"/>
        <div className="grid gap-4 grid-cols-4 w-full max-w-screen-lg grid-cols-auto justify-items-center sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
        {renderView()}
       

        </div>
        <ProductDetail/>
       
      </Layout>
    )
  }
export default Home 