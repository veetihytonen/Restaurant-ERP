import axios from 'axios'

const registerUser = (newUser) => {
  const request = axios.post('/register', newUser)

  return request.then(response => response.data)
}

const userService = {registerUser}

export default userService

