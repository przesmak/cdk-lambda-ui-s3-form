import { useState } from 'react';
import logo from './logo.svg';
import './App.css';

const API_URL_CDK = 'https://dfae6obtva.execute-api.eu-west-1.amazonaws.com/prod/'

function App() {
  const [formInput, setFormInput] = useState({ 'name': '', 'surname': '' , 'fileName': ''})

  const handleChange = (e) => {
    setFormInput({
      ...formInput, 
      [e.target.name]: e.target.value,
    })
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    console.log(formInput);
    uploadToS3(formInput)
  }

  const uploadToS3 = async (formData) => {
    console.log('formData JSON: ', JSON.stringify(formData));
    const url = `${API_URL_CDK}/${formData.fileName || 'formData'}`;
    const options = {
      method: 'POST',
      body: JSON.stringify(formData),
      headers: {
        'Content-Type':'application/json',
      },
    }
    await fetch(url, options)
      .then(response => {
        console.log('response: ', response);
      })
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Hello from my static site hosted by S3 bucket
        </p>

        <form onSubmit={handleSubmit}>
          <div>
            <label>
              Name:
              <input name="name" type="text" value={formInput.name} onChange={handleChange}/>
            </label>
          </div>
          <div>
            <label>
              Surname:
              <input name="surname" type="text" value={formInput.surname} onChange={handleChange}/>
            </label>
          </div>
          <div>
            <label>
              File name to save:
              <input name="fileName" type="text" value={formInput.fileName} onChange={handleChange}/>
            </label>
          </div>
          <button type='Submit'>Submit</button>
        </form>
      </header>
    </div>
  );
}

export default App;
