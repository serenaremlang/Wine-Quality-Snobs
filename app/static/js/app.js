d3.selectAll(".form-range")
    .attr('disabled', true)
    .on('input', function() {
        d3.select('#'+d3.select(this).attr('data-id')).text(this.value)
    });
d3.selectAll(".btn").attr('disabled', true);
d3.select('#wqs').text('?');

function optionChanged(modelId) {  
    if (modelId == 1 || modelId == 2) 
    {
        d3.selectAll(".form-range").attr('disabled', null);
        d3.selectAll(".btn").attr('disabled', null);
    }
    else 
    {
        d3.selectAll(".form-range").attr('disabled', true);
        d3.selectAll(".btn").attr('disabled', true);
    }    
}

function resetUI(event) {    
    d3.selectAll('.rngval').text('0.0');
    d3.select('#wqs').text('?');
    optionChanged('reset');
}

function getWineScore() {    
    const url = "/api/getwinescore";
    d3.json(url).then(function(response) {
  
      console.log(response);
  
      const data = response;
      var displayScore = "UNKNOWN - APP ERROR";

      if (data.score==0) {
        displayScore = 'BAD';
      } else if (data.score==1) {
        displayScore = 'FAIR';
      } else if (data.score==2) {
        displayScore = 'GOOD';
      } else if (data.score==3) {
        displayScore = 'UNKNOWN - SERVER ERROR';
      }
  
      d3.select('#wqs').text(displayScore);
    });
  }

  frmWineVals.addEventListener('reset', resetUI);

  $(function(){
	$('#btnSubmit').click(function(){
        var displayScore = "UNKNOWN - APP ERROR";
        // var fixed_acidity = $('#rng_fa').val();
        // var volatile_acidity = $('#rng_va').val();	
        // var citric_acid = $('#rng_ca').val();
        // var residual_sugar = $('#rng_rs').val();
        // var chlorides = $('#rng_c').val();
        // var free_sulfur_dioxide = $('#rng_fsd').val();
        // var total_sulfur_dioxide = $('#rng_tsd').val();
        // var density = $('#rng_d').val();
        // var pH = $('#rng_ph').val();
        // var sulphates = $('#rng_s').val();
        // var alcohol = $('#rng_a').val();
        // var model_type = $('#ddl_wt').val();   

		$.ajax({
			url: '/api/getwinescore',
			data: $('#frmWineVals').serialize(),
			type: 'POST',
			success: function(data){
				console.log(data[0]);

                if (data[0].score==0) {
                    displayScore = 'BAD';
                } else if (data[0].score==1) {
                    displayScore = 'FAIR';
                } else if (data[0].score==2) {
                    displayScore = 'GOOD';
                } else if (data[0].score==3) {
                    displayScore = 'UNKNOWN - SERVER ERROR';
                }

                $('#wqs').text(displayScore);

			},
			error: function(error){
				console.log(error);
			}
		});
	});
});