console.log("Running script.js")

function change(element)
{
    console.log("element clicked", element);
    if(element.innerText == "Delicious") {
        element.innerText = "Yuck", element.value = "Yuck";
    } 
    else {
        element.innerText = "Delicious", element.value = "Delicious";
    }
}