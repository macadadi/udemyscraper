import './App.css';
import HomeComponent from './components/Home/HomeComponent';
import NavbarComponent from './components/Navigation/NavbarComponent';
import {BrowserRouter as Router,Route,Switch,Redirect} from 'react-router-dom'
import { useDispatch } from 'react-redux';
import { useEffect } from 'react';
import { fetchCourses} from './components/Redux/courseSlice';
import Coursecategory from './components/Category/Coursecategory';

function App() {
  const dispatch = useDispatch()

  useEffect(()=>{
      dispatch( fetchCourses())
     
  },[])
  return (
    <div className=" pt-0 mt-0 app">
      <Router>
      <NavbarComponent />  
      <Switch>
        <Route exact path="/category/:development" component={Coursecategory} />
        <Route exact path="/" component={HomeComponent} />
        <Redirect from="*" to="/" />
       
      </Switch>
      
     
      </Router>
    </div>
  );
}

export default App;
