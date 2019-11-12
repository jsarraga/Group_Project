import React from 'react'
import Search from '../../Search'
import UserHome from './Home'
import RightSidebare from '../../RightSidebare'

const UserHomePage = ()=>{
    return(
        <div className="content">
        <Search/>
      <div className="content_bottom">
          <UserHome/>
          <RightSidebare/>
          
      </div>
      
    </div>
    )
}

export default UserHomePage