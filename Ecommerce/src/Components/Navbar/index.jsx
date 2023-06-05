import { NavLink } from "react-router-dom"
import { useContext } from 'react';
import { ShoppingCartContext } from '../../Context'
import { ShoppingBagIcon } from "@heroicons/react/24/solid";
import { useLocation } from "react-router-dom";
const NavBar = () => {
    const activeStyle = 'underline underline-offset-4'
    const context = useContext(ShoppingCartContext)
    const location = useLocation();

    return (
        <nav className="flex justify-between items-center top-0 fixed z-10 w-full py-5 px-8 text-sm font-light">
            <ul className="flex items-center gap-3">
                <li className="font-semibold text-lg">
                    <NavLink
                        to="/"
                        className={
                            ({ isActive }) =>
                                isActive ? activeStyle : undefined
                        }
                    >
                        Shopi
                    </NavLink>
                </li>
                <li>
                    <NavLink
                        to="/"
                        exact
                        onClick={() => context.setSearchByCategory("")}
                        isActive={() => location.pathname === "/" || location.pathname === "/all"}
                        className={({ isActive }) => (isActive ? activeStyle : undefined)}
                    >
                        All
                    </NavLink>
                </li>
                <li>
                    <NavLink
                        to="/clothes"
                        onClick={() => context.setSearchByCategory('clothes')}
                        className={
                            ({ isActive }) =>
                                isActive ? activeStyle : undefined
                        }
                    >
                        Clothes
                    </NavLink>
                </li>
                <li>
                    <NavLink
                        to="/electronics"
                        onClick={() => context.setSearchByCategory('electronics')}
                        className={
                            ({ isActive }) =>
                                isActive ? activeStyle : undefined
                        }
                    >
                        Electronics
                    </NavLink>
                </li>
                <li>
                    <NavLink
                        to="/furniture"
                        onClick={() => context.setSearchByCategory('furniture')}
                        className={
                            ({ isActive }) =>
                                isActive ? activeStyle : undefined
                        }
                    >
                        Furnitures
                    </NavLink>
                </li>
                <li>
                    <NavLink
                        to="/toys"
                        onClick={() => context.setSearchByCategory('toys')}
                        className={
                            ({ isActive }) =>
                                isActive ? activeStyle : undefined
                        }
                    >
                        Toys
                    </NavLink>
                </li>
                <li>
                    <NavLink
                        to="/others"
                        onClick={() => context.setSearchByCategory('others')}
                        className={
                            ({ isActive }) =>
                                isActive ? activeStyle : undefined
                        }
                    >
                        Others
                    </NavLink>
                </li>
            </ul>

            <ul className="flex items-center gap-3">
                <li className="text-black/60">
                    FrontedGamb
                </li>
                <li>
                    <NavLink
                        to="/my-order"
                        className={
                            ({ isActive }) =>
                                isActive ? activeStyle : undefined
                        }
                    >
                        My orders
                    </NavLink>
                </li>
                <li>
                    <NavLink
                        to="/my-account"
                        className={
                            ({ isActive }) =>
                                isActive ? activeStyle : undefined
                        }
                    >
                        My account
                    </NavLink>
                </li>
                <li>
                    <NavLink
                        to="/sign-in"
                        className={
                            ({ isActive }) =>
                                isActive ? activeStyle : undefined
                        }
                    >
                        Sign in
                    </NavLink>
                </li>

                <li className="flex items-center">
                    <ShoppingBagIcon
                        onClick={context.openCheckoutSideMenu}

                        className="h-6 w-6 text-black cursor-pointer"></ShoppingBagIcon>
                    <div>
                        {context.count}
                    </div>
                </li>

            </ul>


        </nav>
     )
}
export default NavBar