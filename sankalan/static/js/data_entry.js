$(document).ready(function()
{
  var i = 1;
  if (i=1)
  {
    // to delay the modal load
    var delay = setTimeout(myTimer, 400);
  }
  function myTimer()
  {
    // to show the modal - only once
    $('#myModal').show();
    i = 2;
  }
  $("#close_btn").click(function()
  {
    // to close the modal
    $('#myModal').hide();
  })
})

// date constraint for D.O.B.

$(document).ready(function(){
  var today = new Date();
  var dd = String(today.getDate());
  if (dd < 10)
    { dd = '0' + dd; }
  var mm = String(today.getMonth() + 1); //January is 0!
  if (mm < 10)
    { mm = '0' + mm; }
  var yyyy = today.getFullYear();

  today = yyyy + '-' + mm + '-' + dd;
  document.getElementById('dob').setAttribute('max',today);
})