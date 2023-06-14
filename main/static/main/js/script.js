for (var i = 0; i < 10; i++){
   var div = document.getElementById('pulse_column_' + i.toString())
   var pulse = document.getElementById('pulse_' + i.toString())
   div.style.height = pulse.textContent + "px" 
   div.style.top = 150 - parseInt(pulse.textContent) + "px"
   pulse.style.top = 150 - parseInt(pulse.textContent) + "px"
   
   if (pulse.textContent == "0"){
      pulse.style.color = "grey"
   } else{
      date = document.getElementById('pulse_date_' + i.toString())
      date.style.top = (150 -parseInt(pulse.textContent)).toString() + "px"
   }
}