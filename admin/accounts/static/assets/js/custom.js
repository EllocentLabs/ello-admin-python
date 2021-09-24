function passwordShow() {
var x = document.getElementById("passWord2");
console.log(x)
if (x.type === "password") {
    x.type = "text";
} else {
    x.type = "password";
}
}