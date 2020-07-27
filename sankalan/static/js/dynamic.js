//javascript code for responsive collapse bars

var acc = document.getElementsByClassName("accordian");
  var i;
  for(i=0; i<acc.length; i++)
  {
    acc[i].addEventListener("click", accofunction);
  }

  function accofunction()
   {
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
    }

function openBar1()
    {
      var x = document.getElementById('about');
     if (x.style.display === "none")
     {
       x.style.display = "block";
     }
     else
     {
       x.style.display = "none";
     }
   }

 function openBar2()
    {
      var x = document.getElementById("faq");
     if (x.style.display === "none")
     {
       x.style.display = "block";
     }
     else
     {
       x.style.display = "none";
     }
   }

function openBar3()
    {
      var x = document.getElementById("contact");
     if (x.style.display === "none")
     {
       x.style.display = "block";
     }
     else
     {
       x.style.display = "none";
     }
   }

function openBar4()
    {
      var x = document.getElementById("feedback");
     if (x.style.display === "none")
     {
       x.style.display = "block";
     }
     else
     {
       x.style.display = "none";
     }
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
