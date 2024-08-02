// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyA4XX3dGZv22X3tvGqvnKKJPdGNiqUkIL0",
  authDomain: "myshop-f2954.firebaseapp.com",
  projectId: "myshop-f2954",
  storageBucket: "myshop-f2954.appspot.com",
  messagingSenderId: "454542907350",
  appId: "1:454542907350:web:bc96f45b0e34a1c1cb3677",
  measurementId: "G-J6CJ4C6Y5D"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);