import React, { useState } from 'react'
import './index.css'
import MenuIcon from '@material-ui/icons/Menu';
import { Link } from 'react-router-dom'
import CloseIcon from '@material-ui/icons/Close';
import udemy from './udemy.png'

function NavbarComponent() {
    const [menu,setMenu] = useState(false)
    return (
        <div className="nav-component pl-2 pr-1 sticky-top">
            <div className="d-flex justify-content-between align-items-center ">
                <div className=" pt-1 pb-1 banner">
                    <img src={udemy} alt="log" className="banner-img" />
                
                </div>
               <div className="small-screen ">
               <div className={`category p-1 ${menu ? "":"hidemenu"}`}>
                    <Link to='/' onClick={()=>setMenu(!menu)}>Home</Link>
                    <Link to='/category/finance' onClick={()=>setMenu(!menu)}>Finance</Link>
                    <Link to='/category/development' onClick={()=>setMenu(!menu)}>Development</Link>
                    <Link to='/category/business' onClick={()=>setMenu(!menu)}>Business</Link>
                    <Link to='/category/it-and-software' onClick={()=>setMenu(!menu)}>IT and Software</Link>
                    <Link to='/category/design' onClick={()=>setMenu(!menu)}>Design</Link>
                    <Link to='/category/marketing' onClick={()=>setMenu(!menu)}>Marketing</Link>
                    <Link to='/category/health-and-fitness' onClick={()=>setMenu(!menu)}>Health and Fitness</Link>
                    
                </div>
               </div>
               <button onClick={()=>setMenu(!menu)} className="nav-btn p-1 m-3 mt-1 mb-1">{menu ? <CloseIcon /> : <MenuIcon />}    </button>
            </div>
        </div>
    )
}

export default NavbarComponent
