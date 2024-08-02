// static/js/auth.js
const auth = firebase.auth();

// Sign up function
function signUp() {
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  auth.createUserWithEmailAndPassword(email, password)
    .then((userCredential) => {
      console.log('User signed up:', userCredential.user);
      document.getElementById('email').style.display = 'none';
      document.getElementById('password').style.display = 'none';
    })
    .catch((error) => {
      console.error('Error signing up:', error);
    });
}

// Sign in function
function signIn() {
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  auth.signInWithEmailAndPassword(email, password)
    .then((userCredential) => {
      console.log('User signed in:', userCredential.user);
      document.getElementById('email').style.display = 'none';
      document.getElementById('password').style.display = 'none';
    })
    .catch((error) => {
      console.error('Error signing in:', error);
    });
}

// Sign out function
function signOut() {
  auth.signOut().then(() => {
    console.log('User signed out');
  }).catch((error) => {
    console.error('Error signing out:', error);
  });
}
