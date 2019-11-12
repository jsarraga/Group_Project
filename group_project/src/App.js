import React from 'react';
import './App.css';
import UserHome from './components/LoggedView/User/UserHomePage'
import MainMenu from './components/MainSideBare'
import ProviderHome from './components/LoggedView/Provider/ProviderHomePage'
import Home from './components/NotLoggedView/Home'
import Header from './components/NotLoggedView/Header'
import Router from './components/NotLoggedView/Router'
import userRoute from './components/LoggedView/Router'



function App() {
  const token = sessionStorage.getItem("tokenUser")
  let content = null
  if(!token){
    content = (
      <div>
        <Router/>
      </div>
    )
  }else{
    content = (
      <div className="main">
          <MainMenu/>
          <UserHome/>
      </div>
    )
  }

  return (
    <div className="App">
      {content}
    </div>
  );
}

export default App;
