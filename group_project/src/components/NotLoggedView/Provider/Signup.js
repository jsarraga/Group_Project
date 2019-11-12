import React from 'react'

const ProviderSIgnup = ()=>{
    return(
        <div>
      <form>

        <h3>Provider Sign up</h3>

        <label for="firstN">First Name</label>
        <input type="text" placeholder="first Name" id="firstN"/>

        <label for="lastN">Last Name</label>
        <input type="text" placeholder="last Name" id="lastN"/>

        <label for="username">Username</label>
        <input type="text" placeholder="username" id="username"/>

        <label for="username">Department</label>
        <input type="text" placeholder="department" id="department"/>

        <label for="email">Email</label>
        <input type="email" placeholder="email" id="email"/>

        <label for="password">Password</label>
        <input type="text" placeholder="password" id="password"/>

        <input type="button" value="login"/>
      </form>
      <a href="/provider">have an account?</a>
      <a href="/user">Go to User</a>
      </div>
    )
}

export default ProviderSIgnup