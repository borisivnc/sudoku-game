$(document).ready(function() {
    const dropArea = document.querySelector(".drop-zone"),
        dragText = dropArea.querySelector("header"),
        input = dropArea.querySelector("input");
    const icon = dropArea.querySelector("i");
    const subButton = document.getElementById("sub");

input.addEventListener("change", function(){
    file = this.files[0];
    dropArea.classList.add("active");
    displayFile()
});

//If user Drag File Over DropArea
dropArea.addEventListener("dragover", (e)=>{
    e.preventDefault();
    dropArea.classList.add("active");
    dragText.textContent = "Release to Upload File";
});

//If user leave dragged File from DropArea
dropArea.addEventListener("dragleave", ()=>{
    dropArea.classList.remove("active");
    dragText.textContent = "Drop file to upload or click here";
});

dropArea.addEventListener("drop", (e)=>{
    e.stopPropagation();
    e.preventDefault()
    let file = e.dataTransfer.files[0]
    input.files = e.dataTransfer.files;
    console.log(input.files)
    const fileReader = new FileReader();
    $(icon).removeClass('fa-cloud-upload-alt')
    $(icon).addClass('fa-check-circle').css("color","green")
    dragText.textContent = "File uploaded";
    fileReader.readAsDataURL(file);
    subButton.style.visibility = "visible"
});

dropArea.addEventListener("click",() => {
    input.click()
    console.log("here in click")
});

function displayFile(){
    let fileType = file.type;
    let validExtensions = ["image/jpeg", "image/jpg", "image/png"];
    if(validExtensions.includes(fileType)){
        const fileReader = new FileReader();
        $(icon).removeClass('fa-cloud-upload-alt')
        $(icon).addClass('fa-check-circle').css("color","green")
        dragText.textContent = "File uploaded";
        fileReader.readAsDataURL(file);
        subButton.style.visibility = "visible"
    }
    else {
    alert("This is not an image file!");
    dropArea.classList.remove("active");
    dragText.textContent = "Drop file to upload or click here";
    }
}

});