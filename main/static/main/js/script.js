for (var i = 0; i < 10; i++){
   var div1 = document.getElementById('pulse_column1_' + i.toString())
   var div2 = document.getElementById('pulse_column2_' + i.toString())
   var pulse1 = document.getElementById('pulse1_' + i.toString())
   var pulse2 = document.getElementById('pulse2_' + i.toString())
   div1.style.height = pulse1.textContent + "px" 
   div1.style.top = 150 - parseInt(pulse1.textContent) - 190 + "px"
   pulse1.style.top = 150 - parseInt(pulse1.textContent) - 190 + "px"

   div2.style.height = pulse2.textContent + "px" 
   div2.style.top = 150 - parseInt(pulse2.textContent) - 190 + "px"
   pulse2.style.top = 150 - parseInt(pulse2.textContent) - 190 + "px"
   
   if (pulse1.textContent == "0"){
      pulse1.style.color = "grey"
      pulse2.style.color = "grey"
      date = document.getElementById('pulse_date_' + i.toString())
      
      date.style.color = "grey"
   } else{
      date = document.getElementById('pulse_date_' + i.toString())
      
   }
   date.style.top = (150 - Math.max(parseInt(pulse1.textContent), parseInt(pulse2.textContent)) - 200).toString() + "px"


   var div = document.getElementById('rating_column_' + i.toString())
   var rating = document.getElementById('rating_' + i.toString())
   var height = Math.min(Math.max(parseInt(rating.textContent), 0) / 50.0 * 150, 150)
   div.style.height = height + "px"
   div.style.top = -50 - height + "px"
   rating.style.top = 150 - height - 190 + "px"
   date = document.getElementById('rating_date_' + i.toString())
   if (rating.textContent == "-1"){
      date.style.color = "grey"
      rating.style.color = "grey"
      rating.textContent = "0"
   } 
   if (height == 0){
      date.style.top = parseInt(-37 - height) + "px"
   } else{
      date.style.top = parseInt(-50 - height) + "px"
   }
   
}