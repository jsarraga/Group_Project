import React from 'react'

const ProviderLogin = ()=>{
    return(
        <div>
      <form>

        <h3>Provider Login</h3>

        <label for="username">Username</label>
        <input type="text" placeholder="username" id="username"/>
        <label for="password">Password</label>
        <input type="text" placeholder="password" id="password"/>
        <input type="button" value="login"/>
      </form>
      <a href="/provider/signup">Don't have an account?</a>
      <a href="/user">Go to user</a>
      </div>
    )
}

export default ProviderLogin