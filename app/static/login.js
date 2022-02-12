const showlegends = (cliked_id) =>{
let getvalues = document.getElementById(cliked_id).value.trim();
if(cliked_id == "useremail" && getvalues != ""){
    console.log(getvalues);
   document.getElementById("usernamel").style.display = "block";
}else if(cliked_id == "password" && getvalues !== ""){
    console.log(getvalues);
    document.getElementById("passwordl").style.display = "block";
}else if(cliked_id == "cpassword" && getvalues !== ""){
    console.log(getvalues);
    document.getElementById("cpasswordl").style.display = "block";
}else{

}
}

const validatesignup = () =>{
    let passwords = document.getElementById("password").value.trim();
    let cpasswords = document.getElementById("cpassword").value.trim();
    if (passwords !== cpasswords || passwords === "" || cpasswords === ""){
        alert('password dont match,check and try again');
        return false;
    }
}

const validatelogin = () =>{
    let useremail = document.getElementById("useremail").value.trim();
    let passwords = document.getElementById("password").value.trim();
    if(useremail === "" || passwords === ""){
        if(useremail === ""){
            document.getElementById("useremail").style.borderColor = "red";
            return false;
        }else{
            document.getElementById("password").style.borderColor = "red";
            return false;
        }
    }
}

const removeerror = (cliked) =>{
    document.getElementById(cliked).style.borderColor ="#D4CCCE";
}