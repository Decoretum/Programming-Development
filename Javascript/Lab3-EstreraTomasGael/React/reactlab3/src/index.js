import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

import Root from './routes/Clue'

import {
    createBrowserRouter,
    RouterProvider,
} from "react-router-dom";


const router = createBrowserRouter([
    {
        path: '/',
        element: <App /> ,
        errorElement: <h1> There is an error here with the connection to Jservice.IO (num)! Please Refresh this page! </h1>
    },
    {
        path: '/Clues',
        element: <Root />,
    }

])

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    //<React.StrictMode>
        <RouterProvider router={router} />
    //</React.StrictMode>
    
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
