import React, { useState } from 'react'

function BaseItem({course}) {
    const {category,uploaded,name,image_file,description,status,outcome,link} = course
    const [outline,setOutline] = useState(false)
    const course_outcome = outcome.split(',')

    
    return (
        <div className=" col-md-6 col-xl-4 p-3 ">
            <div className=" course  p-1">
               <div className="p-2 pb-0 d-flex justify-content-between"> 
                   <h4>{category}</h4>
                   <div className="d-flex  small-text-section">
                       <h5>Coupon status: </h5><h6>{status}</h6>
                   </div>
               </div>
               
                <div className="course-title">
                   <a href={link}> <h3>{name}</h3></a>
                    <img src={image_file} alt="titel" className="display-div mt-2 mb-2" />
                </div>
               <div className="d-flex small-text-section">
               <h5>Posted:</h5> <h6>{uploaded}</h6>
               </div>
                <div className="d-flex justify-content-between p-3 pt-0 pb-0">
                <h5>Course Description</h5>
                <a href={link}><h6>Enroll Now</h6></a>
                </div>
                <p className="p-2 pt-0 pb-0">{description}</p>


             <div>

                 { outcome.length < 2 ? "":
                 <div className="outcome">
                     <div>
                   <h5 onClick={()=>setOutline(!outline)}>Course outcome</h5> 
                   </div>
                   <ul> {outline && course_outcome.map((item,index)=><li key={index}>{item}</li>)} </ul>
                 </div> }
                   
                 </div>
            </div>
           
        </div>
    )
}

export default BaseItem
