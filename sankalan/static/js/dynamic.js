//javascript code for responsive collapse bars

var acc = document.getElementsByClassName("accordion");
  var i;
  for(i=0; i<acc.length; i++)
  {
    acc[i].addEventListener("click", function(){
      this.classList.toggle("active");
      var panel = this.nextElementSibling;
      if (panel.style.display === "block")
      {
        panel.style.display = "none";
      }
      else
      {
        panel.style.display = "block";
      }
    });
  }


// JAVASCRIPT FOR FEEDBACK FORM RATING PART  OF THE FORM
const ratingEl = document.querySelectorAll(".rating");
var fdBtn = document.querySelector("#feedback_submit_btn");


ratingEl.forEach((e1) =>{
  e1.addEventListener("click",() =>{
    ratingEl.forEach((innerE1) =>{
      innerE1.classList.remove("active");
    });
    e1.classList.add("active");
  });
});