import React, { useState, useEffect } from 'react'
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'

import Home from './pages/home'
import Login from './pages/login'


const App = () => {
  const [currUser, setCurrUser] = useState()

  return (
    <>
      <Router>
        <Routes>
          <Route path='/' element={ currUser ? <Home /> : <Navigate replace to='/login' /> }/>
          <Route path='/login' element={ <Login /> }/>
        </Routes>
      </Router>
    </>
  )
}

export default App;
