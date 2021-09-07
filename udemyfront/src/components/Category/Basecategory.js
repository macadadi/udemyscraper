import React from 'react'
import { useSelector } from 'react-redux'
import BaseItem from './BaseItem'

function Basecategory() {
    const courses = useSelector(state=>state.courses)
    
    return (
        <div className="container-fluid ">
        <div className="row">
         {courses.status ==="fulfilled" ? courses.category.map((course,index)=> <BaseItem key={index} course={course}/>) :
         courses.status ==="rejected" ? <div><h1>We are currently offline for maintainance </h1>
         <p>Routine maintainance usually takes less than an hour, if this turns out to an extended outage
             we will notify you </p> </div> : <h1>Loading please wait..</h1>}
     
         {console.log(courses)}
         
        </div>
     </div>
    )
}

export default Basecategory
