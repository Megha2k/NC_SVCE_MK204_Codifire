//javascript code for responsive collapse bars

var acc = document.getElementsByClassName("accordion");
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
      var x = document.getElementById('contact');
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

function openBar4()
    {
      var x = document.getElementById("about");
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

//functions for voice playing

var audio1 = document.getElementById("audioID1");

function playAudio1() {
  audio1.play();
}

var audio2 = document.getElementById("audioID2");

function playAudio2() {
  audio2.play();
}

var audio3 = document.getElementById("audioID3");

function playAudio3() {
  audio3.play();
}

var audio4 = document.getElementById("audioID4");

function playAudio4() {
  audio4.play();
}

var audio5 = document.getElementById("audioID5");

function playAudio5() {
  audio5.play();
}

var audio6 = document.getElementById("audioID6");

function playAudio6() {
  audio6.play();
}

var audio7 = document.getElementById("audioID7");

function playAudio7() {
  audio7.play();
}

var audio8 = document.getElementById("audioID8");

function playAudio8() {
  audio8.play();
}


