import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import userService from '../services/user_service'

const NewUserForm = ({ 
  submitForm, 
  username,
  handleUsernameChange,
  role,
  handleRoleChange,
  passW1,
  handlePassW1Change,
  passW2,
  handlePassW2Change
}) =>
  <div>
    <form onSubmit={submitForm}>
      <label>
        Käyttäjänimi:
        <input type="text" value={username} onChange={handleUsernameChange} />
      </label>
      <br/>
      <label>
        Rooli:
        <label>
          <input type="radio" value={"0"} onChange={handleRoleChange} checked={role === "0"} />
          Käyttäjä
        </label>
        <label>
          <input type="radio" value={"1"} onChange={handleRoleChange} checked={role === "1"} />
          Esimies
        </label>
        <label>
          <input type="radio" value={"2"} onChange={handleRoleChange} checked={role === "2"} />
          Hallinnoitsija
        </label>
      </label>
      <br/>
      <label>
        Salasana:
        <input type="password" value={passW1} onChange={handlePassW1Change} />
      </label>
      <br/>
      <label>
        Vahvista:
        <input type="password" value={passW2} onChange={handlePassW2Change} />
      </label>
      <br/>  
      <button type="submit">Luo käyttäjä</button>
    </form>
  </div>


const Register = () => {
  const [newName, setNewName] = useState('')
  const [newRole, setNewRole] = useState('0')
  const [newPassword1, setNewPassword1] = useState('')
  const [newPassword2, setNewPassword2] = useState('')
  const navigate = useNavigate()

  const handleUsernameChange = (event) => {
    setNewName(event.target.value)
  }
  
  const handleRoleChange = (event) => {
    setNewRole(event.target.value)
  }

  const handlePassW1Change = (event) => {
    setNewPassword1(event.target.value)
  }

  const handlePassW2Change = (event) => {
    setNewPassword2(event.target.value)
  }

  const validateUsername = (username) => {
    const minUsernameLen = 4

    if (username.lenght < minUsernameLen) {
      window.alert(`Käyttjänimen tulee olla vähintään ${minUsernameLen} merkkiä`)
      return false
    }

    return true
  }

  const validatePasswords = (passW1, passW2) => {
    const minPassWLen = 4

    if (!(passW1 === passW2)) {
      window.alert('Salasanat eivät täsmää')
      return false
    }

    if (passW1.length < minPassWLen) {
      window.alert(`Salasanan tulee olla vähintään ${minPassWLen} merkkiä`)
      return false
    }

    return true
  }

  const submitForm = (event) => {
    event.preventDefault()

    if (!validateUsername(newName)) {
      return
    }
    
    if (!validatePasswords(newPassword1, newPassword2))
      return

    const newUser = {
      username: newName,
      role: newRole,
      password: newPassword1
    }

    userService
      .registerUser(newUser)
      .then(createdUser => {
        console.log(createdUser)
      }
    )
    
    navigate('/login')
  }

  return (
    <div>
      <h2>Luo uusi käyttäjä</h2>
      <NewUserForm 
        submitForm={submitForm}
        username={newName}
        handleUsernameChange={handleUsernameChange}
        role={newRole}
        handleRoleChange={handleRoleChange}
        passW1={newPassword1}
        handlePassW1Change={handlePassW1Change}
        passW2={newPassword2}
        handlePassW2Change={handlePassW2Change}
      />
    </div>
  )
}

export default Register
