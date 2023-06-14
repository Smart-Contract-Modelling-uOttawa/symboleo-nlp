EMPTY_VAL = '[EMPTY]'

input_value_dict = {
  'WITHIN': 'within',
  'IF': 'if',
  'BEFORE': 'before',
  'AFTER': 'after',
  'EVENT': EMPTY_VAL,
  'CUSTOM_EVENT': EMPTY_VAL,
  'SUBJECT': null,
  'VERB': null,
  'DATE': null,
  //....
}


// Add new text value to the running input 
function updateRunningValue(value) {
  var $inputContainer = $('#running-input');
  var $span = $('<span>').text(value);
    $span.addClass('input-value');
    $inputContainer.append($span);
}

// Process a value entered by the user
function processValue(input_id, value) {
  var data = {
    input_id: input_id,
    value: value
  };

  // Send the AJAX request
  $.ajax({
    url: '/value',
    method: 'POST',
    data: data,
    success: function(response) {
      handleUnits(response.units)
    },
    error: function(error) {
      console.error('Error updating content:', error);
    }
  });
}


function submitDynamicValue() { 
  var input_id = $('#input-value-label').text();  
  var value = $('#input-value-form').val();

  updateRunningValue(value)
  processValue(input_id, value)
}

// In some cases, it  will be a dropdown with options...
// Will likely involve an ajax call. Or just store a temp dict on this side...
function setupDynamicValue(input_id) {
  $('#value-entry').show();
  $('#input-value-label').text(input_id);  
}

function handleInputClick(input_id) {
  value = input_value_dict[input_id]
  
  if (value == EMPTY_VAL) {
    // Empty unit
    processValue(input_id, null)
  } else if (value) {
    // Static unit
    updateRunningValue(value)
    processValue(input_id, value)    
  } else {
    // Dynamic unit
    setupDynamicValue(input_id)
    // will need to fetch potential options (e.g. from domain model)...
  }
}


function handleUnits(units) {
  var $buttonContainer = $('#selection-container');

  // Clear the existing buttons
  $buttonContainer.empty();

  // Iterate through the strings and create buttons
  // Each button needs a further handler
  $.each(units, function(index, string) {
    var $button = $('<button>').text(string);
    $button.addClass('btn');
    $button.click(function() {
      handleInputClick(string);
    });
    $buttonContainer.append($button);
  });    
}

function selectParameter() {
  // Hide the input 
  $('#value-entry').hide();

  var selectedParm = $('#parm-selection').val();
  // Create the data payload for the AJAX request
  var data = {
    parameter: selectedParm
  };

  // Send the AJAX request
  $.ajax({
    url: '/parameter',
    method: 'POST',
    data: data,
    success: function(response) {
      handleUnits(response.units)
    },
    error: function(error) {
      console.error('Error updating content:', error);
    }
  });
}

