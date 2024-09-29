function hideNav(){
    document.querySelector("nav").style.opacity = "0%";
}
function showNav(){
    document.querySelector("nav").style.opacity = "100%";
}
function darkMode(){
    document.querySelector("body").classList.toggle("darkmode");
    document.querySelector("#intro-text").classList.toggle("darkmode");
}
var vid = document.querySelector("video")
function endVid(){
    vid.addEventListener("ended",function(){console.log("Video Has Ended")})
}
//Objects and Constructors
function CreateUser(name,email,pass){
    this.name = name;
    this.email = email;
    this.pass = pass;
} 
function submitForm(){
    var userName = document.getElementById("name").value
    var userEmail = document.getElementById("email").value
    var userPass = document.getElementById("pass").value
    var user1 = new CreateUser(userName,userEmail,userPass)
    var greeting = "Welcome " + user1.name + ", you have successfully registered"
    document.getElementById("greeting").textContent = greeting
}
