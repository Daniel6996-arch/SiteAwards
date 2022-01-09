$(document).ready(function(){
  $('form').submit(function(event){
    console.log('hello')
    event.preventDefault()
    form = $("form")

    $.ajax({
      'url':'site_of_day/',
      'type':'POST',
      'data':form.serialize(),
      'dataType':'json',
      'success': function(data){
        alert(data['success'])
      },
    })// END of Ajax method
  //  $('#id_your_name').val('')
   // $("#id_email").val('')
  }) // End of submit event

}) // End of document ready function
