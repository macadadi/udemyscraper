import React, { useEffect, useState } from 'react'
import { useDispatch } from 'react-redux';
import Basecategory from './Basecategory';
import { fetchByCategory } from '../Redux/courseSlice';
import './section.css'

function Coursecategory({match}) {
    const dispatch = useDispatch()
    const [baseUrl,setBaseUrl] = useState('/')
    const value = match.url
    let data;
    let url_link=""
    if(value === '/category/it-and-software'){
        data = "IT and Software"
        url_link="software"
    }
    else if(value ==='/category/development'){
        data = "Development"
        url_link="development"
    }
    else if(value ==='/category/business'){
        data = "Business"
        url_link="business"
    }
    else if(value ==='/category/design'){
        data = "Design"
        url_link="design"
    }
    else if(value ==='/category/marketing'){
        data = "Marketing"
        url_link="marketing"
    }
    else if(value ==='/category/finance'){
        data = "Finance"
        url_link="finance"
    }
    else{
        data = "Health and Fitness"
        url_link="fitness"
    }

 
    useEffect(()=>{
        dispatch(fetchByCategory(url_link))
    },[value])
    return (
        <div>
            <div className=" ">
            <div className="div-category">
            <h1>{data} </h1>
            </div>
            </div>
          
           <div className="mt-2 pt-1">
           <Basecategory />
           </div>
        </div>
    )
}

export default Coursecategory
