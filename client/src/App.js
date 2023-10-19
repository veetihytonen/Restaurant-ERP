import React, { useState, useEffect } from 'react'
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'

import Home from './pages/home'
import Login from './pages/login'
import Register from './pages/register'


const App = () => {
  const [currUser, setCurrUser] = useState()

  return (
    <>
      <Router>
        <Routes>
          <Route path='*' element={ <Navigate replace to='/' /> } />
          <Route path='/' element={ currUser ? <Home /> : <Navigate replace to='/login' /> } />
          <Route path='/login' element={ <Login /> }/>
          <Route path='/register' element={ <Register /> } />
        </Routes>
      </Router>
    </>
  )
}

export default App;
