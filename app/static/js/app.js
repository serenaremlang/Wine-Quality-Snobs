d3.selectAll(".form-range")
    .attr('disabled', true)
    .on('input', function() {
        d3.select('#'+d3.select(this).attr('data-id')).text(this.value)
    });


function optionChanged(modelId) {  
    if (modelId == 1 || modelId == 2) 
    {
        d3.selectAll(".form-range").attr('disabled', null);
    }
    else 
    {
        d3.selectAll(".form-range").attr('disabled', true);
    }    
}

function resetUI(event) {    
    d3.selectAll('.rngval').text('0.0');
    optionChanged('reset');
}

frmWineVals.addEventListener('reset', resetUI);

