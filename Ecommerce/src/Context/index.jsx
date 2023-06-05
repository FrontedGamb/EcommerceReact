import { createContext, useState } from "react";
import { useEffect } from "react";
import axios from "axios";
export const ShoppingCartContext = createContext();

export const ShoppingCartProvider = ({ children }) => {
    const [count, setCount] = useState(0);
    const [isProductDetailOpen, setIsProductDetailOpen] = useState(false)

    const openProductDetail = () => setIsProductDetailOpen(true)
    const CloseProductDetail = () => setIsProductDetailOpen(false)

    const [productShow, setProductShow] = useState({});
    const [cartProducts, setCartProducts] = useState([]);

    const [isCheckoutSideMenuOpen, setisCheckoutSideMenuOpen] = useState(false)

    const openCheckoutSideMenu = () => setisCheckoutSideMenuOpen(true)
    const CloseCheckoutSideMenuOpen = () => setisCheckoutSideMenuOpen(false)

    //Ordenes 

    const [order, setOrder] = useState([]);

    // Products
    const [items, setItems] = useState(null);
    const [filterItems, setFilterItems] = useState(null);
    const [searchByTitle, setSearchByTitle] = useState("");
    // Obtener productos

    const [searchByCategory, setSearchByCategory] = useState("");
    useEffect(() => {
      axios
        .get('http://localhost:8000/api/products')
        .then(response => {
          setItems(response.data);
          setFilterItems(response.data); // Establecer los productos filtrados como los productos iniciales
        })
        .catch(error => {
          console.error(error);
        });
    }, []);
    
    // Filtrar productos por título
    const filteredItemsByTitle = (items, searchByTitle) => {
      return items.filter(item => item.title.toLowerCase().includes(searchByTitle.toLowerCase()));
    };
    
    const filteredItemsByCategory = (items, searchByCategory) => {
      return items.filter(item => item.categoryName.toLowerCase().includes(searchByCategory.toLowerCase()));
    };

    const filterBy=(searchType, items, searchByTitle, searchByCategory)=>{
      if(searchType=='BY_TITLE'){
        return filteredItemsByTitle(items, searchByTitle);
      }
      if(searchType=='BY_CATEGORY'){
        return filteredItemsByCategory(items,searchByCategory)
      }
      if(searchType=='BY_TITLE_AND_CATEGORY'){
        return filteredItemsByCategory(items,searchByCategory).filter(item=>item.title.toLowerCase().includes(searchByTitle.toLowerCase()))
      }
      if(!searchType){
        return items
      }
    }

    useEffect(() => {
      if(searchByCategory && searchByTitle) setFilterItems(filterBy('BY_TITLE_AND_CATEGORY', items, searchByTitle, searchByCategory))
      if(searchByTitle && !searchByCategory)setFilterItems(filterBy('BY_TITLE', items, searchByTitle, searchByCategory))
      if(searchByCategory && !searchByTitle) setFilterItems(filterBy('BY_CATEGORY', items, searchByTitle, searchByCategory))
      if(!searchByCategory && !searchByTitle) setFilterItems(filterBy(null, items, searchByTitle, searchByCategory))
    }, [items, searchByTitle, searchByCategory]);
  




    
    console.log("OBJETOS FILTRADOS:", filterItems);
    
    return (
        <ShoppingCartContext.Provider value={
            {
                count,
                setCount,
                openProductDetail,
                CloseProductDetail,
                isProductDetailOpen,
                productShow,
                setProductShow,
                cartProducts,
                setCartProducts,
                isCheckoutSideMenuOpen,
                openCheckoutSideMenu,
                CloseCheckoutSideMenuOpen,
                order,
                setOrder,
                items,
                setItems,
                searchByTitle,
                setSearchByTitle,
                filterItems,
                setFilterItems,
                filteredItemsByTitle,
                searchByCategory,
                setSearchByCategory
            }
        }>
            {children}
        </ShoppingCartContext.Provider>

    )
}

